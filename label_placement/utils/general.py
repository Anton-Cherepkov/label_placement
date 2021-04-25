from typing import List

from ..label import Label, BoundingBox
from ..position import Position


def label_to_bbox(label: Label) -> BoundingBox:
    if label.position == Position.LEFT_MIDDLE:
        x = label.x
        y = label.y - label.height / 2
    elif label.position == Position.BOTTOM_MIDDLE:
        x = label.x - label.width / 2
        y = label.y
    elif label.position == Position.RIGHT_MIDDLE:
        x = label.x - label.width
        y = label.y - label.height / 2
    elif label.position == Position.TOP_MIDDLE:
        x = label.x - label.width / 2
        y = label.y - label.height
    else:
        raise NotImplementedError
    
    width = label.width
    height = label.height

    return BoundingBox(
        x1=x,
        y1=y,
        x2=x + width,
        y2=y + height
    )


def has_intersection(bbox1: BoundingBox, bbox2: BoundingBox) -> bool:
    x1 = max(bbox1.x1, bbox2.x1)
    x2 = min(bbox1.x2, bbox2.x2)
    y1 = max(bbox1.y1, bbox2.y1)
    y2 = min(bbox1.y2, bbox2.y2)
    return x1 < x2 and y1 < y2


def bbox_in_boundaries(bbox: BoundingBox, xlim: float, ylim: float):
    in_boundaries = True
    in_boundaries &= bbox.x1 >= 0
    in_boundaries &= bbox.y1 >= 0
    in_boundaries &= bbox.x2 <= xlim
    in_boundaries &= bbox.y2 <= ylim
    return in_boundaries


def filter_labels_out_of_boundaries(labels: List[Label], xlim: float, ylim: float) -> List[Label]:
    labels = filter(
        lambda label: bbox_in_boundaries(label_to_bbox(label), xlim, ylim),
        labels
    )
    return list(labels)
