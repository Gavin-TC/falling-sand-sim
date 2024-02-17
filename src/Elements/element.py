class Element:
    position: tuple[int, int] = (0, 0)
    # default is 1, same as water.
    # <1 floats, >1 floats
    density: int = 1
    color: tuple[int, int, int, int] = (255, 255, 255, 255)
    name: str = ""

    def __init__(self, position):
        self.position = position

    def update(self, grid: list[list[int]], elements: list) -> None:
        pass

    def get_out_of_bounds(self, grid: list[list[int]]) -> bool:
        # doesn't allow index out of range error
        if self.position[1] + 1 >= len(grid[0]) or self.position[1] - 1 < 0: return True
        if self.position[0] + 1 >= len(grid) or self.position[0] - 1 < 0: return True
        return False


    def get_position(self) -> tuple:
        return self.position

    def set_position(self, position: tuple) -> None:
        self.position = position

    def get_color(self) -> tuple:
        return self.color

    def get_name(self) -> str:
        return self.name
