from .position import Position


class Label:
    def __init__(self, x: float, y: float, width: float, height: float, position: Position):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = position


class BoundingBox:
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)

        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)
    
    def get_width(self) -> float:
        return self.x2 - self.x1
    
    def get_height(self) -> float:
        return self.y2 - self.y1
