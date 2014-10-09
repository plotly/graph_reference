import set_run

# -------------------------------------------------------------------------------
#
# Set language-specific vocabulary here.
#
# * The table below is used to format methods in `meta.py` and `meta_shortcut.py`.
#
# * The table below is complemented by 'indefinite article' and 'plural'
#   versions generated in make_tables() in `run.py`.
#
# * The vocabulary listed here is intended for descriptions of objects and keys.
#   Language-specific code snippets are set in the `Example` class of `meta.py`.

# Vocabulary:
#
# - LANG : Language's name (with correct cases e.g. MATLAB)
# - WEB : Online docs root URL 
# - OL : Name of ordered lists
# - OL2D : Name of 2d ordered lists
# - UL : Name of unordered lists
# - OLlike : Name of {OL}-like (currently only in Python API)
# - ULlike : Name of {UL}-like (currently only in Python API)
# - TRUE : Boolean true
# - FALSE : Boolean false
# - NAN : code name for Not-a-Numbers
#
# ------------------------------------------------------------------------------

# Define vocabulary
table = dict(
    python = dict(
        LANG = 'python',
        WEB = 'https://plot.ly/python/',
        OL = 'list or 1d numpy array',
        OL2D = 'list of lists or 2d numpy array',
        UL = 'dictionary',
        OLlike = 'list-like object',
        ULlike = 'dictionary-like object',
        TRUE = 'True',
        FALSE = 'False',
        NAN = 'numpy.nan',
    ),
    matlab = dict(
        LANG = 'MATLAB',
        WEB = 'https://plot.ly/matlab/',
        OL = 'array',
        OL2D = '2d array',
        UL = 'structure array',
        OLlike = 'cell array',     # same as OL
        ULlike = 'structure array', # same as UL
        TRUE = 'true',
        FALSE = 'false',
        NAN = 'NaN',
    ),
    r = dict(
        LANG = 'R',
        WEB = 'https://plot.ly/r/',
        OL = 'generic vector (list) or atomic vector',
        OL2D = 'list of lists or matrix',
        UL = 'list',
        OLlike = 'generic vector (list) or atomic vector', # same as OL
        ULlike = 'list', # same as UL
        TRUE = 'TRUE',
        FALSE = 'FALSE',
        NAN = 'NaN'
    ),
    nodejs = dict(
        LANG = 'Node.js',
        WEB = 'https://plot.ly/nodejs/',
        OL = 'array',
        OL2D = 'array of arrays',
        UL = 'object',
        OLlike = 'array',  # same as OL
        ULlike = 'object', # same as UL
        TRUE = 'true',
        FALSE = 'false',
        NAN = 'NaN'
    ),
    julia = dict(
        LANG = 'Julia',
        WEB = 'https://plot.ly/julia/',
        OL = 'array',
        OL2D = '2d array',
        UL = 'dictionary',
        OLlike = 'array',      # same as OL
        ULlike = 'dictionary', # same as UL
        TRUE = 'TRUE',
        FALSE = 'FALSE',
        NAN = 'NaN'
    )
)
        

# Add graph object *names* to table
languages = set_run.languages()
graph_objs_info = set_run.graph_objs_info()
graph_objs = set_run.graph_objs()

for language in languages:
    for graph_obj in graph_objs:
        if language == 'python':  # N.B Special object name in Python API!
            name = (
                graph_obj.title()
                         .replace('_','')
                         .replace('axis','Axis')
                         .replace('bins','Bins')
                         .replace('2D','2d')
                         .replace('3D','3d')
                         .replace('bar','Bar')
                         .replace('contour','Contour')
            )
            table[language][graph_obj] = name
        else:
            table[language][graph_obj] = graph_obj
