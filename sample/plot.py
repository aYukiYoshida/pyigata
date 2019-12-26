# -*- coding: utf-8 -*- 

import matplotlib as _mpl
import matplotlib.pyplot as _plt 
import matplotlib.gridspec as _grs
import matplotlib._color_data as _mcd
import numpy as _np
import seaborn as _sns
from box import Box as _box
from typing import Union as _union

from .core import Common

###-----------------------------------------------------------------------
### DEFAULT PARAMETERS
###-----------------------------------------------------------------------
FIGSIZE = [ 12, 6 ]                # figure size (x,y)
GRIDNUM = [  1, 1 ]                # grid number (v,h)
GRIDSIZE = { 'left': 0.1, 'right': 0.95, 
             'bottom': 0.2, 'top': 0.95 }
GRIDSPACE = [ 0.03, 0.02 ]         # grid space (w,h)
FSIZE = 25.0                       # font size
LABFSIZE = FSIZE*0.8               # font size for label
LEGFSIZE = FSIZE*0.5               # font size for legend
TCKFSIZE = FSIZE                   # font size for ticks
CALIGN = 'center'                  # common alignment
VALIGN = 'center'                  # vertival alignment
HALIGN = 'center'                  # horizontal alignment
LSTYLE = 'solid'                   # line style
LWIDTH = 2.0                       # line width
MARKER = 'o'                       # marker
PLTFMT = ','                       # format for plot with errors
MASIZE = 3.0                       # marker size
IGFONT = {'family':'IPAexGothic'}
COLORS = _box({ 
    'blue'      : _sns.color_palette('muted').as_hex()[0],
    'orange'    : _sns.color_palette('muted').as_hex()[1],
    'green'     : _sns.color_palette('muted').as_hex()[2],
    'red'       : _sns.color_palette('muted').as_hex()[3],
    'violet'    : _sns.color_palette('muted').as_hex()[4], 
    'brown'     : _sns.color_palette('muted').as_hex()[5],
    'pink'      : _sns.color_palette('muted').as_hex()[6],
    'gray'      : _sns.color_palette('muted').as_hex()[7],
    'ocher'     : _sns.color_palette('muted').as_hex()[8],
    'cyan'      : _sns.color_palette('muted').as_hex()[9],
    'white'     : _mcd.CSS4_COLORS['white'],
    'black'     : _mcd.CSS4_COLORS['black'],
    'yellow'    : _mcd.CSS4_COLORS['gold'],
    'peach'     : _sns.color_palette("husl", 8).as_hex()[0],
    'emerald'   : _sns.color_palette("husl", 8).as_hex()[4],
    'turquoise' : _sns.color_palette("husl", 8).as_hex()[5],
    'purple'    : _sns.color_palette("husl", 8).as_hex()[6], 
    'magenta'   : _sns.color_palette("husl", 8).as_hex()[7],
})


###-----------------------------------------------------------------------
def get_figsize() -> float:
###-----------------------------------------------------------------------
    return FIGSIZE


###-----------------------------------------------------------------------
def get_gridnum() -> float:
###-----------------------------------------------------------------------
    return GRIDNUM


###-----------------------------------------------------------------------
def get_gridsize() -> float:
###-----------------------------------------------------------------------
    return GRIDSIZE


###-----------------------------------------------------------------------
def get_gridspace() -> float:
###-----------------------------------------------------------------------
    return GRIDSPACE


###-----------------------------------------------------------------------
def get_fsize() -> float:
###-----------------------------------------------------------------------
    return FSIZE


###-----------------------------------------------------------------------
def get_labfsize() -> float:
###-----------------------------------------------------------------------
    return LABFSIZE


###-----------------------------------------------------------------------
def get_legfsize() -> float:
###-----------------------------------------------------------------------
    return LEGFSIZE


###-----------------------------------------------------------------------
def get_tckfsize() -> float:
###-----------------------------------------------------------------------
    return TCKFSIZE


###-----------------------------------------------------------------------
def get_calign() -> str:
###-----------------------------------------------------------------------
    return CALIGN


###-----------------------------------------------------------------------
def get_valign() -> str:
###-----------------------------------------------------------------------
    return VALIGN


###-----------------------------------------------------------------------
def get_halign() -> str:
###-----------------------------------------------------------------------
    return HALIGN


###-----------------------------------------------------------------------
def get_lstyle() -> str:
###-----------------------------------------------------------------------
    return LSTYLE


###-----------------------------------------------------------------------
def get_lwidth() -> float:
###-----------------------------------------------------------------------
    return LWIDTH


###-----------------------------------------------------------------------
def get_marker() -> str:
###-----------------------------------------------------------------------
    return MARKER


###-----------------------------------------------------------------------
def get_pltfmt() -> str:
###-----------------------------------------------------------------------
    return PLTFMT


