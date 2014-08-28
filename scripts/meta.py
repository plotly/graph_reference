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
        global val_types       # N.B no need to type self.val_types(...)
        val_types = ValTypes()
        global required_cond
        required_cond = RequiredCond()
        global make
        make = Make()

    def _stuff(self, name, docstring, examples, links, keymeta):
        ''' @stuff@ -- Return a list of a tuple packaging graph object stuff
        '''
        return [(name, 
            OrderedDict([
                ('docstring', docstring),
                ('examples',examples), 
                ('links', links), 
                ('keymeta', keymeta)
            ])
        )]

    def Scatter(self):
        '''@Scatter@'''
        name = 'scatter'
        docstring = (
            "A {UL}-like object for representing a scatter trace in plotly."
        )
        links = [
            "{WEB}line-and-scatter/",
            "{WEB}bubble-charts/",
            "{WEB}filled-area-plots/",
            "{WEB}time-series/"
        ]
        examples = MakeExamples.Scatter(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.x('scatter')),
            ('y', make.y('scatter')),
            ('r', make.r('scatter')),  
            ('t', make.t('scatter')),
            ('mode', dict(
                required=False,
                type='style',
                val_types=(
                    "'lines' | 'markers' | 'text' | 'lines+markers' | "
                    "'lines+text' | 'markers+text' | 'lines+markers+text'"
                ),
                description=(
                    "Plotting mode (or style) for the scatter plot. If the "
                    "mode includes 'text' then the 'text' will appear at "
                    "the (x,y) points, otherwise it will appear on "
                    "hover."
                )
            )),
            ('name', make.name()),
            ('text', make.text('scatter')),
            ('error_y', make.error('scatter','y')),
            ('error_x', make.error('scatter','x')),
            ('marker', make.marker('scatter')),
            ('line', make.line('scatter')),
            ('textposition', dict(
                required=False,
                type='style',
                val_types=(
                    "'top left' | 'top' (or 'top center')| 'top right' | "
                    "'left' (or 'middle left') | '' (or 'middle center') |"
                    "'right' (or 'middle right') |"
                    "'bottom left' | 'bottom' (or 'bottom center') |"
                    "'bottom right'"
                ),
                description=(
                    "Sets the position of the text elements "
                    "in the 'text' key with respect to the data points. "
                    "By default, the text elements are plotted directly "
                    "at the (x,y) coordinates."
                )
            )),
            ('textfont', make.textfont('scatter')),
            ('connectgaps', dict(
                required=False,
                type='plot_info',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not missing data points "
                    "(i.e. '' or {NAN}) linked to 'x' and/or 'y', are "
                    "added in by Plotly using linear interpolation."
                )
            )),
            ('fill', dict(
                required=False,
                type='style',
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
            ('type', make.type('scatter')),
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
 
    def Bar(self):
        '''@Bar@'''
        name = 'bar'
        docstring = (
            "A {UL}-like object for representing a bar trace in plotly."
        )
        links = ["{WEB}bar-charts/"]
        examples = MakeExamples.Bar(MakeExamples())
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
            ('type', make.type('bar')),
            ('r', make.r('bar')),   # ARTIFACT
            ('t', make.t('bar')),   # ARTIFACT
            ('line', make.line('bar')),  # ARTIFACT
            ('textfont', make.textfont('bar'))  # ARTIFACT
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def Histogram(self):
        '''@Histogram@'''
        name = 'histogram'
        docstring = (
            "A {UL}-like object for representing a histogram trace in plotly."
        )
        links = ["{WEB}histograms/"]
        examples = MakeExamples.Histogram(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.x('histogram')),
            ('y', make.y('histogram')),
            ('histnorm', make.histnorm()),
            ('name', make.name()),
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
            ('type', make.type('histogram')),
            ('line', make.line('histogram')),  # ARTIFACT
            ('orientation', make.orientation('histogram'))  # ARTIFACT
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Box(self):
        '''@Box@'''
        name = 'box'
        docstring = (
            "A {UL}-like object for representing a box trace in plotly."
        )
        links = ["{WEB}box-plots/"]
        examples = MakeExamples.Box(MakeExamples())
        keymeta = OrderedDict([
            ('y', make.y('box')),
            ('x0', make.x0y0('box')),
            ('x', make.x('box')),
            ('name', make.name()),
            ('boxmean', dict(
                required=False,
                type='style',
                val_types="False | True | 'sd'",
                description=(
                    "Choose between add-on features for this box trace. "
                    "If True then the mean of the data linked to 'y' is shown "
                    "as a dashed line in the box. If 'sd', then the standard "
                    "deviation is also shown. If False (the default), "
                    "then no line shown."
                )
            )),
            ('boxpoints', dict(
                required=False,
                type='style',
                val_types="'outliers' | 'all' | 'suspectedoutliers' | False",
                description=(
                    "Choose between boxpoints options for this box trace. "
                    "If 'outliers' (the default), then only the points lying "
                    "outside the box' whiskers (more info in 'y') are shown. "
                    "If 'all', then all data points linked 'y' are shown. "
                    "If 'suspectedoutliers', then outliers points are shown and "
                    "points either less than 4*Q1-3*Q3 or greater than "
                    "4*Q3-3*Q1 are highlighted (with 'outliercolor' in Marker). "
                    "If False, then only the boxes are shown and the whiskers "
                    "correspond to the minimum and maximum value linked to 'y'."
                )
            )),
            ('jitter', dict(
                required=False,
                type='style',    
                val_types=val_types.number(ge=0,le=1),
                description=(
                    "Sets the width of the jitter in the boxpoints scatter "
                    "in this trace. "
                    "Has an no effect if 'boxpoints' is set to False. "
                    "If 0, then the "
                    "boxpoints are aligned vertically. If 1 then the "
                    "boxpoints are placed in a random horizontal jitter of width "
                    "equal to the width of the boxes."
                )
            )),
            ('pointpos', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=-2, le=2),
                description=(
                    "Sets the horizontal position of the boxpoints "
                    "in relation to the boxes in this trace. "
                    "Has an no effect if 'boxpoints' is set to False. "
                    "If 0, then the boxpoints are placed over the center of " 
                    "each box. If 1 (-1), then the boxpoints are placed on the "
                    "right (left) each box border. "
                    "If 2 (-2), then the boxpoints are  "
                    "placed 1 one box width to right (left) of each box. "
                )
            )),
            ('whiskerwidth', dict(
                required=False,
                type='style',
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
            ('type', make.type('box'))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Heatmap(self):
        '''@Heatmap@'''
        name = 'heatmap'
        docstring = (
            "A {UL}-like object for representing a heatmap trace in plotly."
        )
        links = ["{WEB}heatmaps/"]
        examples = MakeExamples.Heatmap(MakeExamples())
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
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Contour(self):
        '''@Contour@'''
        name = 'contour'
        docstring = (
            "A {UL}-like object for representing a contour trace in plotly."
        )
        links = ["{WEB}contour-plots/"]
        examples = MakeExamples.Contour(MakeExamples())
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
        self += self._stuff(name, docstring, examples, links, keymeta)

    def Histogram2d(self):
        '''@Histogram2d@'''
        name = 'histogram2d'
        docstring = (
            "A {UL}-like object for representing a 2D histogram trace in plotly."
        )
        links = ["{WEB}2D-Histograms/"]
        examples = MakeExamples.Histogram2d(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.x('histogram2d')),
            ('y', make.y('histogram2d')),
            ('histnorm', make.histnorm()),
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
            ('type', make.type('histogram2d'))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Histogram2dContour(self):
        '''@Histogram2dContour@'''
        name = 'histogram2dcontour'
        docstring = (
            "A {UL}-like object for representing a 2D histogram contour "
            "trace in plotly."
        )
        links = ["{WEB}2D-Histograms/"]
        examples = MakeExamples.Histogram2dContour(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.x('histogram2dcontour')),
            ('y', make.y('histogram2dcontour')),
            ('histnorm', make.histnorm()),
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
            ('type', make.type('histogram2dcontour'))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Area(self):
        '''@Area@'''
        name = 'area'
        docstring = (
            "A {UL}-like object for representing an area trace in plotly."
        )
        links = ["{WEB}polar-chart/"]
        examples = MakeExamples.Area(MakeExamples())
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
                type='plot_info',
                val_types='',
                description=(
                    'Polar chart subplots are not supported yet. Info coming soon'
                )
            )),
            ('radialaxis', dict(  #Q? How do polar axes this work?
                required=False,
                type='plot_info',
                val_types='',
                description=(
                    'Polar chart subplots are not supported yet. Info coming soon'
                )
            )),
            ('type', make.type('area'))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def keymeta_error(self,y_or_x):
        '''@keymeta_error@ -- keymeta for ErrorY and ErrorX'''
    
        S = {'y': ['y','vertically','up','down','above','below'],
             'x': ['x','horizontally','right','left','right of','left of']}
        s = S[y_or_x]
        
        _keymeta = [
            ('type', dict(      # Different enough from shortcut
                required=False,
                type='plot_info', 
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
                type='plot_info',
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
                type='data',
                val_types=val_types.data_array(),
                description=(
                   "The array of corresponding to "
                   "error bars' span to be drawn. "
                   "Has only an effect if 'type' is set to "
                   "'data'. Values in the array are plotted "
                   "relative to the '{S0}' coordinates. "
                   "For example, with '{S0}'=[1,2] and "
                   "'array'=[1,2], the error bars will span "
                   "{S1} from {S0}= 0 to 2 and {S0}= 0 to 4 if "
                   "'symmetric'=True; and from {S0}= 1 to 2 and "
                   "{S0}= 2 to 4 if 'symmetric' is set to False "
                   "and 'arrayminus' is empty."
                ).format(S0=s[0],S1=s[1])
            )),
            ('value', dict(
                required=False,
                type='plot_info',
                val_types=val_types.number(ge=0),
                description=(
                   "The value or percentage determining the error bars' "
                   "span, at all trace coordinates. "
                   "Has an effect if 'type' is set to 'value' or "
                   "'percent'. "
                   "If 'symmetric' is set to False, this value corresponds "
                   "to the span {S4} the trace of coordinates. "
                   "To specify multiple error bar lengths, "
                   "you should set 'type' to 'data' and "
                   "use the 'array' key instead."
                ).format(S4=s[4])
            )),
            ('arrayminus', dict(
                required=False,
                type='data',
                val_types=val_types.number(ge=0),
                description=(
                      "Only functional when 'symmetric' is set to False. "
                      "Same as 'array' but corresponding to the span "
                      "of the error bars {S5} the trace coordinates"
                ).format(S5=s[5])
            )),
            ('valueminus', dict(
                required=False,
                type='plot_info',
                val_types=val_types.number(ge=0),
                description=(
                      "Only functional when 'symmetric' "
                      "is set to False. Same as 'value' but corresponding "
                      "to the span of the error bars {S5} the trace coordinates"
                ).format(S5=s[5])
            )),
            ('color', make.color('error')),
            ('thickness', make.thickness('error',y_or_x)),
            ('width', make.width('error')),
            ('opacity', make.opacity()),
        ]
    
        if y_or_x=='x':
            _keymeta += [
                ('copy_ystyle', dict(
                    required=False,
                    type='style',
                    val_types=val_types.bool(),
                    description=(
                          "Toggle whether to set x error bar "
                          "style to the same style "
                          "(color, thickness, width, opacity) "
                          "as y error bars set in YAxis."
                    )
                ))
            ]
    
        _keymeta += [('visible', make.visible())]
        return _keymeta
      
    def ErrorY(self):
        '''@ErrorY@'''
        name = 'error_y'
        docstring = (
            "A {UL}-like object representing a set of error bar spanning "
            "along the y-axis."
        )
        links = ["{WEB}error-bars/"]
        examples = MakeExamples.ErrorY(MakeExamples())
        keymeta = OrderedDict(self.keymeta_error('y'))
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def ErrorX(self):
        '''@ErrorX@'''
        name = 'error_x'
        docstring = (
            "A {UL}-like object representing a set of error bars spanning "
            "along the x-axis."
        )
        links = ["{WEB}error-bars/"]
        examples = MakeExamples.ErrorX(MakeExamples())
        keymeta = OrderedDict(self.keymeta_error('x'))
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def keymeta_bins(self,x_or_y):
        '''@keymeta_bins@ -- keymeta for XBins and YBins'''
        _keymeta = [
            ('start', make.startend('bins','start',x_or_y)),
            ('end', make.startend('bins','end',x_or_y)),
            ('size', make.size('bins',x_or_y))
        ]
        return _keymeta
    
    def XBins(self):
        '''@XBins@'''
        name = 'xbins'
        docstring = (
            "A {UL}-like object containing specifications of the bins "
            "lying along the x-axis."
        )
        links = [
            "{WEB}histograms/",
            "{WEB}2D-Histograms/"
        ]
        examples = MakeExamples.XBins(MakeExamples())
        keymeta = OrderedDict(self.keymeta_bins('x'))
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def YBins(self):
        '''@YBins@'''
        name = 'ybins'
        docstring = (
            "A {UL}-like object containing specifications of the bins "
            "lying along the y-axis."
        )
        links = [
            "{WEB}histograms/"
            "{WEB}2D-Histograms/"
        ]
        examples = MakeExamples.YBins(MakeExamples())
        keymeta = OrderedDict(self.keymeta_bins('y'))
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Contours(self):
        '''@Contours@'''
        name = 'contours'
        docstring = (
            "A {UL}-like object containing specifications of the contours."
        )
        links = ["{WEB}contour-plots/"]
        examples = MakeExamples.Contours(MakeExamples())
        keymeta = OrderedDict([
            ('showlines', dict(
                required=False, type='style',
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
                type='style',
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
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def Stream(self):
        '''@Stream@'''
        name = 'stream'
        docstring = (
            "A {UL}-like object containing specifications of the data stream."
        )
        links = ["{WEB}streaming/"]
        examples = MakeExamples.Stream(MakeExamples())
        keymeta = OrderedDict([
            ('token', dict(  #Q? These are public!! Is that OK?
                required=True,
                type='plot_info',
                val_types="A stream id number, see https://plot.ly/settings",
                description=(
                    "This number links a data object on a plot with a "
                    "stream. In other words, any data object you create "
                    "can reference a 'stream'. If you stream data to "
                    "Plotly with the same stream id (token), Plotly knows "
                    "update this data object with the incoming data "
                    "stream."
                )
            )),
            ('maxpoints', dict(
                required=False,
                type='style',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the maximum number of points to keep on the "
                    "plots from an incoming stream. For example, "
                    "if 'maxpoints' is set to 50, only the newest 50 points "
                    "will be displayed on the plot."
                )
            ))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def Marker(self):
        '''@Marker@'''
        name = 'marker'
        docstring = (
            "A {UL}-like object containing specifications of the marker points."
        )
        links = [
            "{WEB}line-and-scatter/",
            "{WEB}bubble-charts/"
        ]
        examples = MakeExamples.Marker(MakeExamples())
        keymeta = OrderedDict([
            ('color', make.color('marker')),
            ('size', make.size('marker')),
            ('symbol', dict(
                required=False,
                type='style',
                val_types=(
                    "'dot' | 'cross' | 'diamond' | 'square' "
                    "| 'triangle-down' | 'triangle-left' | 'triangle-right' "
                    "| 'triangle-up' | 'x' OR list of these string values"
                ),
                description=(
                      "The symbol that is drawn on the plot for each marker. "
                      "Supported only in scatter traces. "
                      "If 'symbol' is linked to a list or an array of numbers, "
                      "symbol values are mapped to individual marker points "
                      "in the same order as in the data lists or arrays."
                )
            )),
            ('line', make.line('marker')),
            ('opacity', make.opacity(marker=True)),
            ('sizeref', dict(  
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "Sets the scale factor used to determine the rendered size "
                    "of each marker point in this trace. "
                    "Applies only to scatter traces that have an array linked "
                    "to the 'size' key in Marker. "
                    "If set, the value linked to 'sizeref' is used to divide "
                    "each entry linked to 'size'. That is, setting 'sizeref' to "
                    "less (greater) than 1, increases (decreases) the "
                    "rendered marker sizes."
                )
            )),
            ('sizemode', dict(  
                required=False,
                type='style',
                val_types="'diameter'| 'area'",
                description=(
                    "Choose between marker size scaling options for the marker "
                    "points in this trace. "
                    "Applies only to scatter traces that have an array linked "
                    "to the 'size' key in Marker. "
                    "If 'diameter' ('area'), then the diameter (area) of the "
                    "rendered marker points (in pixels) are "
                    "proportional to the numbers linked to 'size'." 
                    "E.g. set 'sizemode' to 'area' for a more a smaller "
                    "range of rendered marker sizes."
                )
            )),
            ('colorscale', make.colorscale('c')),
            ('cauto', make.zcauto('c')),
            ('cmin', make.zcminmax('min','color')),
            ('cmax', make.zcminmax('max','color')),
            ('outliercolor', dict(
                required=False,
                type='style',  
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
                type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "Sets maximum number of displayed points for this "
                    "trace. Applies only to scatter traces."
                )
            ))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def Line(self):
        '''@Line@'''
        name = 'line'
        docstring = (
            "A {UL}-like object containing specifications of the line segments."
        )
        links = [
            "{WEB}line-and-scatter/",
            "{WEB}filled-area-plots/",
            "{WEB}contour-plots/"
        ]
        examples = MakeExamples.Line(MakeExamples())
        keymeta = OrderedDict([
            ('color', make.color('line')),
            ('width', make.width('line')),
            ('dash', dict(
                required=False,
                type='style',
                val_types="'dash' | 'dashdot' | 'dot' | 'solid'",
                description="Sets the drawing style of this line object."
            )),
            ('opacity', make.opacity()),
            ('shape', dict(
                required=False,
                type='style',
                val_types="'linear' | 'spline' | 'hv' | 'vh' | 'hvh' | 'vhv'",
                description=(
                    "Choose the line shape between each coordinate pair "
                    "in this trace. "
                    "Applies only to scatter traces. " 
                    "The default value is 'linear'. "
                    "If 'spline', then the lines are drawn using spline "
                    "interpolation between the coordinate pairs. "
                    "The remaining available values correspond to "
                    "step-wise line shapes."
               )
            )),
            ('smoothing', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description=(
                   "Sets the amount of smoothing applied to this line object. "
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
                type='style',  
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
                type='style',  
                val_types=val_types.color(),
                description=(
                    "For box plots only. Has an effect only if 'boxpoints' is "
                    "set to 'suspectedoutliers'. Sets the width in pixels of "
                    "bordering line of the outlier points."
               ),
               examples=MakeExamples.color(MakeExamples())
            ))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Font(self):
        '''@Font@'''
        name = 'font'
        docstring = (
            "A {UL}-like object containing specifications of the text font."
        )
        links = [
            "{WEB}font/",
            "{WEB}text-and-annotations/",
            "{WEB}line-and-scatter/"
        ]
        examples = MakeExamples.Font(MakeExamples())
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
                type='style',
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
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def keymeta_ticks(self,axis_or_colorbar):
        '''@keymeta_ticks@ -- ticks keymeta for XAxis, YAxis and ColorBar''' 
        _keymeta = [
            ('ticks', dict(
                  required=False,
                  type='style',
                  val_types="'' | 'inside' | 'outside'",
                  description=(
                      "Sets the format of tick visibility on this {}."
                  ).format(axis_or_colorbar)
            )),
            ('showticklabels', make.showticklabels(axis_or_colorbar)),
            ('tick0', dict(
                required=False,
                type='style',
                val_types=val_types.number(),
                description=(
                    "Sets the starting point of the ticks of this {}."
                ).format(axis_or_colorbar)
            )),
            ('dtick', dict(
                required=False,
                type='style',
                val_types=val_types.number(),
                description=(
                    "Sets the distance between ticks on this {}."
                ).format(axis_or_colorbar)
            )),
            ('ticklen', dict(
                required=False,
                type='style',
                val_types=val_types.number(),  # Units?
                description=(
                    "Sets the length of the tick lines on this {}."
                ).format(axis_or_colorbar)
            )),
            ('tickwidth', dict(
                required=False,
                type='style',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the width of the tick lines on this {}."
                ).format(axis_or_colorbar)
            )),
            ('tickcolor', dict(
                required=False,
                type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the tick lines on this {}."
                ).format(axis_or_colorbar),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('tickangle', dict(
                required=False,
                type='style',
                val_types=val_types.number(le=90, ge=-90),
                description=(
                    "Sets the angle in degrees of the ticks on this {}."
                ).format(axis_or_colorbar)
            )),
            ('tickfont', dict(
                required=False,
                type='object',
                val_types=val_types.object(),
                description=(
                    "A dictionary-like object defining the parameters "
                    "of the ticks' font."
                )
            )),
            ('exponentformat', dict(
                required=False,
                type='style',
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
                type='style',
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
      
    def keymeta_axis(self,x_or_y):
        '''@make.axis@ -- keymeta for XAxis and YAxis'''
          
        S = {'x':['x','bottom','top','y','left','right','vertical'], 
             'y':['y','left','right','x','bottom','top','horizontal']}
        s = S[x_or_y]
      
        _keymeta = [
            ('title', make.title('axis',x_or_y)),
            ('titlefont', make.titlefont('axis',x_or_y)),
            ('range', make.range(x_or_y)),
            ('domain', make.domain(x_or_y)),
            ('type', dict(      # Different enough from shortcut
                required=False,
                type='style',
                val_types="'linear' | 'log' | 'date' | 'category'",
                description="Sets the format of this axis."  # TODO! Add info
            )),
            ('rangemode', dict(
                required=False,
                type='style',
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
                type='style',
                val_types="True | False | 'reversed'",
                description=(
                    "Toggle whether or not the range of this {S0}-axis is "
                    "automatically picked by Plotly. "
                    "If 'range' is set, then 'autorange' is set "
                    "to False automatically. Otherwise, if 'autorange' "
                    "is set to True (the default behavior), the range "
                    "of this {S0}-axis can respond to adjustments made in "
                    "the web GUI automatically. If 'autorange' is set "
                    "to 'reversed', then this {S0}-axis is drawn in reverse "
                    "i.e. from {S5} to {S4} instead of from {S4} to {S5} "
                    "(the default behavior)."
                ).format(S0=s[0],S4=s[4],S5=s[5])
            )),
            ('showgrid', dict(
                required=False,
                type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not this axis features grid lines."
                )
            )),
            ('zeroline', dict(
                required=False,
                type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not an additional grid line "
                    "(thicker than the other grid lines, by default) "
                    "will appear on this axis along {}=0."
                ).format(x_or_y)
            )),
            ('showline', make.showline(x_or_y)),
            ('autotick', make.autotick('axis')),
            ('nticks', make.nticks('axis')),
        ]
        _keymeta += self.keymeta_ticks('axis')
        _keymeta += [
            ('mirror', dict(
                required=False,
                type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether to mirror the axis line to the "
                    "opposite side of the plot."
                )
            )),
            ('gridcolor', dict(
                required=False,
                type='style',
                val_types=val_types.color(),
                description="Sets the axis grid color.",
                examples=MakeExamples.color(MakeExamples())
            )),
            ('gridwidth', dict(
                required=False,
                type='style',
                val_types=val_types.number(gt=0),
                description="Sets the grid width (in pixels)."
            )),
            ('zerolinecolor', dict(
                required=False,
                type='style',
                val_types=val_types.color(),
                description="Sets the color of this axis' zeroline.",
                examples=MakeExamples.color(MakeExamples())
            )),
            ('zerolinewidth', dict(
                required=False,
                type='style',
                val_types=val_types.number(gt=0),
                description="Sets the width of this axis' zeroline (in pixels)."
            )),
            ('linecolor', dict(
                required=False,
                type='style',
                val_types=val_types.color(),
                description="Sets the axis line color.",
                examples=MakeExamples.color(MakeExamples())
            )),
            ('linewidth', dict(
                required=False,
                type='style',
                val_types=val_types.number(gt=0),
                description="Sets the width of the axis line (in pixels)."
            )),
            ('anchor', dict(
                required=False,
                type='plot_info',
                val_types=(
                    "'{S3}' | '{S3}1' | '{S3}2' | ... | 'free'"
                ).format(S3=s[3]),
                description=(
                    "Choose whether the position of this {S0}-axis "
                    "will be anchored to a "
                    "corresponding {S3}-axis or will be 'free' to appear "
                    "anywhere in the {S6} space of "
                    "this figure."
                ).format(S0=s[0],S3=s[3],S6=s[6])
            )),
            ('overlaying', dict(  
                required=False,
                type='plot_info',
                val_types=(
                    "'{S0}' | '{S0}1' | '{S0}2' | ... | False"
                ).format(S0=s[0]),
                description=(
                    "Choose to overlay the data bound to this {S0}-axis "
                    "on the same plotting area as a "
                    "corresponding {S3}-axis or choose not overlay other {S0}-"
                    "the other axis/axes of this "
                    "figure."
                ).format(S0=s[0],S3=s[3],S6=s[6])
            )),
            ('side', dict(
                required=False,
                type='plot_info',
                val_types="'{S1}' | '{S2}'".format(S1=s[1],S2=s[2]),
                description=(
                    "Sets whether this {S0}-axis sits at the '{S1}' of the "
                    "plot or at the '{S2}' "
                    "of the plot."
                ).format(S0=s[0],S1=s[1],S2=s[2])
            )),
            ('position', dict(
                required=False,
                type='style',
                val_types=val_types.number(le=1, ge=0),
                description=(
                    "Sets where this {S0}-axis is positioned in the plotting "
                    "space. For example 'position'=0.5 will place this "
                    "axis in the exact center of the plotting space. Has "
                    "an effect only if 'anchor' "
                    "is set to 'free'."
                ).format(S0=s[0])
            ))
        ]
        return _keymeta
    
    def XAxis(self):
        '''@XAxis@'''
        name = 'xaxis'
        docstring = (
            "A {UL}-like object for representing an x-axis in plotly."
        )
        links = [
            "{WEB}axes/",
            "{WEB}multiple-axes/",
            "{WEB}subplots/",
            "{WEB}insets/"
        ]
        examples = MakeExamples.XAxis(MakeExamples())
        keymeta = OrderedDict(self.keymeta_axis('x'))
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def YAxis(self):
        '''@YAxis@'''
        name = 'yaxis'
        docstring = (
            "A {UL}-like object for representing a y-axis in plotly."
        )
        links = [
            "{WEB}axes/",
            "{WEB}multiple-axes/",
            "{WEB}subplots/",
            "{WEB}insets/"
        ]
        examples = MakeExamples.YAxis(MakeExamples())
        keymeta = OrderedDict(self.keymeta_axis('y'))
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def RadialAxis(self):
        '''@RadialAxis@'''
        name = 'radialaxis'
        docstring = (
            "A {UL}-like object for representing a radial axis in plotly."
        )
        links = ["{WEB}/polar-chart/"]
        examples = MakeExamples.RadialAxis(MakeExamples())
        keymeta = OrderedDict([
            ('range', make.range('radial')),
            ('domain', make.domain('radial')),
            ('orientation', dict(
                required=False,
                type='style',
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
                type='style',
                val_types="'horizontal' | 'vertical'",
                description=(
                    "Choose the orientation (from the paper perspective) "
                    "of the radial axis tick labels."
                )
            )),
            ('ticklen', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "Sets the length of the tick lines on this radial axis."
                )
            )),
            ('tickcolor', dict(
                required=False,
                type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the tick lines on this radial axis."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('ticksuffix', dict(
                required=False,
                type='style',
                val_types=val_types.string(),
                description=(
                    "Sets the length of the tick lines on this radial axis."
                )
            )),
            ('endpadding', dict(
                required=False,
                type='style',
                val_types=val_types.number(),
                description="more info coming soon"
            )),
            ('visible', make.visible())
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def AngularAxis(self):
        '''@AngularAxis@'''
        name = 'angularaxis'
        docstring = (
            "A {UL}-like object for representing an angular axis in plotly."
        )
        links = ["{WEB}/polar-chart/"]
        examples = MakeExamples.AngularAxis(MakeExamples())
        keymeta = OrderedDict([
            ('range', make.range('angular')),
            ('domain', make.domain('angular')),  #Q? Does not apply, right?
            ('showline', make.showline('angular')), #Q? Should be 'gridline'
            ('showticklabels', make.showticklabels('angular axis')),
            ('tickorientation', dict(
                required=False,
                type='style',
                val_types="'horizontal' | 'vertical'",
                description=(
                    "Choose the orientation (from the paper's perspective) "
                    "of the radial axis tick labels."
                )
            )),
            ('tickcolor', dict(
                required=False,
                type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the tick lines on this angular axis."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('ticksuffix', dict(
                required=False,
                type='style',
                val_types=val_types.string(),
                description=(
                    "Sets the length of the tick lines on this angular axis."
                )
            )),
            ('endpadding', dict(  # What does this do?
                required=False,
                type='style',
                val_types=val_types.number(),
                description="more info coming soon"
            )),
            ('visible', make.visible())
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def Legend(self):
        '''@Legend@'''
        name = 'legend'
        docstring = (
            "A {UL}-like object for representing a legend in plotly."
        )
        links = [
            "{WEB}/legend/",
            "{WEB}/figure-labels/"
        ]
        examples = MakeExamples.Legend(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.xy_layout('legend', 'x')),
            ('y', make.xy_layout('legend', 'y')),
            ('traceorder', dict(
                required=False,
                type='style',
                val_types="'normal' | 'reversed'",
                description=(
                    "Trace order is set by the order of the data in "
                    "associated grid for the plot. This sets whether this "
                    "order is read from left-to-right or from "
                    "right-to-left."
                )
            )),
            ('font', make.font('legend')),
            ('bgcolor', make.bgcolor('legend')),
            ('bordercolor', make.bordercolor('legend')),
            ('borderwidth', make.borderwidth('legend')),
            ('xref', make.xyref('x')),
            ('yref', make.xyref('y')),
            ('xanchor', make.xyanchor('x')),
            ('yanchor', make.xyanchor('y'))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def ColorBar(self):
        '''@ColorBar@'''
        name = 'colorbar'
        docstring = (
            "A {UL}-like object for representing a color bar in plotly."
        )
        links = ['']
        examples = MakeExamples.ColorBar(MakeExamples())
        _keymeta = [
            ('title', make.title('colorbar')),
            ('titleside', dict(
                required=False,
                type='style',
                val_types="'right' | 'top' | 'bottom'",
                description=(
                    "Location of colorbar title with respect to the colorbar."
                )
            )),
            ('titlefont', make.titlefont('colorbar')),
            ('thickness', make.thickness('colorbar')),
            ('thicknessmode', dict(
                required=False,
                type='style',
                val_types="string: 'pixels' | 'fraction' ",
                description="Sets thickness unit mode."
            )),
            ('len', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description="Sets the length of the colorbar."
            )),
            ('lenmode', dict(
                required=False,
                type='style',
                val_types="string: 'pixels' | 'fraction' ",
                description="Sets length unit mode."
            )),
            ('x', make.xy_layout('colorbar','x')),
            ('y', make.xy_layout('colorbar','y')),
            ('autotick', make.autotick('colorbar')),
            ('nticks', make.nticks('colorbar'))
        ]
        _keymeta += self.keymeta_ticks('colorbar')
        _keymeta += [
            ('xanchor', make.xyanchor('x')),
            ('xanchor', make.xyanchor('y')),
            ('bgcolor', make.bgcolor('colorbar')),
            ('outlinecolor', make.outlinecolor('colorbar')),
            ('outlinewidth', dict(
                required=False,
                type='style',
                val_types=val_types.number(),
                description=(
                    "Sets the width of the outline surrounding this colorbar."
                )
            )),
            ('borderwidth', make.borderwidth('colorbar')),
            ('xpad', dict(
                required=False,
                type='style',
                val_types=val_types.number(le=50, ge=0),
                description=(
                    "Sets the amount of space (padding) between the colorbar and "
                    "the enclosing boarder in the x-direction."
                )
            )),
            ('ypad', dict(
                required=False,
                type='style',
                val_types=val_types.number(le=50, ge=0),
                description=(
                    "Sets the amount of space (padding) between the colorbar and "
                    "the enclosing boarder in the y-direction."
                )
            ))
        ]
        keymeta = OrderedDict(_keymeta)
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def Margin(self):
        '''@Margin@'''
        name = 'margin'
        docstring = (
            "A {UL}-like object containing specification of the margins."
        )
        links = ["{WEB}/setting-graph-size/"]
        examples = MakeExamples.Margin(MakeExamples())
        keymeta = OrderedDict([
            ('l', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description="Sets the left margin size in pixels."
            )),
            ('r', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description="Sets the right margin size in pixels."
            )),
            ('b', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description="Sets the bottom margin size in pixels."
            )),
            ('t', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description="Sets the top margin size in pixels."
            )),
            ('pad', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "Sets the distance between edge of the plot and the "
                    "bounding rectangle that encloses the plot (in pixels)."
                )
            )),
            ('autoexpand', dict(  # TODO: ??
                required=False,
                type='style',
                val_types=val_types.bool(),
                description="more info coming soon"
            ))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Annotation(self):
        '''@Annotation@'''
        name = 'annotation'
        docstring = ("""
            A {UL}-like object for representing an annotation in plotly.

            Annotations appear as notes on the final figure. You can set all the
            features of the annotation text, background color, and location.
            Additionally, these notes can be anchored to actual data or the page
            for help with location after pan-and-zoom actions.
        """)
        links = ["{WEB}/text-and-annotations/"]
        examples = MakeExamples.Annotation(MakeExamples())
        keymeta = OrderedDict([
            ('x', make.xy_layout('annotation','x')),
            ('y', make.xy_layout('annotation','y')),
            ('xref', make.xyref('x')),
            ('yref', make.xyref('y')),
            ('text', dict(      # Different enough from shortcut-text
                required=False,
                type='plot_info',
                val_types=val_types.string(),
                description=(
                    "The text associated with this annotation. "
                    "Plotly uses a subset of HTML tags "
                    "to do things like newline (<br>), bold (<b></b>), "
                    "italics (<i></i>), hyperlinks (<a href='...'></a>). "
                    "Tags <em>, <sup>, <sub>, <span> are also supported."
                ),
                examples=[
                   "regular text", 
                   "an annotation<br>spanning two lines",
                   "<b>bold text</b>", 
                   "<a href='https://plot.ly/'>a link to plot.ly</a>"
                ]
            )),
            ('showarrow', dict(
                required=False,
                type='plot_info',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not the arrow associated with "
                    "this annotation with be shown. "
                    "If False, then the text linked to 'text' lines up with "
                    "the 'x', 'y' coordinates'. If True (the default), then "
                    "'text' is placed near the arrow's tail."
                )
            )),
            ('font', make.font('annotation')),
            ('xanchor', make.xyanchor('x')),
            ('yanchor', make.xyanchor('y')),
            ('align', dict(
                required=False,
                type='plot_info',
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
                type='style',
                val_types='0 | 1 | 2 | 3 | 4 | 5 | 6 | 7',
                description=(
                    "Sets the arrowhead style. "
                    "Has an effect only if 'showarrow' is set to True."
                )
            )),
            ('arrowsize', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "Scales the arrowhead's size. "
                    "Has an effect only if 'showarrow' is set to True."
                )
            )),
            ('arrowwidth', dict(
                required=False,
                type='style',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the arrowhead's width (in pixels). "
                    "Has an effect only if 'showarrow' is set to True."
                )
            )),
            ('arrowcolor', dict(
                required=False,
                type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the arrowhead. "
                    "Has an effect only if 'showarrow' is set to True."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('ax', dict(            # TODO! Better description
                required=False,
                type='plot_info',
                val_types=val_types.number(),
                description=(
                    "Position of the annotation text relative to the "
                    "arrowhead about the x-axis. "
                    "Has an effect only if 'showarrow' is set to True."
                )
            )),
            ('ay', dict(            # TODO! Better description
                required=False,
                type='plot_info',
                val_types=val_types.number(),
                description=(
                    "Position of the annotation text relative to the "
                    "arrowhead about the y-axis. "
                    "Has an effect only if 'showarrow' is set to True."
                )
            )),
            ('textangle', dict(
                required=False,
                type='style',
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
                type='style',
                val_types=val_types.number(le=10, ge=0),
                description=(
                    "The amount of space (padding) between the text and "
                    "the enclosing boarder."
                )
            )),
            ('bgcolor', make.bgcolor('annotation')),
            ('opacity', make.opacity())
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Layout(self):
        '''@Layout@'''
        name = 'layout'
        docstring = (
            "A {UL}-like object containing specification of the layout "
            "of a plotly figure."
        )
        links = [
            "{WEB}/figure-labels/",
            "{WEB}/axes/",
            "{WEB}/bar-charts/",
            "{WEB}/log-plot/"
        ]
        examples = MakeExamples.Layout(MakeExamples())
        keymeta = OrderedDict([
            ('title', make.title('layout')),
            ('titlefont', make.titlefont('layout')),
            ('font', make.font('layout')),
            ('showlegend', make.showlegend(layout=True)),
            ('autosize', dict(
                required=False,
                type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not the dimensions of the figure are "
                    "automatically picked by Plotly. Plotly picks figure's "
                    "dimensions as a function of your machine's display "
                    "resolution. "
                    "Once 'autosize' is set to False, the figure's dimensions "
                    "can be set with 'width' and 'height'."
                )
            )),
            ('width', dict(
                required=False,
                type='style',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the width in pixels of the figure you are generating."
                )
            )),
            ('height', dict(
                required=False,
                type='style',
                val_types=val_types.number(gt=0),
                description=(
                    "Sets the height in pixels of the figure you are generating."
                )
            )),
            ('xaxis', make.axis('x',layout=True)),
            ('yaxis', make.axis('y',layout=True)),
            ('legend', dict(
                required=False,
                type='object',
                val_types=val_types.object(),
                description=(
                    "A dictionary-like object containing the legend "
                    "parameters for this figure."
                )
            )),
            ('annotations', dict(
                required=False,
                type='object',
                val_types=val_types.object_list(),
                description=(
                    "A list-like object that contains one or multiple "
                    "annotation dictionaries."
                )
            )),
            ('margin', dict(
                required=False,
                type='object',
                val_types=val_types.object(),
                description=(
                    "A dictionary-like object containing the margin "
                    "parameters for this figure."
                )
            )),
            ('paper_bgcolor', dict(
                required=False,
                type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the color of the figure's paper "
                    "(i.e. area representing the canvas of the figure)."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('plot_bgcolor', dict(
                required=False,
                type='style',
                val_types=val_types.color(),
                description=(
                    "Sets the background color of the plot (i.e. the area "
                    "laying inside this figure's axes."
                ),
                examples=MakeExamples.color(MakeExamples())
            )),
            ('hovermode', dict(
                required=False,
                type='style',
                val_types="'closest' | 'x' | 'y'",
                description=(
                    "Sets this figure's behavior when a user hovers over it. "
                    "When set to 'x', all data sharing the same 'x' "
                    "coordinate will be shown on screen with "
                    "corresponding trace labels. When set to 'y' all data "
                    "sharing the same 'y' coordainte will be shown on the "
                    "screen with corresponding trace labels. When set to "
                    "'closest', information about the data point closest "
                    "to where the viewer is hovering will appear."
                )
            )),
            ('dragmode', dict(
                required=False,
                type='style',
                val_types="'zoom' | 'pan'",
                description=(
                    "Sets this figure's behavior when a user preforms a mouse "
                    "'drag' in the plot area. When set to 'zoom', a portion of "
                    "the plot will be highlighted, when the viewer "
                    "exits the drag, this highlighted section will be "
                    "zoomed in on. When set to 'pan', data in the plot "
                    "will move along with the viewers dragging motions. A "
                    "user can always depress the 'shift' key to access "
                    "the whatever functionality has not been set as the "
                    "default."
                )
            )),
            ('separators', dict(  
                required=False,
                type='style',
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
                type='plot_info',
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
                type='style',
                val_types=val_types.number(ge=0),
                description=(
                    "For bar and histogram plots only. "
                    "Sets the gap between bars (or sets of bars) at "
                    "different locations."
                )
            )),
            ('bargroupgap', dict(
                required=False,
                type='style',
                val_types=val_types.number(ge=0),
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
                type='plot_info',
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
            ('radialaxis', dict(  
                required=False,
                type='object',
                val_types=val_types.object(),
                description=(
                    "A dictionary-like object describing the radial axis "
                    "in a polar plot."
                )
            )),
            ('angularaxis', dict(
                required=False,
                type='object',
                val_types=val_types.object(),
                description=(
                    "A dictionary-like object describing the angular axis "
                    "in a polar plot."
                )
            )),
            ('direction', dict(
                required=False,
                type='plot_info',
                val_types="'clockwise' | 'counterclockwise'",
                description=(
                    "For polar plots only. "
                    "Sets the direction corresponding to "
                    "positive angles."
                )
            )),
            ('orientation', dict(  # Different enough than in shortcut-orientation
                required=False,
                type='plot_info',
                val_types=val_types.number(ge=-360,le=360),
                description=(
                   "For polar plots only. "
                   "Rotates the entire polar by the given angle."
                )
            )),
            ('hidesources', dict(
                required=False,
                type='style',
                val_types=val_types.bool(),
                description=(
                    "Toggle whether or not an annotation citing the data "
                    "source is placed at the bottom-right corner of the figure." 
                    "This key has an effect only on graphs that have been "
                    "generated from forked graphs from plot.ly."
                )
            ))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Figure(self):
        '''@Figure@'''
        name = 'figure'
        docstring = ("""
            A {UL}-like object representing a figure to be rendered by plotly.

            This is the container for all things to be rendered in a figure.
        """)
        links = ['']
        examples = MakeExamples.Figure(MakeExamples())
        keymeta = OrderedDict([
            ('data', dict(
                required=False,
                type='object',
                val_types=val_types.object_list(),
                description=(
                    "A list-like array of the data trace(s) that is/are "
                    "to be visualized."
                )
            )),
            ('layout', dict(
               required=False,
               type='object',
               val_types=val_types.object(),
               description=(
                   "A dictionary-like object that contains the layout "
                   "parameters (e.g. information about the axis, "
                   "global settings and layout information "
                   "related to the rendering of the figure)."
               )
            ))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def Data(self):
        '''@Data@ (accepts no keys)'''
        name = 'data'
        docstring = (
            "A {OL} of traces to be shown on one plotly figure."
        )
        links = ['']
        examples = MakeExamples.Data(MakeExamples())
        keymeta = dict()
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def Annotations(self):
        '''@Annotations@ (accepts no keys)'''
        name = 'annotations'
        docstring = (
            "A {OL} of annotations to be shown on one plotly figure."
        )
        links = ['']
        examples = MakeExamples.Annotations(MakeExamples())
        keymeta = dict()
        self += self._stuff(name, docstring, examples, links, keymeta)
    
    def Trace(self):
        '''@Trace@'''  #Q? Why keep this?
        name = 'trace'
        docstring = ''
        links = ['']
        examples = ['']
        keymeta = OrderedDict([
            ('x', dict(type='data')),
            ('y', dict(type='data')),
            ('z', dict(type='data')),
            ('r', dict(type='data')),
            ('t', dict(type='data')),
            ('text', dict(type='data')),
            ('name', dict(type='data')),
            ('mode', dict(type='plot_info')),
            ('marker', dict(type='object')),
            ('line', dict(type='object')),
            ('fill', dict(type='style')),
            ('fillcolor', dict(type='style')),
            ('opacity', dict(type='style')),
            ('showlegend', dict(type='style')),
            ('xaxis', dict(type='plot_info')),
            ('yaxis', dict(type='plot_info')),
            ('angularaxis', dict()),
            ('radialaxis', dict()),
            ('error_y', dict(type='object')),
            ('error_x', dict(type='object')),
            ('textfont', dict(type='object')),
            ('type', dict(type='plot_info')),
            ('orientation', dict(type='plot_info')),
            ('boxpoints', dict(type='style')),
            ('jitter', dict(type='style')),
            ('pointpos', dict(type='style')),
            ('boxmean', dict(type='style')),
            ('whiskerwidth', dict(type='style')),
            ('scl', dict(type='style')),
            ('reversescl', dict(type='style')),
            ('colorbar', dict(type='object')),
            ('autobinx', dict(type='style')),
            ('autobiny', dict(type='style')),
            ('xbins', dict(type='object')),
            ('ybins', dict(type='object')),
            ('histnorm', dict(type='plot_info')),
            ('zmax', dict(type='plot_info')),
            ('zmin', dict(type='plot_info')),
            ('dx', dict()),
            ('dy', dict()),
            ('x0', dict()),
            ('y0', dict()),
            ('zauto', dict(type='plot_info')),
            ('hm_id', dict()),
            ('nbinsx', dict(type='style')),
            ('nbinsy', dict(type='style')),
            ('showscale', dict(type='style'))
        ])
        self += self._stuff(name, docstring, examples, links, keymeta)
     
    def PlotlyList(self):
        '''@PlotlyList@ (accepts no keys)'''
        name = 'plotlylist'
        docstring = ''
        links = ['']
        examples = ['']
        keymeta = dict()
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def PlotlyDict(self):
        '''@PlotlyDict@ (accepts no keys)'''
        name = 'plotlydict'
        docstring = ''
        links = ['']
        examples = ['']
        keymeta = dict()
        self += self._stuff(name, docstring, examples, links, keymeta)
      
    def PlotlyTrace(self):
        '''@PlotlyTrace@ (accepts no keys)'''
        name = 'plotlytrace'
        docstring = ''
        links = ['']
        examples = ['']
        keymeta = dict()
        self += self._stuff(name, docstring, examples, links, keymeta)

# -------------------------------------------------------------------------------
