from collections import OrderedDict

def qkgrab(attr_name, **kwargs):
    d = {}
    keyz = ['required', 'type', 'val_types', 'description']
    for k in keyz:
        if k in kwargs:
            d[k] = kwargs[k]
        elif attr_name in quick[k]:
            d[k] = quick[k][attr_name]

    if 'type' in d and d['type'] == 'object':
        d['val_types'] = gen_val_type(attr_name)
    return d


def gen_val_type(name, a=[]):
    ''' TODO: xbins '''
    return '_'.join([si.title() for si in name.split('_')]) + ' object | dict'


def auto_populate_some_stuff():
    for plot_obj in INFO:
        for plot_obj_attr in plot_obj:
            if ('type' in plot_obj and
                plot_obj[plot_obj_attr]['type'] == 'object' and
                'val_types' not in plot_obj[plot_obj_attr]):

                plot_obj[plot_obj_attr]['val_types'] = \
                    gen_val_type(plot_obj_attr)


def histogram(x_or_y):
    histx = OrderedDict([
        ('x', dict(
            required=True,
            type='data',
            val_types=quick['val_types']['data_array'],
            description="The x data that is binned and plotted as bars "
            "along the x-axis.")),

        ('name', qkgrab('name')),

        ('marker', dict(
            required=False,
            type='object')),

        ('autobinx', dict()),

        ('xbins', dict(
            required=False,
            type='object')),

        ('histnorm', dict(
            required=False)),

        ('showlegend', qkgrab('showlegend')),

        ('xaxis', qkgrab('xaxis')),

        ('yaxis', qkgrab('yaxis')),

        ('stream', qkgrab('stream')),

        ('type', qkgrab('type', val_types="'histogramx'",
                        description=
                        quick['description']['type']('Histogramx')))
    ])
    if x_or_y == 'x':
        return histx

    # change up some key names
    histy = OrderedDict([('y', v) if k == 'x' else
                        ('ybins', v) if k == 'xbins' else
                        ('autobiny', v) if k == 'autobiny' else
                        (k, v) for k, v in histx.items()])

    # switch up some 'x' to 'y's
    histy['type']['val_types'] = "'histogramy'"
    histy['type']['description'] = quick['description']['type']('Histogramy')
    histy['y']['description'] = histy['y']['description'].replace('x', 'y')
    return histy


