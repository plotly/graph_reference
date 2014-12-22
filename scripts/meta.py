from collections import OrderedDict

from meta_shortcuts import ValTypes, RequiredCond, Make
from meta_examples import MakeExamples

# -------------------------------------------------------------------------------
#
# Define meta-generation methods, one for each graph object in class MakeMeta()
#
# -------------------------------------------------------------------------------

class MakeMeta(list):
    '''@MakeMeta@ -- Meta-generating methods for each graph object!
    '''

    def __init__(self):
        ''' @make_meta@
        Initialize class as list,
        link `meta_shortcuts.py` instances to global variables
        '''
        self = []
        global val_types       # N.B no need to key_type self.val_types(...)
        val_types = ValTypes()
        global required_cond
        required_cond = RequiredCond()
        global make
        make = Make()

    def _stuff(self, graph_obj, name, obj_type, parent_keys,
              docstring, examples, links, keymeta):
        ''' @stuff@ -- Return a list of a tuple packaging graph object stuff
        '''
        return [(graph_obj,
            OrderedDict([
                ('name', name),
                ('obj_type', obj_type),
                ('parent_keys', parent_keys),
                ('docstring', docstring),
                ('examples',examples),
                ('links', links),
                ('keymeta', keymeta)
            ])
        )]

    def scatter(self):
        '''@scatter@'''
        name = "{scatter}"
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a scatter trace in plotly."
        )
        examples = MakeExamples.scatter(MakeExamples())
        links = [
            "{WEB}line-and-scatter/",
            "{WEB}bubble-charts/",
            "{WEB}filled-area-plots/",
            "{WEB}time-series/"
        ]
        keymeta = OrderedDict([
            ('x', make.x('scatter')),
            ('y', make.y('scatter')),
            ('r', make.r('scatter')),
            ('t', make.t('scatter')),
            ('mode', make.mode()),
            ('name', make.name()),
            ('text', make.text('scatter')),
            ('error_y', make.error('scatter','y')),
            ('error_x', make.error('scatter','x')),
            ('marker', make.marker('scatter')),
            ('line', make.line('scatter')),
            ('textposition', make.textposition()),
            ('textfont', make.textfont('scatter')),
            ('connectgaps', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not missing data points "
                    "(i.e. '' or {NAN}) linked to 'x' and/or 'y', are "
                    "added in by Plotly using linear interpolation."
                )
            )),
            ('fill', dict(
                required=False,
                key_type='plot_info',
                val_types=(
                    "'none' | 'tozeroy' | 'tonexty' | 'tozerox' | 'tonextx"
                ),
                description=(
                    "Use to make area-style charts. "
                    "Determines which area to fill with a solid color."
                    "By default, the area will appear in a more-transparent "
                    "shape of the line color (or of the marker color if "
                    "'mode' does not contains 'lines')."
                )
            )),
            ('fillcolor', make.fillcolor('scatter')),
            ('opacity', make.opacity()),
            ('xaxis', make.axis('x',trace=True)),
            ('yaxis', make.axis('y',trace=True)),
            ('showlegend', make.showlegend(trace=True)),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('xsrc', make.x('scatter', src=True)),
            ('ysrc', make.y('scatter', src=True)),
            ('type', make.type('scatter')),
        ])
        self += self._stuff('scatter', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def bar(self):
        '''@bar@'''
        name = '{bar}'
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a bar trace in plotly."
        )
        links = ["{WEB}bar-charts/"]
        examples = MakeExamples.bar(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.x('bar')),
            ('y', make.y('bar')),
            ('name', make.name()),
            ('orientation', make.orientation('bar')),
            ('text', make.text('bar')),
            ('error_y', make.error('bar','y')),
            ('error_x', make.error('bar','x')),
            ('marker', make.marker('bar')),
            ('opacity', make.opacity()),
            ('xaxis', make.axis('x',trace=True)),
            ('yaxis', make.axis('y',trace=True)),
            ('showlegend', make.showlegend(trace=True)),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('xsrc', make.x('bar', src=True)),
            ('ysrc', make.y('bar', src=True)),
            ('r', make.r('bar')),   # ARTIFACT
            ('t', make.t('bar')),   # ARTIFACT
            ('type', make.type('bar')),
        ])
        self += self._stuff('bar', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def histogram(self):
        '''@histogram@'''
        name = '{histogram}'
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a histogram trace in plotly."
        )
        links = ["{WEB}histograms/"]
        examples = MakeExamples.histogram(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.x('histogram')),
            ('y', make.y('histogram')),
            ('histnorm', make.histnorm()),
            ('histfunc', make.histfunc()),
            ('name', make.name()),
            ('orientation', make.orientation('bar')),
            ('autobinx', make.autobin('x')),
            ('nbinsx', make.nbins('x')),
            ('xbins', make.bins('x')),
            ('autobiny', make.autobin('y')),
            ('nbinsy', make.nbins('y')),
            ('ybins', make.bins('y')),
            ('text', make.text('histogram')),
            ('error_y', make.error('histogram','y')),
            ('error_x', make.error('histogram','x')),
            ('marker', make.marker('histogram')),
            ('opacity', make.opacity()),
            ('xaxis', make.axis('x',trace=True)),
            ('yaxis', make.axis('y',trace=True)),
            ('showlegend', make.showlegend(trace=True)),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('xsrc', make.x('histogram', src=True)),
            ('ysrc', make.y('histogram', src=True)),
            ('type', make.type('histogram')),
        ])
        self += self._stuff('histogram', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def box(self):
        '''@box@'''
        name = "{box}"
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a box trace in plotly."
        )
        links = ["{WEB}box-plots/"]
        examples = MakeExamples.box(MakeExamples())
        keymeta = OrderedDict([
            ('y', make.y('box')),
            ('x0', make.x0y0('box')),
            ('x', make.x('box')),
            ('name', make.name()),
            ('boxmean', dict(
                required=False,
                key_type='style',
                val_types="{FALSE} | {TRUE} | 'sd'",
                description=(
                    "Choose between add-on features for this box trace. "
                    "If {TRUE} then the mean of the data linked to 'y' is shown "
                    "as a dashed line in the box. If 'sd', then the standard "
                    "deviation is also shown. If {FALSE} (the default), "
                    "then no line are shown."
                )
            )),
            ('boxpoints', dict(
                required=False,
                key_type='style',
                val_types="'outliers' | 'all' | 'suspectedoutliers' | {FALSE}",
                description=(
                    "Choose between boxpoints options for this box trace. "
                    "If 'outliers' (the default), then only the points lying "
                    "outside the box' whiskers (more info in 'y') are shown. "
                    "If 'all', then all data points linked 'y' are shown. "
                    "If 'suspectedoutliers', then outliers points are shown and "
                    "points either less than 4*Q1-3*Q3 or greater than "
                    "4*Q3-3*Q1 are highlighted (with 'outliercolor' in Marker). "
                    "If {FALSE}, then only the boxes are shown and the whiskers "
                    "correspond to the minimum and maximum value linked to 'y'."
                )
            )),
            ('jitter', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0,le=1),
                description=(
                    "Sets the width of the jitter in the boxpoints scatter "
                    "in this trace. "
                    "Has an no effect if 'boxpoints' is set to {FALSE}. "
                    "If 0, then the "
                    "boxpoints are aligned vertically. If 1 then the "
                    "boxpoints are placed in a random horizontal jitter of width "
                    "equal to the width of the boxes."
                )
            )),
            ('pointpos', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=-2, le=2),
                description=(
                    "Sets the horizontal position of the boxpoints "
                    "in relation to the boxes in this trace. "
                    "Has an no effect if 'boxpoints' is set to {FALSE}. "
                    "If 0, then the boxpoints are placed over the center of "
                    "each box. If 1 (-1), then the boxpoints are placed on the "
                    "right (left) each box border. "
                    "If 2 (-2), then the boxpoints are  "
                    "placed 1 one box width to right (left) of each box. "
                )
            )),
            ('whiskerwidth', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0, le=1),
                description=(
                    "Sets the width of the whisker of the box relative "
                    "to the box' "
                    "width (in normalized coordinates, e.g. if "
                    "'whiskerwidth' set 1, then the whiskers are as wide "
                    "as the box."
                )
            )),
            ('fillcolor', make.fillcolor('box')),
            ('marker', make.marker('box')),
            ('line', make.line('box')),
            ('opacity', make.opacity()),
            ('xaxis', make.axis('x',trace=True)),
            ('yaxis', make.axis('y',trace=True)),
            ('showlegend', make.showlegend(trace=True)),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('xsrc', make.x('box', src=True)),
            ('ysrc', make.y('box', src=True)),
            ('type', make.type('box'))
        ])
        self += self._stuff('box', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def heatmap(self):
        '''@heatmap@'''
        name = "{heatmap}"
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a heatmap trace in plotly."
        )
        links = ["{WEB}heatmaps/"]
        examples = MakeExamples.heatmap(MakeExamples())
        keymeta = OrderedDict([
            ('z', make.z('heatmap')),
            ('x', make.x('heatmap')),
            ('y', make.y('heatmap')),
            ('name', make.name()),
            ('zauto', make.zcauto('z')),
            ('zmin', make.zcminmax('min','z')),
            ('zmax', make.zcminmax('max','z')),
            ('colorscale', make.colorscale('z')),
            ('reversescale', make.reversescale()),
            ('showscale', make.showscale()),
            ('colorbar', make.colorbar()),
            ('zsmooth', make.zsmooth()),
            ('opacity', make.opacity()),
            ('xaxis', make.axis('x',trace=True)),
            ('yaxis', make.axis('y',trace=True)),
            ('showlegend', make.showlegend(trace=True)),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('x0', make.x0y0('heatmap','x')),
            ('dx', make.dxdy('heatmap','x')),
            ('y0', make.x0y0('heatmap','y')),
            ('dy', make.dxdy('heatmap','y')),
            ('xtype', make.xytype('heatmap','x')),
            ('ytype', make.xytype('heatmap','y')),
            ('type', make.type('heatmap')),
        ])
        self += self._stuff('heatmap', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def contour(self):
        '''@contour@'''
        name = "{contour}"
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a contour trace in plotly."
        )
        links = ["{WEB}contour-plots/"]
        examples = MakeExamples.contour(MakeExamples())
        keymeta = OrderedDict([
            ('z', make.z('contour')),
            ('x', make.x('contour')),
            ('y', make.y('contour')),
            ('name', make.name()),
            ('zauto', make.zcauto('z')),
            ('zmin', make.zcminmax('min','z')),
            ('zmax', make.zcminmax('max','z')),
            ('autocontour', make.autocontour()),
            ('ncontours', make.ncontours()),
            ('contours', make.contours()),
            ('line', make.line('contour')),
            ('colorscale', make.colorscale('z')),
            ('reversescale', make.reversescale()),
            ('showscale', make.showscale()),
            ('colorbar', make.colorbar()),
            ('opacity', make.opacity()),
            ('xaxis', make.axis('x',trace=True)),
            ('yaxis', make.axis('y',trace=True)),
            ('showlegend', make.showlegend(trace=True)),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('x0', make.x0y0('heatmap','x')),
            ('dx', make.dxdy('heatmap','x')),
            ('y0', make.x0y0('heatmap','y')),
            ('dy', make.dxdy('heatmap','y')),
            ('xtype', make.xytype('heatmap','x')),
            ('ytype', make.xytype('heatmap','y')),
            ('type', make.type('contour'))
        ])
        self += self._stuff('contour', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def histogram2d(self):
        '''@histogram2d@'''
        name = '{histogram2d}'
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a 2D histogram trace in plotly."
        )
        links = ["{WEB}2D-Histograms/"]
        examples = MakeExamples.histogram2d(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.x('histogram2d')),
            ('y', make.y('histogram2d')),
            ('histnorm', make.histnorm()),
            ('histfunc', make.histfunc()),
            ('name', make.name()),
            ('autobinx', make.autobin('x')),
            ('nbinsx', make.nbins('x')),
            ('xbins', make.bins('x')),
            ('autobiny', make.autobin('y')),
            ('nbinsy', make.nbins('y')),
            ('ybins', make.bins('y')),
            ('colorscale', make.colorscale('z')),
            ('reversescale', make.reversescale()),
            ('showscale', make.showscale()),
            ('colorbar', make.colorbar()),
            ('zauto', make.zcauto('z')),
            ('zmin', make.zcminmax('min','z')),
            ('zmax', make.zcminmax('max','z')),
            ('zsmooth', make.zsmooth()),
            ('opacity', make.opacity()),
            ('xaxis', make.axis('x',trace=True)),
            ('yaxis', make.axis('y',trace=True)),
            ('showlegend', make.showlegend(trace=True)),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('xsrc', make.x('histogram2d', src=True)),
            ('ysrc', make.y('histogram2d', src=True)),
            ('type', make.type('histogram2d'))
        ])
        self += self._stuff('histogram2d', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def histogram2dcontour(self):
        '''@histogram2dcontour@'''
        name = '{histogram2dcontour}'
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a 2D histogram contour "
            "trace in plotly."
        )
        links = ["{WEB}2D-Histograms/"]
        examples = MakeExamples.histogram2dcontour(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.x('histogram2dcontour')),
            ('y', make.y('histogram2dcontour')),
            ('histnorm', make.histnorm()),
            ('histfunc', make.histfunc()),
            ('name', make.name()),
            ('autobinx', make.autobin('x')),
            ('nbinsx', make.nbins('x')),
            ('xbins', make.bins('x')),
            ('autobiny', make.autobin('y')),
            ('nbinsy', make.nbins('y')),
            ('ybins', make.bins('y')),
            ('autocontour', make.autocontour()),
            ('ncontours', make.ncontours()),
            ('contours', make.contours()),
            ('line', make.line('histogram2dcontour')),
            ('colorscale', make.colorscale('z')),
            ('reversescale', make.reversescale()),
            ('showscale', make.showscale()),
            ('colorbar', make.colorbar()),
            ('zauto', make.zcauto('z')),
            ('zmin', make.zcminmax('min','z')),
            ('zmax', make.zcminmax('max','z')),
            ('opacity', make.opacity()),
            ('xaxis', make.axis('x',trace=True)),
            ('yaxis', make.axis('y',trace=True)),
            ('showlegend', make.showlegend(trace=True)),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('xsrc', make.x('histogram2dcontour', src=True)),
            ('ysrc', make.y('histogram2dcontour', src=True)),
            ('type', make.type('histogram2dcontour'))
        ])
        self += self._stuff('histogram2dcontour', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def area(self):
        '''@area@'''
        name = '{area}'
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing an area trace in plotly."
        )
        links = ["{WEB}polar-chart/"]
        examples = MakeExamples.area(MakeExamples())
        keymeta = OrderedDict([
            ('r', make.r('area')),
            ('t', make.t('area')),
            ('name', make.name()),
            ('marker', make.marker('area')),
            ('showlegend', make.showlegend(trace=True)),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('angularaxis', dict(  #Q? How do polar axes this work?
                required=False,
                key_type='plot_info',
                val_types='',
                description=(
                    'Polar chart subplots are not supported yet. Info coming soon'
                )
            )),
            ('radialaxis', dict(  #Q? How do polar axes this work?
                required=False,
                key_type='plot_info',
                val_types='',
                description=(
                    'Polar chart subplots are not supported yet. Info coming soon'
                )
            )),
            ('type', make.type('area'))
        ])
        self += self._stuff('area', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def scatter3d(self):
        '''@scatter3d@'''
        name = '{scatter3d}'
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a 3D scatter trace in plotly."
        )
        links = []  # TODO
        examples = MakeExamples.scatter3d(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.x('scatter3d')),
            ('y', make.y('scatter3d')),
            ('z', make.z('scatter3d')),
            ('mode', make.mode(is_3d=True)),
            ('name', make.name(is_3d=True)),
            ('text', make.text('scatter3d')),
            ('error_z', make.error('scatter3d','z')),
            ('error_y', make.error('scatter3d','y')),
            ('error_x', make.error('scatter3d','x')),
            ('marker', make.marker('scatter3d')),
            ('line', make.line('scatter3d')),
            ('textposition', make.textposition('scatter3d')),
