from label_placement.utils.general import label_to_bbox
from label_placement.utils.plots import create_empty_figure, plot_one_box, plot_one_point
from label_placement.label_placer import find_placement
from label_placement.utils.parser import parse_labels_file


if __name__ == "__main__":
    labels = parse_labels_file('example.yaml')

    chosen_labels = find_placement(labels)
    
    fig, ax = create_empty_figure(500, 500)
    for label in chosen_labels:
        plot_one_box(ax, label_to_bbox(label))
        plot_one_point(ax, label.x, label.y)
    fig.savefig('test.jpg')
