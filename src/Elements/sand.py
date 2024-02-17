import random

from Elements.element import Element

class Sand(Element):
    def __init__(self, position):
        super().__init__(position)
        self.color = (255, 255, 0, 255)
        self.name = "Sand"
        self.density = 2

    def update(self, grid: list[list], elements: list[Element]) -> None:
        if self.get_out_of_bounds(grid): return

        px: int = self.position[0]
        py: int = self.position[1]

        # go straight down if possible
        if grid[px][py+1] == 0:
            py += 1
        else:
            num = random.randrange(0, 2)
            if num:
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
"""

# i need to grab the element below this one and check if it's water
is_element_below = False
below_element = None

for element in elements:
    if element.get_position() == (px, py+1):
        if element.get_name() == "Water":
            is_element_below = True
            below_element = element

elif grid[px][py+1] == 1 and is_element_below:
    for element in elements:
        if element.get_position() == (px, py+1):
            if grid[px][py+1] == 1 and element.get_name() == "Water":
                py += 1
                break
            elif grid[px][py] == 1 and element.get_name() == "Sand":
                pass
"""
