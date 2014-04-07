# -*- coding: utf-8 -*-

from collections import OrderedDict

shortcuts = {
    'color': {
        'type': 'str describing color',
        'examples': ["'green'", "'rgb(0, 255, 0)'", "'rgba(0, 255, 0, 0.3)'", "'hsl(120,100%,50%)'", "'hsla(120,100%,50%,0.3)'"]
    },
    'data_array': {
        'type': "array_like of numbers, strings, datetimes"
    },
    'text': {
        'val_types': "array_like of strings"
    },
    'name': dict(
        required=False,
        type='plot_info',
        val_types="string",
        description="The label associated with this trace. "
                    "This name will appear in the legend, in the column "
                    "header in the spreadsheet, and on hover."),
    'error_y': dict(
        required=False,
        type='object',
        val_types="Error_Y object | dict",
        description="A dictionary-like object describing vertical error bars "
                    "that can be drawn with this trace's (x, y) points."),

    'xaxis': dict(
        required=False,
        type='object',
        default="'x'",
        val_types="string: 'x', 'x2', 'x3', ...",
        description="This key determines which xaxis the x coordinates in "
                    "this trace will reference in the figure. "
                    "'x' references layout['xaxis'] and 'x2' "
                    "references layout['xaxis2']."),

    'yaxis': dict(
        required=False,
        type='object',
        val_types="string: 'y', 'y2', 'y3', ...",
        description="This key determines which yaxis the y coordinates in "
                    "this trace will reference in the figure. "
                    "'y' references layout['yaxis'] and 'y2' "
                    "references layout['yaxis2']."),    

}



