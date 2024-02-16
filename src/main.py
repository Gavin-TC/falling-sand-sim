import pygame
import time

from Elements.element import Element
from Elements.sand import Sand

pygame.init()

cell_size = 10  # Size of each grid cell

width = 600
height = 600

resolution = 5

cols = width // resolution
rows = height // resolution

screen = pygame.display.set_mode((width, height))
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
            if event.type == pygame.KEYDOWN:
                # escape key, for some reason pygame.QUIT doesn't work on mac.
                if event.key == 27:
                    game_running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: left_drag = True
                if event.button == 2: right_drag = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: left_drag = False
                if event.button == 2: right_drag = False

        if left_drag:
            spawn_element(selected_type, elements)
        elif right_drag:
            # remove_element(elements)
            pass

        screen.fill((0, 0, 0))

        for x in range(cols):
            for y in range(rows):
                grid[x][y] = 0

        for i in range(len(elements)):
            px = elements[i].get_position()[0]
            py = elements[i].get_position()[1]

            grid[px][py] = 1

            pygame.draw.rect(screen, elements[i].get_color(), (px * resolution, py * resolution, resolution, resolution))

        for i in range(len(elements)):
            elements[i].update(grid)

        pygame.display.flip()
        time.sleep(0.01)
    pygame.quit()

def spawn_element(selected_type: int, elements: list[Element]) -> None:
    mouse_pos = pygame.mouse.get_pos()
    match selected_type:
        case 0:
            new_element = Sand((int(mouse_pos[0] / resolution),
                                int(mouse_pos[1] / resolution)))
            elements.append(new_element)
        case _:
            pass


main()
