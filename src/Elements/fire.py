import random

from Elements.element import Element

class Fire(Element):
    turns = 0

    def __init__(self, position):
        super().__init__(position)
        self.color = (200, 0, 0, 255)
        self.name = "Fire"
        self.density = 1

    def update(self, grid: list[list[int]], elements: list[Element]) -> None:
        if self.get_out_of_bounds(grid): return

        px: int = self.position[0]
        py: int = self.position[1]

        grid[px][py] = 0

        if grid[px][py-1] == 0:
            py -= 1
            rand_num = random.randrange(-1, 2)
            if grid[px+rand_num][py] == 0:
                px += rand_num
        elif grid[px+1][py] == 0 or grid[px-1][py] == 0:
            rand_num = random.randrange(-1, 2)
            if grid[px+rand_num][py] == 0:
                px += rand_num
        else:
            rand_num = random.randrange(-1, 2)
            if grid[px+rand_num][py-1] == 0:
                px += rand_num
                py -= 1

        if self.color[0] > 200:
            self.color = (max(255-self.turns, 20), 0, 0, 0)
        else:
            self.color = (max(255-self.turns, 20), max(255-self.turns, 20), max(255-self.turns, 20), 0)

        grid[px][py] = 4
        self.position = (px, py)
        self.turns += 1
