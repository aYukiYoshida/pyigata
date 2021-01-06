# -*- coding: utf-8 -*-

from typing import List, Dict, Tuple, Union

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
from numpy import ndarray
import seaborn as sns

from ..util.extend import ExtendDict

# DEFAULT PARAMETERS
FIGURE_SIZE:Dict[str, int] = ExtendDict(x=16, y=9)
GRID_NUMBER = ExtendDict(v=1, h=1)
GRID_POSITION = ExtendDict(l=0.1, r=0.95, b=0.2, t=0.95)
GRID_SPACE = ExtendDict(w=0.03, h=0.02)
GRID_RATIO = ExtendDict(w=[1], h=[1])
FONT_SIZE = 25.0                       # font size
LABEL_FONT_SIZE = FONT_SIZE*0.8        # font size for label
LEGENG_FONT_SIZE = FONT_SIZE*0.5       # font size for legend
TICKS_FONT_SIZE = FONT_SIZE            # font size for ticks
COMMON_ALIGN = 'center'                # common alignment
VERTICAL_ALIGN = 'center'              # vertical alignment
HORIZONTAL_ALIGN = 'center'            # horizontal alignment
LINE_STYLE = 'solid'                   # line style
LINE_WIDTH = 2.0                       # line width
MARKER = 'o'                           # marker
PLOT_FORMAT = ','                      # format for plot with errors
MARKER_SIZE = 5.0                      # marker size
DPI = 100                              # resolution of the figure
IGFONT = ExtendDict(family='IPAexGothic')
COLORS = ExtendDict({
    'blue': sns.color_palette('muted').as_hex()[0],
    'orange': sns.color_palette('muted').as_hex()[1],
    'green': sns.color_palette('muted').as_hex()[2],
    'red': sns.color_palette('muted').as_hex()[3],
    'violet': sns.color_palette('muted').as_hex()[4],
    'brown': sns.color_palette('muted').as_hex()[5],
    'pink': sns.color_palette('muted').as_hex()[6],
    'gray': sns.color_palette('muted').as_hex()[7],
    'ocher': sns.color_palette('muted').as_hex()[8],
    'cyan': sns.color_palette('muted').as_hex()[9],
    'white': mcd.CSS4_COLORS['white'],
    'black': mcd.CSS4_COLORS['black'],
    'yellow': mcd.CSS4_COLORS['gold'],
    'peach': sns.color_palette("husl", 8).as_hex()[0],
    'emerald': sns.color_palette("husl", 8).as_hex()[4],
    'turquoise': sns.color_palette("husl", 8).as_hex()[5],
    'purple': sns.color_palette("husl", 8).as_hex()[6],
    'magenta': sns.color_palette("husl", 8).as_hex()[7],
})


def configure_figure(figsize: Tuple[int, int] = (FIGURE_SIZE.x, FIGURE_SIZE.y),
                     nrows: int = GRID_NUMBER.v, ncols: int = GRID_NUMBER.h,
                     left: float = GRID_POSITION.l, right: float = GRID_POSITION.r,
                     top: float = GRID_POSITION.t, bottom: float = GRID_POSITION.b,
                     wspace: float = GRID_SPACE.w, hspace: float = GRID_SPACE.h,
                     sharex: bool = True, sharey: bool = True,
                     width_ratios: List = GRID_RATIO.w, 
                     height_ratios: List = GRID_RATIO.h) -> (mpl.figure.Figure, Union[ndarray, mpl.axes.Subplot]):
    if sharex:
        sharex = 'col'
    if sharey:
        sharey = 'row'
    if nrows > GRID_NUMBER.v and height_ratios == GRID_RATIO.h:
        height_ratios = GRID_RATIO.h * nrows
    if ncols > GRID_NUMBER.v and width_ratios == GRID_RATIO.w:
        width_ratios = GRID_RATIO.w * ncols

    fig, ax = plt.subplots(
        nrows=nrows, ncols=ncols,
        sharex=sharex, sharey=sharey,
        figsize=figsize, dpi=DPI,
        gridspec_kw={'height_ratios': height_ratios, 'width_ratios': width_ratios})
    fig.subplots_adjust(
        left=left, right=right, bottom=bottom, top=top,
        wspace=wspace, hspace=hspace)
    # grd = fig.add_gridspec(grid_num_v,grid_num_h)
    return fig, ax


