import random

from Elements.element import Element

class Wood(Element):
    is_on_fire = False
    def __init__(self, position):
        super().__init__(position)
        variation = random.randint(-10, 10)
        self.color = (90 + variation, 60 + variation, 9, 255)
        self.name = "Wood"
        self.density = 1

    def update(self, grid: list[list[int]], elements: list[Element]) -> None:
        # later this has to account for flammability
        if not self.is_on_fire: pass
