# -*- coding: utf-8 -*- 

import inspect
import matplotlib as mpl
import seaborn as sns

from .common import Common


###-----------------------------------------------------------------------
class Parameters(Common):
###-----------------------------------------------------------------------
    ###-------------------------------------------------------------------
    ### CLASS VARIABLES
    ###-------------------------------------------------------------------
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
    comcol = 'black'                   # common color
    bakcol = 'white'                   # back color
    pltcol = sns.color_palette()[0]    # plot color
    makcol = comcol                    # mark color
    lincol = sns.color_palette()[2]    # line color
    modcol = sns.color_palette()[1]    # model color
    igfont = {'family':'IPAexGothic'}


    ###-------------------------------------------------------------------
    def __init__(self,loglv: int) -> None:
    ###-------------------------------------------------------------------
        super().__init__(loglv=loglv)


    ###-------------------------------------------------------------------
    def get_fsize(self) -> float:
    ###-------------------------------------------------------------------
        return fsize


    ###-------------------------------------------------------------------
    def get_labfsize(self) -> float:
    ###-------------------------------------------------------------------
        return labfsize


    ###-------------------------------------------------------------------
    def get_legfsize(self) -> float:
    ###-------------------------------------------------------------------
        return legfsize


    ###-------------------------------------------------------------------
    def get_tckfsize(self) -> float:
    ###-------------------------------------------------------------------
        return tckfsize


    ###-------------------------------------------------------------------
    def get_calign(self) -> str:
    ###-------------------------------------------------------------------
        return calign


    ###-------------------------------------------------------------------
    def get_valign(self) -> str:
    ###-------------------------------------------------------------------
        return valign


    ###-------------------------------------------------------------------
    def get_halign(self) -> str:
    ###-------------------------------------------------------------------
        return halign


    ###-------------------------------------------------------------------
    def get_lstyle(self) -> str:
    ###-------------------------------------------------------------------
        return lstyle


    ###-------------------------------------------------------------------
    def get_lwidth(self) -> float:
    ###-------------------------------------------------------------------
        return lwidth


    ###-------------------------------------------------------------------
    def get_pltfmt(self) -> str:
    ###-------------------------------------------------------------------
        return pltfmt


    ###-------------------------------------------------------------------
    def get_masize(self) -> float:
    ###-------------------------------------------------------------------
        return masize


    ###-------------------------------------------------------------------
    def get_comcol(self) -> str:
    ###-------------------------------------------------------------------
        return comcol


    ###-------------------------------------------------------------------
    def get_bakcol(self) -> str:
    ###-------------------------------------------------------------------
        return bakcol


    ###-------------------------------------------------------------------
    def get_pltcol(self) -> str:
    ###-------------------------------------------------------------------
        return pltcol


    ###-------------------------------------------------------------------
    def get_makcol(self) -> str:
    ###-------------------------------------------------------------------
        return makcol


    ###-------------------------------------------------------------------
    def get_lincol(self) -> str:
    ###-------------------------------------------------------------------
        return lincol


    ###-------------------------------------------------------------------
    def get_modcol(self) -> str:
    ###-------------------------------------------------------------------
        return modcol


    ###-------------------------------------------------------------------
    def get_igfont(self) -> dict:
    ###-------------------------------------------------------------------
        return igfont


    ###-------------------------------------------------------------------
    def set_rcparams(self) -> None:
    ###-------------------------------------------------------------------
        self.logger('START',0,inspect.currentframe())
        mpl.pyplot.rcParams['font.family'] = 'Times New Roman'
        mpl.pyplot.rcParams['mathtext.fontset'] = 'cm'
        mpl.pyplot.rcParams['mathtext.rm'] = 'serif'
        mpl.pyplot.rcParams['axes.titleweight'] = 'bold'
        # mpl.pyplot.rcParams['axes.labelweight'] = 'bold'
        mpl.pyplot.rcParams['axes.linewidth'] = self.lwidth
        mpl.pyplot.rcParams['grid.linestyle'] = 'solid'
        mpl.pyplot.rcParams['grid.linewidth'] = 1.0
        mpl.pyplot.rcParams['grid.alpha'] = 0.2
        mpl.pyplot.rcParams['xtick.major.size'] = 8
        mpl.pyplot.rcParams['xtick.minor.size'] = 5
        mpl.pyplot.rcParams['xtick.major.width'] = self.lwidth
        mpl.pyplot.rcParams['xtick.minor.width'] = self.lwidth
        mpl.pyplot.rcParams['xtick.major.pad'] = 5
        mpl.pyplot.rcParams['ytick.major.size'] = 8
        mpl.pyplot.rcParams['xtick.top'] = True
        mpl.pyplot.rcParams['ytick.minor.size'] = 5
        mpl.pyplot.rcParams['ytick.major.width'] = self.lwidth
        mpl.pyplot.rcParams['ytick.minor.width'] = self.lwidth
        mpl.pyplot.rcParams['ytick.major.pad'] = 5
        mpl.pyplot.rcParams['xtick.direction'] = 'in'
        mpl.pyplot.rcParams['ytick.direction'] = 'in'
        mpl.pyplot.rcParams['xtick.labelsize'] = self.labfsize
        mpl.pyplot.rcParams['ytick.labelsize'] = self.labfsize
        mpl.pyplot.rcParams['ytick.right'] = True
        self.logger('END',0,inspect.currentframe())


###---------------------------------------------------------------
def configure_figure(
        figsize_x :int = 12,
        figsize_y :int = 6,
        grid_num_v :int = 1,
        grid_num_h :int = 1,
        grid_l  :float = 0.1,
        grid_r  :float = 0.95,
        grid_b  :float = 0.2,
        grid_t  :float = 0.95,
        grid_ws :float = 0.03,
        grid_hs :float = 0.02
        ) -> (mpl.figure.Figure,mpl.gridspec.GridSpec):
###---------------------------------------------------------------
    fig = mpl.pyplot.figure(figsize=(figsize_x, figsize_y))
    grd = mpl.gridspec.GridSpec(grid_num_v,grid_num_h)
    grd.update(left=grid_l, right=grid_r, bottom=grid_b, top=grid_t,
                wspace=grid_ws, hspace=grid_hs)
    # ax = fig.add_subplot(grd[0,0])
    return fig,grd