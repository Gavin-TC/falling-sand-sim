class Element:
    position = (0, 0)
    color = (0, 0, 0)

    def __init__(self, position):
        self.position = position

    def update(self, grid) -> None:
        pass

    def get_position(self) -> tuple:
        return self.position

    def get_color(self) -> tuple:
        return self.color
