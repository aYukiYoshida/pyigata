# -*- coding: utf-8 -*- 

import matplotlib.pyplot as __plt 
import matplotlib.gridspec as __grs
import matplotlib._color_data as __mcd
import seaborn as __sns
from box import Box as __box


###-----------------------------------------------------------------------
### DEFAULT PARAMETERS
###-----------------------------------------------------------------------
figsize = [ 12, 6 ]                # figure size (x,y)
gridnum = [  1, 1 ]                # grid number (v,h)
gridsize = { 'left': 0.1, 'right': 0.95, 
             'bottom': 0.2, 'top': 0.95 }
gridspace = [ 0.03, 0.02 ]         # grid space (w,h)
fsize = 25.0                       # font size
labfsize = fsize*0.8               # font size for label
legfsize = fsize*0.5               # font size for legend
tckfsize = fsize                   # font size for ticks
calign = 'center'                  # common alignment
valign = 'center'                  # vertival alignment
halign = 'center'                  # horizontal alignment
lstyle = 'solid'                   # line style
lwidth = 2.0                       # line width
marker = 'o'                       # marker
pltfmt = ','                       # format for plot with errors
masize = 3.0                       # marker size
igfont = {'family':'IPAexGothic'}
color = __box({ 
    'blue'      : __sns.color_palette('muted').as_hex()[0],
    'orange'    : __sns.color_palette('muted').as_hex()[1],
    'green'     : __sns.color_palette('muted').as_hex()[2],
    'red'       : __sns.color_palette('muted').as_hex()[3],
    'violet'    : __sns.color_palette('muted').as_hex()[4], 
    'brown'     : __sns.color_palette('muted').as_hex()[5],
    'pink'      : __sns.color_palette('muted').as_hex()[6],
    'gray'      : __sns.color_palette('muted').as_hex()[7],
    'ocher'     : __sns.color_palette('muted').as_hex()[8],
    'cyan'      : __sns.color_palette('muted').as_hex()[9],
    'white'     : __mcd.CSS4_COLORS['white'],
    'black'     : __mcd.CSS4_COLORS['black'],
    'yellow'    : __mcd.CSS4_COLORS['gold'],
    'peach'     : __sns.color_palette("husl", 8).as_hex()[0],
    'emerald'   : __sns.color_palette("husl", 8).as_hex()[4],
    'turquoise' : __sns.color_palette("husl", 8).as_hex()[5],
    'purple'    : __sns.color_palette("husl", 8).as_hex()[6], 
    'magenta'   : __sns.color_palette("husl", 8).as_hex()[7],
})


###-----------------------------------------------------------------------
def get_figsize() -> float:
###-----------------------------------------------------------------------
    return figsize


###-----------------------------------------------------------------------
def get_gridnum() -> float:
###-----------------------------------------------------------------------
    return gridnum


###-----------------------------------------------------------------------
def get_gridsize() -> float:
###-----------------------------------------------------------------------
    return gridsize


###-----------------------------------------------------------------------
def get_gridspace() -> float:
###-----------------------------------------------------------------------
    return gridspace


###-----------------------------------------------------------------------
def get_fsize() -> float:
###-----------------------------------------------------------------------
    return fsize


###-----------------------------------------------------------------------
def get_labfsize() -> float:
###-----------------------------------------------------------------------
    return labfsize


###-----------------------------------------------------------------------
def get_legfsize(self) -> float:
###-----------------------------------------------------------------------
    return legfsize


###-----------------------------------------------------------------------
def get_tckfsize(self) -> float:
###-----------------------------------------------------------------------
    return tckfsize


###-----------------------------------------------------------------------
def get_calign(self) -> str:
###-----------------------------------------------------------------------
    return calign


###-----------------------------------------------------------------------
def get_valign(self) -> str:
###-----------------------------------------------------------------------
    return valign


###-----------------------------------------------------------------------
def get_halign(self) -> str:
###-----------------------------------------------------------------------
    return halign


###-----------------------------------------------------------------------
def get_lstyle(self) -> str:
###-----------------------------------------------------------------------
    return lstyle


###-----------------------------------------------------------------------
def get_lwidth(self) -> float:
###-----------------------------------------------------------------------
    return lwidth


###-----------------------------------------------------------------------
def get_pltfmt(self) -> str:
###-----------------------------------------------------------------------
    return pltfmt


###-----------------------------------------------------------------------
def get_masize(self) -> float:
###-----------------------------------------------------------------------
    return masize


###-----------------------------------------------------------------------
def get_igfont() -> dict:
###-----------------------------------------------------------------------
    return igfont


###-----------------------------------------------------------------------
def get_color() -> dict:
###-----------------------------------------------------------------------
    return color


###-----------------------------------------------------------------------
def set_rcparams() -> None:
###-----------------------------------------------------------------------
    __plt.rcParams['font.family'] = 'Times New Roman'
    __plt.rcParams['mathtext.fontset'] = 'cm'
    __plt.rcParams['mathtext.rm'] = 'serif'
    __plt.rcParams['axes.titleweight'] = 'bold'
    # __plt.rcParams['axes.labelweight'] = 'bold'
    __plt.rcParams['axes.linewidth'] = lwidth
    __plt.rcParams['grid.linestyle'] = 'solid'
    __plt.rcParams['grid.linewidth'] = 1.0
    __plt.rcParams['grid.alpha'] = 0.2
    __plt.rcParams['xtick.major.size'] = 8
    __plt.rcParams['xtick.minor.size'] = 5
    __plt.rcParams['xtick.major.width'] = lwidth
    __plt.rcParams['xtick.minor.width'] = lwidth
    __plt.rcParams['xtick.major.pad'] = 5
    __plt.rcParams['ytick.major.size'] = 8
    __plt.rcParams['xtick.top'] = True
    __plt.rcParams['ytick.minor.size'] = 5
    __plt.rcParams['ytick.major.width'] = lwidth
    __plt.rcParams['ytick.minor.width'] = lwidth
    __plt.rcParams['ytick.major.pad'] = 5
    __plt.rcParams['xtick.direction'] = 'in'
    __plt.rcParams['ytick.direction'] = 'in'
    __plt.rcParams['xtick.labelsize'] = labfsize
    __plt.rcParams['ytick.labelsize'] = labfsize
    __plt.rcParams['ytick.right'] = True


###-----------------------------------------------------------------------
def configure_figure(
        figsize_x :int = figsize[0],
        figsize_y :int = figsize[1],
        grid_num_v :int = gridnum[0],
        grid_num_h :int = gridnum[1],
        grid_l  :float = gridsize['left'],
        grid_r  :float = gridsize['right'],
        grid_b  :float = gridsize['bottom'],
        grid_t  :float = gridsize['top'],
        grid_ws :float = gridspace[0],
        grid_hs :float = gridspace[1],
        ) -> (__plt.figure, __grs.GridSpec):
###-----------------------------------------------------------------------
    fig = __plt.figure(figsize=(figsize_x, figsize_y))
    grd = __grs.GridSpec(grid_num_v,grid_num_h)
    grd.update(left=grid_l, right=grid_r, bottom=grid_b, top=grid_t,
                wspace=grid_ws, hspace=grid_hs)
    # ax = fig.add_subplot(grd[0,0])
    return fig,grd