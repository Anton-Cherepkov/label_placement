import matplotlib.pyplot as plt
import matplotlib.patches as patches

from ..label import BoundingBox


def create_empty_figure(xlim: float, ylim: float):
    fig = plt.figure(figsize=(10, 10), dpi=300)
    ax = fig.subplots()
    ax.set_xlim([0, xlim])
    ax.set_ylim([0, ylim])
    return fig, ax


def plot_one_box(ax, bbox: BoundingBox):
    xy = (bbox.x1, bbox.y1)
    width = bbox.get_width()
    height = bbox.get_height()

    rect = patches.Rectangle(
        xy=xy,
        width=width,
        height=height,
        lw=1,
        edgecolor='r',
        facecolor='none'
    )
    ax.add_patch(rect)


def plot_one_point(ax, x: float, y: float):
    ax.scatter([x], [y], lw=2, color='r')
