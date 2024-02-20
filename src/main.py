import pygame
import threading
import time

from Elements.element import Element
from Elements.sand import Sand
from Elements.water import Water
from Elements.wood import Wood
from Elements.fire import Fire

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

positions = [] 

def main():
    global positions
    game_running = True


    # 1 = sand, 2 = water, 3 = wood
    selected_type = 1

    left_drag = False
    right_drag = False
    slow_motion = False

    # spawn_thread = threading.Thread(target=spawn_element, args=elements)
    # remove_thread = threading.Thread(target=remove_element, args=elements)
    # spawn_thread.start()
    # remove_thread.start()

    elements: list[Element] = []
    grid: list[list[int]] = [[0 for _ in range(rows)] for _ in range(cols)]
    positions = [element.get_position() for element in elements]

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.KEYDOWN:
                match event.key:
                    case 27:  # escape key, for some reason pygame.QUIT doesn't work on mac.
                        game_running = False
                    case 49:
                        selected_type = 1
                    case 50:
                        selected_type = 2
                    case 51:
                        selected_type = 3
                    case 52:
                        selected_type = 4
                    case 98:
                        slow_motion = not slow_motion
                    case _:
                        selected_type = 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: left_drag = True
                if event.button == 3: right_drag = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: left_drag = False
                if event.button == 3: right_drag = False

        if left_drag:    spawn_element(selected_type, elements, grid)
        elif right_drag: remove_element(elements, grid)

        screen.fill((0, 0, 0))

        grid = [[0 for _ in range(rows)] for _ in range(cols)]

        # get all the element objects in 2d array
        for element in elements:
            px = element.get_position()[0]
            py = element.get_position()[1]

            match element.get_name():
                case "Sand":
                    grid[px][py] = 1
                case "Water":
                    grid[px][py] = 2
                case "Wood":
                    grid[px][py] = 3

            if not element.get_name() == "Wood": 
                element.update(grid, elements)
            
            if py < 0:
                elements.remove(element)

            positions.remove((px, py))
            px = element.get_position()[0]
            py = element.get_position()[1]
            positions.append((px, py))
           
            pygame.draw.rect(screen, element.get_color(), (px * resolution, py * resolution, resolution, resolution))

        # =========
        # FPS/Display stuff
        clock.tick()
        fps = str(int(clock.get_fps()))
        fps_text = font.render("FPS: " + fps, True, (255, 255, 255))
        screen.blit(fps_text, (5, 5))

        pygame.display.flip()
        # =========

        if slow_motion:
            time.sleep(0.075)
    pygame.quit()

def spawn_element(selected_type: int, elements: list[Element], grid: list[list[int]])-> None:
    global positions
    
    mouse_pos = pygame.mouse.get_pos()
    radius = 1
    # if selected_type == 2:
    #     radius = 5
    if selected_type == 3 or selected_type == 4:
        radius = 5

    for x in range(radius):
        for y in range(radius):
            px = int(mouse_pos[0] / resolution) - x
            py = int(mouse_pos[1] / resolution) - y

            if selected_type == 1:
                if grid[px][py] == 0:
                    grid[px][py] = 1
                    elements.append(Sand((px, py)))
                    positions.append((px, py))
            elif selected_type == 2:
                if grid[px][py] == 0:
                    grid[px][py] = 1
                    elements.append(Water((px, py)))
                    positions.append((px, py))
            elif selected_type == 3:
                if grid[px][py] == 0:
                    grid[px][py] = 3
                    elements.append(Wood((px, py)))
                    positions.append((px, py))
            elif selected_type == 4:
                if grid[px][py] == 0:
                    grid[px][py] = 4
                    elements.append(Fire((px, py)))
                    positions.append((px, py))
                    


def remove_element(elements: list[Element], grid: list[list[int]]) -> None:
    global positions

    mouse_pos = pygame.mouse.get_pos()
    mx = mouse_pos[0]
    my = mouse_pos[1]
    radius = 10

    for x in range(radius):
        for y in range(radius):
            px = int(mx / resolution) - x
            py = int(my / resolution) - y
            
            if (px, py) in positions:
                try:
                    if grid[px][py] != 0:
                        try:
                            grid[px][py] = 0
                            elements.remove(elements[positions.index((px, py))])
                            positions.remove((px, py))
                        except:
                            pass
                except:
                    pass
main()
