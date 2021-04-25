from typing import List
import yaml

from ..label import Label
from ..position import Position, POSITION_STR_TO_ENUM


def parse_labels_file(fname: str) -> List[List[Label]]:
    with open(fname, 'r') as stream:
        labels_raw = yaml.safe_load(stream)

    labels = list()
    for label in labels_raw:
        current_labels = list()
        for position_str in label['positions']:
            current_labels.append(Label(
                x=label['x'],
                y=label['y'],
                width=label['width'],
                height=label['height'],
                position=POSITION_STR_TO_ENUM[position_str]
            ))
        labels.append(current_labels)

    return labels
