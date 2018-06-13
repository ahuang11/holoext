# HoloExt - HoloViews Extension Mod v1.0.3

### An extension to beautify your plots and process.

## HoloExt features:
1. 'intelligent' resizing and activation of tools in addition to grid lines
2. a straightforward method of saving to file `.apply(plot, 'name_of_file')`
3. immediate application of a minimalistic style to plots
4. [keywords like `xlim`, `ylim`, `xlabel`, `ylabel`, `title` can be used](https://holoext.readthedocs.io/en/latest/examples/matplotlib_xlim_ylim_xlabel_ylabel_title.html)
5. [user forgiving parsing of toolbar and legend locs](https://holoext.readthedocs.io/en/latest/examples/amend_loc_keyword_showcase.html)
6. [automatic discretization of color bars](https://holoext.readthedocs.io/en/latest/examples/changing_colorbar_cmap.html)
7. [color maps (color tables) from NCAR Command Language (NCL)](https://holoext.readthedocs.io/en/latest/examples/changing_colorbar_cmap.html)
8. [And more!](https://holoext.readthedocs.io/en/latest/examples/user_guide.html)

## Here's some motivation to [get started!](https://holoext.readthedocs.io/en/latest/examples/quick_start.html)

### Do your plotting as usual in Holoviews.
```python
curves = hv.Curve(df, 'day', 'min_temp_f', label='Max Temp', group='KCMI') * \
         hv.Curve(df, 'day', 'max_temp_f', label='Min Temp', group='KCMI')
curves  # curve without mod
```
![Before Mod](https://raw.githubusercontent.com/ahuang11/holoext/master/docs/examples/static_output/quick_start_before.png)

### Then simply apply the mod!
```python
from holoext.xbokeh import Mod

Mod().apply(curves)
```
This automatically increases figure size, applies a minimalistic look, and adds the hover tool, albeit hidden in the toolbar.

However, these mods are not fixed in stone; you can easily adjust it:<br />
`Mod(width=300, height=300, tools='default')`

If you would like to show the hover tool in the toolbar, it's easily done too:<br />
`Mod(show_hover=True)`

![After Mod](https://raw.githubusercontent.com/ahuang11/holoext/master/docs/examples/static_output/quick_start_after.png)

### Apply more settings easily and save to .html by passing in any string argument to .apply()
```python
mod_curves = Mod(
    xlabel='Date', ylabel='Temperature [F]',
    tools=['xpan', 'xwheel_zoom', 'save', 'reset', 'hover']
).apply(curves, save='html_output/kcmi_2016_2017_temps')
mod_curves
```
![After Mod with Settings](https://raw.githubusercontent.com/ahuang11/holoext/master/docs/examples/static_output/quick_start_final.png)

## Check out the [gallery](https://holoext.readthedocs.io/en/latest/docs/examples/gallery.html) to see it work for all types of plots like these!

![Station Temperature and Precipitation](https://raw.githubusercontent.com/ahuang11/holoext/master/docs/examples/static_output/gallery_station_temperature_and_precipitation.png)

![ORD Wind Speed and Wind Direction](https://raw.githubusercontent.com/ahuang11/holoext/master/docs/examples/static_output/gallery_ord_wind_speed_wind_dir.png)

## HOW TO GET IT:
Method 1
1. `pip install holoext`
2. Ensure your packages version (`pip list`) match with ones listed in requirements.txt

Method 2
1. Type `git clone https://github.com/ahuang11/holoext`
2. Go into holoext folder (where setup.py is)
3. Type `pip install -e .`

### Check out the docs [here](https://holoext.readthedocs.io/en/latest/index.html)!

### Random, but awesome, tips: https://github.com/ahuang11/ahhsumtips
