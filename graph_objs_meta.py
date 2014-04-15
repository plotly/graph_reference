from collections import OrderedDict


# use this to format 'val_types' for general numbers
def number(lt=None, le=None, gt=None, ge=None):
    if any((all((lt is not None, le is not None)),
            all((gt is not None, ge is not None)))):
        raise Exception("over-constrained number definition")
    if [lt, le, gt, ge] == [None, None, None, None]:
        return "number"
    elif lt is not None and ([ge, gt] == [None, None]):
        return "number: x < {lt}".format(lt=lt)
    elif le is not None and ([ge, gt] == [None, None]):
        return "number: x <= {le}".format(le=le)
    elif gt is not None and ([le, lt] == [None, None]):
        return "number: x > {gt}".format(gt=gt)
    elif ge is not None and ([le, lt] ==[None, None]):
        return "number: x >= {ge}".format(ge=ge)
    elif (lt is not None) and (gt is not None):
        return "number: x in ({gt}, {lt})".format(gt=gt, lt=lt)
    elif (lt is not None) and (ge is not None):
        return "number: x in [{ge}, {lt})".format(ge=ge, lt=lt)
    elif (le is not None) and (gt is not None):
        return "number: x in ({gt}, {le}]".format(gt=gt, le=le)
    elif (le is not None) and (ge is not None):
        return "number: x in [{ge}, {le}]".format(le=le, ge=ge)

val_types = dict(
    general=dict(
        bool="bool: True | False",
        color="str describing color",
        string="string",
        data_array="array_like of numbers, strings, datetimes",
        string_array="array_like of strings",
        object="dictionary-like",
    ),
    trace=dict(),
    map=dict(
        xtype="'array' | 'scaled'",
        ytype="'array' | 'scaled'",
        z="matrix-like: list of lists, numpy.matrix"
    ),
    bar=dict(
        bardir="'v' | 'h'",
    ),
    histogram=dict(

    ),
    scatter=dict(
        fill="'none' | 'tozeroy' | 'tonexty' | 'tozerox' | 'tonextx",
        fillcolor="str describing color",
    ),
    axis=dict(),
    bins=dict(),
)

description = dict(
    general=dict(),
    trace=dict(

        type=
        "Plotly identifier for this data's trace type. This defines how this "
        "data dictionary will be handled.",

        error_y=
        "A dictionary-like object describing vertical error bars that can be "
        "drawn with this trace's (x, y) points.",

        stream=
        "The stream dict that initializes traces as writable-streams, "
        "for use with the real-time streaming API. See examples here:\n"
        "http://nbviewer.ipython.org/github/plotly/Streaming-Demos",
    ),
    map=dict(

        x=
        "This array-like value contains the HORIZONTAL labels referring to "
        "the COLUMNS of the 'z' matrix. If strings, the x-labels are spaced "
        "evenly.",

        y=
        "This array-like value contains the VERTICAL labels referring to "
        "the ROWS of the 'z' matrix. If strings, the y-labels are spaced "
        "evenly.",

        z=
        "The data that describes the heatmap. The dimensions of the 'z' "
        "matrix are (nxm) where there are 'n' COLUMNS defining the "
        "number of partitions along the x-axis; this is equal to the "
        "length of the 'x' array. There are 'm' ROWS defining the number of "
        "partitions along the y-axis; this is equal to the length of the "
        "'y' array. Therefore, the color of the cell z[i][j] is mapped to "
        "the ith partition of the y-axis (starting from the bottom of the "
        "plot) and the jth partition of the x-axis (starting from the left "
        "of the plot).",

        zmax=
        "The value used as the maximum in the color scale normalization in "
        "'scl'. The default is the minimum of the 'z' data values.",

        zmin=
        "The value used as the minimum in the color scale normalization in "
        "'scl'. The default is the minimum of the 'z' data values.",

    ),

    bar=dict(
        x="The x coordinates of the bars OR the bar chart's categories.",
        y="The y data for bar charts, which is the length of the bars.",
        bardir="This defines the orientation (direction) of the bars. If "
               "set to 'h', the bars run horizontally along the xaxis. If set "
               "to 'v', the bars run vertically along the 'y' axis. However, "
               "you do not need to change 'x' and 'y' arrays as 'x' always "
               "defines the location of the bars (or category) and 'y' always "
               "defines the height of the bars.",
    ),
    histogram=dict(

        autobinx=
        "Toggle whether or not to allow plotly to automatically pick the bin "
        "sizing in the x direction for this histogram.",

        autobiny=
        "Toggle whether or not to allow plotly to automatically pick the bin "
        "sizing in the y direction for this histogram.",

        x=
        "The x data that is binned and plotted as bars along the x-axis.",

        xbins=
        "A dictionary-like object explaining how the bins should be created in "
        "the x direction for this histogram.",

        y=
        "The y data that is binned and plotted as bars along the y-axis.",

        ybins=
        "A dictionary-like object explaining how the bins should be created in "
        "the x direction for this histogram.",
    ),
    scatter=dict(),
    axis=dict(),
)

