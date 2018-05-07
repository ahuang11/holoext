# fix order of hovertool
# add tests
# hover tool tips

# -*- coding: utf-8 -*-

import os
import holoviews as hv

from bokeh import models
from bokeh.io import export_svgs
from bokeh.plotting.helpers import _tool_from_string
from holoviews.plotting.bokeh.__init__ import associations

from holoext.utils import DEFAULT_N, get_cmap, flatten, tidy_fn

SVG_STR = 'svg'
BACKEND = 'bokeh'
HOVER_STR = 'hover'
DEFAULT_STR = 'default'
COLORBAR_STR = 'colorbar'

DEFAULT_WIDTH = 725
DEFAULT_HEIGHT = 600
DEFAULT_TITLE_FORMAT = '{label} {group} {dimensions}'

FIGURES = [item[0].name for item in associations.items()]
FIGURES.remove('AdjointLayout')  # bugs out (I think width/height)

DEFAULT_LABEL_SIZES = dict(
    title='1.65em',
    labels='1.2em',
    ticks='1.05em',
    legend='1.05em',
    legend_title='0.9em',
    colorbar='1.05em',
)

DEFAULT_TOOLS = dict(
    pan=models.PanTool(),
    box_zoom=models.BoxZoomTool(),
    wheel_zoom=models.WheelZoomTool(),
    save=models.SaveTool(),
    reset=models.ResetTool()
)


