import random

from Elements.element import Element

class Sand(Element):
    def __init__(self, position):
        super().__init__(position)
        self.color = (255, 255, 0, 255)

    def update(self, grid: list[list[int]]) -> None:
        if self.get_out_of_bounds(grid): return

        px: int = self.position[0]
        py: int = self.position[1]

        # go straight down if possible
        if grid[px][py+1] == None:
            py += 1
        # go down to the right or left randomly
        else:
            num = random.randrange(0, 2)
            if num:
                if grid[px-1][py+1] == None:
                    px -= 1
                    py += 1
                elif grid[px+1][py+1] == None:
                    px += 1
                    py += 1
            else:
                if grid[px+1][py+1] == None:
                    px += 1
                    py += 1
                elif grid[px-1][py+1] == None:
                    px -= 1
                    py += 1

        grid[px][py] = 1
        self.position = (px, py)