class SimplePlot(object):
    def __init__(self, configure:bool=True, **args) -> None:
        self.figsize: Tuple[int, int] = args.get('figsize', (FIGURE_SIZE.x, FIGURE_SIZE.y))
        self.nrows: int = args.get('nrows', GRID_NUMBER.v)
        self.ncols: int = args.get('ncols', GRID_NUMBER.h)
        self.left: float = args.get('left', GRID_POSITION.l)
        self.right: float = args.get('right', GRID_POSITION.r)
        self.top: float = args.get('top', GRID_POSITION.t)
        self.bottom: float = args.get('bottom', GRID_POSITION.b)
        self.wspace: float = args.get('wspace', GRID_SPACE['w'])
        self.hspace: float = args.get('hspace', GRID_SPACE.h)
        self.fsize: float = args.get('fsize', FONT_SIZE)
        self.labfsize: float = args.get('labfsize', LABEL_FONT_SIZE)
        self.legfsize: float = args.get('legfsize', LEGENG_FONT_SIZE)
        self.tckfsize: float = args.get('tckfsize', TICKS_FONT_SIZE)
        self.calign: str = args.get('calign', COMMON_ALIGN)
        self.valign: str = args.get('valign', VERTICAL_ALIGN)
        self.halign: str = args.get('halign', HORIZONTAL_ALIGN)
        self.lstyle: str = args.get('lstyle', LINE_STYLE)
        self.lwidth: float = args.get('lwidth', LINE_WIDTH)
        self.marker: str = args.get('marker', MARKER)
        self.pltfmt: str = args.get('pltfmt', PLOT_FORMAT)
        self.masize: float = args.get('masize', MARKER_SIZE)
        self.igfont: ExtendDict = args.get('igfont', IGFONT)
        self.colors: ExtendDict = args.get('colors', COLORS)
        self.sharex: bool = args.get('sharex', True)
        self.sharey: bool = args.get('sharey', True)
        self.width_ratios: List = args.get('width_ratios', GRID_RATIO.w)
        self.height_ratios: List = args.get('height_ratios', GRID_RATIO.h)
        if configure:
            self.configure()

    def configure(self) -> None:
        self.set_rcparams()
        self.fig, self.axes = configure_figure(
            figsize=self.figsize,
            nrows=self.nrows, ncols=self.ncols,
            left=self.left, right=self.right,
            top=self.top, bottom=self.bottom,
            wspace=self.wspace, hspace=self.hspace,
            sharex=self.sharex, sharey=self.sharey,
            width_ratios=self.width_ratios,
            height_ratios=self.height_ratios)

    def set_rcparams(self) -> None:
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['mathtext.fontset'] = 'cm'
        plt.rcParams['mathtext.rm'] = 'serif'
        plt.rcParams['axes.titleweight'] = 'bold'
        # plt.rcParams['axes.labelweight'] = 'bold'
        plt.rcParams['axes.linewidth'] = self.lwidth
        plt.rcParams['grid.linestyle'] = 'solid'
        plt.rcParams['grid.linewidth'] = 1.0
        plt.rcParams['grid.alpha'] = 0.2
        plt.rcParams['xtick.major.size'] = 8
        plt.rcParams['xtick.minor.size'] = 5
        plt.rcParams['xtick.major.width'] = self.lwidth
        plt.rcParams['xtick.minor.width'] = self.lwidth
        plt.rcParams['xtick.major.pad'] = 5
        plt.rcParams['ytick.major.size'] = 8
        plt.rcParams['xtick.top'] = True
        plt.rcParams['ytick.minor.size'] = 5
        plt.rcParams['ytick.major.width'] = self.lwidth
        plt.rcParams['ytick.minor.width'] = self.lwidth
        plt.rcParams['ytick.major.pad'] = 5
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['xtick.labelsize'] = self.labfsize
        plt.rcParams['ytick.labelsize'] = self.labfsize
        plt.rcParams['ytick.right'] = True

    def get(self, name):
        return self.__dict__.get(name)

    def set(self, name, value):
        self.__dict__[name] = value
        return self.get(name)