###-----------------------------------------------------------------------
def get_masize() -> float:
###-----------------------------------------------------------------------
    return MASIZE


###-----------------------------------------------------------------------
def get_igfont() -> dict:
###-----------------------------------------------------------------------
    return IGFONT


###-----------------------------------------------------------------------
def get_colors() -> dict:
###-----------------------------------------------------------------------
    return COLORS


###-----------------------------------------------------------------------
def set_rcparams() -> None:
###-----------------------------------------------------------------------
    _plt.rcParams['font.family'] = 'Times New Roman'
    _plt.rcParams['mathtext.fontset'] = 'cm'
    _plt.rcParams['mathtext.rm'] = 'serif'
    _plt.rcParams['axes.titleweight'] = 'bold'
    # _plt.rcParams['axes.labelweight'] = 'bold'
    _plt.rcParams['axes.linewidth'] = LWIDTH
    _plt.rcParams['grid.linestyle'] = 'solid'
    _plt.rcParams['grid.linewidth'] = 1.0
    _plt.rcParams['grid.alpha'] = 0.2
    _plt.rcParams['xtick.major.size'] = 8
    _plt.rcParams['xtick.minor.size'] = 5
    _plt.rcParams['xtick.major.width'] = LWIDTH
    _plt.rcParams['xtick.minor.width'] = LWIDTH
    _plt.rcParams['xtick.major.pad'] = 5
    _plt.rcParams['ytick.major.size'] = 8
    _plt.rcParams['xtick.top'] = True
    _plt.rcParams['ytick.minor.size'] = 5
    _plt.rcParams['ytick.major.width'] = LWIDTH
    _plt.rcParams['ytick.minor.width'] = LWIDTH
    _plt.rcParams['ytick.major.pad'] = 5
    _plt.rcParams['xtick.direction'] = 'in'
    _plt.rcParams['ytick.direction'] = 'in'
    _plt.rcParams['xtick.labelsize'] = LABFSIZE
    _plt.rcParams['ytick.labelsize'] = LABFSIZE
    _plt.rcParams['ytick.right'] = True


###-----------------------------------------------------------------------
def configure_figure(
        figsize_x :int = FIGSIZE[0],
        figsize_y :int = FIGSIZE[1],
        grid_num_v :int = GRIDNUM[0],
        grid_num_h :int = GRIDNUM[1],
        grid_l  :float = GRIDSIZE['left'],
        grid_r  :float = GRIDSIZE['right'],
        grid_b  :float = GRIDSIZE['bottom'],
        grid_t  :float = GRIDSIZE['top'],
        grid_ws :float = GRIDSPACE[0],
        grid_hs :float = GRIDSPACE[1],
        ) -> (_mpl.figure.Figure, _union[_np.ndarray, _mpl.axes.Subplot]):
###-----------------------------------------------------------------------
    fig = _plt.figure(figsize=(figsize_x, figsize_y))
    grd = _grs.GridSpec(grid_num_v,grid_num_h)
    grd.update(left=grid_l, right=grid_r, bottom=grid_b, top=grid_t,
                wspace=grid_ws, hspace=grid_hs)

    if grid_num_v == 1 and grid_num_h == 1:
        ax = fig.add_subplot(grd[0,0])
    elif (grid_num_v > 1 and grid_num_h == 1):
        ax = list()
        for v in range(grid_num_v):
            ax.append(fig.add_subplot(grd[v,0]))
        ax = _np.array(ax)
    elif (grid_num_v == 1 and grid_num_h > 1):
        ax = list()
        for h in range(grid_num_h):
            ax.append(fig.add_subplot(grd[0,h]))
        ax = _np.array(ax)
    elif (grid_num_v > 1 and grid_num_h > 1):
        ax_parent = list()
        for h in range(grid_num_h):
            ax_child = list()
            for v in range(grid_num_v):
                ax_child.append(fig.add_subplot(grd[v,h]))
            ax_parent.append(ax_child)
        ax = _np.array(ax_parent)
    return fig, ax


###-----------------------------------------------------------------------
class Parameters(Common):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    ### CLASS VARIABLES
    ###-------------------------------------------------------------------
    figsize = get_figsize()
    gridnum = get_gridnum()
    gridsize = get_gridsize()
    gridspace = get_gridspace()
    fsize = get_fsize()
    labfsize = get_labfsize()
    legfsize = get_legfsize()
    tckfsize = get_tckfsize()
    calign = get_calign()
    valign = get_valign()
    halign = get_halign()
    lstyle = get_lstyle()
    lwidth = get_lwidth()
    marker = get_marker()
    pltfmt = get_pltfmt()
    masize = get_masize()
    igfont = get_igfont()
    colors = get_colors() 

    ###-------------------------------------------------------------------
    def __init__(self,loglv: int = 1) -> None:
    ###-------------------------------------------------------------------
        super().__init__(loglv=loglv)
