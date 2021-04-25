import os
import click

from label_placement.utils.general import label_to_bbox
from label_placement.utils.plots import create_empty_figure, plot_one_box, plot_one_point
from label_placement.label_placer import find_placement
from label_placement.utils.parser import parse_labels_file


@click.command()
@click.option(
    '--input_labels_file',
    type=click.Path(),
    default='example.yaml',
    help='Path to file describing labels'
)
@click.option(
    '--output_folder',
    type=click.Path(),
    default='.',
    help='Folder for saving output images'
)
@click.option(
    '--xlim',
    type=float,
    default=500,
    help='Canvas x-axis boundary'
)
@click.option(
    '--ylim',
    type=float,
    default=500,
    help='Canvas y-axis boundary'
)
def find_placement_and_draw(input_labels_file, output_folder, xlim, ylim):
    labels = parse_labels_file(input_labels_file)
    name, _ = os.path.splitext(input_labels_file)
    output_name = f"{name}.jpg"

    chosen_labels = find_placement(labels)
    if chosen_labels is None:
        print('Placement does not exist!')
    else:
        print('Placement exists!')

        fig, ax = create_empty_figure(xlim, ylim)
        for label in chosen_labels:
            plot_one_box(ax, label_to_bbox(label))
            plot_one_point(ax, label.x, label.y)
        fig.savefig(output_name)


if __name__ == "__main__":
    find_placement_and_draw()