def heatmap_or_contour(hm_or_contour):
    heatmap = OrderedDict([
        ('z', dict(
            required=True,
            type='data',
            val_types="matrix_like: list of lists, numpy.matrix",
            description="The data that describes the heatmap. The "
                        "color of the cell in row i, column j "
                        "is mapped from the value of z[i][j].")),

        ('x', dict(
            required=False,
            type='data',
            val_types=quick['val_types']['data_array'],
            description="If numerical or date-like, the coordinates of the "
                        "horizontal edges of the heatmap cells where the "
                        "length of 'x' must be one more than the number of "
                        "columns in the heatmap. "
                        "If strings, then the x-labels the heatmap cells "
                        "where the length of 'x' is equal to "
                        "the number of columns in the heatmap.")),

        ('y', dict(
            required=False,
            type='data',
            val_types=quick['val_types']['data_array'],
            description="If numerical or date-like, the coordinates of the "
                        "vertical edges of the heatmap cells where the length "
                        "of 'y' must be one more than the number of rows in "
                        "the heatmap. "
                        "If strings, then y labels the heatmap cells where "
                        "the length of 'y' is equal to the "
                        "number of rows in the heatmap.")),

        ('name', qkgrab('name')),

        ('scl', dict(
            required=quick['type']['scl'],
            type=quick['type']['scl'],
            val_types=quick['val_types']['data_array'],
            description="The color scale. The strings are pre-defined color "
                        "scales. For custom color scales, define a list of "
                        "color-value pairs, where the first element of the "
                        "pair corresponds to a normalized value of z from 0-1 "
                        "(i.e. (z-zmin)/(zmax-zmin)), and the second element "
                        "of pair corresponds to a color.",
            examples=quick['examples']['scl'])),

        ('colorbar', dict(
            required=False,
            type='object',
            val_types="Colorbar object | dict")),

        ('xtype', dict(
            required=False,
            type='style',
            val_types="'array' | 'scaled'")),

        ('ytype', dict(
            required=False,
            type='style',
            val_types="'array' | 'scaled'")),

        ('dx', dict(
            required=False,
            type='style',
            val_types='number')),

        ('dy', dict(
            required=False,
            type='style',
            val_types='number')),

        ('zmin', dict(
            required=False,
            type='style',
            val_types='number',
            description="The value used as the minimum in the color scale "
                        "normalization in 'scl'. "
                        "The default is the minimum of the 'z' data values.")),

        ('zmax', dict(
            required=False,
            type='style',
            val_types='number',
            description="The value used as the maximum in the color scale "
                        "normalization in 'scl'. "
                        "The default is the minimum of the 'z' data values.")),

        ('showlegend', qkgrab('showlegend')),

        ('xaxis', qkgrab('xaxis')),

        ('yaxis', qkgrab('yaxis')),

        ('type', qkgrab('type', val_types="'heatmap'",
                        description=
                        quick['description']['type']('Heatmap')))
    ])

    if hm_or_contour == 'heatmap':
        return heatmap

    unordered_contour = heatmap
    # Add some contour-specific items
    unordered_contour['type'] = qkgrab('type', val_types="'contour'",
                                       description=
                                       quick['description']['type']('Contour'))
    unordered_contour['autocontour'] = dict(
        required=False,
        type='style',
        default=True,
        val_types=quick['val_types']['bool'],
        description="If True, the contours settings are set automatically. "
                    "If False, the contours settings must be set manually "
                    "with the contours object."
    )
    unordered_contour['ncontours'] = dict(
        required=False,
        type='style',
        default=0,
        val_types=quick['val_types']['bool']
    )
    unordered_contour['contours'] = dict(
        required=False,
        type='style',
        val_types='object'
    )
    contour_order = ['z', 'x', 'y', 'name', 'autocontour', 'contours',
                     'ncontours', 'scl', 'colorbar', 'xtype', 'ytype',
                     'dx', 'dy', 'zmin', 'zmax', 'showlegend', 'xaxis',
                     'yaxis', 'type']

    contour = OrderedDict([(k, unordered_contour[k])
                          for k in contour_order])
    return contour