#             ('delaunayaxis' ,),  # TODO change name
#             ('delaunaycolor' ,), # TODO change name
            ('scene', make.scene()),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('type', make.type('scatter3d'))
        ])
        self += self._stuff('scatter3d', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def surface(self):
        '''@surface@'''
        name = '{surface}'
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing a 3D surface trace in plotly."
        )
        links = []  # TODO
        examples = MakeExamples.surface(MakeExamples())
        keymeta = OrderedDict([
            ('z', make.z('surface')),
            ('x', make.x('surface')),
            ('y', make.y('surface')),
            ('name', make.name(is_3d=True)),
            ('colorscale', make.colorscale('z')),
            ('scene', make.scene()),
            ('stream', make.stream()),
            ('visible', make.visible()),
            ('type', make.type('surface'))
        ])
        self += self._stuff('surface', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def _keymeta_error(self, which_axis):
        '''@keymeta_error@ -- keymeta for error_y, error_x (and error_z)'''
        S = {'y': ['y','vertically','up','down','above','below'],
             'x': ['x','horizontally','right','left','right of','left of'],
             'z': ['z','','positive z', 'negative z', 'above', 'below']}
        s = S[which_axis]
        _keymeta = [
            ('type', dict(  # Different enough from shortcut
                required=False,
                key_type='plot_info',
                val_types="'data' | 'percent' | 'constant' | 'sqrt'",
                description=(
                    "Specify how the 'value' or 'array' key in "
                    "this error bar will be used to render the bars. "
                    "Using 'data' will set error bar lengths to the "
                    "actual numbers specified in 'array'.  "
                    "Using 'percent' will set bar lengths to the "
                    "percent of error associated with 'value'. "
                    "Using 'constant' will set each error "
                    "bar length to the single value specified "
                    "in 'value'. Using 'sqrt' will set "
                    "each error bar length to the square root of "
                    "the x data at each point ('value' and 'array' "
                    "do not apply)."
                ),
            )),
            ('symmetric', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not error bars are the same length "
                    "in both directions ({S2} and {S3}). If not specified, "
                    "the error bars will be "
                    "symmetric."
                ).format(S2=s[2],S3=s[3])
            )),
            ('array', dict(
                required=False,
                key_type='data',
                val_types=val_types.data_array(),
                description=(
                   "The array corresponding to the span of the "
                   "error bars. "
                   "Has only an effect if 'type' is set to "
                   "'data'. Values in the array are plotted "
                   "relative to the '{S0}' coordinates. "
                   "For example, with '{S0}'=[1,2] and "
                   "'array'=[1,2], the error bars will span "
                   "from {S0}= 0 to 2 and {S0}= 0 to 4 if "
                   "'symmetric' is set to {{TRUE}}; and from {S0}= 1 to 2 "
                   "and {S0}= 2 to 4 if 'symmetric' is set to {{FALSE}} "
                   "and 'arrayminus' is empty."
                ).format(S0=s[0])
            )),
            ('value', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(ge=0),
                description=(
                   "The value or percentage determining the error bars' "
                   "span, at all trace coordinates. "
                   "Has an effect if 'type' is set to 'value' or "
                   "'percent'. "
                   "If 'symmetric' is set to {{FALSE}}, this value corresponds "
                   "to the span {S4} the trace of coordinates. "
                   "To specify multiple error bar lengths, "
                   "you should set 'type' to 'data' and "
                   "use the 'array' key instead."
                ).format(S4=s[4])
            )),
            ('arrayminus', dict(
                required=False,
                key_type='data',
                val_types=val_types.data_array(),
                description=(
                      "Has an effect only when 'symmetric' is set to {{FALSE}}. "
                      "Same as 'array' but corresponding to the span "
                      "of the error bars {S5} the trace coordinates"
                ).format(S5=s[5])
            )),
            ('valueminus', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(ge=0),
                description=(
                      "Has an effect only when 'symmetric' "
                      "is set to {{FALSE}}. Same as 'value' but corresponding "
                      "to the span of the error bars {S5} the trace coordinates"
                ).format(S5=s[5])
            )),
            ('color', make.color('error')),
            ('thickness', make.thickness('error', which_axis)),
            ('width', make.width('error')),
            ('opacity', make.opacity()),
        ]
        if which_axis=='x':
            _keymeta += [
                ('copy_ystyle', dict(
                    required=False,
                    key_type='style',
                    val_types=val_types.bool(),
                    description=(
                          "Toggle whether to set x error bar "
                          "style to the same style "
                          "(color, thickness, width, opacity) "
                          "as y error bars set in 'yaxis'."
                    )
                ))
            ]
        _keymeta += [('visible', make.visible())]
        return _keymeta


    def error_y(self):
        '''@error_y@'''
        name = '{error_y}'
        obj_type = "{UL}"
        parent_keys = ["error_y"]
        docstring = (
            "{A_ULlike} object representing a set of error bar spanning "
            "along the y-axis."
        )
        links = ["{WEB}error-bars/"]
        examples = MakeExamples.error_y(MakeExamples())
        keymeta = OrderedDict(self._keymeta_error('y'))
        self += self._stuff('error_y', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def error_x(self):
        '''@error_x@'''
        name = '{error_x}'
        obj_type = "{UL}"
        parent_keys = ["error_x"]
        docstring = (
            "A {ULlike} representing a set of error bars spanning "
            "along the x-axis."
        )
        links = ["{WEB}error-bars/"]
        examples = MakeExamples.error_x(MakeExamples())
        keymeta = OrderedDict(self._keymeta_error('x'))
        self += self._stuff('error_x', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def error_z(self):
        '''@error_z@'''
        name = '{error_z}'
        obj_type = "{UL}"
        parent_keys = ["error_z"]
        docstring = (
            "A {ULlike} representing a set of error bars spanning "
            "along the z-axis in a 3D plot."
        )
        links = []  # TODO
        examples = MakeExamples.error_z(MakeExamples())
        keymeta = OrderedDict(self._keymeta_error('z'))
        self += self._stuff('error_z', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def _keymeta_bins(self,x_or_y):
        '''@keymeta_bins@ -- keymeta for XBins and YBins'''
        _keymeta = [
            ('start', make.startend('bins','start',x_or_y)),
            ('end', make.startend('bins','end',x_or_y)),
            ('size', make.size('bins',x_or_y))
        ]
        return _keymeta

    def xbins(self):
        '''@xbins@'''
        name = '{xbins}'
        obj_type = "{UL}"
        parent_keys = ["xbins"]
        docstring = (
            "{A_ULlike} containing specifications of the bins "
            "lying along the x-axis."
        )
        links = [
            "{WEB}histograms/",
            "{WEB}2D-Histograms/"
        ]
        examples = MakeExamples.xbins(MakeExamples())
        keymeta = OrderedDict(self._keymeta_bins('x'))
        self += self._stuff('xbins', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def ybins(self):
        '''@ybins@'''
        name = '{ybins}'
        obj_type = "{UL}"
        parent_keys = ["ybins"]
        docstring = (
            "{A_ULlike} containing specifications of the bins "
            "lying along the y-axis."
        )
        links = [
            "{WEB}histograms/",
            "{WEB}2D-Histograms/"
        ]
        examples = MakeExamples.ybins(MakeExamples())
        keymeta = OrderedDict(self._keymeta_bins('y'))
        self += self._stuff('ybins', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def contours(self):
        '''@contours@'''
        name = '{contours}'
        obj_type = "{UL}"
        parent_keys = ["contours"]
        docstring = (
            "{A_ULlike} containing specifications of the contours."
        )
        links = ["{WEB}contour-plots/"]
        examples = MakeExamples.contours(MakeExamples())
        keymeta = OrderedDict([
            ('showlines', dict(
                required=False,
                key_type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not the contour lines appear on the plot."
                )
            )),
            ('start', make.startend('contours','start','x')),
            ('end', make.startend('contours','end','x')),
            ('size', make.size('contours')),
            ('coloring', dict(
                required=False,
                key_type='style',
                val_types=" 'fill' | 'heatmap' | 'lines' | 'none' ",
                description=(
                    "Choose the coloring method for this contour trace. "
                    "The default value is 'fill' "
                    "where coloring is done evenly between each contour line. "
                    "'heatmap' colors on a grid point-by-grid point basis. "
                    "'lines' colors only the contour lines, each with "
                    "respect to the color scale. "
                    "'none' prints all contour lines with the same color; "
                    "choose their color in a Line object at the trace level "
                    "if desired."
                )
            ))
        ])
        self += self._stuff('contours', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def stream(self):
        '''@stream@'''
        name = '{stream}'
        obj_type = "{UL}"
        parent_keys = ["stream"]
        docstring = (
            "{A_ULlike} containing specifications of the data stream."
        )
        links = ["{WEB}streaming/"]
        examples = MakeExamples.stream(MakeExamples())
        keymeta = OrderedDict([
            ('token', dict(  #Q? These are public!! Is that OK?
                required=True,
                key_type='plot_info',
                val_types="A stream id number, see https://plot.ly/settings",
                description=(
                    "The stream id number links a data trace on a plot with a "
                    "stream. In other words, any data trace you create "
                    "can reference a 'stream'. If you stream data to "
                    "Plotly with the same stream id (token), Plotly knows "
                    "update this data object with the incoming data "
                    "stream."
                )
            )),
            ('maxpoints', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the maximum number of points to keep on the "
                    "plots from an incoming stream. For example, "
                    "if 'maxpoints' is set to 50, only the newest 50 points "
                    "will be displayed on the plot."
                )
            ))
        ])
        self += self._stuff('stream', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def marker(self):
        '''@marker@'''
        name = '{marker}'
        obj_type = "{UL}"
        parent_keys = ["marker"]
        docstring = (
            "{A_ULlike} containing specifications of the marker points."
        )
        links = [
            "{WEB}line-and-scatter/",
            "{WEB}bubble-charts/"
        ]
        examples = MakeExamples.marker(MakeExamples())
        keymeta = OrderedDict([
            ('color', make.color('marker')),
            ('size', make.size('marker')),
            ('symbol', dict(
                required=False,
                key_type='plot_info',
                val_types=( # TODO add new symbols!
                    "'dot' | 'cross' | 'diamond' | 'square' "
                    "| 'triangle-down' | 'triangle-left' | 'triangle-right' "
                    "| 'triangle-up' | 'x' OR list of these string values"
                ),
                description=(
                      "The symbol that is drawn on the plot for each marker. "
                      "Supported only in scatter traces. "
                      "If 'symbol' is linked to {a_OL}, the "
                      "symbol values are mapped to individual marker points "
                      "in the same order as in the {OL} linked to 'x', 'y' "
                      "(or 'z')."
                )
            )),
            ('line', make.line('marker')),
            ('opacity', make.opacity(marker=True)),
            ('sizeref', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "Sets the scale factor used to determine the rendered size "
                    "of each marker point in this trace. "
                    "Applies only to scatter traces that have their 'size' key "
                    "in 'marker' linked to {a_OL}. "
                    "If set, the value linked to 'sizeref' is used to divide "
                    "each entry linked to 'size'. Specifically, setting 'sizeref' "
                    "to less (greater) than 1, increases (decreases) the "
                    "rendered marker sizes."
                )
            )),
            ('sizemode', dict(
                required=False,
                key_type='style',
                val_types="'diameter'| 'area'",
                description=(
                    "Choose between marker size scaling options for the marker "
                    "points in this trace. "
                    "Applies only to scatter traces that have their 'size' key "
                    "in 'marker' linked to {a_OL}. "
                    "If 'diameter' ('area'), then the diameter (area) of the "
                    "rendered marker points (in pixels) are "
                    "proportional to the numbers linked to 'size'."
                    "For example, set 'sizemode' to 'area' for a more a smaller "
                    "range of rendered marker sizes."
                )
            )),
            ('colorscale', make.colorscale('c')),
            ('cauto', make.zcauto('c')),
            ('cmin', make.zcminmax('min','color')),
            ('cmax', make.zcminmax('max','color')),
            ('outliercolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "For box plots only. Has an effect only if 'boxpoints' is "
                    "set to 'suspectedoutliers'. Sets the face color of the "
                    "outlier points."
               ),
               examples=MakeExamples.color(MakeExamples())
            )),
            ('maxdisplayed', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "Sets maximum number of displayed points for this "
                    "trace. Applies only to scatter traces."
                )
            ))
        ])
        self += self._stuff('marker', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def line(self):
        '''@line@'''
        name = '{line}'
        obj_type = "{UL}"
        parent_keys = ["line"]
        docstring = (
            "{A_ULlike} containing specifications of the line segments."
        )
        links = [
            "{WEB}line-and-scatter/",
            "{WEB}filled-area-plots/",
            "{WEB}contour-plots/"
        ]
        examples = MakeExamples.line(MakeExamples())
        keymeta = OrderedDict([
            ('color', make.color('line')),
            ('width', make.width('line')),
            ('dash', dict(
                required=False,
                key_type='style',
                val_types="'dash' | 'dashdot' | 'dot' | 'solid'",
                description=(
                    "Sets the drawing style of the lines segments "
                    "in this trace."
                )
            )),
            ('opacity', make.opacity()),
            ('shape', dict(
                required=False,
                key_type='style',
                val_types="'linear' | 'spline' | 'hv' | 'vh' | 'hvh' | 'vhv'",
                description=(
                    "Choose the line shape between each coordinate pair "
                    "in this trace. "
                    "Applies only to scatter traces. "
                    "The default value is 'linear'. "
                    "If set to 'spline', then the lines are drawn using spline "
                    "interpolation between the coordinate pairs. "
                    "The remaining available values correspond to "
                    "step-wise line shapes."
               )
            )),
            ('smoothing', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0),
                description=(
                   "Sets the amount of smoothing applied to the lines segments "
                   "in this trace. "
                   "Applies only to contour traces "
                   "and scatter traces if 'shape' is set to 'spline'. "
                   "The default value is 1. If 'smoothing' is set to 0, then "
                   "no smoothing is applied. "
                   "Set 'smoothing' to a value less "
                   "(greater) than 1 for a less (more) pronounced line "
                   "smoothing."
                )
            )),
            ('outliercolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "For box plots only. Has an effect only if 'boxpoints' is "
                    "set to 'suspectedoutliers'. Sets the color of the "
                    "bordering line of the outlier points."
               ),
               examples=MakeExamples.color(MakeExamples())
            )),
            ('outlierwidth', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "For box plots only. Has an effect only if 'boxpoints' is "
                    "set to 'suspectedoutliers'. Sets the width in pixels of "
                    "bordering line of the outlier points."
               ),
               examples=MakeExamples.color(MakeExamples())
            ))
        ])
        self += self._stuff('line', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def font(self):
        '''@font@'''
        name = '{font}'
        obj_type = "{UL}"
        parent_keys = ["font","titlefont","textfont", "tickfont"]
        docstring = (
            "{A_ULlike} containing specifications of on-plot, title or "
            "global text font."
        )
        links = [
            "{WEB}font/",
            "{WEB}text-and-annotations/",
            "{WEB}line-and-scatter/"
        ]
        examples = MakeExamples.font(MakeExamples())
        keymeta = OrderedDict([
            ('family', dict(
                required=False,
                val_types=(
                    "'Arial, sans-serif' | "
                    " 'Balto, sans-serif' | "
                    " 'Courier New, monospace' | "
                    " 'Droid Sans, sans-serif' | "
                    " 'Droid Serif, serif' | "
                    " 'Droid Sans Mono, sans-serif' | "
                    " 'Georgia, serif' | "
                    " 'Gravitas One, cursive' | "
                    " 'Old Standard TT, serif' | "
                    " 'Open Sans, sans-serif' or ('') | "
                    " 'PT Sans Narrow, sans-serif' | "
                    " 'Raleway, sans-serif' | "
                    " 'Times New Roman, Times, serif'"
                ),
                key_type='style',
                description=(
                    "Sets the font family. "
                    "If linked in the first level of the layout object,  "
                    "set the color of the global font. "
                    "The default font in Plotly is 'Open Sans, sans-serif'."
                )
            )),
            ('size', make.size('font')),
            ('color', make.color('font')),
            ('outlinecolor', make.outlinecolor('font'))
        ])
        self += self._stuff('font', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def _keymeta_ticks(self, axis_or_colorbar):
        '''@keymeta_ticks@ -- ticks keymeta for xaxis, yaxis (zaxis), colorbar'''
        _keymeta = [
            ('ticks', dict(
                  required=False,
                  key_type='style',
                  val_types="'' | 'inside' | 'outside'",
                  description=(
                      "Sets the format of the ticks on this {}. "
                      "For hidden ticks, link 'ticks' to an empty string."
                  ).format(axis_or_colorbar)
            )),
            ('showticklabels', make.showticklabels(axis_or_colorbar)),
            ('tick0', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(),
                description=(
                    "Sets the starting point of the ticks of this {}."
                ).format(axis_or_colorbar)
            )),
            ('dtick', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(),
                description=(
                    "Sets the distance between ticks on this {}."
                ).format(axis_or_colorbar)
            )),
            ('ticklen', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(),  # Units?
                description=(
                    "Sets the length of the tick lines on this {}."
                ).format(axis_or_colorbar)
            )),
            ('tickwidth', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the width of the tick lines on this {}."
                ).format(axis_or_colorbar)
            )),
            ('tickcolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the tick lines on this {}."
                ).format(axis_or_colorbar),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('tickangle', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(le=90, ge=-90),
                description=(
                    "Sets the angle in degrees of the ticks on this {}."
                ).format(axis_or_colorbar)
            )),
            ('tickfont', dict(
                required=False,
                key_type='object',
                val_types=val_types.object(),
                description=(
                    "Links {a_ULlike} defining the parameters "
                    "of the ticks' font."
                )
            )),
            ('exponentformat', dict(
                required=False,
                key_type='style',
                val_types="'none' | 'e' | 'E' | 'power' | 'SI' | 'B'",
                description=(
                    "Sets how exponents show up. Here's how the number "
                    "1000000000 (1 billion) shows up in each. If set to "
                    "'none': 1,000,000,000. If set to 'e': 1e+9. If set "
                    "to 'E': 1E+9. If set to 'power': 1x10^9 (where the 9 "
                    "will appear super-scripted). If set to 'SI': 1G. If "
                    "set to 'B': 1B (useful when referring to currency)."
                )
            )),
            ('showexponent', dict(
                required=False,
                key_type='style',
                val_types="'all' | 'first' | 'last' | 'none'",
                description=(
                    "If set to 'all', ALL exponents will be shown "
                    "appended to their significands. If set to 'first', "
                    "the first tick's exponent will be appended to its "
                    "significand, however no other exponents will "
                    "appear--only the significands. If set to 'last', "
                    "the last tick's exponent will be appended to its "
                    "significand, however no other exponents will "
                    "appear--only the significands. If set to 'none', "
                    "no exponents will appear, only the significands."
                )
            ))
        ]
        return _keymeta


    def _keymeta_axis(self, which_axis):
        '''@keymeta_axis@ -- keymeta for xaxis, yaxis (and zaxis)'''
        S = {'x':['x','bottom','top','y','left','right','vertical'],
             'y':['y','left','right','x','bottom','top','horizontal'],
             'z':['z','','','','','','']}
        s = S[which_axis]
        _keymeta = [
            ('title', make.title('axis', which_axis)),
            ('titlefont', make.titlefont('axis', which_axis)),
            ('range', make.range(which_axis)),
            ('domain', make.domain(which_axis)),
            ('type', dict( # N.B. different enough from shortcut
                required=False,
                key_type='plot_info',
                val_types="'linear' | 'log' | 'date' | 'category'",
                description="Sets the format of this axis."  # TODO Add info
            )),
            ('rangemode', dict(
                required=False,
                key_type='style',
                val_types="'normal' | 'tozero' | 'nonnegative'",
                description=(
                    "Choose between Plotly's automated axis generation "
                    "modes: 'normal' (the default) sets the axis range "
                    "in relation to the extrema in the data object, "
                    "'tozero' extends the axes to {S0}=0 no matter "
                    "the data plotted and 'nonnegative' sets a "
                    "non-negative range no matter the "
                    "data plotted."
                ).format(S0=s[0])
            )),
            ('autorange', dict(
                required=False,
                key_type='style',
                val_types="{TRUE} | {FALSE} | 'reversed'",
                description=(
                    "Toggle whether or not the range of this {S0}-axis is "
                    "automatically picked by Plotly. "
                    "If 'range' is set, then 'autorange' is set "
                    "to {{FALSE}} automatically. Otherwise, if 'autorange' "
                    "is set to {{TRUE}} (the default behavior), the range "
                    "of this {S0}-axis can respond to adjustments made in "
                    "the web GUI automatically. If 'autorange' is set "
                    "to 'reversed', then this {S0}-axis is drawn in reverse"
                    +
                    (", e.g. in a 2D plot, from {S5} to {S4} instead of "
                    "from {S4} to {S5} (the default behavior)."
                    if not which_axis=='z' else '.')
                ).format(S0=s[0],S4=s[4],S5=s[5])
            )),
            ('showgrid', dict(
                required=False,
                key_type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not this axis features grid lines."
                )
            )),
            ('zeroline', dict(
                required=False,
                key_type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not an additional grid line "
                    "(thicker than the other grid lines, by default) "
                    "will appear on this axis along {}=0."
                ).format(which_axis)
            )),
            ('showline', make.showline(which_axis)),
            ('autotick', make.autotick('axis')),
            ('nticks', make.nticks('axis')),
        ]
        _keymeta += self._keymeta_ticks('axis')
        _keymeta += [
            ('mirror', dict(
                required=False,
                key_type='style',
                val_types="{TRUE} | {FALSE} | 'ticks' | 'all' | 'allticks'",
                description=(
                    "Toggle the axis line and/or ticks across the plots or subplots. "
                    "If {TRUE}, mirror the axis line across the primary subplot "
                    "(i.e. the axis that this axis is anchored to). "
                    "If 'ticks', mirror the axis line and the ticks. "
                    "If 'all', mirror the axis line to all subplots containing this axis. "
                    "If 'allticks', mirror the line and ticks to all subplots containing this axis. "
                    "If {FALSE}, don't mirror the axis or the ticks."
                    if not which_axis=='z' else "Has no effect in 3D plots."
                )
            )),
            ('gridcolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description="Sets the axis grid color.",
                examples=MakeExamples.color(MakeExamples())
            )),
            ('gridwidth', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(gt=0),
                description="Sets the grid width (in pixels)."
            )),
            ('zerolinecolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description="Sets the color of this axis' zeroline.",
                examples=MakeExamples.color(MakeExamples())
            )),
            ('zerolinewidth', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(gt=0),
                description="Sets the width of this axis' zeroline (in pixels)."
            )),
            ('linecolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description="Sets the axis line color.",
                examples=MakeExamples.color(MakeExamples())
            )),
            ('linewidth', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(gt=0),
                description="Sets the width of the axis line (in pixels)."
            )),
            ('anchor', dict(
                required=False,
                key_type='plot_info',
                val_types=(
                    "'{S3}' | '{S3}1' | '{S3}2' | ... | 'free' "
                    if not which_axis=='z' else ''
                ).format(S3=s[3]),
                description=(
                    "Choose whether the position of this {S0}-axis "
                    "will be anchored to a "
                    "corresponding {S3}-axis or will be 'free' to appear "
                    "anywhere in the {S6} space of "
                    "this figure. "
                    "Has no effect in 3D plots."
                    if not which_axis=='z' else "Has no effect in 3D plots."
                ).format(S0=s[0],S3=s[3],S6=s[6])
            )),
            ('overlaying', dict(
                required=False,
                key_type='plot_info',
                val_types=(
                    "'{S0}' | '{S0}1' | '{S0}2' | ... | False"
                    if not which_axis=='z' else ''
                ).format(S0=s[0]),
                description=(
                    "Choose to overlay the data bound to this {S0}-axis "
                    "on the same plotting area as a "
                    "corresponding {S3}-axis or choose not overlay other {S0}-"
                    "the other axis/axes of this "
                    "figure."
                    "Has no effect in 3D plots."
                    if not which_axis=='z' else "Has no effect in 3D plots."
                ).format(S0=s[0],S3=s[3],S6=s[6])
            )),
            ('side', dict(
                required=False,
                key_type='plot_info',
                val_types=(
                    "'{S1}' | '{S2}'".format(S1=s[1],S2=s[2])
                    if not which_axis=='z' else ''
                ),
                description=(
                    "Sets whether this {S0}-axis sits at the '{S1}' of the "
                    "plot or at the '{S2}' "
                    "of the plot."
                    "Has no effect in 3D plots."
                    if not which_axis=='z' else "Has no effect in 3D plots."
                ).format(S0=s[0],S1=s[1],S2=s[2])
            )),
            ('position', dict(
                required=False,
                key_type='style',
                val_types=(
                    val_types.number(le=1, ge=0)
                    if not which_axis=='z' else ''
                ),
                description=(
                    "Sets where this {S0}-axis is positioned in the plotting "
                    "space. For example if 'position' is set to 0.5, "
                    "then this axis is placed at the exact center of the "
                    "plotting space. Has an effect only if 'anchor' "
                    "is set to 'free'."
                    "Has no effect in 3D plots."
                    if not which_axis=='z' else "Has no effect in 3D plots."
                ).format(S0=s[0])
            )),
            ('showbackground', dict(
                required=False,
                key_type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not this {S0}-axis will have "
                    "a background color. "
                    "Has an effect only in 3D plots."
                ).format(S0=s[0])
            )),
            ('backgroundcolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the background color of this {S0}-axis. "
                    "Has an effect only in 3D plots and if 'showbackground' "
                    "is set to {{TRUE}}."
                ).format(S0=s[0])
            )),
            ('showspikes', dict(
                required=False,
                key_type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not spikes will link up to this "
                    "{S0}-axis when hovering over data points. "
                    "Has an effect only in 3D plots."
                ).format(S0=s[0])
            )),
            ('spikesides', dict(
                required=False,
                key_type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not the spikes will expand out to the "
                    "{S0}-axis bounds when hovering over data points. "
                    "Has an effect only in 3D plots and if 'showspikes' "
                    "is set to {{TRUE}}."
                ).format(S0=s[0])
            )),
            ('spikethickness', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the thickness (in pixels) of the {S0}-axis spikes."
                    "Has an effect only in 3D plots and if 'showspikes' "
                    "is set to {{TRUE}}."
                ).format(S0=s[0])
            )),
