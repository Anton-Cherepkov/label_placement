from label_placement.label import Label
from label_placement.position import Position
from label_placement.utils import label_to_bbox


if __name__ == "__main__":
    label = Label(0, 0, 1, 1, Position.LEFT_MIDDLE)
    bbox = label_to_bbox(label)
