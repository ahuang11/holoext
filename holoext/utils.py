import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, rgb2hex

# https://www.ncl.ucar.edu/Document/Graphics/color_tables.shtml
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
NCL_CMAPS = pd.read_pickle(os.path.join(THIS_DIR, 'data', 'ncl_cmaps.pkl'))
NCL_CMAP_NAMES = NCL_CMAPS.columns.tolist()
DEFAULT_N = 7


def get_color_list(cmap, hexcodes=False, **kwargs):
    """
    Converts a registered colormap into a list of RGB tuples or hexcodes

    Args:
        cmap_name (mpl.cmap/str): actual colormap or name of color
        hexcodes (boolean): whether to return a list of hexcodes
        kwargs (kwargs): additional keyword arguments

    Returns:
        :return cmap: (list): list of RGB tuples or hexcodes
    """
    if isinstance(cmap, str):
        if cmap in NCL_CMAP_NAMES:
            cmap = NCL_CMAPS[cmap].values[0]
        else:
            cmap = plt.get_cmap(cmap)

    if not hexcodes:
        color_list = [cmap(i)[:3] for i in range(cmap.N)]
    else:
        color_list = [rgb2hex(cmap(i)[:3])
                      for i in range(cmap.N)]

    return color_list


def get_cmap(colors, n=None, r=False, start=0, stop=1, **kwargs):
    """
    Converts a list of colors into a color map or discretizes a cmap
    http://matplotlib.org/examples/color/colormaps_reference.html
    http://www.ncl.ucar.edu/Document/Graphics/color_table_gallery.shtml

    Args:
        colors (list/str): a list containing RGB or Python/NCL cmap name
        n (int): number of colors in cmap
        r (boolean): reverse colormap
        start (scalar): value to start on the cmap between 0 and 1
        stop (scalar): value to end on the cmap between 0 and 1
        kwargs (kwargs): additional keyword arguments

    Returns:
        cmap (mpl.cmap): color map
    """
    try:
        if '_r' in colors:
            colors = colors[:-2]
            r = True
    except:
        pass

    if colors in NCL_CMAP_NAMES:
        if r:
            color_list = get_color_list(NCL_CMAPS[colors].values[0])[::-1]
            cmap = LinearSegmentedColormap.from_list('cmap',
                                                     colors=color_list)
        else:
            cmap = NCL_CMAPS[colors].values[0]
        if n is None:
            n = NCL_CMAPS[colors].values[1]
    else:
        if isinstance(colors, str):
            if r:
                colors += '_r'
            if n is None:
                n = DEFAULT_N
            cmap = plt.get_cmap(colors, **kwargs)
        elif isinstance(colors, LinearSegmentedColormap):
            return colors
        else:
            if r:
                colors = colors[::-1]
            if n is None and len(colors) > 2:
                n = len(colors)
            elif n is None:
                n = DEFAULT_N
            if not isinstance(colors[0], str):
                if (np.array(colors) > 1).any():
                    for i, tup in enumerate(colors):
                        colors[i] = np.array(tup) / 255.
            cmap = LinearSegmentedColormap.from_list('mycmap', colors=colors,
                                                     **kwargs)
    colors = cmap(np.linspace(start, stop, cmap.N))

    return LinearSegmentedColormap.from_list('mycmap', colors=colors, N=n)


def flatten(container):
    """
    Flattens a list/tuple with ANY number of levels of nesting, not just one.
    Adapted from: https://stackoverflow.com/questions/10823877/
    what-is-the-fastest-way-to-flatten-arbitrarily-nested-lists-in-python

    Args:
        container (list/tuple): a nested list or tuple

    Returns:
        cmap (generator): generator of unnested container
    """
    for i in container:
        if isinstance(i, (list, tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i


def tidy_fn(fn):
    """
    Cleans up a string to be used as a valid file name

    Args:
        fn (str): file name to be cleansed

    Returns:
        tidied_fn (str): tidied file name
    """
    fn = ''.join(x for x in fn if (x.isalnum() or x in "[]()._- "))
    return fn.lower().replace(' ', '_').replace(':', '')
