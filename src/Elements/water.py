import random

from Elements.element import Element

class Water(Element):
    def __init__(self, position) -> None:
        super().__init__(position)
        self.color = (0, 0, 255)

    def update(self, grid: list[list[int]]) -> None:
        if self.get_out_of_bounds(grid): return

        px: int = self.position[0]
        py: int = self.position[1]

        # if you can go down, do it
        if grid[px][py+1] == 0:
            py += 1
        # if you can't go down, go to the left or the right.
        else:
            num = random.randrange(-1, 2)
            if grid[px+num][py] == 0:
                px += num

        self.position = (px, py)
