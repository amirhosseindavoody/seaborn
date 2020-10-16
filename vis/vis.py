__version__ = '0.0'
__author__ = 'Amirhossein Davoody'

import numbers
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib
from scipy import stats
from itertools import cycle
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
import anal
import itertools
import matplotlib.tri as tri

import warnings

matplotlib.rcParams['figure.facecolor'] = 'w'



def transparent_boxplot(ax, alpha=0.3):
    '''
    make boxplot from seaborn transparent

    Parameters:
    -----------
    ax : Matplotlib.Axes
        matplotlib axis object from seaborn
    alpha : float, optional
        alpha transparency parameter

    Returns:
    --------
    ax : Matplotlib.Axes
        matplotlib axis object from seaborn
    '''
    for patch in ax.artists:
        r, g, b, a = patch.get_facecolor()
        patch.set_facecolor((r, g, b, alpha))

    return ax


def rotate_xticks(ax, rotation=90, horizontalalignment='right', fontweight='light', fontsize='x-large):
    '''
    rotate xticks labels for a matplotlib axis

    Parameters:
    -----------
    ax : Matplotlib.Axes
        matplotlib axis object from seaborn
    rotation : float, optional
        rotation angle, default = 90
    horizontalalignment : str, optional
        horizontal alignment, default is 'right'
    fontweight : str, optional
        font weight, default is 'light'
    fontsize : str, optional
        font size, default is 'x-large'

    Returns:
    --------
    ax : Matplotlib.Axes
        matplotlib axis object from seaborn
    '''

    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=rotation,
        horizontalalignment=horizontalalignment,
        fontweight=fontweight,
        fontsize=fontsize,
    )

    returns ax