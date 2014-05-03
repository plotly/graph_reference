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
    elif ge is not None and ([le, lt] == [None, None]):
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
        data_array="array-like of numbers, strings, datetimes",
        string_array="array-like of strings",
        object="dictionary-like",
    ),
    trace=dict(),
    map=dict(
        xtype="'array' | 'scaled'",
        ytype="'array' | 'scaled'",
        z="matrix-like: list of lists, numpy.matrix"
    ),
    bar=dict(
        orientation="'v' | 'h'",
    ),
    histogram=dict(

    ),
    scatter=dict(
        fill="'none' | 'tozeroy' | 'tonexty' | 'tozerox' | 'tonextx",
        fillcolor="str describing color",
    )
)

description = dict(
    general=dict(
        color="str describing color"
    ),
    trace=dict(

        type=
        "Plotly identifier for this data's trace type. This defines how this "
        "data dictionary will be handled. For example, 'scatter' type expects "
        "x and y data-arrays corresponding to (x, y) coordinates wheras a "
        "'histogramx' only requires a single x array and a 'heatmap' type "
        "requires x and y data-arrays as well as a z matrix.",

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
        "evenly. If the dimensions of z are (n x m), the length of the 'x' "
        "array should be 'm'.",

        y=
        "This array-like value contains the VERTICAL labels referring to "
        "the ROWS of the 'z' matrix. If strings, the y-labels are spaced "
        "evenly. If the dimensions of z are (n x m), the length of the 'y' "
        "array should be 'n'.",

        z=
        "The data that describes the mapping. The dimensions of the 'z' "
        "matrix are (n x m) where there are 'n' ROWS defining the "
        "number of partitions along the y-axis; this is equal to the "
        "length of the 'y' array. There are 'm' COLUMNS defining the number of "
        "partitions along the x-axis; this is equal to the length of the "
        "'x' array. Therefore, the color of the cell z[i][j] is mapped to "
        "the ith partition of the y-axis (starting from the bottom of the "
        "plot) and the jth partition of the x-axis (starting from the left "
        "of the plot). In Python, a (non-numpy) matrix is best thought of as "
        "a list of lists (of lists, of lists, etc.). Therefore, running len(z) "
        "will give you the number of ROWS and running len(z[0]) will give you "
        "the number of COLUMNS. If you ARE using numpy, then running z.shape "
        "will give you the tuple, (n, m), e.g., (3, 5).",

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
        orientation="This defines the direction of the bars. If set to 'v', "
                    "the length of each bar will run vertically.If set to 'h', "
                    "the length of each bar will run horizontally",
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
        "the y direction for this histogram.",
    )
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
        description="This object represents a color bar that will be shown on "
                    "the figure where the color is related to the data being "
                    "shown."),

    error_y=dict(
        required=False,
        type='object',
        val_types=val_types['general']['object'],
        description="A dictionary-like object describing vertical error bars "
                    "that can be drawn with this trace's (x, y) points."),

    exponentformat=dict(
        required=False,
        type='style',
        val_types="'none' | 'e' | 'E' | 'power' | 'SI' | 'B'",
        description="Sets how exponents show up. Here's how the number "
                    "1000000000 (1 billion) shows up in each. If set to "
                    "'none': 1,000,000,000. If set to 'e': 1e+9. If set "
                    "to 'E': 1E+9. If set to 'power': 1x10^9 (where the 9 "
                    "will appear super-scripted. If set to 'SI': 1G. If "
                    "set to 'B': 1B (useful when referring to currency."),

    showexponent=dict(
        required=False,
        type='style',
        val_types="'all' | 'first' | 'last' | 'none'",
        description="If set to 'all', ALL exponents will be shown "
                    "appended to their significands. If set to 'first', "
                    "the first tick's exponent will be appended to its "
                    "significand, however no other exponents will "
                    "appear--only the significands. If set to 'last', "
                    "the last tick's exponent will be appended to its "
                    "significand, however no other exponents will "
                    "appear--only the significands. If set to 'none', "
                    "NO exponents will appear, only the significands."),

    histnorm=dict(
        requried=False,
        type='plot_info',
        val_types="'' | 'percent' | 'probability' | 'density' | 'probability "
                  "density'",
        description="If histnorm is not specified, or histnorm='' ("
                    "empty string), the height of each bar displays the "
                    "frequency of occurrence, i.e., the number of times this "
                    "value was found in the corresponding bin. If "
                    "histnorm='percent', the height of each bar displays the "
                    "percentage of total occurrences found within the "
                    "corresponding bin. If histnorm='probability', the height "
                    "of each bar displays the probability that an event will "
                    "fall into the corresponding bin. If histnorm='density', "
                    "the height of each bar is equal to the number of "
                    "occurrences in a bin divided by the size of the bin "
                    "interval such that summing the area of all bins will "
                    "yield the total number of occurrences. If "
                    "histnorm='probability density', the height of each bar "
                    "is equal to the number of probability that an event will "
                    "fall into the corresponding bin divided by the size of "
                    "the bin interval such that summing the area of all bins "
                    "will yield 1, i.e. an event must fall into one of the "
                    "bins."
    ),

    name=dict(
        required=False,
        type='data',
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

    reversescl=dict(
        required=False,
        type='style'
    ),

    textposition=dict(
        required=False,
        type='style',
        val_types="'top' | 'bottom'",
        description="Set's position of the text elements in the 'text' key."
    ),

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
        examples=["Greys", [[0, "rgb(0,0,0)"], [1, "rgb(255,255,255)"]],
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

    showscale=dict(
        required=False,
        type='plot_info',
        val_types=val_types['general']['bool'],
        description="Toggle whether or not the color scale associated with "
                    "this mapping will be shown alongside the rendered "
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

    xref=dict(
        required=False,
        type='plot_info',
        val_types="'paper' | 'x1' | 'x2' | etc",
        description="This defines what the x coordinate for this object "
                    "*refers* to. If you reference an axis, e.g., 'x2', the "
                    "object will move with pan-and-zoom to stay fixed to this "
                    "point. If you reference the 'paper', it remains fixed "
                    "regardless of pan-and-zoom. In other words, if set to "
                    "'paper', the 'x' location refers to the distance from the "
                    "left side of the plotting area in normalized coordinates "
                    "where 0=='left' and 1=='right'. If set to refer to an "
                    "'xaxis' object, e.g., 'x1', 'x2', 'x3', etc., the 'x' "
                    "location will refer to the location in terms of this "
                    "axis."),

    yref=dict(
        required=False,
        type='plot_info',
        val_types="'paper' | 'y1' | 'y2' | etc",
        description="This defines what the x coordinate for this object "
                    "*refers* to. If you reference an axis, e.g., 'x2', the "
                    "object will move with pan-and-zoom to stay fixed to this "
                    "point. If you reference the 'paper', it remains fixed "
                    "regardless of pan-and-zoom. In other words, if set to "
                    "'paper', the 'y' location refers to the distance from the "
                    "bottom of the plotting area in normalized coordinates "
                    "where 0=='bottom' and 1=='top'. If set to refer to a "
                    "'yaxis' object, e.g., 'y1', 'y2', 'y3', etc., the 'y' "
                    "location will refer to the location in terms of this "
                    "axis."),

    xanchor=dict(
        required=False,
        type='plot_info',
        val_types="'left' | 'center' | 'right'",
        description="This defines the horizontal location on the object "
                    "referenced by 'x'. For example, if 'x'==1, "
                    "'xref'='paper', and 'xanchor'='right', the rightmost "
                    "portion of this object will line up with the rightmost "
                    "edge of the plotting area."),

    yanchor=dict(
        required=False,
        type='plot_info',
        val_types="'bottom' | 'middle' | 'top'",
        description="This defines the vertical location on the object "
                    "referenced by 'y'. For example, if 'y'==1, "
                    "'yref'='paper', and 'yanchor'='top', the upper edge "
                    "of this object will line up with the upper edge of the "
                    "plotting area.")
)


INFO = OrderedDict([

    ('plotlylist', dict()),

    ('data', dict()),

    ('annotations', dict()),

    ('plotlydict', dict()),

    ('plotlytrace', dict()),

    ('trace', OrderedDict([
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
        ('angularAxis', dict()),
        ('radialAxis', dict()),
        ('error_y', dict(type='object')),
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
    ])),

    ('scatter', OrderedDict([

        ('x', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
            description="The x coordinates from the (x,y) pair on the scatter "
                        "plot.")),

        ('y', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
            description="The y coordinates from the (x,y) pair on the scatter "
                        "plot.")),

        ('text', dict(
            required=False,
            type='data',
            val_types=val_types['general']['string_array'],
            description="The text elements associated with every (x,y) pair on "
                        "the scatter plot. If the scatter 'mode' doesn't "
                        "include 'text' then text will appear on hover. If "
                        "'text' is included in 'mode', the entries in 'text' "
                        "will be rendered on the plot at the locations "
                        "specified by their corresponding (x, y) pair."
        )),

        ('textposition', drop_in['textposition']),

        ('name', drop_in['name']),

        ('mode', dict(
            required=False,
            type='plot_info',
            val_types="'lines' | 'markers' | 'text' | 'lines+markers' | "
                      "'lines+text' | 'markers+text' | 'lines+markers+text'",
            description="Plotting mode (style) for the scatter plot. If the "
                        "mode includes 'text' then the 'text' will appear at "
                        "the (x,y) points, otherwise it will appear on "
                        "hover.")),

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
            description="If the 'fill' for a line is not 'none', the fill "
                        "color will appear in the specified fill area.",
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
                        "of this scatter's text elements. This only has "
                        "an effect if 'text' is an array of strings and "
                        "'mode' is set to include 'text'.")),

        ('r', dict(
            requried=False,
            type='data'
        )),

        ('t', dict(
            requried=False,
            type='data'
        )),

        ('type', dict(
            required=False,
            type='plot_info',
            val_types="'scatter'",
            description=description['trace']['type']
        )),

    ])),

    ('area', OrderedDict([
        ('x', dict(type='data')),
        ('y', dict(type='data')),
        ('z', dict(type='data')),
        ('r', dict(type='data')),
        ('t', dict(type='data')),
        ('text', dict(type='data')),
        ('textposition', dict(type='plot_info')),
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
        ('angularAxis', dict()),
        ('radialAxis', dict()),
        ('error_y', dict(type='object')),
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

        ('orientation', dict(
            required=False,
            type='plot_info',
            val_types=val_types['bar']['orientation'],
            description=description['bar']['orientation']
        )),

        ('text', dict(
            required=False,
            type='data',
            val_types=val_types['general']['string_array'],
            description="This array of strings corresponds to the bar at "
                        "location 'x' with length 'y'. This will appear upon "
                        "hovering over the bar."
        )),

        ('textposition', drop_in['textposition']),

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

        ('textfont', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary-like object describing the font for the "
                        "strings listed in the 'text' string-array.")),

        ('visible', drop_in['visible']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types="'bar'",
            description=description['trace']['type']
        )),

        ('r', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
        )),

        ('t', dict(
            required=True,
            type='data',
            val_types=val_types['general']['data_array'],
        )),

    ])),

    ('box', OrderedDict([

        ('y', dict(
            required=True,
            type="data",
            val_types=val_types['general']['data_array'],
            description="This array is used to define the an individual "
                        "box plot, or, a concatenation of multiple boxplots. "
                        "Statistics from these numbers define the bounds of "
                        "the box, the length of the whiskers, etc. For "
                        "details on defining multiple boxes with locations "
                        "see 'x'.")),

        ('x', dict(
            required=False,
            type='data',
            val_types=val_types['general']['data_array'],
            description="Usually, you do NOT need to set this value as "
                        "plotly will handle box locations for you. However "
                        "this allows you to have fine control over the "
                        "location data for the box. Unlike making a bar, "
                        "a box plot is made of MANY y values. Therefore, "
                        "to give location data to the values you place in "
                        "'y', the length of 'x' must equal the length of 'y'. "
                        "When making multiple box plots, you can concatenate "
                        "the data sets for each box into a single 'y' array. "
                        "Then, the entries in 'x' define which box plot each "
                        "entry in 'y' belongs to. When making a single box "
                        "plot, you must set each entry in 'x' to THE SAME "
                        "VALUE, see 'x0' for a more practical way to handle "
                        "this case. If you don't include 'x', the box will "
                        "simply be assigned a location.",
            code=">>> y0 = [1,2,3,1,1]"
                 ">>> y1 = [3,2,1,2,3]"
                 ">>> y = y0+y1  # the syntax is different for numpy arrays!"
                 ">>> x = [0,0,0,0,0,1,1,1,1,1]  # len(x) == len(y)"
                 ">>> Box(y=y, x=x, name='two boxes SHARE this name.')")),

        ('x0', dict(
            required=False,
            type='data',
            val_types=number(),
            description="The location of this box. When 'y' defines a SINGLE "
                        "box, 'x0' can be used to set where this box is "
                        "centered on the x-axis. If many boxes are set to "
                        "appear at the same 'x0' location, they will form a "
                        "box group.")),

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
            val_types=number(ge=-2, le=2),
            description="Horizontal position of the center of the boxpoints "
                        "relative to the center and width of the box.")),

        ('boxmean', dict(
            required=False,
            type='style',
            val_types="False | True | 'sd'",
            default='False',
            description="If True then the mean of the y-points is shown as a "
                        "dashed line in the box. If 'sd', then the standard "
                        "deviation is also shown. If False, then no line "
                        "shown.")),

        ('whiskerwidth', dict(
            required=False,
            type='style',
            val_types=number(ge=0, le=1),
            default=0.75,
            description="Width of the whisker of the box.")),

        ('fillcolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Color of the box interior.",
            examples=examples['general']['color'])),

        ('showlegend', drop_in['showlegend_trace']),

        ('stream', drop_in['stream']),

        ('xaxis', drop_in['xaxis_trace']),

        ('xaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('marker', dict(  # TODO!!! both line and marker CAN describe box color!
            required=False,
            type='object')),

        ('line', dict(  # TODO!!! both line and marker CAN describe box color!
            required=False,
            type='object')),

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
            val_types=val_types['general']['bool'],
            description="Speficy the number of countours lines that will "
                        "appear.")),

        ('contours', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary-like object defining parameters of "
                        "the contours in this plot like spacing, whether or "
                        "not to show lines, etc.")),

        ('scl', drop_in['scl']),

        ('reversescl', drop_in['reversescl']),

        ('colorbar', drop_in['colorbar']),

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

        ('showscale', drop_in['showscale']),

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

        ('zauto', dict(
            required=False,
            type='sytle',
            val_types=val_types['general']['bool'])),

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

        ('reversescl', drop_in['reversescl']),

        ('colorbar', drop_in['colorbar']),

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

        ('showscale', drop_in['showscale']),

        ('x0', dict(type='plot_info')),

        ('y0', dict(type='plot_info')),

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

        ('zauto', dict(
            required=False,
            type='sytle',
            val_types=val_types['general']['bool'])),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='heatmap',
            description=description['trace']['type']))

    ])),

    ('histogram', OrderedDict([

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

        ('name', drop_in['name']),

        ('orientation', dict(
            required=False,
            type='plot_info',
            val_types=val_types['bar']['orientation'],
            description=val_types['bar']['orientation']
        )),

        ('marker', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'])),

        ('opacity', drop_in['opacity']),

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

        ('nbinsx', dict(
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Specifies the number of bins in the x-direction.")),

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

        ('nbinsy', dict(
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Specifies the number of bins in the y-direction.")),

        ('histnorm', drop_in['histnorm']),

        ('showlegend', drop_in['showlegend_trace']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('stream', drop_in['stream']),

        ('error_y', drop_in['error_y']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='histogram',
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

        ('reversescl', drop_in['reversescl']),

        ('colorbar', drop_in['colorbar']),

        ('name', drop_in['name']),

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

        ('nbinsx', dict(
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Specifies the number of bins in the x-direction.")),

        ('nbinsy', dict(
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Specifies the number of bins in the y-direction.")),

        ('histnorm', drop_in['histnorm']),

        ('showlegend', drop_in['showlegend_trace']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('showscale', drop_in['showscale']),

        ('stream', drop_in['stream']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='histogram2d',
            description=description['trace']['type'])),

    ])),

    ('histogram2dcontour', OrderedDict([

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

        ('reversescl', drop_in['reversescl']),

        ('colorbar', drop_in['colorbar']),

        ('name', drop_in['name']),

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

        ('showlegend', drop_in['showlegend_trace']),

        ('xaxis', drop_in['xaxis_trace']),

        ('yaxis', drop_in['yaxis_trace']),

        ('visible', drop_in['visible']),

        ('showscale', dict()),

        ('stream', drop_in['stream']),

        ('type', dict(
            required=True,
            type='plot_info',
            val_types='histogram2dcontour',
            description=description['trace']['type'])),

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

        ('textposition', drop_in['textposition']),

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

        ('xref', drop_in['xref']),

        ('yref', drop_in['yref']),

        ('showarrow', dict(
            required=False,
            type='plot_info',
            val_types="bool: True | False",
            description="Show the arrow associated with this annotation.")),

        ('arrowwidth', dict(
            requried=False,
            type='style',
            val_types=number(gt=0)
        )),

        ('arrowcolor', dict(
            requried=False,
            type='style',
            val_types=val_types['general']['color']
        )),

        ('arrowhead', dict(
            requried=False,
            type='style',
        )),

        ('arrowsize', dict(
            requried=False,
            type='style',
        )),

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

        ('xanchor', drop_in['xanchor']),

        ('yanchor', drop_in['yanchor']),

        ('ay', dict(type='plot_info')),

        ('ax', dict(type='plot_info')),

        ('xatype', dict(type='plot_info')),

        ('yatype', dict(type='plot_info')),

        ('ref', dict(type='plot_info'))
    ])),

    ('colorbar', OrderedDict([])),

    ('error_y', OrderedDict([  # TODO: Line object here?
        ('value', dict(
            required=False,
            type='data'
        )),

        ('array', dict(
            required=False,
            type='data',
            val_types=val_types['general']['data_array'] + " or " + number(),
            description="The array of error bar spans to be drawn. This can "
                        "be specified as a data-array or as a single value ("
                        "see error_y's 'type' help for more information."
        )),
        ('color', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description=description['general']['color'],
            examples=examples['general']['color']
        )),
        ('opacity', drop_in['opacity']),
        ('thickness', dict(type='style')),  # TODO: why thickness and width?
        ('traceref', dict()),
        ('type', dict(
            required=False,
            type='plot_info',  # TODO: data?
            val_types="'data' | 'percent' | 'constant' | 'sqrt'",
            description="Specify how the 'array' key in this error bar will "
                        "be used to render the bars. Using 'data' will "
                        "require 'array' to be set to a multi-valued list of "
                        "spans for the error bar. Using 'percent' requires "
                        "'array' to be a single value set to the percent of "
                        "error associated with all data points, e.g., "
                        "array=50. Using 'constant' will set each error bar "
                        "span to the single value specified in 'array', e.g., "
                        "array=2. Use 'sqrt' with histogramx or histogramy. "
                        "This will set the error bar span to be sqrt(n) where "
                        "n is equal to the number of values in a particular "
                        "bin."
        )),
        ('visible', drop_in['visible']),
        ('width', dict(type='style'))
    ])),

    ('figure', OrderedDict([

        ('data', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A list-like array of the data that is to be "
                        "visualized.")),

        ('layout', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="The layout dictionary-like object contains axes "
                        "information, gobal settings, and layout information "
                        "related to the rendering of the figure."))
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
            required=False,
            type='plot_info',
            val_types=val_types['general']['string'],
            description="The figure title.")),

        ('xaxis', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="The first 'xaxis' object can be entered into layout "
                        "as 'xaxis' OR 'xaxis1', they're identical to plotly. "
                        "After this, to create references to new x-axes, "
                        "you need to define them in the layout dictionary.")),

        ('yaxis', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="The first 'yaxis' object can be entered into layout "
                        "as 'yaxis' OR 'yaxis1', they're identical to plotly. "
                        "After this, to create references to new y-axes, "
                        "you need to define them in the layout dictionary.")),

        ('legend', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary-like object describing the legend "
                        "settings for this figure.")),

        ('width', dict(
            required=False,
            type='style',
            val_types=number(gt=0),
            description="The width in pixels of the figure you're creating.")),

        ('height', dict(
            required=False,
            type='style',
            val_types=number(gt=0),
            description="The height in pixels of the figure you're creating.")),
        
        ('autosize', dict(
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Toggle whether or not to let plotly autosize this "
                        "figure for you.")),

        ('categories', dict(
            required=False,
            type='plot_info')),

        ('margin', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary-like object for describing the figure's "
                        "margins."
        )),

        ('paper_bgcolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description=description['general']['color']
        )),

        ('plot_bgcolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description=description['general']['color']
        )),

        ('dragmode', dict(
            required=False,
            type='style',
            val_types="'zoom' | 'pan'",
            description="Set what happens when a user preforms a mouse 'drag' "
                        "in the plot area. When set to 'zoom', a portion of "
                        "the plot will be highlighted, when the viewer "
                        "exits the drag, this highlighted section will be "
                        "zoomed in on. When set to 'pan', data in the plot "
                        "will move along with the viewers dragging motions. A "
                        "user can always depress the 'shift' key to access "
                        "the whatever functionality has not been set as the "
                        "default."
        )),

        ('hovermode', dict(
            required=False,
            type='style',
            val_types="'closest' | 'x' | 'y'",
            description="Set what happens when a user hovers over the figure. "
                        "When set to 'x', all data sharing the same 'x' "
                        "coordinate will be shown on screen with "
                        "corresponding trace labels. When set to 'y' all data "
                        "sharing the same 'y' coordainte will be shown on the "
                        "screen with corresponding trace labels. When set to "
                        "'closest', information about the data point closest "
                        "to where the viewer is hovering will appear."
        )),

        ('barmode', dict(
            required=False,
            type='plot_info',
            val_types="'stack' | 'group' | 'overlay'",
            description="This sets how multiple bar objects are plotted "
                        "together. In other words, this defines how bars at "
                        "the same location appear on the plot. If set to "
                        "'stack' the bars are stacked ontop of one another. "
                        "If set to 'group', the bars are plotted next to one "
                        "another, centered around the shared location. If set "
                        "to 'overlay', the bars are simply plotted over one "
                        "another, you may need to set the opacity to see this."
        )),

        ('bargap', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="This sets the gap between bars (or sets of bars) at "
                        "different locations."
        )),

        ('bargroupgap', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="This sets the gap between bars in the same group. "
                        "That is, when multiple bar objects are plotted and "
                        "share the same locations, this sets the distance "
                        "between bars at each location."
        )),

        ('boxmode', dict(
            required=False,
            type='style',
            val_types="'overlay' | 'group'",
            description="Sets how groups of box plots appear. If set to "
                        "'overlay', a group of boxes will be plotted directly "
                        "on top of one another at their specified location. "
                        "If set to 'group', the boxes will be centered around "
                        "their shared location, but they will not overlap.")),

        ('boxgap', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Set the spacing between neighboring box locations. "
                        "This does not effect the spacing within groups of "
                        "boxes.")),

        ('boxgroupgap', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Set the spacing between neighboring boxes within a "
                        "group. This does not effect the spacing between "
                        "boxes at neighboring box locations.")),

        ('font', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="Set the global font for the figure, e.g., all axis "
                        "labels."
        )),

        ('titlefont', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="Set the title font for the figure."
        )),

        ('separators', dict(
            required=False,
        )),

        ('labeloffset', dict(
            required=False,
        )),

        ('bardir', dict(
            required=False,
            type='plot_info'
        )),

        ('direction', dict(
            required=False,
        )),

        ('tickcolor', dict(
            required=False,
            type='style'
        )),

        ('minortickcolor', dict(
            required=False,
            type='style'
        )),

        ('defaultcolorrange', dict(
            required=False,
            type='style'
        )),

        ('hidesources', dict(
            required=False,
            type='plot_info'
        )),

        ('showlegend', drop_in['showlegend_layout']),

        ('annotations', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A list-like object that holds annotation "
                        "dictionaries.")),

        ('orientation', dict(
            required=False,
            type='plot_info')),

        ('radialAxis', dict(  # TODO polar
            required=False,
            type='object',
            val_types=val_types['general']['object']
        )),

        ('angularAxis', dict(  # TODO polar
            required=False,
            type='object',
            val_types=val_types['general']['object']
        )),

        ('needsEndSpacing', dict(  # TODO polar

        ))

    ])),

    ('legend', OrderedDict([

        ('x', dict(
            required=False,
            type='plot_info',
            val_types=number(),
            description="Sets the 'x' location of the legend."
        )),

        ('y', dict(
            required=False,
            type='plot_info',
            val_types=number(),
            description="Sets the 'y' location of the legend."
        )),

        ('bgcolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Sets the background color for the legend.",
            examples=examples['general']['color']
        )),

        ('bordercolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Sets the enclosing border color for the legend.",
            examples=examples['general']['color']
        )),

        ('borderwidth', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Sets the width of the enclosing border for the legend."
        )),

        ('font', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="This dictionary-like object describes the font "
                        "settings within the legend.")),

        ('showlegend', drop_in['showlegend_layout']),

        ('traceorder', dict(
            required=False,
            type='style',
            val_types="'normal' | 'reversed'",
            description="Trace order is set by the order of the data in "
                        "associated grid for the plot. This sets whether this "
                        "order is read from left-to-right or from "
                        "right-to-left.")),

        ('xref', drop_in['xref']),

        ('yref', drop_in['yref']),

        ('xanchor', drop_in['xanchor']),

        ('yanchor', drop_in['yanchor'])

    ])),

    ('line', OrderedDict([

        ('dash', dict(
            requried=False,
            type='style',
            val_types="'dash' | 'dashdot' | 'dot' | 'solid'",
            description="The style of the line."
        )),

        ('color', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="The color of the line."
        )),

        ('width', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="The width of the line."
        )),

        # ('thickness', dict()),  # TODO: redundant?

        ('opacity', drop_in['opacity']),

        ('smoothing', dict(  # TODO: should this be here if only for contours?
            type='style',
            description="Only applies to contours"))
    ])),


    ('margin', OrderedDict([

        ('l', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Left margin size in pixels.")),

        ('r', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Right margin size in pixels.")),

        ('b', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Bottom margin size in pixels.")),

        ('t', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Top margin size in pixels.")),

        ('pad', dict(
            required=False,
            type='style',
            val_types=number(ge=0),
            description="The distance between edge of the plot and the "
                        "bounding rectangle that encloses the plot.")),

        ('autoexpand', dict(  # TODO: ??
            required=False,
            type='style',
            val_types=val_types['general']['bool']
        ))
    ])),

    ('marker', OrderedDict([

        ('symbol', dict(
            required=False,
            type='style',
            val_types="'dot' | 'cross' | 'diamond' | 'square' "
                      "| 'triangle-down' | 'triangle-left' | 'triangle-right' "
                      "| 'triangle-up' | 'x'",
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
            required=False,
            type='style'
        )),

        ('sizeref', dict(
            required=False,
            type='style'
        )),

        ('color', dict(
            requried=False,
            type='style',
            val_types=val_types['general']['color'],
            description="The color of the marker face.",
            examples=examples['general']['color']
        )),

        ('opacity', drop_in['opacity']),

        ('type', dict(  # TODO REMOVE, this should be changed...
            required=False,
            type='style'))

    ])),

    ('stream', OrderedDict([

        ('token', dict(  # TODO: these are public!! Is that OK?
            required=True,
            type='plot_info',
            val_types="A stream id number, see https://plot.ly/settings",
            description="This number links a data object on a plot with a "
                        "stream. In other words, any data object you create "
                        "can reference a 'stream'. If you stream data to "
                        "plotly with the same stream id (token), plotly knows "
                        "update THIS data object with the incoming data "
                        "stream.")),

        ('maxpoints', dict(
            required=False,
            type='plot_info',
            val_types=number(gt=0),
            description="Sets the maximum number of points to keep on the "
                        "plots from an incoming stream. For example, "
                        "if 'maxpoints'=50, only the newest 50 points will be "
                        "displayed on the plot."))

    ])),

    ('radialAxis', OrderedDict([

    ])),

    ('angularAxis', OrderedDict([

    ])),

    ('xaxis', OrderedDict([

        ('title', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['string'],
            description="The xaxis title.")),

        ('domain', dict(
            required=False,
            type='plot_info',
            val_types="number array of length 2",
            description="Sets the domain of this axis. The available space "
                        "for this axis to live in is from 0 to 1.",
            examples=[[0, 1], [0, 0.5]])),

        ('range', dict(
            required=False,
            type='style',  # TODO: changed this!!!  was plot_info
            val_types="number array of length 2",
            description="Defines the start and end point for the axis.",
            examples=[[-13, 20], [0, 1]])),

        ('type', dict(
            required=False,
            type='plot_info',
            val_types="string: linear | log | category",
            description="Defines format of the axis.")),

        ('showline', dict(
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Defines whether or not to show this axis line.")),

        ('linecolor', dict(  # TODO: why isn't this just a Line object here?
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Defines the axis line color.",
            examples=examples['general']['color'])),

        ('linewidth', dict(  # TODO: why isn't this just a Line object here?
            required=False,
            type='style',
            val_types=number(),
            description="Sets the width of the axis line.")),

        ('tick0', dict(  # TODO: better description?
            required=False,
            type='plot_info',
            val_types=number(),
            description="Sets the starting point of the axis.")),

        ('dtick', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_type=number(),
            description="Sets the difference between ticks on this axis."
        )),

        ('ticks', dict(  # TODO: separate object for ticks?
            requried=False,
            type='style',
            val_types="string: 'inside' | 'outside' | '' (Empty str for NONE)",
            description="Sets format of tick visibility.")),

        ('ticklen', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=number(),
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
            val_types=number(ge=0),
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

        ('exponentformat', drop_in['exponentformat']),

        ('showexponent', drop_in['showexponent']),

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
            type='style',
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

        ('overlaying', dict()),  # TODO: ??

        ('position', dict(
            required=False,
            type='style',
            val_types=number(le=1, ge=0),
            description="Sets where the axis is positioned in the plotting "
                        "space. For example 'position'=0.5 will place this "
                        "axis in the exact center of the plotting space. This "
                        "only has functionality if 'anchor'='free'."
        )),

        ('anchor', dict(
            required=False,
            type='plot_info',
            val_types="'y' | 'free'",
            description="Sets whether the xaxis will be anchored to its "
                        "corresponding yaxis OR 'free' to appear anywhere in "
                        "the vertical space of the plot."
        )),

        ('side', dict(
            required=False,
            type='style',
            val_types="'bottom' | 'top'",
            description="Set whether this axis sits at the 'bottom' of the "
                        "plot or at the 'top' of the plot."
        )),

        ('mirror', dict(
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Toggle whether to mirror the axis line to the "
                        "opposite side of the plot.")),

        # ('drange', dict()),
        # ('r0', dict()),
    ])),

    ('xbins', OrderedDict([
        ('start', dict(
            required=False,
            type='plot_info',
            val_types=number(),
            description="The starting point on the xaxis for the FIRST bin."
        )),
        ('end', dict(
            required=False,
            type='plot_info',
            val_types=number(),
            description="The end point on the xaxis for the FINAL bin."
        )),
        ('size', dict(
            requried=False,
            type='plot_info',
            val_types=number(gt=0),
            description="The size of each bin."
        ))
    ])),

    ('yaxis', OrderedDict([

        ('title', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['string'],
            description="The yaxis title.")),

        ('domain', dict(
            required=False,
            type='plot_info',
            val_types="number array of length 2",
            description="Sets the domain of this axis. The available space "
                        "for this axis to live in is from 0 to 1.",
            examples=[[0, 1], [0, 0.5]])),

        ('range', dict(
            required=False,
            type='style',  # TODO: changed this!!!  was plot_info
            val_types="number array of length 2",
            description="Defines the start and end point for the axis.",
            examples=[[-13, 20], [0, 1]])),

        ('type', dict(
            required=False,
            type='plot_info',
            val_types="string: linear | log | category",
            description="Defines format of the axis.")),

        ('showline', dict(
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Defines whether or not to show this axis line.")),

        ('linecolor', dict(  # TODO: why isn't this just a Line object here?
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Defines the axis line color.",
            examples=examples['general']['color'])),

        ('linewidth', dict(  # TODO: why isn't this just a Line object here?
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Sets the width of the axis line.")),

        ('tick0', dict(  # TODO: better description?
            required=False,
            type='plot_info',
            val_types="number",
            description="Sets the starting point of the axis.")),

        ('dtick', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_type=number(ge=0),
            description="Sets the difference between ticks on this axis.")),

        ('ticks', dict(  # TODO: separate object for ticks?
            requried=False,
            type='style',
            val_types="string: 'inside' | 'outside' | '' (Empty str for NONE)",
            description="Sets format of tick visibility.")),

        ('ticklen', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Sets the length of the tick lines.")),  # in points?

        ('tickcolor', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Sets the color of the tick lines.")),

        ('tickwidth', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Sets the width of the tick lines.")),


        ('nticks', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=number(ge=0),
            description="Sets the number of ticks to appear on the axis.")),

        ('showticklabels', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Show/Hide the axis tick labels.")),

        ('tickangle', dict(  # TODO: separate object for ticks?
            required=False,
            type='style',
            val_types=number(le=90, ge=-90),
            description="Sets the angle of the ticks in degrees.")),

        ('exponentformat', drop_in['exponentformat']),

        ('showexponent', drop_in['showexponent']),

        ('showgrid', dict(
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Show/Hide grid for the axis.")),

        ('gridcolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Sets the axis grid color. Any HTML specified color "
                        "is accepted.",
            examples=examples['general']['color'])),

        ('gridwidth', dict(
            requried=False,
            type='style',
            val_types=number(gt=0),
            description="Sets the grid width.")),

        ('autorange', dict(
            required=False,
            type='plot_info',
            val_types=val_types['general']['bool'],
            description="Toggle whether to let plotly autorange the axis.")),

        ('rangemode', dict(
            required=False,
            type='plot_info',  # TODO: style?
            val_types="string: 'normal' | 'tozero' | 'nonnegative'")),

        ('autotick', dict(
            required=False,
            type='style',  # TODO: 'plot_info' ??
            val_types=val_types['general']['bool'],
            description="Toggle axis autoticks.")),

        ('zeroline', dict(
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Show/Hide an additional zeroline for this axis.")),

        ('zerolinecolor', dict(
            required=False,
            type='style',
            val_types=val_types['general']['color'],
            description="Set the color of this axis' zeroline.",
            examples=examples['general']['color'])),

        ('zerolinewidth', dict(
            required=False,
            type='style',
            val_types=number(gt=0),
            description="Sets the width of this axis' zeroline.")),

        ('titlefont', dict(
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary for configuring the axis title font.")),

        ('tickfont', dict(  # TODO: separate object for ticks?
            required=False,
            type='object',
            val_types=val_types['general']['object'],
            description="A dictionary for configuring the tick font.")),

        ('position', dict(
            required=False,
            type='style',
            val_types=number(le=1, ge=0),
            description="Sets where the axis is positioned in the plotting "
                        "space. For example 'position'=0.5 will place this "
                        "axis in the exact center of the plotting space. This "
                        "only has functionality if 'anchor'='free'.")),

        ('anchor', dict(
            required=False,
            type='plot_info',
            val_types="'x' | 'free'",
            description="Sets whether the yaxis will be anchored to its "
                        "corresponding xaxis OR 'free' to appear anywhere in "
                        "the horizontal space of the plot.")),

        ('side', dict(
            required=False,
            type='style',
            val_types="'left' | 'right'",
            description="Set whether this axis sits at the 'left' of the "
                        "plot or at the 'right' of the plot.")),

        ('mirror', dict(
            required=False,
            type='style',
            val_types=val_types['general']['bool'],
            description="Toggle whether to mirror the axis line to the "
                        "opposite side of the plot.")),

        ('overlaying', dict()),

        # ('drange', dict()),
        # ('r0', dict()),

    ])),

    ('ybins', OrderedDict([

        ('start', dict(
            required=False,
            type='plot_info',
            val_types=number(),
            description="The starting point on the yaxis for the FIRST bin.")),

        ('end', dict(
            required=False,
            type='plot_info',
            val_types=number(),
            description="The end point on the yaxis for the FINAL bin.")),

        ('size', dict(
            requried=False,
            type='plot_info',
            val_types=number(gt=0),
            description="The size of each bin."))

    ])),

    ('contours', OrderedDict([  # TODO: !!

        ('start', dict(
            requried=False,
            type='plot_info')),

        ('end', dict(
            requried=False,
            type='plot_info')),

        ('size', dict(
            requried=False,
            type='plot_info')),

        ('coloring', dict()),

        ('showlines', dict(
            requried=False,
            type='sytle',
            val_types=val_types['general']['bool'],
            description="Toggle whether the contour lines appear on the "
                        "plot.")),
    ]))

])

if __name__ == "__main__":
    import json

    with open('graph_objs_meta.json', 'w') as f:
        f.write(json.dumps(INFO, indent=4, sort_keys=False))

    obj_keys = dict()
    for key, val in INFO.items():
        obj_keys[key] = list()
        for k, v in val.items():
            try:
                obj_keys[key].append("'{}': '{}'".format(k, v['type']))
            except KeyError:
                obj_keys[key].append("'{}': {}".format(k, 'UNCLASSIFIED'))
    with open('graph_objs_keys.json', 'w') as f:
        f.write(json.dumps(obj_keys, indent=4, sort_keys=False))

