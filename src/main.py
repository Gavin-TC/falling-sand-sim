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

    elements: list[list[Element]] = [[None for _ in range(rows)] for _ in range(cols)]
    # grid: list[list[int]] = [[0 for _ in range(rows)] for _ in range(cols)]

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
            spawn_element(selected_type, elements)
        elif right_drag:
            remove_element(elements)

        screen.fill((0, 0, 0))

        # get all the element objects in 2d array
        for list in elements:
            for element in list:
                if element:
                    px = element.get_position()[0]
                    py = element.get_position()[1]

                    element.update(elements)
                    pygame.draw.rect(screen, element.get_color(), (px * resolution, py * resolution, resolution, resolution))

        # FPS stuff
        clock.tick()
        fps = str(int(clock.get_fps()))
        fps_text = font.render("FPS: " + fps, True, (255, 255, 255))
        screen.blit(fps_text, (5, 5))

        pygame.display.flip()
        # time.sleep(0.05)
    pygame.quit()

def spawn_element(selected_type: int, elements: list[list[Element]]) -> None:
    mouse_pos = pygame.mouse.get_pos()
    radius = 5

    for x in range(radius):
        for y in range(radius):
            px = int(mouse_pos[0] / resolution) - x
            py = int(mouse_pos[1] / resolution) - y

            if selected_type == 0:
                if elements[px][py] is None:
                    elements[px][py] = Sand((px, py))
                elif selected_type == 1:
                    if elements[px][py] is None:
                        elements[px][py] = Water((px, py))

def remove_element(elements: list[list[Element]]) -> None:
    mouse_pos = pygame.mouse.get_pos()
    radius = 10

    for x in range(radius):
        for y in range(radius):
            px = int(mouse_pos[0] / resolution) - x
            py = int(mouse_pos[1] / resolution) - y

            for element in elements:
                if element.get_position() == (px, py):
                    elements.remove(element)

main()
