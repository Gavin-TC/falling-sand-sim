import pygame
import threading
import time

from Elements.element import Element
from Elements.sand import Sand
from Elements.water import Water

pygame.init()

cell_size = 10  # Size of each grid cell

width: int = 960
height: int = 640

resolution: int = 5

cols: int = width // resolution
rows: int = height // resolution

screen: pygame.Surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling Sand Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

def main():
    game_running = True


    # 0 = sand, 1 = water, 2 = wood, 3 = fire
    selected_type = 0

    left_drag = False
    right_drag = False

    # spawn_thread = threading.Thread(target=spawn_element, args=elements)
    # remove_thread = threading.Thread(target=remove_element, args=elements)
    # spawn_thread.start()
    # remove_thread.start()

    elements: list[Element] = []
    grid: list[list[int]] = [[0 for _ in range(rows)] for _ in range(cols)]

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.KEYDOWN:
                match event.key:
                    # escape key, for some reason pygame.QUIT doesn't work on mac.
                    case 27:
                        game_running = False
                    case 49:
                        selected_type = 0
                    case 50:
                        selected_type = 1
                    case _:
                        selected_type = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: left_drag = True
                if event.button == 3: right_drag = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: left_drag = False
                if event.button == 3: right_drag = False

        if left_drag:
            spawn_element(selected_type, elements, grid)
        elif right_drag:
            remove_element(elements, grid)

        screen.fill((0, 0, 0))

        grid = [[0 for _ in range(rows)] for _ in range(cols)]

        # get all the element objects in 2d array
        for element in elements:
            px = element.get_position()[0]
            py = element.get_position()[1]

            grid[px][py] = 1

            element.update(grid, elements)
            pygame.draw.rect(screen, element.get_color(), (px * resolution, py * resolution, resolution, resolution))

        # FPS stuff
        clock.tick()
        fps = str(int(clock.get_fps()))
        fps_text = font.render("FPS: " + fps, True, (255, 255, 255))
        screen.blit(fps_text, (5, 5))

        pygame.display.flip()
        # time.sleep(0.1)
    pygame.quit()

def spawn_element(selected_type: int, elements: list[Element], grid: list[list[int]])-> None:
    mouse_pos = pygame.mouse.get_pos()
    radius = 1

    for x in range(radius):
        for y in range(radius):
            px = int(mouse_pos[0] / resolution) - x
            py = int(mouse_pos[1] / resolution) - y

            if selected_type == 0:
                if grid[px][py] == 0:
                    grid[px][py] = 1
                    elements.append(Sand((px, py)))
            elif selected_type == 1:
                if grid[px][py] == 0:
                    grid[px][py] = 1
                    elements.append(Water((px, py)))

def remove_element(elements: list[Element], grid: list[list[int]]) -> None:
    mouse_pos = pygame.mouse.get_pos()
    radius = 10

    for x in range(radius):
        for y in range(radius):
            positions = [element.get_position() for element in elements]
            if positions:
                px = int(mouse_pos[0] / resolution) - x
                py = int(mouse_pos[1] / resolution) - y

                if grid[px][py] == 1:
                    try:
                        grid[px][py] = 0
                        elements.remove(elements[positions.index((px, py))])
                    except:
                        pass
main()
