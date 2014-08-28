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
# - NAN : Name in code for Not-a-Numbers
#
# ------------------------------------------------------------------------------

table = dict(
    python = dict(
        LANG = 'python',
        WEB = 'https://plot.ly/python/',
        OL = 'list or 1d numpy array',
        OL2D = 'list of lists or 2d numpy array',
        UL = 'dictionary',
        TRUE = 'True',
        FALSE = 'False',
        NAN = '`numpy.nan`',
        scatter = "Scatter"
    ),
    matlab = dict(
        LANG = 'MATLAB',
        WEB = 'https://plot.ly/matlab/',
        OL = 'array',
        OL2D = '2d array',
        UL = 'structure',
        TRUE = 'TRUE',
        FALSE = 'FALSE',
        NAN = '`NaN`',
        scatter = "trace type='scatter'"
    ),
    r = dict(
        LANG = 'R',
        WEB = 'https://plot.ly/r/',
        OL = 'array',
        NAN = '`NaN`'
    ),
    nodejs = dict(
        LANG = 'Node.js',
        WEB = 'https://plot.ly/nodejs/',
    ),
    julia = dict(
        LANG = 'Julia',
        WEB = 'https://plot.ly/julia/',
    )
)
