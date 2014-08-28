
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
            graph_objs=[
                'scatter',
                'bar',
                'histogram',
                'box', 
                'heatmap',
                'contour',
                'histogram2d',
                'histogram2dcontour',
                'area'
            ]
        ),
        dict(
            group='Trace auxiliary objects',
            description='Add some spice to your traces with these',
            graph_objs=[
                'error_y',
                'error_x',
                'xbins',
                'ybins',
                'marker',
                'line',
                'contours',
                'stream'
            ]
        ),
        dict(
            group='Axis objects',
            description="Set the your axes' specifications and style with these",
            graph_objs=[
                'xaxis',
                'yaxis',
                'radialaxis',
                'angularaxis'
            ]
        ),
        dict(
            group='Layout and layout style objects',
            description="Customize your figure's layout with these",
            graph_objs=[
                'layout',
                'font',
                'legend',
                'annotation',
                'colorbar',
                'margin'
            ]
        ),
        dict(
            group='Figure object',
            description='Package layout and data with this object',
            graph_objs=[
                'figure'
            ]
        ),
        dict(
            group='List-like objects',
            description=False,        # => will not appear on plot.ly/
            graph_objs=[
                'data',
                'annotations'
            ],
        ),
        dict(
            group='Primitive',
            description=False,        # => will not appear on plot.ly/
            graph_objs=[
                'trace',
                'plotlylist',
                'plotlydict',
                'plotlytrace'
            ]
        )
    ]
    graph_objs = [graph_obj 
                 for info in graph_objs_info 
                 for graph_obj in info['graph_objs']]
    return graph_objs_info, graph_objs

# -------------------------------------------------------------------------------