def axis():
    return OrderedDict([
        ('title', dict()),

        ('domain', dict(
            required=False,
            type='plot_info',
            val_types="number array of length 2",
            description="Sets the domain of this axis. The available space "
                        "for this axis to live in is from 0 to 1."
        )),

        ('range', dict(
            required=False,
            type='plot_info',
            val_types="number array of length 2",
            description="Defines the start and end point for the axis.",
            examples=[[-13, 20], [0, 1]]
        )),

        ('type', dict(
            required=False,
            type='plot_info',
            val_types="string: linear | log",
            description="Defines format of the axis."
        )),

        ('showline', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['bool'],
            description="Defines whether or not to show this axis line."
        )),

        ('mirror', dict()),

        ('linecolor', dict(  # TODO: why isn't this just a Line object here?
            required=False,
            type='style',
            val_types=quick['val_types']['color'],
            description="Defines the axis line color.",
            examples=quick['examples']['color']
        )),

        ('linewidth', dict(  # TODO: why isn't this just a Line object here?
            required=False,
            type='style',
            val_types="number",
            description="Sets the width of the axis line."
        )),

        ('tick0', dict(  # TODO: better description?
            required=False,
            type='plot_info',
            val_types="number",
            description="Sets the starting point of the axis."
        )),

        ('dtick', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_type="number",
            description="Sets the difference between ticks on this axis."
        )),

        ('ticks', dict(  # TODO: separate object for ticks?
            requried=False,
            type='plot_info',  # TODO: 'style'?
            val_types="string: 'inside' | 'outside' | '' (Empty str for NONE)",
            description="Sets format of tick visibility."
        )),

        ('ticklen', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types="number",
            description="Sets the length of the tick lines."   # in points?
        )),

        ('tickcolor', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=quick['val_types']['color'],
            description="Sets the color of the tick lines."
        )),

        ('tickwidth', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=quick['val_types']['number'](ut=0),
            description="Sets the color of the tick lines."
        )),


        ('nticks', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types="number",
            description="Sets the number of ticks to appear on the axis."
        )),

        ('showticklabels', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=quick['val_types']['bool'],
            description="Show/Hide the axis tick labels."
        )),

        ('tickangle', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types="number",
            description="Sets the angle of the ticks in degrees."
        )),

        ('drange', dict()),

        ('r0', dict()),

        ('exponentformat', dict(
            required=False,
            type='style'
        )),

        ('showexponent', dict(
            required=False,
            type='style'
        )),


        ('showgrid', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['bool'],
            description="Show/Hide grid for the axis."
        )),

        ('gridcolor', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['bool'],
            description="Sets the axis grid color. Any HTML specified color "
                        "is accepted.",
            examples=quick['examples']['color']
        )),

        ('gridwidth', dict(
            requried=False,
            type='style',
            val_types="number",
            description="Sets the grid width."
        )),

        ('autorange', dict(
            required=False,
            type='plot_info',
            val_types=quick['val_types']['bool'],
            description="Toggle whether to let plotly autorange the axis."
        )),

        ('rangemode', dict(
            required=False,
            type='plot_info',
            val_types="string: 'normal' | 'tozero' | 'nonnegative'"
        )),

        ('autotick', dict(
            required=False,
            type='style',  # TODO: 'plot_info' ??
            val_types=quick['val_types']['bool'],
            description="Toggle axis autoticks."
        )),

        ('zeroline', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['bool'],
            description="Show/Hide an additional zeroline for this axis."
        )),

        ('zerolinecolor', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['color'],
            description="Set the color of this axis' zeroline."
        )),

        ('zerolinewidth', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['number'](),
            description="Sets the width of this axis' zeroline."
        )),

        ('titlefont', dict(
            required=False,
            type='object',
            val_types="Font object | dict",
            description="A dictionary for configuring the axis title font."
        )),

        ('tickfont', dict(  # TODO: separate object for ticks?
            required=False,
            type='object',
            val_types="Font object | dict",
            description="A dictionary for configuring the tick font."
        )),

        ('overlaying', dict()),

        ('position', dict()),

        ('anchor', dict()),

        ('unit', dict()),
        ('tmin', dict()),
        ('tmax', dict()),
        ('b', dict()),
        ('m', dict()),
        ('tickround', dict()),
        ('tickexponent', dict())
    ])



def bins():
    return OrderedDict([

        ('start', dict()),

        ('end', dict()),

        ('size', dict())
    ])

def number(lt=None, leq=None, ut=None, uep=None):
    if not lt and not leq and not ut and not uep:
        return "number"
    elif lt and not ut and not uep:
        return "number: x < {0}".format(lt)
    elif leq and not ut and not uep:
        return "number: x <= {0}".format(leq)
    elif ut and not lt and not leq:
        return "number: x > {0}".format(ut)
    elif uep and not lt and not leq:
        return "number: x >= {0}".format(uep)
    elif lt and ut:
        return "number: x in ({0}, {1})".format(lt, ut)
    elif lt and uep:
        return "number: x in [{0}, {1})".format(lt, uep)
    elif leq and ut:
        return "number: x in ({0}, {1}]".format(leq, ut)
    elif leq and uep:
        return "number: x in [{0}, {1}]".format(leq, uep)

base = dict(
    val_types=dict(
        bool="bool: True | False",
        number=number,
        color="str describing color",
        data_array="array_like of numbers, strings, datetimes",
        text_array="array_like of strings"
    )
)

