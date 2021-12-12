# -*- coding: utf-8 -*-

from typing import List, Tuple, Union

import matplotlib.pyplot as plt
from matplotlib.axes import Subplot
from matplotlib.figure import Figure
from numpy import ndarray

from .color import PlotColor
from .extend import ExtendDict


# DEFAULT PARAMETERS
class PlotProperty(object):
    FIGURE_SIZE: Tuple[int, int] = (16, 9)
    ROWS_NUMBER: int = 1
    COLS_NUMBER: int = 1
    GRID_POSITION_LEFT: float = 0.1
    GRID_POSITION_RIGHT: float = 0.95
    GRID_POSITION_BOTTOM: float = 0.2
    GRID_POSITION_TOP: float = 0.95
    GRID_SPACE_WIDTH: float = 0.03
    GRID_SPACE_HEIGHT: float = 0.02
    GRID_RATIO_WIDTH: List[float] = [1.0]
    GRID_RATIO_HEIGHT: List[float] = [1.0]
    FONT_SIZE: float = 25.0
    LABEL_FONT_SIZE = FONT_SIZE * 0.8
    LEGENG_FONT_SIZE = FONT_SIZE * 0.5
    TICKS_FONT_SIZE = FONT_SIZE
    COMMON_ALIGN = "center"
    VERTICAL_ALIGN = "center"
    HORIZONTAL_ALIGN = "center"
    LINE_STYLE = "solid"
    LINE_WIDTH = 2.0
    MARKER = "o"
    PLOT_FORMAT = ","
    MARKER_SIZE = 5.0
    DPI = 100  # resolution of the figure in unit of dot per inch
    IGFONT = ExtendDict(family="IPAexGothic")


def configure_figure(
    figsize: Tuple[int, int] = PlotProperty.FIGURE_SIZE,
    nrows: int = PlotProperty.ROWS_NUMBER,
    ncols: int = PlotProperty.COLS_NUMBER,
    left: float = PlotProperty.GRID_POSITION_LEFT,
    right: float = PlotProperty.GRID_POSITION_RIGHT,
    top: float = PlotProperty.GRID_POSITION_TOP,
    bottom: float = PlotProperty.GRID_POSITION_BOTTOM,
    wspace: float = PlotProperty.GRID_SPACE_WIDTH,
    hspace: float = PlotProperty.GRID_SPACE_HEIGHT,
    sharex: bool = True,
    sharey: bool = True,
    width_ratios: List[float] = PlotProperty.GRID_RATIO_WIDTH,
    height_ratios: List[float] = PlotProperty.GRID_RATIO_HEIGHT,
) -> Tuple[Figure, Union[ndarray, Subplot]]:

    sharex_ = "col" if sharex else None
    sharey_ = "row" if sharey else None
    if (
        nrows > PlotProperty.ROWS_NUMBER
        and height_ratios == PlotProperty.GRID_RATIO_HEIGHT
    ):
        height_ratios = PlotProperty.GRID_RATIO_HEIGHT * nrows
    if (
        ncols > PlotProperty.COLS_NUMBER
        and width_ratios == PlotProperty.GRID_RATIO_WIDTH
    ):
        width_ratios = PlotProperty.GRID_RATIO_WIDTH * ncols

    fig, ax = plt.subplots(
        nrows=nrows,
        ncols=ncols,
        sharex=sharex_,
        sharey=sharey_,
        figsize=figsize,
        dpi=PlotProperty.DPI,
        gridspec_kw={"height_ratios": height_ratios, "width_ratios": width_ratios},
    )
    fig.subplots_adjust(
        left=left, right=right, bottom=bottom, top=top, wspace=wspace, hspace=hspace
    )
    # grd = fig.add_gridspec(grid_num_v,grid_num_h)
    return fig, ax


