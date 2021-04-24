from .label import Label, BoundingBox
from .position import Position


def label_to_bbox(label: Label) -> BoundingBox:
    if label.position == Position.LEFT_MIDDLE:
        x = label.x
        y = label.y - label.height / 2
    elif label.position == Position.TOP_MIDDLE:
        x = label.x - label.width / 2
        y = label.y
    elif label.position == Position.RIGHT_MIDDLE:
        x = label.x - label.width
        y = label.y - label.height / 2
    elif label.position == Position.BOTTOM_MIDDLE:
        x = label.x - label.width / 2
        y = label.y - label.height
    else:
        raise NotImplementedError
    
    width = label.width
    height = label.height
    return BoundingBox(x, y, width, height)


def has_intersection(bbox1: BoundingBox, bbox2: BoundingBox) -> bool:
    raise NotImplementedError
