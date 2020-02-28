# -*- coding: utf-8 -*- 

import matplotlib as _mpl
import matplotlib.pyplot as _plt 
import matplotlib._color_data as _mcd
import numpy as _np
import seaborn as _sns
from box import Box as _box

from .core import Common
from .core import Union as _union

###-----------------------------------------------------------------------
### DEFAULT PARAMETERS
###-----------------------------------------------------------------------
FIGSIZE = _box({'x':12, 'y':6})
GRIDNUM = _box({'v':1, 'h':1})
GRIDSIZE = _box({'left': 0.1, 'right': 0.95, 'bottom': 0.2, 'top': 0.95})
GRIDSPACE = _box({'w':0.03, 'h':0.02})
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
IGFONT = _box({'family':'IPAexGothic'})
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
def get_figsize() -> _box:
###-----------------------------------------------------------------------
    return FIGSIZE


###-----------------------------------------------------------------------
def get_gridnum() -> _box:
###-----------------------------------------------------------------------
    return GRIDNUM


###-----------------------------------------------------------------------
def get_gridsize() -> _box:
###-----------------------------------------------------------------------
    return GRIDSIZE


###-----------------------------------------------------------------------
def get_gridspace() -> _box:
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
def get_igfont() -> _box:
###-----------------------------------------------------------------------
    return IGFONT


###-----------------------------------------------------------------------
def get_colors() -> _box:
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
        figsize_x :int = FIGSIZE.x,
        figsize_y :int = FIGSIZE.y,
        grid_num_v :int = GRIDNUM.v,
        grid_num_h :int = GRIDNUM.h,
        grid_l  :float = GRIDSIZE.left,
        grid_r  :float = GRIDSIZE.right,
        grid_b  :float = GRIDSIZE.bottom,
        grid_t  :float = GRIDSIZE.top,
        grid_ws :float = GRIDSPACE.w,
        grid_hs :float = GRIDSPACE.h,
        sharex :bool = True,
        sharey :bool = True
        ) -> (_mpl.figure.Figure, _union[_np.ndarray, _mpl.axes.Subplot]):
###-----------------------------------------------------------------------
    if sharex:
        sharex = 'col'
    if sharey:
        sharey = 'row'
    fig,ax = _plt.subplots(grid_num_v,grid_num_h,
                figsize=(figsize_x, figsize_y),
                sharex=sharex,sharey=sharey)
    fig.subplots_adjust(
        left=grid_l, right=grid_r,
        bottom=grid_b, top=grid_t,
        wspace=grid_ws, hspace=grid_hs)
    grd = fig.add_gridspec(grid_num_v,grid_num_h)
    return fig, ax


###-----------------------------------------------------------------------
class Parameters(Common):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    ### CLASS VARIABLES
    ###-------------------------------------------------------------------


    ###-------------------------------------------------------------------
    def __init__(self,loglv: int = 1) -> None:
    ###-------------------------------------------------------------------
        super().__init__(loglv=loglv)
        self.figsize = get_figsize()
        self.gridnum = get_gridnum()
        self.gridsize = get_gridsize()
        self.gridspace = get_gridspace()
        self.fsize = get_fsize()
        self.labfsize = get_labfsize()
        self.legfsize = get_legfsize()
        self.tckfsize = get_tckfsize()
        self.calign = get_calign()
        self.valign = get_valign()
        self.halign = get_halign()
        self.lstyle = get_lstyle()
        self.lwidth = get_lwidth()
        self.marker = get_marker()
        self.pltfmt = get_pltfmt()
        self.masize = get_masize()
        self.igfont = get_igfont()
        self.colors = get_colors()


    ###-------------------------------------------------------------------
    def get_figsize(self) -> _box:
    ###-------------------------------------------------------------------
        return FIGSIZE


    ###-------------------------------------------------------------------
    def get_gridnum(self) -> _box:
    ###-------------------------------------------------------------------
        return GRIDNUM


    ###-------------------------------------------------------------------
    def get_gridsize(self) -> _box:
    ###-------------------------------------------------------------------
        return GRIDSIZE


    ###-------------------------------------------------------------------
    def get_gridspace(self) -> _box:
    ###-------------------------------------------------------------------
        return GRIDSPACE


    ###-------------------------------------------------------------------
    def get_fsize(self) -> float:
    ###-------------------------------------------------------------------
        return FSIZE


    ###-------------------------------------------------------------------
    def get_labfsize(self) -> float:
    ###-------------------------------------------------------------------
        return LABFSIZE


    ###-------------------------------------------------------------------
    def get_legfsize(self) -> float:
    ###-------------------------------------------------------------------
        return LEGFSIZE


    ###-------------------------------------------------------------------
    def get_tckfsize(self) -> float:
    ###-------------------------------------------------------------------
        return TCKFSIZE


    ###-------------------------------------------------------------------
    def get_calign(self) -> str:
    ###-------------------------------------------------------------------
        return CALIGN


    ###-------------------------------------------------------------------
    def get_valign(self) -> str:
    ###-------------------------------------------------------------------
        return VALIGN


    ###-------------------------------------------------------------------
    def get_halign(self) -> str:
    ###-------------------------------------------------------------------
        return HALIGN


    ###-------------------------------------------------------------------
    def get_lstyle(self) -> str:
    ###-------------------------------------------------------------------
        return LSTYLE


    ###-------------------------------------------------------------------
    def get_lwidth(self) -> float:
    ###-------------------------------------------------------------------
        return LWIDTH


    ###-------------------------------------------------------------------
    def get_marker(self) -> str:
    ###-------------------------------------------------------------------
        return MARKER


    ###-------------------------------------------------------------------
    def get_pltfmt(self) -> str:
    ###-------------------------------------------------------------------
        return PLTFMT


    ###-------------------------------------------------------------------
    def get_masize(self) -> float:
    ###-------------------------------------------------------------------
        return MASIZE


    ###-------------------------------------------------------------------
    def get_igfont(self) -> _box:
    ###-------------------------------------------------------------------
        return IGFONT


    ###-------------------------------------------------------------------
    def get_colors(self) -> _box:
    ###-------------------------------------------------------------------
        return COLORS