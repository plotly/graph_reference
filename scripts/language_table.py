import set_run

# -------------------------------------------------------------------------------
#
# Set language-specific vocabulary here.
#
# * This table is used to format methods in `meta.py` and `meta_shortcut.py`.
#
# * The vocabulary listed here is intended for descriptions of objects and keys.
#   Language-specific code snippets are set in the `Example` class of `meta.py`.
#
# Vocabulary:
#
# - LANG : Language's name (with correct cases e.g. MATLAB)
# - WEB : Online docs root URL 
# - OL : Name for ordered lists
# - OL2D : Name for 2d ordered lists
# - UL : Name for unordered lists
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
        TRUE = 'True',
        FALSE = 'False',
        NAN = 'numpy.nan',
    ),
    matlab = dict(
        LANG = 'MATLAB',
        WEB = 'https://plot.ly/matlab/',
        OL = 'array',
        OL2D = '2d array',
        UL = 'structure',
        TRUE = 'TRUE',
        FALSE = 'FALSE',
        NAN = 'NaN',
    ),
    r = dict(
        LANG = 'R',
        WEB = 'https://plot.ly/r/',
        OL = 'generic vector (list) or atomic vector',
        OL2D = 'list of lists or matrix',
        UL = 'list',
        TRUE = 'TRUE',
        FALSE = 'FALSE',
        NAN = 'NaN'
    ),
    nodejs = dict(
        LANG = 'Node.js',
        WEB = 'https://plot.ly/nodejs/',
        OL = 'object',
        OL2D = 'array of arrays',
        UL = 'object',
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
        if language == 'python':  # N.B for python!
            name = (
                graph_obj.title()
                         .replace('_','')
                         .replace('axis','Axis')
                         .replace('bins','Bins')
                         .replace('2D','2d')
                         .replace('bar','Bar')
                         .replace('contour','Contour')
            )
            table[language][graph_obj] = name
        else:
            if graph_obj in graph_objs_info['trace']['graph_objs']:
                name = (
                    "trace {0} with 'type' set to '{1}'"
                ).format(table[language]['UL'], graph_obj)
                table[language][graph_obj] = name
            elif graph_obj in graph_objs_info['list-like']['graph_objs']:
                name = (
                    "{0} of one '{1}' {2} or more"
                ).format(table[language]['UL'], graph_obj, table[language]['OL'])
                table[language][graph_obj] = name
            else:
                name = (
                    "{1} {0} object with "
                ).format(graph_obj, table[language]['UL'])
                table[language][graph_obj] = name