#             ('showaxeslabels')  # TODO (overlap?)
        ]
        return _keymeta

    def xaxis(self):
        '''@xaxis@'''
        name = '{xaxis}'
        obj_type = "{UL}"
        parent_keys = ["xaxis"]
        docstring = (
            "{A_ULlike} for representing an x-axis in plotly."
        )
        links = [
            "{WEB}axes/",
            "{WEB}multiple-axes/",
            "{WEB}subplots/",
            "{WEB}insets/"
        ]
        examples = MakeExamples.xaxis(MakeExamples())
        keymeta = OrderedDict(self._keymeta_axis('x'))
        self += self._stuff('xaxis', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def yaxis(self):
        '''@yaxis@'''
        name = '{yaxis}'
        obj_type = "{UL}"
        parent_keys = ["yaxis"]
        docstring = (
            "{A_ULlike} for representing a y-axis in plotly."
        )
        links = [
            "{WEB}axes/",
            "{WEB}multiple-axes/",
            "{WEB}subplots/",
            "{WEB}insets/"
        ]
        examples = MakeExamples.yaxis(MakeExamples())
        keymeta = OrderedDict(self._keymeta_axis('y'))
        self += self._stuff('yaxis', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def zaxis(self):
        '''@zaxis@'''
        name = '{zaxis}'
        obj_type = "{UL}"
        parent_keys = ["zaxis"]
        docstring = (
            "{A_ULlike} for representing a z-axis in 3D plotly graphs."
        )
        links = []
        examples = MakeExamples.zaxis(MakeExamples())
        keymeta = OrderedDict(self._keymeta_axis('z'))
        self += self._stuff('zaxis', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def radialaxis(self):
        '''@radialaxis@'''
        name = '{radialaxis}'
        obj_type = "{UL}"
        parent_keys = ["radialaxis"]
        docstring = (
            "{A_ULlike} for representing a radial axis in plotly."
        )
        links = ["{WEB}polar-chart/"]
        examples = MakeExamples.radialaxis(MakeExamples())
        keymeta = OrderedDict([
            ('range', make.range('radial')),
            ('domain', make.domain('radial')),
            ('orientation', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=-360,le=360),
                description=(
                    "Sets the orientation (an angle with respect to the origin) "
                    "of the radial axis."
                )
            )),
            ('showline', make.showline('radial')),
            ('showticklabels', make.showticklabels('radial axis')),
            ('tickorientation', dict(
                required=False,
                key_type='style',
                val_types="'horizontal' | 'vertical'",
                description=(
                    "Choose the orientation (from the paper perspective) "
                    "of the radial axis tick labels."
                )
            )),
            ('ticklen', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "Sets the length of the tick lines on this radial axis."
                )
            )),
            ('tickcolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the tick lines on this radial axis."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('ticksuffix', dict(
                required=False,
                key_type='style',
                val_types=val_types.string(),
                description=(
                    "Sets the length of the tick lines on this radial axis."
                )
            )),
            ('endpadding', dict(  # TODO
                required=False,
                key_type='style',
                val_types=val_types.number(),
                description="more info coming soon"
            )),
            ('visible', make.visible())
        ])
        self += self._stuff('radialaxis', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def angularaxis(self):
        '''@angularaxis@'''
        name = '{angularaxis}'
        obj_type = "{UL}"
        parent_keys = ["angularaxis"]
        docstring = (
            "{A_ULlike} for representing an angular axis in plotly."
        )
        links = ["{WEB}polar-chart/"]
        examples = MakeExamples.angularaxis(MakeExamples())
        keymeta = OrderedDict([
            ('range', make.range('angular')),
            ('domain', make.domain('angular')),  #Q? Does not apply, right?
            ('showline', make.showline('angular')), #Q? Should be 'gridline'
            ('showticklabels', make.showticklabels('angular axis')),
            ('tickorientation', dict(
                required=False,
                key_type='style',
                val_types="'horizontal' | 'vertical'",
                description=(
                    "Choose the orientation (from the paper's perspective) "
                    "of the radial axis tick labels."
                )
            )),
            ('tickcolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the tick lines on this angular axis."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('ticksuffix', dict(
                required=False,
                key_type='style',
                val_types=val_types.string(),
                description=(
                    "Sets the length of the tick lines on this angular axis."
                )
            )),
            ('endpadding', dict(  # What does this do?
                required=False,
                key_type='style',
                val_types=val_types.number(),
                description="more info coming soon"
            )),
            ('visible', make.visible())
        ])
        self += self._stuff('angularaxis', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def scene(self):
        '''@scene@'''
        name = '{scene}'
        obj_type = "{UL}"
        parent_keys = ["scene"]
        docstring = (
            "{A_ULlike} for representing a 3D scene in plotly."
        )
        links = []
        examples = MakeExamples.scene(MakeExamples())
        keymeta = OrderedDict([
             ('xaxis', make.axis('x', scene=True)),
             ('yaxis', make.axis('y', scene=True)),
             ('zaxis', make.axis('z', scene=True)),
             ('cameraposition', dict(
                required=False,
                key_type='plot_info',
                val_types='camera position {OL}',
                description=(
                    "Sets the camera position with respect to the scene. "
                    "The first entry (a {OL} of length 4) "
                    "sets the angular position of the camera. "
                    "The second entry (a {OL} of length 3) "
                    "sets the (x,y,z) translation of the camera. "
                    "The third entry (a scalar) sets zoom of the camera."
                ),
                examples = MakeExamples.cameraposition(MakeExamples())
             )),
#             ('domain', ),  # TODO change name (confusing with axis.domain)
#             ('position', ),  # TODO (needed? overlaps with 'domain');
             ('bgcolor', make.bgcolor('scene'))
        ])
        self += self._stuff('scene', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)


    def legend(self):
        '''@legend@'''
        name = '{legend}'
        obj_type = "{UL}"
        parent_keys = ["legend"]
        docstring = (
            "{A_ULlike} for representing a legend in plotly."
        )
        links = [
            "{WEB}legend/",
            "{WEB}figure-labels/"
        ]
        examples = MakeExamples.legend(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.xy_layout('legend', 'x')),
            ('y', make.xy_layout('legend', 'y')),
            ('traceorder', dict(
                required=False,
                key_type='style',
                val_types="'normal' | 'reversed'",
                description=(
                    "Trace order is set by the order of trace in the data {UL}. "
                    "The 'traceorder' key sets whether "
                    "the legend labels are shown from first-to-last trace "
                    "('normal') or from last-to-first ('reversed')."
                )
            )),
            ('font', make.font('legend')),
            ('bgcolor', make.bgcolor('legend')),
            ('bordercolor', make.bordercolor('legend')),
            ('borderwidth', make.borderwidth('legend')),
            ('xref', make.xyref('legend','x')),
            ('yref', make.xyref('legend','y')),
            ('xanchor', make.xyanchor('legend','x')),
            ('yanchor', make.xyanchor('legend','y'))
        ])
        self += self._stuff('legend', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def colorbar(self):
        '''@colorbar@'''
        name = '{colorbar}'
        obj_type = "{UL}"
        parent_keys = ["colorbar"]
        docstring = (
            "{A_ULlike} object for representing a color bar in plotly."
        )
        links = []
        examples = MakeExamples.colorbar(MakeExamples())
        _keymeta = [
            ('title', make.title('colorbar')),
            ('titleside', dict(
                required=False,
                key_type='style',
                val_types="'right' | 'top' | 'bottom'",
                description=(
                    "Location of colorbar title with respect to the colorbar."
                )
            )),
            ('titlefont', make.titlefont('colorbar')),
            ('thickness', make.thickness('colorbar')),
            ('thicknessmode', dict(
                required=False,
                key_type='style',
                val_types="string: 'pixels' | 'fraction' ",
                description="Sets thickness unit mode."
            )),
            ('len', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0),
                description="Sets the length of the colorbar."
            )),
            ('lenmode', dict(
                required=False,
                key_type='style',
                val_types="string: 'pixels' | 'fraction' ",
                description="Sets length unit mode."
            )),
            ('autotick', make.autotick('colorbar')),
            ('nticks', make.nticks('colorbar'))
        ]
        _keymeta += self._keymeta_ticks('colorbar')
        _keymeta += [
            ('x', make.xy_layout('colorbar','x')),
            ('y', make.xy_layout('colorbar','y')),
            ('xanchor', make.xyanchor('colorbar','x')),
            ('yanchor', make.xyanchor('colorbar','y')),
            ('bgcolor', make.bgcolor('colorbar')),
            ('outlinecolor', make.outlinecolor('colorbar')),
            ('outlinewidth', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(),
                description=(
                    "Sets the width of the outline surrounding this colorbar."
                )
            )),
            ('bordercolor', make.bordercolor('colorbar')),
            ('borderwidth', make.borderwidth('colorbar')),
            ('xpad', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(le=50, ge=0),
                description=(
                    "Sets the amount of space (padding) between the colorbar and "
                    "the enclosing boarder in the x-direction."
                )
            )),
            ('ypad', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(le=50, ge=0),
                description=(
                    "Sets the amount of space (padding) between the colorbar and "
                    "the enclosing boarder in the y-direction."
                )
            ))
        ]
        keymeta = OrderedDict(_keymeta)
        self += self._stuff('colorbar', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def margin(self):
        '''@margin@'''
        name = '{margin}'
        obj_type = "{UL}"
        parent_keys = ["margin"]
        docstring = (
            "{A_ULlike} containing specification of the margins."
        )
        links = ["{WEB}setting-graph-size/"]
        examples = MakeExamples.margin(MakeExamples())
        keymeta = OrderedDict([
            ('l', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(ge=0),
                description="Sets the left margin size in pixels."
            )),
            ('r', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(ge=0),
                description="Sets the right margin size in pixels."
            )),
            ('b', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(ge=0),
                description="Sets the bottom margin size in pixels."
            )),
            ('t', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(ge=0),
                description="Sets the top margin size in pixels."
            )),
            ('pad', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(ge=0),
                description=(
                    "Sets the distance between edge of the plot and the "
                    "bounding rectangle that encloses the plot (in pixels)."
                )
            )),
            ('autoexpand', dict(  # TODO: ??
                required=False,
                key_type='plot_info',
                val_types=val_types.bool(),
                description="more info coming soon"
            ))
        ])
        self += self._stuff('margin', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def annotation(self):
        '''@annotation@'''
        name = '{annotation}'
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} for representing an annotation in plotly. "
            "Annotations appear as notes on the final figure. "
            "You can set all the features of the annotation text, "
            "background color, and location. "
            "Additionally, these notes can be anchored to actual data "
            "or the page for help with location after pan-and-zoom actions."
        )
        links = ["{WEB}text-and-annotations/"]
        examples = MakeExamples.annotation(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.xy_layout('annotation','x')),
            ('y', make.xy_layout('annotation','y')),
            ('xref', make.xyref('annotation','x')),
            ('yref', make.xyref('annotation','y')),
            ('text', dict(      # Different enough from shortcut-text
                required=False,
                key_type='plot_info',
                val_types=val_types.string(),
                description=(
                    "The text associated with this annotation. "
                    "Plotly uses a subset of HTML tags "
                    "to do things like newline (<br>), bold (<b></b>), "
                    "italics (<i></i>), hyperlinks (<a href='...'></a>). "
                    "Tags <em>, <sup>, <sub>, <span> are also supported."
                ),
                examples = MakeExamples.text(MakeExamples())
            )),
            ('showarrow', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not the arrow associated with "
                    "this annotation with be shown. "
                    "If {FALSE}, then the text linked to 'text' lines up with "
                    "the 'x', 'y' coordinates'. If {TRUE} (the default), then "
                    "'text' is placed near the arrow's tail."
                )
            )),
            ('font', make.font('annotation')),
            ('xanchor', make.xyanchor('annotation','x')),
            ('yanchor', make.xyanchor('annotation','y')),
            ('align', dict(
                required=False,
                key_type='plot_info',
                val_types="'left' | 'center' | 'right'",
                description=(
                    "Sets the vertical alignment of the text in the "
                    "annotation with respect to the set 'x', 'y' position. "
                    "Has only an effect if the text linked to "
                    "'text' spans more two or more lines "
                    "(using <br> HTML one or more tags)."
                )
            )),
            ('arrowhead', dict(
                required=False,
                key_type='style',
                val_types='0 | 1 | 2 | 3 | 4 | 5 | 6 | 7',
                description=(
                    "Sets the arrowhead style. "
                    "Has an effect only if 'showarrow' is set to True."
                )
            )),
            ('arrowsize', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "Scales the arrowhead's size. "
                    "Has an effect only if 'showarrow' is set to {TRUE}."
                )
            )),
            ('arrowwidth', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the arrowhead's width (in pixels). "
                    "Has an effect only if 'showarrow' is set to {TRUE}."
                )
            )),
            ('arrowcolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the arrowhead. "
                    "Has an effect only if 'showarrow' is set to {TRUE}."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('ax', dict(            # TODO Better description
                required=False,
                key_type='plot_info',
                val_types=val_types.number(),
                description=(
                    "Position of the annotation text relative to the "
                    "arrowhead about the x-axis. "
                    "Has an effect only if 'showarrow' is set to {TRUE}."
                )
            )),
            ('ay', dict(            # TODO Better description
                required=False,
                key_type='plot_info',
                val_types=val_types.number(),
                description=(
                    "Position of the annotation text relative to the "
                    "arrowhead about the y-axis. "
                    "Has an effect only if 'showarrow' is set to {TRUE}."
                )
            )),
            ('textangle', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=-180,le=180),
                description=(
                   "Sets the angle of the text linked to 'text' with respect "
                   "to the horizontal."
                )
            )),
            ('bordercolor', make.bordercolor('annotation')),
            ('borderwidth', make.borderwidth('annotation')),
            ('borderpad', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(le=10, ge=0),
                description=(
                    "The amount of space (padding) between the text and "
                    "the enclosing boarder."
                )
            )),
            ('bgcolor', make.bgcolor('annotation')),
            ('opacity', make.opacity())
        ])
        self += self._stuff('annotation', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def layout(self):
        '''@layout@'''
        name = '{layout}'
        obj_type = "{UL}"
        parent_keys = ["layout"]
        docstring = (
            "{A_ULlike} containing specification of the layout "
            "of a plotly figure."
        )
        links = [
            "{WEB}figure-labels/",
            "{WEB}axes/",
            "{WEB}bar-charts/",
            "{WEB}log-plot/"
        ]
        examples = MakeExamples.layout(MakeExamples())
        keymeta = OrderedDict([
            ('title', make.title('layout')),
            ('titlefont', make.titlefont('layout')),
            ('font', make.font('layout')),
            ('showlegend', make.showlegend(layout=True)),
            ('autosize', dict(
                required=False,
                key_type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not the dimensions of the figure are "
                    "automatically picked by Plotly. Plotly picks figure's "
                    "dimensions as a function of your machine's display "
                    "resolution. "
                    "Once 'autosize' is set to {FALSE}, the figure's dimensions "
                    "can be set with 'width' and 'height'."
                )
            )),
            ('width', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the width in pixels of the figure you are generating."
                )
            )),
            ('height', dict(
                required=False,
                key_type='plot_info',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the height in pixels of the figure you are generating."
                )
            )),
            ('xaxis', make.axis('x', layout=True)),
            ('yaxis', make.axis('y', layout=True)),
            ('legend', dict(
                required=False,
                key_type='object',
                val_types=val_types.object(),
                description=(
                    "Links {a_ULlike} containing the legend "
                    "parameters for this figure."
                )
            )),
            ('annotations', dict(
                required=False,
                key_type='object',
                val_types=val_types.object_list(),
                description=(
                    "Links {a_OLlike} that contains one or multiple "
                    "annotation {pl_ULlike}."
                )
            )),
            ('margin', dict(
                required=False,
                key_type='object',
                val_types=val_types.object(),
                description=(
                    "Links {a_ULlike} containing the margin "
                    "parameters for this figure."
                )
            )),
            ('paper_bgcolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the figure's paper "
                    "(i.e. area representing the canvas of the figure)."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('plot_bgcolor', dict(
                required=False,
                key_type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the background color of the plot (i.e. the area "
                    "laying inside this figure's axes."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('hovermode', dict(
                required=False,
                key_type='style',
                val_types="'closest' | 'x' | 'y'",
                description=(
                    "Sets this figure's behavior when a user hovers over it. "
                    "When set to 'x', all data sharing the same 'x' "
                    "coordinate will be shown on screen with "
                    "corresponding trace labels. When set to 'y' all data "
                    "sharing the same 'y' coordinates will be shown on the "
                    "screen with corresponding trace labels. When set to "
                    "'closest', information about the data point closest "
                    "to where the viewer is hovering will appear."
                )
            )),
            ('dragmode', dict(
                required = False,
                key_type = 'style',
                val_types = "'zoom' | 'pan' | 'rotate' (in 3D plots)",
                description = (
                    "Sets this figure's behavior when a user preforms a mouse "
                    "'drag' in the plot area. When set to 'zoom', a portion of "
                    "the plot will be highlighted, when the viewer "
                    "exits the drag, this highlighted section will be "
                    "zoomed in on. When set to 'pan', data in the plot "
                    "will move along with the viewers dragging motions. A "
                    "user can always depress the 'shift' key to access "
                    "the whatever functionality has not been set as the "
                    "default. In 3D plots, the default drag mode is 'rotate' "
                    "which rotates the scene."
                )
            )),
            ('separators', dict(
                required=False,
                key_type='style',
                val_types="a two-character string",
                description=(
                    "Sets the decimal (the first character) and thousands "
                    "(the second character) separators to be displayed on "
                    "this figure's tick labels and hover mode. "
                    "This is meant for internationalization purposes. "
                    "For example, if "
                    "'separator' is set to ', ', then decimals are separated "
                    "by commas and thousands by spaces. "
                    "One may have to set 'exponentformat' to 'none' "
                    "in the corresponding axis object(s) to see the "
                    "effects."
                )
            )),
            ('barmode', dict(
                required=False,
                key_type='plot_info',
                val_types="'stack' | 'group' | 'overlay'",
                description=(
                    "For bar and histogram plots only. "
                    "This sets how multiple bar objects are plotted "
                    "together. In other words, this defines how bars at "
                    "the same location appear on the plot. If set to "
                    "'stack' the bars are stacked on top of one another. "
                    "If set to 'group', the bars are plotted next to one "
                    "another, centered around the shared location. If set "
                    "to 'overlay', the bars are simply plotted over one "
                    "another, you may need to set the opacity to see this."
                )
            )),
            ('bargap', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0, lt=1),
                description=(
                    "For bar and histogram plots only. "
                    "Sets the gap between bars (or sets of bars) at "
                    "different locations."
                )
            )),
            ('bargroupgap', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0, lt=1),
                description=(
                    "For bar and histogram plots only. "
                    "Sets the gap between bars in the same group. "
                    "That is, when multiple bar objects are plotted and "
                    "share the same locations, this sets the distance "
                    "between bars at each location."
                )
            )),
            ('boxmode', dict(
                required=False,
                key_type='plot_info',
                val_types="'overlay' | 'group'",
                description=(
                    "For box plots only. "
                    "Sets how groups of box plots appear. "
                    "If set to 'overlay', a group of boxes "
                    "will be plotted directly on top of one "
                    "another at their specified location. "
                    "If set to 'group', the boxes will be "
                    "centered around their shared location, "
                    "but they will not overlap."
                )
            )),
            ('boxgap', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0, lt=1),
                description=(
                    "For box plots only. "
                    "Sets the gap between boxes at "
                    "different locations (i.e. x-labels). "
                    "If there are multiple boxes at a single x-label, "
                    "then this sets the gap between these sets of boxes."
                    "For example, if 0, then there is no gap between boxes. "
                    "If 0.25, then this gap occupies 25% of the "
                    "available space and the box width "
                    "(or width of the set of boxes) occupies "
                    "the remaining 75%."
                )
            )),
            ('boxgroupgap', dict(
                required=False,
                key_type='style',
                val_types=val_types.number(ge=0, lt=1),
                description=(
                    "For box plots only. "
                    "Sets the gap between boxes in the same group, "
                    "where a group is the set of boxes with the "
                    "same location (i.e. x-label). "
                    "For example, if 0, then there is no gap between boxes. "
                    "If 0.25, then this gap occupies 25% of the available "
                    "space and the box width occupies the remaining 75%."
                )
            )),
            ('radialaxis', dict(
                required=False,
                key_type='object',
                val_types=val_types.object(),
                description=(
                    "Links {a_ULlike} describing the radial axis "
                    "in a polar plot."
                )
            )),
            ('angularaxis', dict(
                required=False,
                key_type='object',
                val_types=val_types.object(),
                description=(
                    "Links {a_ULlike} describing the angular axis "
                    "in a polar plot."
                )
            )),
            ('scene', dict(
                required=False,
                key_type='object',
                val_types=val_types.object(),
                description=(
                "Links {a_ULlike} describing a scene in a 3D plot. "
                "The first {scene} object can be entered into "
                "'layout' by linking it to 'scene' OR "
                "'scene1', both keys are identical to Plotly. "
                "Link subsequent {scene} objects using "
                "'scene2', 'scene3', etc."
                )
            )),
            ('direction', dict(
                required=False,
                key_type='plot_info',
                val_types="'clockwise' | 'counterclockwise'",
                description=(
                    "For polar plots only. "
                    "Sets the direction corresponding to "
                    "positive angles."
                )
            )),
            ('orientation', dict(  # Different enough than in shortcut-orientation
                required=False,
                key_type='plot_info',
                val_types=val_types.number(ge=-360,le=360),
                description=(
                   "For polar plots only. "
                   "Rotates the entire polar by the given angle."
                )
            )),
            ('hidesources', dict(
                required=False,
                key_type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not an annotation citing the data "
                    "source is placed at the bottom-right corner of the figure."
                    "This key has an effect only on graphs that have been "
                    "generated from forked graphs from plot.ly."
                )
            ))
        ])
        self += self._stuff('layout', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def figure(self):
        '''@figure@'''
        name = '{figure}'
        obj_type = "{UL}"
        parent_keys = []
        docstring = (
            "{A_ULlike} representing a figure to be rendered by plotly. "
            "This is the container for all things to be rendered in a figure."
        )
        links = []
        examples = MakeExamples.figure(MakeExamples())
        keymeta = OrderedDict([
            ('data', dict(
                required=False,
                key_type='object',
                val_types=val_types.object_list(),
                description=(
                    "{A_OLlike} of one or multiple trace {pl_ULlike} to be "
                    "shown on one plotly figure."
                )
            )),
            ('layout', dict(
               required=False,
               key_type='object',
               val_types=val_types.object(),
               description=(
                   "{A_ULlike} that contains the layout "
                   "parameters (e.g. information about the axis, "
                   "global settings and layout information "
                   "related to the rendering of the figure)."
               )
            ))
        ])
        self += self._stuff('figure', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def data(self):
        '''@data@ (accepts no keys)'''
        name = '{data}'
        obj_type = "{OL}"
        parent_keys = ["data"]
        docstring = (
            "{A_OLlike} of trace {pl_ULlike} to be shown on one plotly figure."
        )
        links = []
        examples = MakeExamples.data(MakeExamples())
        keymeta = dict()
        self += self._stuff('data', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

    def annotations(self):
        '''@annotations@ (accepts no keys)'''
        name = '{annotations}'
        obj_type = "{OL}"
        parent_keys = ["annotations"]
        docstring = (
            "{A_OLlike} of annotation {pl_ULlike} to be shown on one plotly figure."
        )
        links = []
        examples = MakeExamples.annotations(MakeExamples())
        keymeta = dict()
        self += self._stuff('annotations', name, obj_type, parent_keys,
                            docstring, examples, links, keymeta)

# -------------------------------------------------------------------------------