INFO = OrderedDict(

    plotlylist=dict(),

    data=dict(),

    annotations=dict(),

    plotlydict=dict(),

    plotlytrace=dict(),

    scatter=OrderedDict(

        x=dict(
            required=True,
            type='data',
            val_types=shortcuts['data_array']['type'],
            description="the x coordinates from the (x,y) pair on the scatter "
                        "plot."),

        y=dict(
            required=True,
            type='data',
            val_types=shortcuts['data_array']['type'],
            description="the y coordinatey from the (x,y) pair on the scatter "
                        "plot."),

        text=dict(
            required=False,
            type='data',
            val_types=shortcuts['text']['val_types'],
            description="the text elements associated with every (x,y) pair on "
                        "the scatter plot. If the scatter 'mode' doesn't include "
                        "'text' then text will appear on hover."),

        name=shortcuts['name'],

        mode=dict(
            required=False,
            type='plot_info',
            val_types="'lines' | 'markers' | 'text' | 'lines+markers' | 'lines+text' "
                        "| 'markers+text' | 'lines+markers+text'",
            description="Plotting mode (style) for the scatter plot. If the mode includes "
                        "'text' then the 'text' will appear next to the (x,y) points, "
                        "otherwise it will appear on hover."),

        marker=dict(
            required=False,
            type='object',
            val_types="Marker object | dict",
            description="A dictionary-like object containing information "
                        "about the marker style of the scatter plot."),

        line=dict(
            required=False,
            type='object',
            val_types="Line object | dict",
            description="A dictionary-like object containing information "
                        "about the line connecting points on the scatter plot."),

        fill=dict(
            required=False,
            default='none',
            type='style',
            val_types="'none' | 'tozeroy' | 'tonexty' | 'tozerox' | 'tonextx",
            description="Used to make area-style charts. Determines which area "
                        "to fill with a solid color. ",
        ),

        fillcolor=dict(
            required=False,
            type='style',
            val_types=shortcuts['color']['type'],
            examples=shortcuts['color']['examples']
        ),

        opacity=dict(
            required=False,
            type='style',
            val_types="number in [0, 1]",
            description="Sets the opacity, or transparency, of the markers "
                        " and lines of the scatter plot. Also known as the "
                        " alpha channel. The opacity can also be set in the "
                        " 'marker' and 'line' objects."),

        showlegend=dict(
            required=False,
            type='plot_info',
            val_types="True | False",
            default="True",
            description="If True, this trace will appear in the legend. Otherwise "
                        " it will be hidden in the legend."),

        xaxis=shortcuts['xaxis'],

        yaxis=shortcuts['yaxis'],

        error_y=shortcuts['error_y'],

        textfont=dict(
            required=False,
            type='object',
            val_types="Font object | dict",
            description="A dictionary-like object describing the font style "
                        "of this scatter's text elements."),

        type=dict(
            required=False,
            type='plot_info',
            val_types="'scatter'",
            description="Plotly identifier for trace type, this is set "
                        "automatically with a call to Scatter(...).")

    ),


    bar=OrderedDict(

        x=dict(
            required=True,
            type='data',
            val_types=shortcuts['data_array']['type'],
            description="the x coordinates of the bars or the bar chart's categories. "),

        y=dict(
            required=True,
            type='data',
            val_types=shortcuts['data_array']['type'],
            description="the y data for bar charts, which is the length of the bars."),

        text=dict(
            required=False,
            type='data',
            val_types=shortcuts['text']['val_types'],
            description='text elements that appear on hover of the bars'),

        name=shortcuts['name'],

        marker=dict(
            required=False,
            type='structure',
            val_types="Marker | dict",
            description="A dictionary-like object describing the "
                        "style of the bars, like the color and the border."),

        xaxis=shortcuts['xaxis'],

        yaxis=shortcuts['yaxis'],

        error_y=shortcuts['error_y'],

        type=dict(
            required=True,
            type='plot_info',
            val_types="'bar'",
            description="Plotly identifier for trace type, this is set "
                        "automatcally with a call to Bar(...).")
    ),

    box=dict(

        y=dict(
            required=True,
            type="plot_info",
            val_types="array_like of numbers",
            description="Array of the numbers from which the box plot describes."
        ),

        name=dict(
            required=False,
            type="plot_info",
            val_types="string",
            description="The label associated with this box plot. This name appears "
                "on the x-axis, in the legend, on hover, and  in the column "
                "header in the spreadsheet"),

        boxpoints=dict(
            required=False,
            type='plot_info',
            val_types="'all' | 'outliers' | False",
            description="If 'all' then the 'y' points are shown with the box. If "
                "'outliers' then only the 'outliers' of the 'y' points are shown. If False "
                "then no points are shown",
            default=False),

        jitter=dict(
            required=False,
            type='style',
            val_types="number in [0, 1]",
            description="Width of the jittered scatter. If 0, then the boxpoints "
                        "are aligned vertically, if 1 then the points are randomly "
                        "jittered horizontally up to the width of the box."),

        pointpos=dict(
            required=False,
            type='style',
            val_types="number in [-2, 2]",
            description="Horizontal position of the center of the boxpoints relative to "
                        "the center and width of the box."),

        boxmean=dict(
            required=False,
            type="False | True | 'sd'",
            default='False',
            description="If True then the mean of the y-points is shown as a "
                        "dashed line in the box. If 'sd', then the standard deviation "
                        "is also shown. If False, then no line shown."),

        whiskerwidth=dict(
            required=False,
            type='number in [0, 1]',
            default=0.75,
            description="Width of the whisker of the box."),

        fillcolor=dict(
            required=False,
            type='style',
            description="Color of the box interior.",
            val_types=shortcuts['color']['type'],
            examples=shortcuts['color']['examples']),

        type=dict(
            required=True,
            type='plot_info',
            val_types="default: type='box'",
            description="Plotly identifier for trace type, this is set "
                        "automatcally with a call to Box(...).")
    ),

    contour=dict(

        type=dict(
            required=True,
            type='plot_info',
            val_types="default: type='contour'",
            description="Plotly identifier for trace type, this is set "
                        "automatcally with a call to Contour(...).")
    ),

    heatmap=OrderedDict(

        z=dict(
            required=True,
            type='data',
            val_types="matrix_like: list of lists, numpy.matrix",
            description="The data that describes the heatmap. The "
                        "color of the cell in row i, column j "
                        "is mapped from the value of z[i][j]."),

        x=dict(
            required=False,
            type='data',
            val_types=shortcuts['data_array']['type'],
            description="If numerical or date-like, the coordinates of "
                        "the horizontal edges of the heatmap cells "
                        "where the length of 'x' must be one more than the number of "
                        "columns in the heatmap. If strings, then the x-labels "
                        "the heatmap cells where the length of 'x' is equal to "
                        "the number of columns in the heatmap."
        ),

        y=dict(
            required=False,
            type='data',
            val_types=shortcuts['data_array']['type'],
            description="If numerical or date-like, the coordinates of "
                        "the vertical edges of the heatmap cells "
                        "where the length of 'y' must be one more than the number of "
                        "rows in the heatmap. If strings, then the y-labels "
                        "the heatmap cells where the length of 'y' is equal to "
                        "the number of rows in the heatmap."
        ),

        scl=dict(
            required=False,
            type='style',
            val_types="array_like of value-color pairs | 'Greys' | 'Greens' | "
                "'Bluered' | 'Hot' | 'Picnic' | 'Portland' | 'Jet' | "
                "'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'",
            description="The color scale. The strings are pre-defined color scales. For "
                        "custom color scales, define a list of color-value pairs, where the "
                        "first element of the pair corresponds to a "
                        "normalized value of z from 0-1 (i.e. (z-zmin)/(zmax-zmin)), "
                        "and the second element of pair corresponds to a color.",
            examples=["Greys", [[0,"rgb(0,0,0)"],[1,"rgb(255,255,255)"]], 
                    [[0,"rgb(8, 29, 88)"],[0.125,"rgb(37, 52, 148)"],[0.25,"rgb(34, 94, 168)"],
                    [0.375,"rgb(29, 145, 192)"],[0.5,"rgb(65, 182, 196)"],[0.625,"rgb(127, 205, 187)"],
                    [0.75,"rgb(199, 233, 180)"],[0.875,"rgb(237, 248, 217)"],[1,"rgb(255, 255, 217)"]]]
        ),

        colorbar=dict(
            required=False,
            type='object',
            val_types="Colorbar object | dict",
            description=False
        ),

        xtype=dict(
            required=False,
            type='style',
            val_types="'array' | 'scaled'",
            description=False
        ),

        ytype=dict(
            required=False,
            type='style',
            val_types="'array' | 'scaled'",
            description=False
        ),

        dx=dict(
            required=False,
            type='style',
            val_types='number',
            description=False
        ),

        dy=dict(
            required=False,
            type='style',
            val_types='number',
            description=False
        ),

        zmin=dict(
            required=False,
            type='style',
            val_types='number',
            description="The value used as the minimum in the color scale normalization in 'scl'. "
                        "The default is the minimum of the 'z' data values."
        ),

        zmax=dict(
            required=False,
            type='style',
            val_types='number',
            description="The value used as the maximum in the color scale normalization in 'scl'. "
                        "The default is the minimum of the 'z' data values."
        ),

        type=dict(
            required=True,
            type='plot_info',
            val_types="default: type='heatmap'",
            description="Plotly identifier for trace type, this is set "
                        "automatcally with a call to Heatmap(...).")
    ),

    histogram2d=dict(

        type=dict(
            required=True,
            type='plot_info',
            val_types="default: type='histogram2d'",
            description="Plotly identifier for trace type, this is set "
                        "automatcally with a call to Histogram2d(...)."),
    ),

    histogramx=dict(

        type=dict(
            required=True,
            type='plot_info',
            val_types="default: type='histogramx'",
            description="Plotly identifier for trace type, this is set "
                        "automatcally with a call to Histogramx(...).")
    ),

    histogramy=dict(

        type=dict(
            required=True,
            type='plot_info',
            val_types="default: type='histogramy'",
            description="Plotly identifier for trace type, this is set "
                        "automatcally with a call to Histogramy(...)."),
    ),


    annotation=dict(

        text=dict(
            required=False,
            type='plot_info',
            val_types="coming soon!",
            descriptors="coming soon!"),

        bordercolor=dict(),

        borderwidth=dict(),

        borderpad=dict(),

        bgcolor=dict(),

        xref=dict(
            required=False,
            type='plot_info',
            val_types="coming soon!",
            description="coming soon!"),

        yref=dict(
            required=False,
            type='plot_info',
            val_types="coming soon!",
            description="coming soon!"),

        showarrow=dict(
            required=False,
            type='plot_info',
            val_types="coming soon!",
            description="coming soon!"),

        arrowwidth=dict(),

        arrowcolor=dict(),

        arrowhead=dict(),

        arrowsize=dict(),

        tag=dict(),

        font=dict(),

        opacity=dict(),

        align=dict(
            required=False,
            type='plot_info',
            val_types="coming soon!",
            description="coming soon!"),

        xanchor=dict(
            required=False,
            type='plot_info',
            val_types="coming soon!",
            description="coming soon!"),

        yanchor=dict(),

        ay=dict(),

        ax=dict(),

        y=dict(),

        x=dict()
    ),

    figure=dict(

        data=dict(),

        layout=dict(),
    ),

    font=dict(

        color=dict(),

        size=dict(),

        family=dict(),
    ),

    layout=dict(

        title=dict(),

        xaxis=dict(),

        yaxis=dict(),

        legend=dict(),

        width=dict(),

        height=dict(),

        autosize=dict(),

        margin=dict(),

        paper_bgcolor=dict(),


        plot_bgcolor=dict(),

        barmode=dict(),

        bargroupgap=dict(),

        boxmode=dict(),

        boxgap=dict(),

        boxgroupgap=dict(),

        font=dict(),

        titlefont=dict(),

        dragmode=dict(),

        hovermode=dict(),

        separators=dict(),

        hidesources=dict(),

        showlegend=dict(),

        annotations=dict()
    ),

    legend=dict(

        bgcolor=dict(),

        bordercolor=dict(),

        font=dict(),

        traceorder=dict()
    ),

    line=dict(

        dash=dict(),

        color=dict(),

        width=dict(),

        opacity=dict(),
    ),

    margin=dict(

        l=dict(),

        r=dict(),

        b=dict(),

        t=dict(),

        pad=dict()
    ),

    marker=dict(

        symbol=dict(),

        line=dict(),

        size=dict(),

        color=dict(),

        opacity=dict()
    ),

    xaxis=dict(

        range=dict(),

        type=dict(),

        showline=dict(),

        mirror=dict(),

        linecolor=dict(),

        linewidth=dict(),

        tick0=dict(),

        dtick=dict(),

        ticks=dict(),

        ticklen=dict(),

        tickcolor=dict(),

        nticks=dict(),

        showticklabels=dict(),

        tickangle=dict(),

        exponentformat=dict(),

        showgrid=dict(),

        gridcolor=dict(),

        gridwidth=dict(),

        autorange=dict(),

        rangemode=dict(),

        autotick=dict(),

        zeroline=dict(),

        zerolinecolor=dict(),

        zerolinewidth=dict(),

        titlefont=dict(),

        tickfont=dict(),

        overlaying=dict(),

        domain=dict(),

        position=dict(),

        anchor=dict(),

        title=dict()
    ),

    yaxis=dict(

        range=dict(),

        type=dict(),

        showline=dict(),

        mirror=dict(),

        linecolor=dict(),

        linewidth=dict(),

        tick0=dict(),

        dtick=dict(),

        ticks=dict(),

        ticklen=dict(),

        tickcolor=dict(),

        nticks=dict(),

        showticklabels=dict(),

        tickangle=dict(),

        exponentformat=dict(),

        showgrid=dict(),

        gridcolor=dict(),

        gridwidth=dict(),

        autorange=dict(),

        rangemode=dict(),

        autotick=dict(),

        zeroline=dict(),

        zerolinecolor=dict(),

        zerolinewidth=dict(),

        titlefont=dict(),

        tickfont=dict(),

        overlaying=dict(),

        domain=dict(),

        position=dict(),

        anchor=dict(),

        title=dict()
    ),

    error_x=dict(),

    error_y=dict(),

    titlefont=dict()
)

import json
print json.dumps(INFO)