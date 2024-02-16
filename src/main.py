import pygame
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


def main():
    game_running = True

    elements: list[Element] = []
    grid: list[list[int]] = [[0 for _ in range(rows)] for _ in range(cols)]

    # 0 = sand, 1 = water, 2 = wood, 3 = fire
    selected_type = 0

    left_drag = False
    right_drag = False

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
                print(event.button)
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

        # reset the grid
        for x in range(cols):
            for y in range(rows):
                if grid[x][y] != 0:
                    grid[x][y] = 0

        for i in range(len(elements)):
            px = elements[i].get_position()[0]
            py = elements[i].get_position()[1]

            grid[px][py] = 1

            elements[i].update(grid)
            pygame.draw.rect(screen, elements[i].get_color(), (px * resolution, py * resolution, resolution, resolution))

        pygame.display.flip()
        time.sleep(0.01)
    pygame.quit()

def spawn_element(selected_type: int, elements: list[Element]) -> None:
    mouse_pos = pygame.mouse.get_pos()
    radius = 5

    for x in range(radius):
        for y in range(radius):
            px = int(mouse_pos[0] / resolution) - x
            py = int(mouse_pos[1] / resolution) - y

            if selected_type == 0:
                if not Sand((px, py)) in elements:
                    new_element = Sand((px, py))
                    elements.append(new_element)
            elif selected_type == 1:
                if not Water((px, py)) in elements:
                    new_element = Water((px, py))
                    elements.append(new_element)

def remove_element(elements: list[Element]) -> None:
    mouse_pos = pygame.mouse.get_pos()
    radius = 5

    for x in range(radius):
        for y in range(radius):
            px = int(mouse_pos[0] / resolution) - x
            py = int(mouse_pos[1] / resolution) - y

            positions = [element.get_position() for element in elements]
            if (px, py) in positions:
                print("there's something in there to remove!")
                elements.remove(elements[positions.index((px, py))])
main()