quick = dict(
    required=dict(
        name=False,
        error_y=False,
        xaxis=False,
        yaxis=False,
        scl=False,
        colorbar=False,
        showlegend=False,
        type=True,
        text=False,
        stream=False
    ),

    type=dict(
        name='data',
        error_y='object',
        xaxis='plot_info',
        yaxis='plot_info',
        scl='style',
        colorbar='style',
        showlegend='style',
        type='plot_info',
        text='data',
        stream='object'
    ),

    val_types=dict(
        name="string",
        xaxis="string: 'x' | 'x2' | 'x3' | etc.",
        yaxis="string: 'y' | 'y2' | 'y3' | etc.",
        showlegend=base['val_types']['bool'],
        text=base['val_types']['text_array'],
        **base['val_types']
    ),

    description=dict(

        name=
        "The label associated with this trace. This name will appear in the "
        "legend, in the column header in the spreadsheet, and on hover.",

        error_y=
        "A dictionary-like object describing vertical error bars that can be "
        "drawn with this trace's (x, y) points.",

        xaxis=
        "This key determines which xaxis the x coordinates in this trace will "
        "reference in the figure. 'x' references layout['xaxis'] and 'x2' "
        "references layout['xaxis2'].",

        yaxis=
        "This key determines which yaxis the y coordinates in this trace will "
        "reference in the figure. 'y' references layout['yaxis'] and 'y2' "
        "references layout['yaxis2'].",

        scl=
        "array_like of value-color pairs | 'Greys' | 'Greens' | "
        "'Bluered' | 'Hot' | 'Picnic' | 'Portland' | 'Jet' | "
        "'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' "
        "| 'YIGnBu'",

        type=lambda(name): "Plotly identifier for trace type, "
        "this is set automatically with a call to "
        "{Obj}(...).".format(Obj=name),

        stream=
        "The stream dict that initializes traces as writable-streams, "
        "for use with the real-time streaming API. "
        "For more help, see: `help(plotly.plotly.Stream)`"
        "or see examples here: "
        "http://nbviewer.ipython.org/github/plotly/Streaming-Demos"


    ),

    examples=dict(

        color=[
            "'green'", "'rgb(0, 255, 0)'", "'rgba(0, 255, 0, 0.3)'",
            "'hsl(120,100%,50%)'", "'hsla(120,100%,50%,0.3)'"],

        scl=["Greys",
            [[0, "rgb(0,0,0)"], [1, "rgb(255,255,255)"]],
            [[0, "rgb(8, 29, 88)"], [0.125, "rgb(37, 52, 148)"],
                [0.25, "rgb(34, 94, 168)"], [0.375, "rgb(29, 145, 192)"],
                [0.5, "rgb(65, 182, 196)"], [0.625, "rgb(127, 205, 187)"],
                [0.75, "rgb(199, 233, 180)"],
                [0.875, "rgb(237, 248, 217)"],
                [1, "rgb(255, 255, 217)"]]],
    ),

    default=dict(
        xaxis="'x'",
        yaxis="'x'"
    ),
)