class Mod(object):
    def __init__(
            self,
            title_format='',
            title='',
            xlabel='',
            ylabel='',
            neaten_io=True,
            width=None,
            height=None,
            autosize=True,
            xlim=None,
            ylim=None,
            xticks=None,
            yticks=None,
            num_xticks=None,
            num_yticks=None,
            major_tick_alpha=0,
            minor_tick_alpha=0,
            axis_line_alpha=0,
            show_grid=True,
            xgridticks=None,
            ygridticks=None,
            grid_line_dash='solid',
            tools=None,
            show_hover=False,
            logo='normal',
            toolbar_location='above',
            legend_location='top_right',
            legend_orientation='horizontal',
            legend_background_fill_alpha=0.5,
            legend_border_line_alpha=0,
            legend_label_standoff=6,
            legend_glyph_width=15,
            legend_spacing=12,
            colorbar=True,
            colorbar_n=DEFAULT_N,
            colorbar_cmap='viridis',
            colorbar_title='',
            colorbar_label_align='center',
            colorbar_tick_alpha=0,
            colorbar_label_standoff=9,
            colorbar_outline_alpha=0,
            label_scaler=1.,
            label_font='arial',
            label_color='#5b5b5b',
            label_alpha=0.925,
            label_style='normal',
            merge_tools=False,
            framewise=False,
            axiswise=False,
            **plot_kwargs
            ):
        """Extension Mod for HoloViews' Bokeh Backend

        Applies a sleek, minimalistic look to HoloViews,
        and offers easy access to typical functionality
        like changing the figure size, adjusting ticks
        and limits, choosing tools, and saving to file.
        All args are optional.

        Args:
            title_format (str): title of figure; if both keywords, `title`
                and `title_format`, is used, `title` will be ignored
            title (str): title of figure; alias to title_format
            xlabel (str): label on the x axis; will be inactive if ''
            ylabel (str): label on the y axis; will be inactive if ''
            neaten_io (bool): whether to replace underscores with spaces

            width (scalar): width of the figure; default 725
            height (scalar): height of the figure; default 600
            autosize (bool): whether to use native width and height

            xlim (tuple): initial view's x-axis limits
            ylim (tuple): initial view's y-axis limits

            xticks (list): location of ticks on the x-axis
            yticks (list): location of ticks on the y-axis;
                if [] is provided, ticks on the x-axis are hidden
            num_xticks (int): desired  number of xticks to show
            num_yticks (int): desired number of yticks to show

            major_tick_alpha (scalar): opacity of axis major tick marks
            minor_tick_alpha (scalar): opacity of axis minor tick marks
            axis_line_alpha (scalar): opacity of axes

            show_grid (bool): whether to show grid lines
            xgridticks (list): location of grid lines on the x-axis;
                if None is provided, automatically match xticks
                if [] is provided, hides the grid lines on the x-axis
            ygridticks (list): location of grid lines on the y-axis;
                if None is provided, automatically match xticks
                if [] is provided, hides the grid lines on the y-axis
            grid_line_dash (str): the line dash of grid lines
                either: 'solid', 'dashed, 'dotted, 'dotdash, 'dashdot'

            tools (list): tools available to use in the toolbar;
                choices are: ['pan', 'box_zoom', 'wheel_zoom', 'save',
                'reset', 'box_select', 'lasso_select', 'poly_select',
                'tap', 'wheel_pan', 'undo', 'redo', 'save', 'zoom_in',
                'zoom_out', 'cross_hair', 'box_edit', 'point_draw',
                'poly_draw', 'poly_edit'] and the xy versions
            show_hover (bool): whether to show hover tools in toolbar;
                note that the hover tool's functionality is retained if False
            logo (str/bool): whether to show Bokeh's logo in toolbar
                choices are False or None, or 'gray' which desaturates the logo
            toolbar_location (str): location of toolbar
                either 'above', 'below', 'left', 'right' or None

            legend_location (str): region where the legend resides
                either 'top_left', 'top_center', 'top_right', 'center_left',
                'center', 'center_right', 'bottom_left',
                'bottom_center', 'bottom_right'
            legend_location (str): either: 'horizontal', 'vertical'
            legend_background_fill_alpha (scalar): background opacity
            legend_border_line_alpha (scalar): border line opacity
            legend_label_standoff (scalar): space between labels and glyph
            legend_glyph_width (scalar): length of legend glyph
            legend_spacing (scalar): space between each label

            colorbar (bool): show colorbar
            colorbar_n (int): number of colors in colorbar
            colorbar_cmap (str/mpl.cmap): colormap of colorbar
            colorbar_title (str): title of colorbar
            colorbar_label_align (str): alignment of labels
                either 'center', 'left', 'right'
            colorbar_tick_alpha (scalar): opacity of tick marks
            colorbar_label_standoff (scalar): distance from labels to colorbar
            colorbar_outline_alpha (scalar): opacity of colorbar's outline

            label_font (str): labels' font name
            label_color (str): labels' color with typical colors or hexcode
            label_alpha (scalar): labels' opacity
            label_style (str): labels' style; either normal, italic or bold
            label_scaler (scalar): percent of original label size
                original size = 1; double the size = 2

            merge_tools (bool): whether to merge all toolbars into one toolbar
                note that some functionality may be disabled if True

            framewise (bool): whether to have unique limits across frames
                default False, have all frames the same limits
            axiswise (bool): whether to have unique limits across axes
                default False, each plot will not have their own axes
        """
        if title_format != '':
            self.title_format = title_format
        elif title != '':
            self.title_format = title
        else:
            self.title_format = DEFAULT_TITLE_FORMAT

        self.xlabel = xlabel
        self.ylabel = ylabel

        self.width = width
        self.height = height
        self.autosize = autosize

        self.xlim = xlim
        self.ylim = ylim

        self.xticks = xticks
        self.yticks = yticks
        self.num_xticks = num_xticks
        self.num_yticks = num_yticks

        self.show_grid = show_grid
        self.xgridticks = xgridticks
        self.ygridticks = ygridticks
        self.grid_line_dash = grid_line_dash
        self.neaten_io = neaten_io

        self.major_tick_alpha = major_tick_alpha
        self.minor_tick_alpha = minor_tick_alpha
        self.axis_line_alpha = axis_line_alpha

        self.tools = tools
        self.show_hover = show_hover
        self.logo = logo
        self.toolbar_location = toolbar_location

        self.legend_location = legend_location
        self.legend_orientation = legend_orientation
        self.legend_background_fill_alpha = legend_background_fill_alpha
        self.legend_border_line_alpha = legend_border_line_alpha
        self.legend_label_standoff = legend_label_standoff
        self.legend_glyph_width = legend_glyph_width
        self.legend_spacing = legend_spacing

        self.colorbar = colorbar
        self.colorbar_n = colorbar_n
        self.colorbar_cmap = colorbar_cmap
        self.colorbar_title = colorbar_title
        self.colorbar_label_align = colorbar_label_align
        self.colorbar_tick_alpha = colorbar_tick_alpha
        self.colorbar_label_standoff = colorbar_label_standoff
        self.colorbar_outline_alpha = colorbar_outline_alpha

        self.label_font = label_font
        self.label_color = label_color
        self.label_alpha = label_alpha
        self.label_style = label_style.lower()
        self.label_scaler = label_scaler

        self.merge_tools = merge_tools
        self.framewise = framewise
        self.axiswise = axiswise

        self.plot_kwargs = plot_kwargs

        self.already_run = False
        self.p_list = []
        self.tools_dict = {}

    def _neaten_label(self, string):
        if self.neaten_io:
            return string.replace('_', ' ')
        else:
            return string

    def _style_label(self, axis, label=None, title_io=False):
        if title_io:
            axis.text = self._neaten_label(axis.text)
            axis.text_font = self.label_font
            axis.text_color = self.label_color
            axis.text_alpha = self.label_alpha
            axis.text_font_style = self.label_style
        else:
            if label == '':
                label = axis.axis_label
            axis.axis_label = self._neaten_label(label)
            axis.axis_label_text_font = self.label_font
            axis.axis_label_text_color = self.label_color
            axis.axis_label_text_alpha = self.label_alpha
            axis.axis_label_text_font_style = self.label_style

            axis.major_label_text_color = self.label_color
            axis.major_label_text_alpha = self.label_alpha
            axis.major_label_text_font_style = self.label_style

    def _clean_axis(self, axis):
        axis.major_tick_line_alpha = self.major_tick_alpha
        axis.minor_tick_line_alpha = self.minor_tick_alpha
        axis.axis_line_alpha = self.axis_line_alpha

    def _fix_axis_ticks(self, axis, x_io=True):
        if x_io and self.xticks is not None:
            axis.ticker = models.FixedTicker(ticks=list(self.xticks))
        elif not x_io and self.yticks is not None:
            axis.ticker = models.FixedTicker(ticks=list(self.yticks))

        if x_io and self.num_xticks is not None:
            axis.ticker.desired_num_ticks = self.num_xticks
        elif not x_io and self.num_yticks is not None:
            axis.ticker.desired_num_ticks = self.num_yticks

    def _fix_grid_ticks(self, grid, x_io=True):
        if x_io:
            if self.xgridticks is None and self.xticks is not None:
                self.xgridticks = list(self.xticks)
            if self.xgridticks is not None:
                grid.ticker = models.FixedTicker(ticks=list(self.xgridticks))
        elif not x_io:
            if self.ygridticks is None and self.yticks is not None:
                self.ygridticks = list(self.yticks)
            if self.ygridticks is not None:
                grid.ticker = models.FixedTicker(ticks=list(self.ygridticks))

    def _initialize_limits(self, p):
        if self.xlim is not None:
            p.x_range = models.Range1d(self.xlim[0], self.xlim[-1])
        if self.ylim is not None:
            p.y_range = models.Range1d(self.ylim[0], self.ylim[-1])

    @staticmethod
    def _flip_loc_keyword(loc):
        return '_'.join(loc.split('_')[::-1])

    def _amend_loc_keyword(self, loc, toolbar_io=False):
        if loc is not None:
            loc = loc.strip().replace(' ', '_')

            if toolbar_io:
                above_keyword = 'above'
                below_keyword = 'below'
            else:
                above_keyword = 'top'
                below_keyword = 'bottom'

            loc = (loc.replace('top', above_keyword)
                      .replace('above', above_keyword)
                      .replace('north', above_keyword)
                      .replace('upper', above_keyword)
                   )
            loc = (loc.replace('bottom', below_keyword)
                      .replace('below', below_keyword)
                      .replace('south', below_keyword)
                      .replace('lower', below_keyword)
                   )
            loc = (loc.replace('west', 'left')
                      .replace('east', 'right'))

            loc = loc.replace('middle', 'center')

            if 'top' in loc and not loc.startswith('top'):
                loc = self._flip_loc_keyword(loc)
            elif 'bottom' in loc and not loc.startswith('bottom'):
                loc = self._flip_loc_keyword(loc)
            elif 'center' in loc and not loc.startswith('center') and \
                    ('top' not in loc and 'bottom' not in loc):
                loc = self._flip_loc_keyword(loc)

            return loc.strip('_')

    def _set_axes(self, p):
        axes_labels_x_ios = [(p.xaxis, self.xlabel, True),
                             (p.yaxis, self.ylabel, False)]
        for xyaxes, xylabel, x_io in axes_labels_x_ios:
            for xyaxis in xyaxes:  # weirdly nested
                self._style_label(xyaxis, label=xylabel)
                self._clean_axis(xyaxis)
                self._fix_axis_ticks(xyaxis, x_io=x_io)
                if not x_io:  # someday integrate x and y
                    xyaxis.axis_label_standoff = 9
        self._initialize_limits(p)

    def _set_grids(self, p):
        if p not in self.p_list:  # don't rerun if already run
            grids_x_ios = [(p.xgrid, True), (p.ygrid, False)]
            for xygrids, x_io in grids_x_ios:
                for xygrid in xygrids:
                    self._fix_grid_ticks(xygrid, x_io=x_io)
                    xygrid.grid_line_dash = self.grid_line_dash

    def _set_tools(self, p):
        if p not in self.p_list:  # don't rerun if already run
            if self.tools is None:  # tools = None
                self.tools = [DEFAULT_STR, HOVER_STR]
            elif isinstance(self.tools, list):
                # ['wheel_zoom, default']
                if (all(isinstance(tool, str) for tool in self.tools)
                    and len(self.tools) == 1):
                        self.tools = self.tools[0].replace(' ', '').split(',')
                else:
                    # [HoverTool, 'default']
                    tool_list = []
                    for tool in self.tools:
                        if isinstance(tool, str):
                            tool_str_list = tool.replace(' ', '').split(',')
                            tool_list.extend(tool_str_list)
                        else:
                            tool_list.append(tool)
                    self.tools = tool_list
            elif isinstance(self.tools, str):  # tools = 'hover, default'
                self.tools = self.tools.replace(' ', '').split(',')
            elif not isinstance(self.tools, list):
                self.tools = [self.tools]

            tools = []
            for tool in p.tools:  # add hover tools
                if (isinstance(tool, models.HoverTool) and
                        HOVER_STR in self.tools):
                    tool.toggleable = self.show_hover
                    tools.append(tool)

            for tool in p.tools:  # default tools defined in HoloViews
                if DEFAULT_STR in self.tools:
                    # handles 'default' which offers all default tools
                    tools.extend(list(DEFAULT_TOOLS.values()))
                    break
                else:  # add default tools one by one
                    for default_name, default_tool in DEFAULT_TOOLS.items():
                        if (isinstance(tool, type(default_tool)) and
                                default_name in self.tools):
                            tools.append(tool)

            for tool in self.tools:
                if (tool not in DEFAULT_TOOLS.keys() and
                        tool not in [DEFAULT_STR, HOVER_STR]):
                    if isinstance(tool, str):
                        tools.append(_tool_from_string(tool))
                    elif tool:  # I forget why this logic works?
                        # handle customized hover tools
                        if isinstance(tool, models.HoverTool):
                            tool.toggleable = self.show_hover
                        tools.append(tool)
            self.tools_dict[p] = tools

        p.tools = self.tools_dict[p]

    def _set_toolbar(self, p):
        if p not in self.p_list:  # don't rerun if already run
            if not self.logo:
                self.logo = None

            p.toolbar.logo = self.logo
            p.toolbar_location = self._amend_loc_keyword(
                self.toolbar_location, toolbar_io=True)

    def _set_legend(self, p):
        legend = p.legend

        legend.location = self._amend_loc_keyword(
            self.legend_location, toolbar_io=False)
        legend.orientation = self.legend_orientation

        legend.label_text_color = self.label_color
        legend.label_text_alpha = self.label_alpha

        legend.background_fill_alpha = self.legend_background_fill_alpha
        legend.border_line_alpha = self.legend_border_line_alpha

        legend.label_standoff = self.legend_label_standoff
        legend.glyph_width = self.legend_glyph_width
        legend.spacing = self.legend_spacing

    def _adjust_state(self, plot, element):
        # the function that links mostly everything; used in finalize_hooks

        p = plot.state

        self._style_label(p.title, title_io=True)
        self._set_axes(p)
        self._set_grids(p)
        self._set_tools(p)
        self._set_toolbar(p)
        self._set_legend(p)

        self.p_list.append(p)

    def _scale_plots(self, obj):
        try:
            positions = list(zip(*obj.grid_items().keys()))
            rows = max(positions[0]) + 1  # it starts counting at 0
            cols = max(positions[1]) + 1
        except:
            rows = 1
            cols = 1

        if self.width is None:
            self.width = DEFAULT_WIDTH

        if cols != 1:
            self.width = int(self.width / cols * 1.25)

        if self.height is None:
            self.height = DEFAULT_HEIGHT

        if rows != 1 or cols != 1:
            self.height = int(self.height / (rows * 1.5))

        return rows, cols

    def _scale_labels(self, obj, rows, cols):
        row_col_scaler = max([rows, cols]) ** 0.05
        label_sizes = {}
        for label, label_size_str in DEFAULT_LABEL_SIZES.items():
            label_size = float(label_size_str[:-2])
            label_size_str = str(label_size *
                                 self.label_scaler /
                                 row_col_scaler)
            label_sizes[label] = label_size_str + 'em'
        return label_sizes

    def _get_figures_core(self, objs):
        if isinstance(objs, list):
            objs = [self._get_figures_core(plot) for plot in objs]
        elif isinstance(objs, (models.Column, models.Row)):
            objs = [self._get_figures_core(child) for child in objs.children
                    if not isinstance(child, (models.ToolbarBox,
                                              models.WidgetBox))]
        return objs

    def _get_figures(self, objs):
        try:
            return list(flatten(self._get_figures_core(objs)))
        except TypeError:
            return [self._get_figures_core(objs)]

    def _save_to_svg(self, bokeh_obj, save):
        figures = self._get_figures(bokeh_obj)
        for i, figure in enumerate(figures):
            figure.output_backend = SVG_STR

            if len(figures) != 1:
                if not os.path.exists(save):
                    os.mkdir(save)
                tidied_title = tidy_fn(figure.title.text)
                save_fp = os.path.join(
                    save, '{0}_{1}'.format(tidied_title, i))
            else:
                save_fp = save

            if not save_fp.endswith(SVG_STR):
                save_fp = '{0}.{1}'.format(save_fp, SVG_STR)

            export_svgs(figure, save_fp)

    def apply(self, obj, save='', fmt=None):
        """Applies settings from Mod() to a HoloViews object

        Args:
            obj (hv.object): HoloViews object
            save (str): file name of output;
                default is '' which does not save
            fmt (str): format of output file;
                choices are: ['html', 'json', 'auto', 'png',
                'widgets', 'scrubber', 'auto']
        """
        rows, cols = self._scale_plots(obj)
        label_sizes = self._scale_labels(obj, rows, cols)

        colorbar_dict = {
            'title': self.colorbar_title,
            'title_text_font': self.label_font,
            'title_text_alpha': self.label_alpha,
            'title_text_color': self.label_color,
            'title_text_font_size': label_sizes[COLORBAR_STR],
            'title_text_font_style': self.label_style,
            'major_label_text_font': self.label_font,
            'major_label_text_alpha': self.label_alpha,
            'major_label_text_color': self.label_color,
            'major_label_text_font_size': label_sizes[COLORBAR_STR],
            'major_label_text_font_style': self.label_style,
            'major_label_text_align': self.colorbar_label_align,
            'major_tick_line_alpha': self.colorbar_tick_alpha,
            'label_standoff': self.colorbar_label_standoff,
            'bar_line_alpha': self.colorbar_outline_alpha
        }
        label_sizes.pop(COLORBAR_STR)  # not included in holoviews

        if not isinstance(self.title_format, str):
            self.title_format = ''

        generic_plot_dict = dict(
            show_grid=self.show_grid,
            tools=[HOVER_STR],  # need to initialize it
            width=self.width,
            height=self.height,
            fontsize=label_sizes,
            merge_tools=self.merge_tools,
            colorbar=self.colorbar,
            colorbar_opts=colorbar_dict,
            title_format=self.title_format,
            finalize_hooks=[self._adjust_state],
            **self.plot_kwargs
        )

        table_plot_dict = dict(
            tools=[HOVER_STR],  # need to initialize it
            width=self.width,
            height=self.height,
            fontsize=label_sizes,
            merge_tools=self.merge_tools
        )

        if self.colorbar_cmap is not None:
            cmap = get_cmap(self.colorbar_cmap, n=self.colorbar_n)
        else:
            cmap = None
        generic_style_dict = dict(cmap=cmap)

        generic_norm_dict = dict(
            framewise=self.framewise,
            axiswise=self.axiswise
        )

        if not self.autosize or \
            isinstance(obj, hv.AdjointLayout) or \
                isinstance(obj, hv.GridSpace):
            generic_plot_dict.pop('width')
            generic_plot_dict.pop('height')

        plot_dict = {}
        style_dict = {}
        norm_dict = {}
        for figure in FIGURES:
            if figure != 'Table':
                plot_dict[figure] = generic_plot_dict
            else:
                plot_dict[figure] = table_plot_dict
            style_dict[figure] = generic_style_dict
            norm_dict[figure] = generic_norm_dict

        obj = obj.opts(plot=plot_dict, style=style_dict, norm=norm_dict)

        if save != '':
            renderer = hv.renderer(BACKEND)
            if fmt != SVG_STR:
                renderer.save(obj, save, fmt=fmt)
            else:
                bokeh_obj = renderer.get_plot(obj).state
                self._save_to_svg(bokeh_obj, save)

        return obj