class SimplePlot(object):
    def __init__(self, configure: bool = True, **args) -> None:
        self.figsize: Tuple[int, int] = args.get("figsize", PlotProperty.FIGURE_SIZE)
        self.nrows: int = args.get("nrows", PlotProperty.ROWS_NUMBER)
        self.ncols: int = args.get("ncols", PlotProperty.COLS_NUMBER)
        self.left: float = args.get("left", PlotProperty.GRID_POSITION_LEFT)
        self.right: float = args.get("right", PlotProperty.GRID_POSITION_RIGHT)
        self.top: float = args.get("top", PlotProperty.GRID_POSITION_TOP)
        self.bottom: float = args.get("bottom", PlotProperty.GRID_POSITION_BOTTOM)
        self.wspace: float = args.get("wspace", PlotProperty.GRID_SPACE_WIDTH)
        self.hspace: float = args.get("hspace", PlotProperty.GRID_SPACE_HEIGHT)
        self.fsize: float = args.get("fsize", PlotProperty.FONT_SIZE)
        self.labfsize: float = args.get("labfsize", PlotProperty.LABEL_FONT_SIZE)
        self.legfsize: float = args.get("legfsize", PlotProperty.LEGENG_FONT_SIZE)
        self.tckfsize: float = args.get("tckfsize", PlotProperty.TICKS_FONT_SIZE)
        self.calign: str = args.get("calign", PlotProperty.COMMON_ALIGN)
        self.valign: str = args.get("valign", PlotProperty.VERTICAL_ALIGN)
        self.halign: str = args.get("halign", PlotProperty.HORIZONTAL_ALIGN)
        self.lstyle: str = args.get("lstyle", PlotProperty.LINE_STYLE)
        self.lwidth: float = args.get("lwidth", PlotProperty.LINE_WIDTH)
        self.marker: str = args.get("marker", PlotProperty.MARKER)
        self.pltfmt: str = args.get("pltfmt", PlotProperty.PLOT_FORMAT)
        self.masize: float = args.get("masize", PlotProperty.MARKER_SIZE)
        self.igfont: ExtendDict = args.get("igfont", PlotProperty.IGFONT)
        self.colors = args.get("colors", PlotColor)
        self.sharex: bool = args.get("sharex", True)
        self.sharey: bool = args.get("sharey", True)
        self.width_ratios: List = args.get(
            "width_ratios", PlotProperty.GRID_RATIO_WIDTH
        )
        self.height_ratios: List = args.get(
            "height_ratios", PlotProperty.GRID_RATIO_HEIGHT
        )
        if configure:
            self.configure()

    def configure(self) -> None:
        self.set_rcparams()
        self.fig, self.axes = configure_figure(
            figsize=self.figsize,
            nrows=self.nrows,
            ncols=self.ncols,
            left=self.left,
            right=self.right,
            top=self.top,
            bottom=self.bottom,
            wspace=self.wspace,
            hspace=self.hspace,
            sharex=self.sharex,
            sharey=self.sharey,
            width_ratios=self.width_ratios,
            height_ratios=self.height_ratios,
        )

    def set_rcparams(self) -> None:
        plt.rcParams["font.family"] = "Times New Roman"
        plt.rcParams["mathtext.fontset"] = "cm"
        plt.rcParams["mathtext.rm"] = "serif"
        plt.rcParams["axes.titleweight"] = "bold"
        # plt.rcParams['axes.labelweight'] = 'bold'
        plt.rcParams["axes.linewidth"] = self.lwidth
        plt.rcParams["grid.linestyle"] = "solid"
        plt.rcParams["grid.linewidth"] = 1.0
        plt.rcParams["grid.alpha"] = 0.2
        plt.rcParams["xtick.major.size"] = 8
        plt.rcParams["xtick.minor.size"] = 5
        plt.rcParams["xtick.major.width"] = self.lwidth
        plt.rcParams["xtick.minor.width"] = self.lwidth
        plt.rcParams["xtick.major.pad"] = 5
        plt.rcParams["ytick.major.size"] = 8
        plt.rcParams["xtick.top"] = True
        plt.rcParams["ytick.minor.size"] = 5
        plt.rcParams["ytick.major.width"] = self.lwidth
        plt.rcParams["ytick.minor.width"] = self.lwidth
        plt.rcParams["ytick.major.pad"] = 5
        plt.rcParams["xtick.direction"] = "in"
        plt.rcParams["ytick.direction"] = "in"
        plt.rcParams["xtick.labelsize"] = self.labfsize
        plt.rcParams["ytick.labelsize"] = self.labfsize
        plt.rcParams["ytick.right"] = True