INFO = OrderedDict([

    ('plotlylist', dict()),

    ('data', dict()),

    ('annotations', dict()),

    ('plotlydict', dict()),

    ('plotlytrace', dict()),

    ('trace', OrderedDict([
        ('x', dict()),
        ('y', dict()),
        ('z', dict()),
        ('r', dict()),
        ('t', dict()),
        ('text', dict()),
        ('name', dict()),
        ('mode', dict()),
        ('marker', dict(
            type='object'
        )),
        ('line', dict(
            type='object'
        )),
        ('fill', dict()),
        ('fillcolor', dict()),
        ('opacity', dict()),
        ('showlegend', dict()),
        ('xaxis', dict()),
        ('yaxis', dict()),
        ('angularAxis', dict()),
        ('radialAxis', dict()),
        ('error_y', dict(
            type='object'
        )),
        ('textfont', dict(
            type='object'
        )),
        ('type', dict()),
        ('bardir', dict()),
        ('boxpoints', dict()),
        ('jitter', dict()),
        ('pointpos', dict()),
        ('boxmean', dict()),
        ('whiskerwidth', dict()),
        ('scl', dict()),
        ('colorbar', dict(
            type='object'
        )),
        ('autobinx', dict()),
        ('autobiny', dict()),
        ('xbins', dict(
            type='object'
        )),
        ('ybins', dict(
            type='object'
        )),
        ('histnorm', dict()),
        ('zmax', dict()),
        ('zmin', dict()),
        ('dx', dict()),
        ('dy', dict()),
        ('x0', dict()),
        ('y0', dict()),
        ('zauto', dict()),
        ('hm_id', dict()),
        ('nbinsx', dict()),
        ('nbinsy', dict()),
    ])),

    ('area', OrderedDict([])),

    ('scatter', OrderedDict([

        ('x', dict(
            required=True,
            type='data',
            val_types=quick['val_types']['data_array'],
            description="the x coordinates from the (x,y) pair on the scatter "
                        "plot.")),

        ('y', dict(
            required=True,
            type='data',
            val_types=quick['val_types']['data_array'],
            description="the y coordinatey from the (x,y) pair on the scatter "
                        "plot.")),

        ('r', dict(
            required=False,
            type='data',
            val_types=quick['val_types']['data_array'],
        )),

        ('t', dict(
            required=False,
            type='data',
            val_types=quick['val_types']['data_array'],
        )),

        ('text', qkgrab('text', description="the text elements associated "
                        "with every (x,y) pair on the scatter plot. "
                        "If the scatter 'mode' doesn't include 'text' "
                        "then text will appear on hover.")),

        ('name', qkgrab('name')),

        ('mode', dict(
            required=False,
            type='plot_info',
            val_types="'lines' | 'markers' | 'text' | 'lines+markers' | "
                      "'lines+text' | 'markers+text' | 'lines+markers+text'",
            description="Plotting mode (style) for the scatter plot. If the "
                        "mode includes 'text' then the 'text' will appear "
                        "next to the (x,y) points, otherwise it will appear "
                        "on hover.")),

        ('marker', dict(
            required=False,
            type='object',
            val_types="Marker object | dict",
            description="A dictionary-like object containing information "
                        "about the marker style of the scatter plot.")),

        ('line', dict(
            required=False,
            type='object',
            val_types="Line object | dict",
            description="A dictionary-like object containing information "
                        "about the line connecting points "
                        "on the scatter plot.")),

        ('fill', dict(
            required=False,
            default='none',
            type='style',
            val_types="'none' | 'tozeroy' | 'tonexty' | 'tozerox' | 'tonextx",
            description="Used to make area-style charts. "
                        "Determines which area to fill with a solid color.")),

        ('fillcolor', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['color'],
            examples=quick['examples']['color'])),

        ('opacity', dict(
            required=False,
            type='style',
            val_types="number in [0, 1]",
            description="Sets the opacity, or transparency, of the markers "
                        "and lines of the scatter plot. Also known as the "
                        "alpha channel of colors. "
                        "The opacity can also be set in the "
                        "'marker' and 'line' objects.")),

        ('showlegend', qkgrab('showlegend')),

        ('xaxis', qkgrab('xaxis')),

        ('yaxis', qkgrab('yaxis')),

        ('error_y', qkgrab('error_y')),

        ('textfont', dict(
            required=False,
            type='object',
            description="A dictionary-like object describing the font style "
                        "of this scatter's text elements.")),

        ('type', qkgrab('type', val_types="'scatter'",
                        description=quick['description']['type']('Scatter')))
    ])),


    ('bar', OrderedDict([

        ('x', dict(
            required=True,
            type='data',
            val_types=quick['val_types']['data_array'],
            description="the x coordinates of the bars or the bar chart's "
                        "categories.")),

        ('y', dict(
            required=True,
            type='data',
            val_types=quick['val_types']['data_array'],
            description="the y data for bar charts, which is the length of the"
                        "bars.")),

        ('bardir', dict()),

        ('text', qkgrab('text',
                        description='text elements that '
                        'appear on hover of the bars')),

        ('name', qkgrab('name')),

        ('marker', dict(
            required=False,
            type='object',
            description="A dictionary-like object describing the "
                        "style of the bars, like the color and the border.")),

        ('opacity', dict(
            required=False,
            type='style',
            val_types="number in [0, 1]",
            description="Sets the opacity, or transparency, of the markers "
                        "and lines of the scatter plot. Also known as the "
                        "alpha channel of colors. The opacity can also be set "
                        "in the 'marker' and 'line' objects.")),

        ('showlegend', qkgrab('showlegend')),

        ('xaxis', qkgrab('xaxis')),

        ('yaxis', qkgrab('yaxis')),

        ('error_y', qkgrab('error_y')),

        ('type', qkgrab('type', val_types="'bar'",
                        description=quick['description']['type']('Bar')))

    ])),

    ('box', OrderedDict([

        ('y', dict(
            required=True,
            type="data",
            val_types="array_like of numbers",
            description="Array of the numbers from which the box plot "
                        "describes.")),

        ('name', qkgrab('name')),

        ('boxpoints', dict(
            required=False,
            type='plot_info',
            val_types="'all' | 'outliers' | False",
            description="If 'all' then the 'y' points are shown with the box. "
                        "If 'outliers' then only the 'outliers' of the 'y' "
                        "points are shown. If False then no points are shown",
            default=False)),

        ('jitter', dict(
            required=False,
            type='style',
            val_types="number in [0, 1]",
            description="Width of the jittered scatter. If 0, then the "
                        "boxpoints are aligned vertically, if 1 then the "
                        "points are randomly jittered horizontally up to the "
                        "width of the box.")),

        ('pointpos', dict(
            required=False,
            type='style',
            val_types="number in [-2, 2]",
            description="Horizontal position of the center of the boxpoints "
                        "relative to the center and width of the box.")),

        ('boxmean', dict(
            required=False,
            type="False | True | 'sd'",
            default='False',
            description="If True then the mean of the y-points is shown as a "
                        "dashed line in the box. If 'sd', then the standard "
                        "deviation is also shown. If False, then no line "
                        "shown.")),

        ('whiskerwidth', dict(
            required=False,
            type='number in [0, 1]',
            default=0.75,
            description="Width of the whisker of the box.")),

        ('fillcolor', dict(
            required=False,
            type='style',
            description="Color of the box interior.",
            val_types=quick['val_types']['color'],
            examples=quick['examples']['color'])),

        ('showlegend', qkgrab('showlegend')),

        ('xaxis', qkgrab('xaxis')),

        ('yaxis', qkgrab('yaxis')),

        ('type', qkgrab('type', val_types="'box'",
                        description=quick['description']['type']('Box')))
    ])),

    ('contour', heatmap_or_contour('contour')),

    ('heatmap', heatmap_or_contour('heatmap')),

    ('histogramx', histogram('x')),

    ('histogramy', histogram('y')),

    ('histogram2d', OrderedDict([

        ('x', dict(
            required=True,
            type='data',
            val_types=quick['val_types']['data_array'],
            description="The x coordinates of the x, y pairs that are binned "
                        "and plotted according to their distribution.")),

        ('y', dict(
            required=True,
            type='data',
            val_types=quick['val_types']['data_array'],
            description="The x coordinates of the x, y pairs that are binned "
                        "and plotted according to their distribution.")),

        ('name', qkgrab('name')),

        ('scl', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['data_array'],
            description="The color scale. The strings are pre-defined color "
                        "scales. For custom color scales, define a list of "
                        "color-value pairs, where the first element of the "
                        "pair corresponds to a normalized value from 0-1 of "
                        "the binned data and the second element of the pair "
                        "corresponds to a color.",
            examples=quick['examples']['scl'])),

        ('colorbar', dict(
            required=False,
            type='object',
            val_types="ColorBar object | dict")),

        ('autobinx', dict(
            required=False,
            default=True,
            type='style',
            val_types='True | False')),

        ('autobiny', dict()),

        ('xbins', dict(
            required=False,
            type='object',
            val_types="XBins object | dict")),

        ('ybins', dict(
            required=False,
            type='object',
            val_types="YBins object | dict")),

        ('histnorm', dict()),

        ('showlegend', qkgrab('showlegend')),

        ('xaxis', qkgrab('xaxis')),

        ('yaxis', qkgrab('yaxis')),

        ('type', qkgrab('type', val_types="'histogram2d'",
                        description=
                        quick['description']['type']('Histogram2d')))

    ])),

    ('annotation', OrderedDict([

        ('x', dict(
            required=False,
            type='plot_info',
            val_types="number",
            description="The x coordinate of the annotation location.")),

        ('y', dict(
            required=False,
            type='plot_info',
            val_types="number",
            description="The y coordinate of the annotation location.")),

        ('text', dict(
            required=False,
            type='plot_info',
            val_types="string",
            descriptors="The text note that will be added with this "
                        "annotation.")),

        ('bordercolor', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['color'],
            description="The color of the enclosing boarder of this "
                        "annotation.",
            examples=quick['val_types']['color'])),

        ('borderwidth', dict(
            required=False,
            type='style',
            val_types='number',
            description="The width of the boarder enclosing this annotation")),

        ('borderpad', dict(
            required=False,
            type='style',
            val_types="number in [0,10]",
            description="The amount of space (padding) between the text and "
                        "the enclosing boarder.")),

        ('bgcolor', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['color'],
            description="The background (bg) color for this annotation.",
            examples=quick['val_types']['color'])),

        ('xref', dict(
            required=False,
            type='plot_info',
            val_types="string: 'paper' | 'x' | 'x2' | 'x3' | etc.",
            description="This defines what the x coordinate for this "
                        "annotation *refers* to. If you reference an axis, "
                        "e.g., 'x2', the annotation will move with "
                        "pan-and-zoom to stay fixed to this point. If you "
                        "reference the 'paper', it remains fixed regardless "
                        "of pan-and-zoom.")),

        ('yref', dict(
            required=False,
            type='plot_info',
            val_types="string: 'paper' | 'y' | 'y2' | 'y3' | etc.",
            description="This defines what the x coordinate for this "
                        "annotation *refers* to. If you reference an axis, "
                        "e.g., 'y2', the annotation will move with "
                        "pan-and-zoom to stay fixed to this point. If you "
                        "reference the 'paper', it remains fixed regardless "
                        "of pan-and-zoom.")),

        ('showarrow', dict(
            required=False,
            type='plot_info',
            val_types="bool: True | False",
            description="Show the arrow associated with this annotation?")),

        ('arrowwidth', dict()),  # TODO, ya'll should make an `arrow` dict?

        ('arrowcolor', dict()),

        ('arrowhead', dict()),

        ('arrowsize', dict()),

        ('tag', dict()),

        ('font', dict(
            required=False,
            type='object',
            val_types="Font object | dict")),

        ('opacity', dict(
            required=False,
            type='style',
            val_types="number in [0, 1]",
            description="Sets the opacity, or transparency, of the annotation."
                        " Also known as the alpha channel.")),

        ('align', dict(
            required=False,
            type='plot_info',
            val_types="string: 'left' | 'center' | 'right'",
            description="The alignment of the text in the annotation.")),

        ('xanchor', dict(
            required=False,
            type='plot_info',
            val_types="coming soon!",
            description="coming soon!")),

        ('yanchor', dict(
            required=False,
            type='plot_info',
            val_types="coming soon!",
            description="coming soon!")),

        ('ay', dict()),

        ('ax', dict()),
    ])),

    ('colorbar', OrderedDict([])),

    ('error_y', OrderedDict([])),

    ('figure', OrderedDict([

        ('data', dict(
            required=False,
            type='object')),

        ('layout', dict(
            required=False,
            type='object'))
    ])),

    ('font', OrderedDict([

        ('family', dict(
            required=False,
            type='style',
            description="Setting for the font family."
        )),

        ('size', dict(
            required=False,
            type='style',
            val_types="number",
            description="Setting for the font size."
        )),

        ('color', dict(
            required=False,
            type='style',
            val_types=quick['val_types']['color'],
            description="Color of the text.",
            examples=quick['examples']['color']
        ))
    ])),

    ('layout', OrderedDict([

        ('title', dict(
            type='plot_info'
        )),

        ('xaxis', dict(
            type='object'
        )),

        ('radialAxis', dict(
            type='object'
        )),

        ('angularAxis', dict(
            type='object'
        )),

        ('yaxis', dict(
            type='object'
        )),

        ('legend', dict(
            type='object'
        )),

        ('width', dict(
            type='style'
        )),

        ('height', dict(
            type='style'
        )),

        ('categories', dict()),

        ('needsEndSpacing', dict()),

        ('autosize', dict(
            type='style'
        )),

        ('margin', dict(
            type='object'
        )),

        ('paper_bgcolor', dict(
            type='style'
        )),

        ('plot_bgcolor', dict(
            type='style'
        )),

        ('barmode', dict(
            type='plot_info'
        )),

        ('bargap', dict(
            type='plot_info'
        )),

        ('bargroupgap', dict(
            type='plot_info'
        )),

        ('boxmode', dict(
            type='plot_info'
        )),

        ('boxgap', dict(
            type='plot_info'
        )),

        ('boxgroupgap', dict(
            type='plot_info'
        )),

        ('font', dict(
            type='object'
        )),

        ('titlefont', dict(
            type='object'
        )),

        ('dragmode', dict(
        )),

        ('hovermode', dict(
        )),

        ('separators', dict(
        )),

        ('labeloffset', dict()),

        ('orientation', dict()),

        ('direction', dict()),

        ('tickcolor', dict()),

        ('minortickcolor', dict()),

        ('defaultcolorrange', dict()),

        ('hidesources', dict()),

        ('showlegend', dict(
            type='plot_info'
        )),

        ('annotations', dict(
            type='object'
        )),

        ('bardir', dict()),

        ('smith', OrderedDict([
        ])),

    ])),

    ('legend', OrderedDict([

        ('x', dict(
            type='plot_info'
        )),

        ('y', dict(
            type='plot_info'
        )),

        ('bgcolor', dict(
            type='style'
        )),

        ('bordercolor', dict(
            type='style'
        )),

        ('borderwidth', dict(
            type='style'
        )),

        ('font', dict(
            type='object'
        )),

        ('showlegend', dict()),

        ('traceorder', dict(
            type='plot_info'
        )),

        ('xref', dict(
            type='plot_info'
        )),

        ('yref', dict(
            type='plot_info'
        )),

        ('xanchor', dict(
            type='plot_info'
        )),

        ('yanchor', dict(
            type='plot_info'
        ))
    ])),

    ('line', OrderedDict([

        ('dash', dict(
            type='style'
        )),

        ('color', dict(
            type='style'
        )),

        ('width', dict(
            type='style'
        )),

        ('opacity', dict(
            type='style'
        )),

        ('smoothing', dict(
            type='style',
            description="Only applies to contours"))
    ])),


    ('margin', OrderedDict([

        ('l', dict(
            type='style'
        )),

        ('r', dict(
            type='style'
        )),

        ('b', dict(
            type='style'
        )),

        ('t', dict(
            type='style'
        )),

        ('pad', dict(
            type='style'
        )),

        ('autoexpand', dict(
            type='style'
        ))
    ])),

    ('marker', OrderedDict([

        ('symbol', dict(
            required=False,
            type='style',
            description="The symbol that is drawn on the plot for each marker."
        )),

        ('line', dict(
            required=False,
            type='object',
            val_types="Line object | dict",
            description="A dict-like object describing the line belonging to "
                        "the marker.",
        )),

        ('size', dict(
            required=False,
            type='style',
            val_types=number(),
            description="The size of the marker to be drawn."
        )),

        ('sizemode', dict(
        )),

        ('sizeref', dict()),

        ('color', dict(
            type='style'
        )),

        ('opacity', dict(
            type='style'
        )),
    ])),

    ('radialAxis', dict()),

    ('angularAxis', dict()),

    ('stream', OrderedDict([])),

    ('xaxis', axis()),

    ('xbins', bins()),

    ('yaxis', axis()),

    ('ybins', bins()),

    ('contours', OrderedDict([
        ('start', dict()),
        ('end', dict()),
        ('size', dict()),
        ('coloring', dict()),
        ('showlines', dict()),
    ]))


])


auto_populate_some_stuff()

if __name__ == "__main__":
    import json
    with open('graph_objs_meta.min.json', 'w') as f:
        f.write(json.dumps(INFO, sort_keys=False))
    with open('graph_objs_meta.json', 'w') as f:
        f.write(json.dumps(INFO, indent=4, sort_keys=False))
