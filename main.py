from label_placement.label import Label
from label_placement.position import Position
from label_placement.utils.general import label_to_bbox, has_intersection
from label_placement.utils.plots import create_empty_figure, plot_one_box, plot_one_point
from label_placement.label_placer import find_placement


if __name__ == "__main__":
    labels = [
        [
            Label(250, 250, 100, 100, Position.BOTTOM_MIDDLE),
            Label(250, 250, 100, 100, Position.TOP_MIDDLE)
        ],
        [
            Label(200, 200, 10, 10, Position.BOTTOM_MIDDLE),
            Label(200, 200, 10, 10, Position.TOP_MIDDLE),
        ],
    ]

    find_placement(labels)
    
    fig, ax = create_empty_figure(500, 500)
    for labe in labels:
        for lab in labe:
            plot_one_box(ax, label_to_bbox(lab))
    fig.savefig('test.jpg')
