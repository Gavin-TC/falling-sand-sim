import random

from Elements.element import Element

class Sand(Element):
    def __init__(self, position):
        super().__init__(position)
        self.color = (255, 255, 0)

    def update(self, grid: list[list]) -> None:
        px = self.position[0]
        py = self.position[1]

        # doesn't allow index out of range error
        if py + 1 >= len(grid[0]) or py - 1 < 0: return
        if px + 1 >= len(grid) or px - 1 < 0: return

        # go straight down if possible
        if grid[px][py+1] == 0:
            py += 1
        # go down to the right or left randomly
        else:
           if random.randrange(0, 1):
               if grid[px-1][py+1] == 0:
                   px -= 1
                   py += 1
               elif grid[px+1][py+1] == 0:
                   px += 1
                   py += 1
           else:
               if grid[px+1][py+1] == 0:
                   px += 1
                   py += 1
               elif grid[px-1][py+1] == 0:
                   px -= 1
                   py += 1

        grid[px][py] = 1
        self.position = (px, py)
