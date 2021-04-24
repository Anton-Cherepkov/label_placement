from .position import Position


class Label:
    def __init__(self, x: float, y: float, width: float, height: float, position: Position):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = position


class BoundingBox:
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
