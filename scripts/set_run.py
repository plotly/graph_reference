# -------------------------------------------------------------------------------
# 
# Set which language and which graph object to generate meta for.
#
# -------------------------------------------------------------------------------

def languages():
    '''Set list of languages'''
#    languages = [
#        'python',
#        'matlab',
#        'r',
#        'nodejs',
#        'julia'
#    ]
    languages = ['python', 'matlab']
    return languages

def graph_objs():
    '''
    Set list of graph objects, 
    along with their category group
    and a description (for the plot.ly/<lang>/reference/ table of content)
    '''
    graph_objs_info = [
        dict(
            group='Trace graph objects',
            description='Bind your data to traces with these',
            names=[
                'Scatter',
                'Bar',
                'Histogram',
                'Box', 
                'Heatmap',
                'Contour',
                'Histogram2d',
                'Histogram2dContour',
                'Area'
            ]
        ),
        dict(
            group='Trace auxiliary objects',
            description='Add some spice to your traces with these',
            names=[
                'ErrorY',
                'ErrorX',
                'XBins',
                'YBins',
                'Marker',
                'Line',
                'Contours',
                'Stream'
            ]
        ),
        dict(
            group='Axis objects',
            description="Set the your axes' specifications and style with these",
            names=[
                'XAxis',
                'YAxis',
                'RadialAxis',
                'AngularAxis'
            ]
        ),
        dict(
            group='Layout and layout style objects',
            description="Customize your figure's layout with these",
            names=[
                'Layout',
                'Font',
                'Legend',
                'Annotation',
                'ColorBar',
                'Margin'
            ]
        ),
        dict(
            group='Figure object',
            description='Package layout and data with this object',
            names=[
                'Figure'
            ]
        ),
        dict(
            group='List-like objects',
            description=False,        # => will not appear on plot.ly/
            names=[
                'Data',
                'Annotations'
            ],
        ),
        dict(
            group='Primitive',
            description=False,        # => will not appear on plot.ly/
            names=[
                'Trace',
                'PlotlyList',
                'PlotlyDict',
                'PlotlyTrace'
            ]
        )
    ]
    graph_objs = [name for info in graph_objs_info for name in info['names']]
    return graph_objs_info, graph_objs

# -------------------------------------------------------------------------------

