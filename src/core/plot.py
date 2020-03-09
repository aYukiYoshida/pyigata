# -*- coding: utf-8 -*- 

import matplotlib as _mpl
import matplotlib.pyplot as _plt 
import matplotlib._color_data as _mcd
import numpy as _np
import seaborn as _sns
from box import Box as _box

from ..util.common import Common
from ..util.common import Union as _union


###-----------------------------------------------------------------------
### DEFAULT PARAMETERS
###-----------------------------------------------------------------------
FIGSIZE = _box({'x':16, 'y':9})
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
def configure_figure(
        figsize_x :int=FIGSIZE.x,
        figsize_y :int=FIGSIZE.y,
        grid_num_v :int=GRIDNUM.v,
        grid_num_h :int=GRIDNUM.h,
        grid_l  :float=GRIDSIZE.left,
        grid_r  :float=GRIDSIZE.right,
        grid_b  :float=GRIDSIZE.bottom,
        grid_t  :float=GRIDSIZE.top,
        grid_ws :float=GRIDSPACE.w,
        grid_hs :float=GRIDSPACE.h,
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
class Plotter(object):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    ### CLASS VARIABLES
    ###-------------------------------------------------------------------
    figsize = FIGSIZE
    gridnum = GRIDNUM
    gridsize = GRIDSIZE
    gridspace = GRIDSPACE
    fsize = FSIZE
    labfsize = LABFSIZE
    legfsize = LEGFSIZE
    tckfsize = TCKFSIZE
    calign = CALIGN
    valign = VALIGN
    halign = HALIGN
    lstyle = LSTYLE
    lwidth = LWIDTH
    marker = MARKER
    pltfmt = PLTFMT
    masize = MASIZE
    igfont = IGFONT
    colors = COLORS
    sharex = True
    sharey = True


    ###-------------------------------------------------------------------
    def __init__(self) -> None:
    ###-------------------------------------------------------------------
        pass


    @classmethod
    ###-------------------------------------------------------------------
    def configure_figure(cls) -> (_mpl.figure.Figure, _union[_np.ndarray, _mpl.axes.Subplot]):
    ###-------------------------------------------------------------------
        return configure_figure(
            cls.figsize.x,cls.figsize.y,
            cls.gridnum.v,cls.gridnum.h,
            cls.gridsize.left,cls.gridsize.right,
            cls.gridsize.bottom,cls.gridsize.top,
            cls.gridspace.w,cls.gridspace.h,
            cls.sharex,cls.sharey)


    @classmethod
    ###-------------------------------------------------------------------
    def set_rcparams(cls) -> None:
    ###-------------------------------------------------------------------
        set_rcparams()
        _plt.rcParams['axes.linewidth'] = cls.lwidth
        _plt.rcParams['xtick.major.width'] = cls.lwidth
        _plt.rcParams['xtick.minor.width'] = cls.lwidth
        _plt.rcParams['ytick.major.width'] = cls.lwidth
        _plt.rcParams['ytick.minor.width'] = cls.lwidth
        _plt.rcParams['xtick.labelsize'] = cls.labfsize
        _plt.rcParams['ytick.labelsize'] = cls.labfsize


    @classmethod
    ###-------------------------------------------------------------------
    def get_sharex(cls) -> bool:
    ###-------------------------------------------------------------------
        return cls.sharex


    @classmethod
    ###-------------------------------------------------------------------
    def set_sharex(cls,share:bool) -> bool:
    ###-------------------------------------------------------------------
        cls.sharex = share
        return cls.sharex


    @classmethod
    ###-------------------------------------------------------------------
    def get_sharey(cls) -> bool:
    ###-------------------------------------------------------------------
        return cls.sharey


    @classmethod
    ###-------------------------------------------------------------------
    def set_sharey(cls,share:bool) -> bool:
    ###-------------------------------------------------------------------
        cls.sharey = share
        return cls.sharey


    @classmethod
    ###-------------------------------------------------------------------
    def get_figsize(cls) -> _box:
    ###-------------------------------------------------------------------
        return cls.figsize


    @classmethod
    ###-------------------------------------------------------------------
    def set_figsize(cls,x:int,y:int) -> _box:
    ###-------------------------------------------------------------------
        cls.figsize = _box(zip(FIGSIZE.keys(),[x,y]))
        return cls.figsize


    @classmethod
    ###-------------------------------------------------------------------
    def get_gridnum(cls) -> _box:
    ###-------------------------------------------------------------------
        return cls.gridnum


    @classmethod
    ###-------------------------------------------------------------------
    def set_gridnum(cls,v:int=1,h:int=1) -> _box:
    ###-------------------------------------------------------------------
        cls.gridnum = _box(zip(GRIDNUM.keys(),[v,h]))
        return cls.gridnum


    @classmethod
    ###-------------------------------------------------------------------
    def get_gridsize(cls) -> _box:
    ###-------------------------------------------------------------------
        return cls.gridsize


    @classmethod
    ###-------------------------------------------------------------------
    def set_gridsize(cls,l:float,r:float,b:float,t:float) -> _box:
    ###-------------------------------------------------------------------
        cls.gridsize = _box(zip(GRIDSIZE.keys(),[l,r,b,t]))
        return cls.gridsize


    @classmethod
    ###-------------------------------------------------------------------
    def get_gridspace(cls) -> _box:
    ###-------------------------------------------------------------------
        return cls.gridspace


    @classmethod
    ###-------------------------------------------------------------------
    def set_gridspace(cls,w:float,h:float) -> _box:
    ###-------------------------------------------------------------------
        cls.gridspace = _box(zip(GRIDSPACE.keys(),[w,h]))
        return cls.gridspace


    @classmethod
    ###-------------------------------------------------------------------
    def get_fsize(cls) -> float:
    ###-------------------------------------------------------------------
        return cls.fsize


    @classmethod
    ###-------------------------------------------------------------------
    def set_fsize(cls,s:float) -> float:
    ###-------------------------------------------------------------------
        cls.figsize = s        
        return cls.fsize


    @classmethod
    ###-------------------------------------------------------------------
    def get_labfsize(cls) -> float:
    ###-------------------------------------------------------------------
        return cls.labfsize


    @classmethod
    ###-------------------------------------------------------------------
    def set_labfsize(cls,s:float) -> float:
    ###-------------------------------------------------------------------
        cls.labfsize = s
        return cls.labfsize


    @classmethod
    ###-------------------------------------------------------------------
    def get_legfsize(cls) -> float:
    ###-------------------------------------------------------------------
        return cls.legfsize


    @classmethod
    ###-------------------------------------------------------------------
    def set_legfsize(cls,s:float) -> float:
    ###-------------------------------------------------------------------
        cls.legfsize = s
        return cls.legfsize


    @classmethod
    ###-------------------------------------------------------------------
    def get_tckfsize(cls) -> float:
    ###-------------------------------------------------------------------
        return cls.tckfsize


    @classmethod
    ###-------------------------------------------------------------------
    def set_tckfsize(cls,s:float) -> float:
    ###-------------------------------------------------------------------
        cls.tckfsize = s
        return cls.tckfsize


    @classmethod
    ###-------------------------------------------------------------------
    def get_calign(cls) -> str:
    ###-------------------------------------------------------------------
        return cls.calign


    @classmethod
    ###-------------------------------------------------------------------
    def set_calign(cls,s:str) -> str:
    ###-------------------------------------------------------------------
        cls.calign = s
        return cls.calign


    @classmethod
    ###-------------------------------------------------------------------
    def get_valign(cls) -> str:
    ###-------------------------------------------------------------------
        return cls.valign


    @classmethod
    ###-------------------------------------------------------------------
    def set_valign(cls,s:str) -> str:
    ###-------------------------------------------------------------------
        cls.valign = s
        return cls.valign


    @classmethod
    ###-------------------------------------------------------------------
    def get_halign(cls) -> str:
    ###-------------------------------------------------------------------
        return cls.halign


    @classmethod
    ###-------------------------------------------------------------------
    def set_halign(cls,s:str) -> str:
    ###-------------------------------------------------------------------
        cls.halign = s
        return cls.halign


    @classmethod
    ###-------------------------------------------------------------------
    def get_lstyle(cls) -> str:
    ###-------------------------------------------------------------------
        return cls.lstyle


    @classmethod
    ###-------------------------------------------------------------------
    def set_lstyle(cls,s:str) -> str:
    ###-------------------------------------------------------------------
        cls.lstyle = s
        return cls.lstyle


    @classmethod
    ###-------------------------------------------------------------------
    def get_lwidth(cls) -> float:
    ###-------------------------------------------------------------------
        return cls.lwidth


    @classmethod
    ###-------------------------------------------------------------------
    def set_lwidth(cls,w:float) -> float:
    ###-------------------------------------------------------------------
        cls.lwidth = w
        return cls.lwidth


    @classmethod
    ###-------------------------------------------------------------------
    def get_marker(cls) -> str:
    ###-------------------------------------------------------------------
        return cls.marker


    @classmethod
    ###-------------------------------------------------------------------
    def set_marker(cls,m:str) -> str:
    ###-------------------------------------------------------------------
        cls.marker = m
        return cls.marker


    @classmethod
    ###-------------------------------------------------------------------
    def get_pltfmt(cls) -> str:
    ###-------------------------------------------------------------------
        return cls.pltfmt


    @classmethod
    ###-------------------------------------------------------------------
    def set_pltfmt(cls,f:str) -> str:
    ###-------------------------------------------------------------------
        cls.pltfmt = f
        return cls.pltfmt


    @classmethod
    ###-------------------------------------------------------------------
    def get_masize(cls) -> float:
    ###-------------------------------------------------------------------
        return cls.masize


    @classmethod
    ###-------------------------------------------------------------------
    def set_masize(cls,s:float) -> float:
    ###-------------------------------------------------------------------
        cls.masize = s
        return cls.masize


    @classmethod
    ###-------------------------------------------------------------------
    def get_igfont(cls) -> _box:
    ###-------------------------------------------------------------------
        return cls.igfont


    @classmethod
    ###-------------------------------------------------------------------
    def get_colors(cls) -> _box:
    ###-------------------------------------------------------------------
        return cls.colors