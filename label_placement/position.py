from enum import Enum, auto


class Position(Enum):
    LEFT_MIDDLE = auto()
    TOP_MIDDLE = auto()
    RIGHT_MIDDLE = auto()
    BOTTOM_MIDDLE = auto()
    LEFT_TOP = auto()
    RIGHT_TOP = auto()
    RIGHT_BOTTOM = auto()
    LEFT_BOTTOM = auto()


POSITION_STR_TO_ENUM = {
    "LEFT_MIDDLE": Position.LEFT_MIDDLE,
    "TOP_MIDDLE": Position.TOP_MIDDLE,
    "RIGHT_MIDDLE": Position.RIGHT_MIDDLE,
    "BOTTOM_MIDDLE": Position.BOTTOM_MIDDLE,
    "LEFT_TOP": Position.LEFT_TOP,
    "RIGHT_TOP": Position.RIGHT_TOP,
    "RIGHT_BOTTOM": Position.RIGHT_BOTTOM,
    "LEFT_BOTTOM": Position.LEFT_BOTTOM,
}
