import random

from Elements.element import Element

class Water(Element):
    def __init__(self, position) -> None:
        super().__init__(position)
        self.color = (0, 0, random.randrange(180, 255), 255)
        self.name = "Water"
        self.density = 1

    def update(self, grid: list[list[int]], elements: list[Element]) -> None:
        if self.get_out_of_bounds(grid): return

        px: int = self.position[0]
        py: int = self.position[1]

        grid[px][py] = 0

        if grid[px][py+1] == 0:
            py += 1
        elif grid[px+1][py] == 0 or grid[px-1][py] == 0:
            rand_num = random.choice([-1, 1])
            if grid[px+rand_num][py] == 0:
                px += rand_num
        else:
            rand_num = random.choice([-1, 1])
            if grid[px+rand_num][py+1] == 0:
                px += rand_num
                py += 1

        grid[px][py] = 2
        self.position = (px, py)