examples = dict(
    general=dict(
        color=[
            "'green'", "'rgb(0, 255, 0)'", "'rgba(0, 255, 0, 0.3)'",
            "'hsl(120,100%,50%)'", "'hsla(120,100%,50%,0.3)'"],
    ),
    trace=dict(),
    map=dict(),
    bar=dict(),
    histogram=dict(),
    scatter=dict(),
    axis=dict(),
)

default = dict(
    general=dict(),
    trace=dict(
        xaxis="'x1'",
        yaxis="'y1'"
    ),
    map=dict(),
    bar=dict(),
    histogram=dict(),
    scatter=dict(),
    axis=dict(),
)

drop_in = dict(

    colorbar=dict(
        required=False,
        type='object',
        val_types=val_types['general']['object'],
        description="This object represents a colorbar that will be shown on "
                    "the figure where the color is related to the data being "
                    "shown."),

    error_y=dict(
        required=False,
        type="object",
        val_types=val_types['general']['object'],
        description="A dictionary-like object describing vertical error bars "
                    "that can be drawn with this trace's (x, y) points."),

    name=dict(
        required=False,
        type='data',  # TODO??
        val_types=val_types['general']['string'],
        description="The label associated with this trace. This name will "
                    "appear in the legend, in the column header in the "
                    "spreadsheet, and on hover."),

    opacity=dict(
        required=False,
        type="style",
        val_types=number(ge=0, le=1),
        description="Sets the opacity, or transparency, of this object. Also "
                    "known as the alpha channel of colors, if the object's "
                    "color is given in terms of 'rgba', this does not need to "
                    "be defined."),

    scl=dict(
        required=False,
        type="style",
        val_types="array_like of value-color pairs | 'Greys' | 'Greens' | "
                  "'Bluered' | 'Hot' | 'Picnic' | 'Portland' | 'Jet' | "
                  "'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | "
                  "'YIGnBu'",
        description="The color scale. The strings are pre-defined color "
                    "scales. For custom color scales, define a list of "
                    "color-value pairs, where the first element of the pair "
                    "corresponds to a normalized value of z from 0-1  (i.e. ("
                    "z-zmin)/(zmax-zmin)), and the second element of pair "
                    "corresponds to a color.",
        examples=["Greys",[[0, "rgb(0,0,0)"], [1, "rgb(255,255,255)"]],
                  [[0, "rgb(8, 29, 88)"], [0.125, "rgb(37, 52, 148)"],
                   [0.25, "rgb(34, 94, 168)"], [0.375, "rgb(29, 145, 192)"],
                   [0.5, "rgb(65, 182, 196)"], [0.625, "rgb(127, 205, 187)"],
                   [0.75, "rgb(199, 233, 180)"], [0.875, "rgb(237, 248, 217)"],
                   [1, "rgb(255, 255, 217)"]]]),

    showlegend_trace=dict(
        required=False,
        type='style',
        val_types=val_types['general']['bool'],
        description="Toggle whether or not this trace will show up in the "
                    "legend."),

    showlegend_layout=dict(
        required=False,
        type='style',
        val_types=val_types['general']['bool'],
        description="Toggle whether or not the legend will be shown in this "
                    "figure."),

    stream=dict(
        required=False,
        type='plot_info',
        val_types=val_types['general']['object'],
        description="The stream dict that initializes traces as "
                    "writable-streams, for use with the real-time streaming "
                    "API. See examples here:\n"
                    "http://nbviewer.ipython.org/github/plotly/Streaming-Demos"
    ),

    visible=dict(
        required=False,
        type='plot_info',
        val_types=val_types['general']['bool'],
        description="Toggles whether this will actually be visible in the "
                    "rendered figure."),

    xaxis_trace=dict(
        required=False,
        type='plot_info',
        val_types="string: 'x1' | 'x2' | 'x3' | etc.",
        description="This key determines which xaxis the x coordinates in this "
                    "trace will reference in the figure. 'x' references "
                    "layout['xaxis'] and 'x2' references layout['xaxis2']. "
                    "'x1' will always refer to layout['xaxis'] or layout["
                    "'xaxis1'], they are the same."),
    yaxis_trace=dict(
        required=False,
        type='plot_info',
        val_types="string: 'y1' | 'y2' | 'y3' | etc.",
        description="This key determines which yaxis the y coordinates in this "
                    "trace will reference in the figure. 'y' references "
                    "layout['yaxis'] and 'y2' references layout['yaxis2']. "
                    "'y1' will always refer to layout['yaxis'] or layout["
                    "'yaxis1'], they are the same."),
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
        ('marker', dict(type='object')),
        ('line', dict(type='object')),
        ('fill', dict()),
        ('fillcolor', dict()),
        ('opacity', dict()),
        ('showlegend', dict()),
        ('xaxis', dict()),
        ('yaxis', dict()),
        ('angularAxis', dict()),
        ('radialAxis', dict()),
        ('error_y', dict(type='object')),
        ('textfont', dict(type='object')),
        ('type', dict()),
        ('bardir', dict()),
        ('boxpoints', dict()),
        ('jitter', dict()),
        ('pointpos', dict()),
        ('boxmean', dict()),
        ('whiskerwidth', dict()),
        ('scl', dict()),
        ('colorbar', dict(type='object')),
        ('autobinx', dict()),
        ('autobiny', dict()),
        ('xbins', dict(type='object')),
        ('ybins', dict(type='object')),
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

    # ('area', OrderedDict([])),  # TODO: we need this? or only for polar...

    ('scatter', OrderedDict([

        ('x', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
            description="the x coordinates from the (x,y) pair on the scatter "
                        "plot.")),

        ('y', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
            description="the y coordinatey from the (x,y) pair on the scatter "
                        "plot.")),

        ('r', dict(
            required=False,
            type='data',
            val_types=val_types['general']['data_array'],
        )),

        ('t', dict(
            required=False,
            type='data',
            val_types=val_types['general']['data_array'],
        )),

        ('text', dict(
            required=False,
            type='data',
            val_types=val_types['general']['string_array'],
            description="The text elements associated with every (x,y) pair on "
                        "the scatter plot. If the scatter 'mode' doesn't "
                        "include 'text' then text will appear on hover."
        )),

        ('name', drop_in['name']),

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
            val_types=val_types['general']['object'],
            description="A dictionary-like object containing information "
                        "about the marker style of the scatter plot.")),

        ('line', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary-like object containing information "
                        "about the line connecting points on the scatter "
                        "plot.")),

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
            val_types="str describing color",
            examples=examples['general']['color'])),

        ('opacity', drop_in['opacity']),

        ('showlegend', drop_in['showlegend_trace']),

        ('stream', drop_in['stream']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('error_y', drop_in['error_y']),

        ('visible', drop_in['visible']),

        ('textfont', dict(
            required=False,
            type='object',
            description="A dictionary-like object describing the font style "
                        "of this scatter's text elements.")),  # TODO?!?

        ('type', dict(
            required=False,
            type='plot_info',
            val_types="'scatter'",
            description=description['trace']['type']
        ))
    ])),

    ('bar', OrderedDict([
        ('x', dict(
            required=True,
            type='data',
            val_types=" ".join([val_types['general']['data_array'],
                                "OR",
                                val_types['general']['string_array']]),
            description="The x coordinates of the bars or the bar chart's "
                        "categories."
        )),

        ('y', dict(
            required=True,
            type='data',
            val_types=" ".join([val_types['general']['data_array'],
                                "OR",
                                val_types['general']['string_array']]),
            description="The y coordinates of the bars or the bar chart's "
                        "categories."
        )),

        ('bardir', dict(
            required=False,
            type="style",
            val_types=val_types['bar']['bardir'],
            description=description['bar']['bardir']
        )),

        ('text', dict()),

        ('name', drop_in['name']),

        ('marker', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'])),

        ('line', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary-like object containing information "
                        "about the enclosing line for each bar."
        )),

        ('opacity', drop_in['opacity']),

        ('showlegend', drop_in['showlegend_trace']),

        ('stream', drop_in['stream']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('error_y', drop_in['error_y']),

        ('textfont', dict(type='object')),

        ('visible', drop_in['visible']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types="'bar'",
            description=description['trace']['type']
        ))

    ])),

    ('box', OrderedDict([

        ('y', dict(
            required=True,
            type="data",
            val_types=val_types['general']['data_array'],
            description="This array is used to define the an individual "
                        "box plot. Statistics from these numbers define "
                        "the bounds of the box, the length of the "
                        "whiskers, etc.")),

        ('name', drop_in['name']),

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
            val_types=val_types['general']['color'],
            description="Color of the box interior.",
            examples=examples['general']['color'])),

        ('marker', dict(type='object')),

        ('line', dict(type='object')),

        ('textfont', dict(type='object')),

        ('showlegend', drop_in['showlegend_trace']),

        ('stream', drop_in['stream']),

        ('xaxis', drop_in['xaxis_trace']),

        ('xaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('error_y', drop_in['error_y']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='box',
            description=description['trace']['type']))

    ])),

    ('contour', OrderedDict([

        ('z', dict(
            required=True,
            type='data',
            val_types=val_types['map']['z'],
            description=description['map']['z'])),

        ('x', dict(
            required=False,
            type='data',
            val_types=val_types['general']['data_array'],
            description=description['map']['x'])),

        ('y', dict(
            required=False,
            type='data',
            val_types=val_types['general']['data_array'],
            description=description['map']['y'])),

        ('name', drop_in['name']),

        ('autocontour', dict(
            required=False,
            type='style',
            default=True,
            val_types=val_types['general']['bool'],
            description="If True, the contours settings are set automatically. "
                        "If False, the contours settings must be set manually "
                        "with the contours object.")),

        ('ncontours', dict(
            required=False,
            type='style',
            default=0,
            val_types=val_types['general']['bool'])),

        ('contours', dict(
            required=False,
            type='object',  # TODO: this was 'style' before, any reason?
            val_types=val_types['general']['object'])),

        ('scl', drop_in['scl']),

        ('colorbar', drop_in['colorbar']),

        ('xtype', dict(  # TODO: ??
            required=False,
            type='style',
            val_types=val_types['map']['xtype'])),

        ('ytype', dict(  # TODO: ??
            required=False,
            type='style',
            val_types=val_types['map']['xtype'])),

        ('dx', dict(  # TODO: ??
            required=False,
            type='style',
            val_types=number())),

        ('dy', dict(  # TODO: ??
            required=False,
            type='style',
            val_types=number())),

        ('zmin', dict(
            required=False,
            type='style',
            val_types=number(),
            description=description['map']['zmin'])),

        ('zmax', dict(
            required=False,
            type='style',
            val_types=number(),
            description=description['map']['zmax'])),

        ('showlegend', drop_in['showlegend_trace']),

        ('stream', drop_in['stream']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='contour',
            description=description['trace']['type']))
    ])),

    ('heatmap', OrderedDict([

        ('z', dict(
            required=True,
            type='data',
            val_types=val_types['map']['z'],
            description=description['map']['z'])),

        ('x', dict(
            required=False,
            type='data',
            val_types=val_types['general']['data_array'],
            description=description['map']['x'])),

        ('y', dict(
            required=False,
            type='data',
            val_types=val_types['general']['data_array'],
            description=description['map']['y'])),

        ('name', drop_in['name']),

        ('scl', drop_in['scl']),

        ('colorbar', drop_in['colorbar']),

        ('xtype', dict(  # TODO: ??
            required=False,
            type='style',
            val_types=val_types['map']['xtype'])),

        ('ytype', dict(  # TODO: ??
            required=False,
            type='style',
            val_types=val_types['map']['xtype'])),

        ('dx', dict(  # TODO: ??
            required=False,
            type='style',
            val_types=number())),

        ('dy', dict(  # TODO: ??
            required=False,
            type='style',
            val_types=number())),

        ('zmin', dict(
            required=False,
            type='style',
            val_types=number(),
            description=description['map']['zmin'])),

        ('zmax', dict(
            required=False,
            type='style',
            val_types=number(),
            description=description['map']['zmax'])),

        ('showlegend', drop_in['showlegend_trace']),

        ('stream', drop_in['stream']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='heatmap',
            description=description['trace']['type']))

    ])),

    ('histogramx', OrderedDict([

        ('x', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
            description=description['histogram']['x'])),

        ('name', drop_in['name']),

        ('mode', dict()),

        ('marker', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'])),

        ('line', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'])),

        ('autobinx', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['bool'],
            description=description['histogram']['autobinx'])),

        ('xbins', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description=description['histogram']['xbins'])),

        ('nbinsx', dict()),

        ('histnorm', dict()),

        ('showlegend', drop_in['showlegend_trace']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('stream', drop_in['stream']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='histogramx',
            description=description['trace']['type']))
    ])),

    ('histogramy', OrderedDict([

        ('y', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
            description=description['histogram']['y'])),

        ('name', drop_in['name']),

        ('mode', dict()),

        ('marker', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'])),

        ('line', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'])),

        ('autobiny', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['bool'],
            description=description['histogram']['autobiny'])),

        ('ybins', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description=description['histogram']['ybins'])),

        ('nbinsy', dict()),

        ('histnorm', dict()),

        ('showlegend', drop_in['showlegend_trace']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('stream', drop_in['stream']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='histogramy',
            description=description['trace']['type']))
    ])),

    ('histogram2d', OrderedDict([

        ('x', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
            description=description['histogram']['x'])),

        ('y', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
            description=description['histogram']['y'])),

        ('scl', drop_in['scl']),

        ('colorbar', drop_in['colorbar']),

        ('name', drop_in['name']),

        ('mode', dict()),

        ('marker', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'])),

        ('line', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'])),

        ('autobinx', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['bool'],
            description=description['histogram']['autobinx'])),

        ('autobiny', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['bool'],
            description=description['histogram']['autobiny'])),

        ('xbins', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description=description['histogram']['xbins'])),

        ('ybins', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description=description['histogram']['ybins'])),

        ('nbinsx', dict()),

        ('nbinsy', dict()),

        ('histnorm', dict()),

        ('showlegend', drop_in['showlegend_trace']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('stream', drop_in['stream']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='histogram2d',
            description=description['trace']['type']))

    ])),

    ('annotation', OrderedDict([

        ('x', dict(
            required=False,
            type='plot_info',
            val_types=number(),
            description="The x coordinate of the annotation location.")),

        ('y', dict(
            required=False,
            type='plot_info',
            val_types=number(),
            description="The y coordinate of the annotation location.")),

        ('text', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['string'],
            description="The text note that will be added with this "
                        "annotation.")),

        ('bordercolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="The color of the enclosing boarder of this "
                        "annotation.",
            examples=examples['general']['color'])),

        ('borderwidth', dict(
            required=False,
            type='style',
            val_types=number(),
            description="The width of the boarder enclosing this annotation")),

        ('borderpad', dict(
            required=False,
            type='style',
            val_types=number(le=10, ge=0),
            description="The amount of space (padding) between the text and "
                        "the enclosing boarder.")),

        ('bgcolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="The background (bg) color for this annotation.",
            examples=examples['general']['color'])),

        ('xref', dict(
            required=False,
            type='plot_info',
            val_types="string: 'paper' | 'x1' | 'x2' | 'x3' | etc.",
            description="This defines what the x coordinate for this "
                        "annotation *refers* to. If you reference an axis, "
                        "e.g., 'x2', the annotation will move with "
                        "pan-and-zoom to stay fixed to this point. If you "
                        "reference the 'paper', it remains fixed regardless "
                        "of pan-and-zoom.")),

        ('yref', dict(
            required=False,
            type='plot_info',
            val_types="string: 'paper' | 'y1' | 'y2' | 'y3' | etc.",
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
            description="Show the arrow associated with this annotation.")),

        ('arrowwidth', dict()),  # TODO, ya'll should make an `arrow` dict?

        ('arrowcolor', dict()),

        ('arrowhead', dict()),

        ('arrowsize', dict()),

        ('tag', dict()),

        ('font', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'])),

        ('opacity', drop_in['opacity']),

        ('align', dict(
            required=False,
            type='plot_info',
            val_types="string: 'left' | 'center' | 'right'",
            description="The alignment of the text in the annotation.")),

        ('xanchor', dict(
            required=False,
            type='plot_info')),

        ('yanchor', dict(
            required=False,
            type='plot_info')),

        ('ay', dict()),

        ('ax', dict()),

        ('xatype', dict()),

        ('yatype', dict()),

        ('ref', dict()),
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
            val_types=val_types['general']['color'],
            description="Color of the text.",
            examples=examples['general']['color']
        ))
    ])),

    ('layout', OrderedDict([

        ('title', dict(
            type='plot_info'
        )),

        ('xaxis', dict(
            type='object'
        )),

        # ('radialAxis', dict(
        #     type='object'
        # )),
        #
        # ('angularAxis', dict(
        #     type='object'
        # )),

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

        ('categories', dict(
            type='plot_info'
        )),

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

        ('smith', dict())

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

        ('thickness', dict()),  # TODO: redundant?

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

    ('stream', OrderedDict([])),

    ('xaxis', OrderedDict([

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
            val_types=val_types['general']['bool'],
            description="Defines whether or not to show this axis line."
        )),

        ('mirror', dict()),

        ('linecolor', dict(  # TODO: why isn't this just a Line object here?
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Defines the axis line color.",
            examples=examples['general']['color']
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
            val_types=val_types['general']['color'],
            description="Sets the color of the tick lines."
        )),

        ('tickwidth', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Sets the width of the tick lines."
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
            val_types=val_types['general']['bool'],
            description="Show/Hide the axis tick labels."
        )),

        ('tickangle', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=number(le=90, ge=-90),
            description="Sets the angle of the ticks in degrees."
        )),

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
            val_types=val_types['general']['bool'],
            description="Show/Hide grid for the axis."
        )),

        ('gridcolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Sets the axis grid color. Any HTML specified color "
                        "is accepted.",
            examples=examples['general']['color']
        )),

        ('gridwidth', dict(
            requried=False,
            type='style',
            val_types=number(gt=0),
            description="Sets the grid width."
        )),

        ('autorange', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['bool'],
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
            val_types=val_types['general']['bool'],
            description="Toggle axis autoticks."
        )),

        ('zeroline', dict(
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Show/Hide an additional zeroline for this axis."
        )),

        ('zerolinecolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Set the color of this axis' zeroline.",
            examples=examples['general']['color']
        )),

        ('zerolinewidth', dict(
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Sets the width of this axis' zeroline."
        )),

        ('titlefont', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary for configuring the axis title font."
        )),

        ('tickfont', dict(  # TODO: separate object for ticks?
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary for configuring the tick font."
        )),

        ('overlaying', dict()),

        ('position', dict()),

        ('anchor', dict()),

        ('unit', dict()),

        ('b', dict()),

        ('m', dict()),

        ('tickround', dict()),

        ('tickexponent', dict()),

        ('side', dict()),

        ('color', dict()),

        ('tmin', dict()),

        ('tmax', dict())
    ])),

    ('xbins', OrderedDict([
        ('start', dict()),
        ('end', dict()),
        ('size', dict())
    ])),

    ('yaxis', OrderedDict([

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
            val_types=val_types['general']['bool'],
            description="Defines whether or not to show this axis line."
        )),

        ('mirror', dict()),

        ('linecolor', dict(  # TODO: why isn't this just a Line object here?
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Defines the axis line color.",
            examples=examples['general']['color']
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
            val_types=val_types['general']['color'],
            description="Sets the color of the tick lines."
        )),

        ('tickwidth', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Sets the width of the tick lines."
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
            val_types=val_types['general']['bool'],
            description="Show/Hide the axis tick labels."
        )),

        ('tickangle', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=number(le=90, ge=-90),
            description="Sets the angle of the ticks in degrees."
        )),

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
            val_types=val_types['general']['bool'],
            description="Show/Hide grid for the axis."
        )),

        ('gridcolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Sets the axis grid color. Any HTML specified color "
                        "is accepted.",
            examples=examples['general']['color']
        )),

        ('gridwidth', dict(
            requried=False,
            type='style',
            val_types=number(gt=0),
            description="Sets the grid width."
        )),

        ('autorange', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['bool'],
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
            val_types=val_types['general']['bool'],
            description="Toggle axis autoticks."
        )),

        ('zeroline', dict(
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Show/Hide an additional zeroline for this axis."
        )),

        ('zerolinecolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Set the color of this axis' zeroline.",
            examples=examples['general']['color']
        )),

        ('zerolinewidth', dict(
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Sets the width of this axis' zeroline."
        )),

        ('titlefont', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary for configuring the axis title font."
        )),

        ('tickfont', dict(  # TODO: separate object for ticks?
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary for configuring the tick font."
        )),

        ('overlaying', dict()),

        ('position', dict()),

        ('anchor', dict()),

        ('unit', dict()),

        ('b', dict()),

        ('m', dict()),

        ('tickround', dict()),

        ('tickexponent', dict()),

        ('side', dict()),

        ('color', dict()),

        ('tmin', dict()),

        ('tmax', dict())

    ])),

    ('ybins', OrderedDict([
        ('start', dict()),
        ('end', dict()),
        ('size', dict())
    ])),

    ('contours', OrderedDict([
        ('start', dict()),
        ('end', dict()),
        ('size', dict()),
        ('coloring', dict()),
        ('showlines', dict()),
    ]))

])

if __name__ == "__main__":
    import json
    with open('graph_objs_meta.min.json', 'w') as f:
        f.write(json.dumps(INFO, sort_keys=False))
    with open('graph_objs_meta.json', 'w') as f:
        f.write(json.dumps(INFO, indent=4, sort_keys=False))

