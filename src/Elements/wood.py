import random

from Elements.element import Element

class Wood(Element):
    def __init__(self, position):
        super().__init__(position)
        self.color = (127, 88, 0, 255)
        self.name = "Wood"
        self.density = 1

    def update(self, grid: list[list[int]], elements: list[Element]) -> None:
        # later this has to account for flammability
        pass
