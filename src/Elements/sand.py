import random

from Elements.element import Element

class Sand(Element):
    def __init__(self, position):
        super().__init__(position)
        self.color = (255, 255, 0, 255)
        self.name = "Sand"
        self.density = 2

    def update(self, grid: list[list[int]], elements: list[Element]) -> None:
        if self.get_out_of_bounds(grid): return

        px: int = self.position[0]
        py: int = self.position[1]

        grid[px][py] = 0

        if grid[px][py+1] == 0 or grid[px][py+1] == 2:
            py += 1
        elif grid[px+1][py+1] == 0 or grid[px+1][py+1] == 2:
            px += 1
            py += 1
        elif grid[px-1][py+1] == 0 or grid[px-1][py+1] == 2:
            px -= 1
            py += 1

        grid[px][py] = 1
        self.position = (px, py)
