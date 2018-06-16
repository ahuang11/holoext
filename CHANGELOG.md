### 1.0.4
Allow from `from holoext import Mod` and `from holoext import get_cmap`
Hide UserWarning from `matplotlib.use('agg')` if matplotlib.pyplot is already imported

### 1.0.3
Attempt fixing docs

### 1.0.2
Change title_format, title, xlabel, ylabel defaults in Mod from '' to None to better handle empty strings
Add functionality to adjust the limits of colorbar without the need to call redim.range
Add alias cmap (colorbar_cmap), legend_location (legend_position), zlim (colorbar_lim)
Readjust the auto sizing for height
Fix docstrings

### 1.0.1
Optimize slightly by reading NCL cmaps only when called and fix minor bug with inputting colormap lists.

### 1.0.0
"from holoext.bokeh import Mod" is now "from holoext.xbokeh import Mod"
Improved parsing of cmap string e.g. 'viridis_r_n=10_start=0.3_stop=0.7'

### 0.0.3
Improved flexibility with tools input to allow for customized tools
Allow colorbar_cmap=None
New save to svg functionality
Moved examples under docs
Utilized nbsphinx for docs instead of hacky html

### 0.0.2
Release on pip

### 0.0.1
Official release