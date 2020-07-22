# -*- coding: utf-8 -*- 

from typing import Union

import matplotlib as mpl
import matplotlib.pyplot as plt 
import matplotlib._color_data as mcd
from numpy import ndarray
import seaborn as sns

from ..util.common import Common
from ..util.object import ObjectLikeDict


###-----------------------------------------------------------------------
### DEFAULT PARAMETERS
###-----------------------------------------------------------------------
FIGSIZE = ObjectLikeDict({'x':16, 'y':9})
GRIDNUM = ObjectLikeDict({'v':1, 'h':1})
GRIDSIZE = ObjectLikeDict({'left': 0.1, 'right': 0.95, 'bottom': 0.2, 'top': 0.95})
GRIDSPACE = ObjectLikeDict({'w':0.03, 'h':0.02})
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
IGFONT = ObjectLikeDict({'family':'IPAexGothic'})
COLORS = ObjectLikeDict({ 
    'blue'      : sns.color_palette('muted').as_hex()[0],
    'orange'    : sns.color_palette('muted').as_hex()[1],
    'green'     : sns.color_palette('muted').as_hex()[2],
    'red'       : sns.color_palette('muted').as_hex()[3],
    'violet'    : sns.color_palette('muted').as_hex()[4], 
    'brown'     : sns.color_palette('muted').as_hex()[5],
    'pink'      : sns.color_palette('muted').as_hex()[6],
    'gray'      : sns.color_palette('muted').as_hex()[7],
    'ocher'     : sns.color_palette('muted').as_hex()[8],
    'cyan'      : sns.color_palette('muted').as_hex()[9],
    'white'     : mcd.CSS4_COLORS['white'],
    'black'     : mcd.CSS4_COLORS['black'],
    'yellow'    : mcd.CSS4_COLORS['gold'],
    'peach'     : sns.color_palette("husl", 8).as_hex()[0],
    'emerald'   : sns.color_palette("husl", 8).as_hex()[4],
    'turquoise' : sns.color_palette("husl", 8).as_hex()[5],
    'purple'    : sns.color_palette("husl", 8).as_hex()[6], 
    'magenta'   : sns.color_palette("husl", 8).as_hex()[7],
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
        ) -> (mpl.figure.Figure, Union[ndarray, mpl.axes.Subplot]):
###-----------------------------------------------------------------------
    if sharex:
        sharex = 'col'
    if sharey:
        sharey = 'row'
    fig,ax = plt.subplots(grid_num_v,grid_num_h,
                figsize=(figsize_x, figsize_y),
                sharex=sharex,sharey=sharey)
    fig.subplots_adjust(
        left=grid_l, right=grid_r,
        bottom=grid_b, top=grid_t,
        wspace=grid_ws, hspace=grid_hs)
    grd = fig.add_gridspec(grid_num_v,grid_num_h)
    return fig, ax


class PlotEnvironment(object):

    def __init__(
        self, figsize=FIGSIZE, gridnum=GRIDNUM,
        gridsize=GRIDSIZE, gridspace=GRIDSPACE, fsize=FSIZE,
        labfsize=LABFSIZE, legfsize=LEGFSIZE, tckfsize=TCKFSIZE,
        calign=CALIGN, valign=VALIGN, halign=HALIGN,
        lstyle=LSTYLE, lwidth=LWIDTH, marker=MARKER,
        pltfmt=PLTFMT, masize=MASIZE, igfont=IGFONT,
        colors=COLORS, sharex=True, sharey=True) -> None:

        self.figsize = figsize
        self.gridnum = gridnum
        self.gridsize = gridsize
        self.gridspace = gridspace
        self.fsize = fsize
        self.labfsize = labfsize
        self.legfsize = legfsize
        self.tckfsize = tckfsize
        self.calign = calign
        self.valign = valign
        self.halign = halign
        self.lstyle = lstyle
        self.lwidth = lwidth
        self.marker = marker
        self.pltfmt = pltfmt
        self.masize = masize
        self.igfont = igfont
        self.colors = colors
        self.sharex = sharex
        self.sharey = sharey
        self.set_rcparams()
        self.configure_figure()
        

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


    def configure_figure(self) -> None:
        self.fig, self.axes = configure_figure(
            self.figsize.x,self.figsize.y,
            self.gridnum.v,self.gridnum.h,
            self.gridsize.left,self.gridsize.right,
            self.gridsize.bottom,self.gridsize.top,
            self.gridspace.w,self.gridspace.h,
            self.sharex,self.sharey)


    def get_sharex(self) -> bool:
        return self.sharex


    def set_sharex(self, share:bool) -> bool:
        self.sharex = share
        return self.sharex


    def get_sharey(self) -> bool:
        return self.sharey


    def set_sharey(self, share:bool) -> bool:
        self.sharey = share
        return self.sharey


    def get_figsize(self) -> ObjectLikeDict:
        return self.figsize


    def set_figsize(self, x:int, y:int) -> ObjectLikeDict:
        self.figsize = ObjectLikeDict(zip(FIGSIZE.keys(),[x,y]))
        return self.figsize


    def get_gridnum(self) -> ObjectLikeDict:
        return self.gridnum


    def set_gridnum(self, v:int=1, h:int=1) -> ObjectLikeDict:
        self.gridnum = ObjectLikeDict(zip(GRIDNUM.keys(),[v,h]))
        return self.gridnum


    def get_gridsize(self) -> ObjectLikeDict:
        return self.gridsize


    def set_gridsize(self, l:float, r:float, b:float, t:float) -> ObjectLikeDict:
        self.gridsize = ObjectLikeDict(zip(GRIDSIZE.keys(),[l,r,b,t]))
        return self.gridsize


    def get_gridspace(self) -> ObjectLikeDict:
        return self.gridspace


    def set_gridspace(self, w:float,h:float) -> ObjectLikeDict:
        self.gridspace = ObjectLikeDict(zip(GRIDSPACE.keys(),[w,h]))
        return self.gridspace


    def get_fsize(self) -> float:
        return self.fsize


    def set_fsize(self, s:float) -> float:
        self.fsize = s        
        return self.fsize


    def get_labfsize(self) -> float:
        return self.labfsize


    def set_labfsize(self, s:float) -> float:
        self.labfsize = s
        return self.labfsize


    def get_legfsize(self) -> float:
        return self.legfsize


    def set_legfsize(self, s:float) -> float:
        self.legfsize = s
        return self.legfsize


    def get_tckfsize(self) -> float:
        return self.tckfsize


    def set_tckfsize(self, s:float) -> float:
        self.tckfsize = s
        return self.tckfsize


    def get_calign(self) -> str:
        return self.calign


    def set_calign(self, s:str) -> str:
        self.calign = s
        return self.calign


    def get_valign(self) -> str:
        return self.valign


    def set_valign(self, s:str) -> str:
        self.valign = s
        return self.valign


    def get_halign(self) -> str:
        return self.halign


    def set_halign(self, s:str) -> str:
        self.halign = s
        return self.halign


    def get_lstyle(self) -> str:
        return self.lstyle


    def set_lstyle(self, s:str) -> str:
        self.lstyle = s
        return self.lstyle


    def get_lwidth(self) -> float:
        return self.lwidth


    def set_lwidth(self, w:float) -> float:
        self.lwidth = w
        return self.lwidth


    def get_marker(self) -> str:
        return self.marker


    def set_marker(self, m:str) -> str:
        self.marker = m
        return self.marker


    def getpltfmt(self) -> str:
        return self.pltfmt


    def setpltfmt(self, f:str) -> str:
        self.pltfmt = f
        return self.pltfmt


    def get_masize(self) -> float:
        return self.masize


    def set_masize(self, s:float) -> float:
        self.masize = s
        return self.masize


    def get_igfont(self) -> ObjectLikeDict:
        return self.igfont


    def get_colors(self) -> ObjectLikeDict:
        return self.colors