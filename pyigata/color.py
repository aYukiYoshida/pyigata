# -*- coding: utf-8 -*-
import matplotlib._color_data as mcd
import seaborn as sns

from pyigata.constant import ConstantMeta


class StringColor(metaclass=ConstantMeta):
    BLACK = ("\033[30m",)  # (文字)黒
    RED = ("\033[31m",)  # (文字)赤
    GREEN = ("\033[32m",)  # (文字)緑
    YELLOW = ("\033[33m",)  # (文字)黄
    BLUE = ("\033[34m",)  # (文字)青
    MAGENTA = ("\033[35m",)  # (文字)マゼンタ
    CYAN = ("\033[36m",)  # (文字)シアン
    WHITE = ("\033[37m",)  # (文字)白
    DEFAULT = ("\033[39m",)  # 文字色をデフォルトに戻す
    BOLD = ("\033[1m",)  # 太字
    UNDERLINE = ("\033[4m",)  # 下線
    INVISIBLE = ("\033[08m",)  # 不可視
    REVERSE = ("\033[07m",)  # 文字色と背景色を反転
    BG_BLACK = ("\033[40m",)  # (背景)黒
    BG_RED = ("\033[41m",)  # (背景)赤
    BG_GREEN = ("\033[42m",)  # (背景)緑
    BG_YELLOW = ("\033[43m",)  # (背景)黄
    BG_BLUE = ("\033[44m",)  # (背景)青
    BG_MAGENTA = ("\033[45m",)  # (背景)マゼンタ
    BG_CYAN = ("\033[46m",)  # (背景)シアン
    BG_WHITE = ("\033[47m",)  # (背景)白
    BG_DEFAULT = ("\033[49m",)  # 背景色をデフォルトに戻す
    RESET = "\033[0m"  # 全てリセット


class PlotColor(metaclass=ConstantMeta):
    BLUE = (sns.color_palette("muted").as_hex()[0],)
    ORANGE = (sns.color_palette("muted").as_hex()[1],)
    GREEN = (sns.color_palette("muted").as_hex()[2],)
    RED = (sns.color_palette("muted").as_hex()[3],)
    VIOLET = (sns.color_palette("muted").as_hex()[4],)
    BROWN = (sns.color_palette("muted").as_hex()[5],)
    PINK = (sns.color_palette("muted").as_hex()[6],)
    GRAY = (sns.color_palette("muted").as_hex()[7],)
    OCHER = (sns.color_palette("muted").as_hex()[8],)
    CYAN = (sns.color_palette("muted").as_hex()[9],)
    WHITE = (mcd.CSS4_COLORS["white"],)
    BLACK = (mcd.CSS4_COLORS["black"],)
    YELLOW = (mcd.CSS4_COLORS["gold"],)
    PEACH = (sns.color_palette("husl", 8).as_hex()[0],)
    EMERALD = (sns.color_palette("husl", 8).as_hex()[4],)
    TURQUOISE = (sns.color_palette("husl", 8).as_hex()[5],)
    PURPLE = (sns.color_palette("husl", 8).as_hex()[6],)
    MAGENTA = sns.color_palette("husl", 8).as_hex()[7]
