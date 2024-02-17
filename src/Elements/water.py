import random

from Elements.element import Element

class Water(Element):
    def __init__(self, position) -> None:
        super().__init__(position)
        self.color = (0, 0, 255, 255//2)

    def update(self, grid: list[list[int]]) -> None:
        if self.get_out_of_bounds(grid): return

        px: int = self.position[0]
        py: int = self.position[1]

        # if you can go down, do it
        if grid[px][py+1] == None:
            py += 1
        else:
            num = random.choice([-1, 1])
            if grid[px+num][py] == None:
                px += num

        self.position = (px, py)
