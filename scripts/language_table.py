# -------------------------------------------------------------------------------
#
# Set language-specific vocabulary here.
#
# * This table in imported in `meta.py` and `meta_shortcut.py`.
#
# * The vocabulary listed here is intended for object and key descriptions,
#   language-specific code snippets are set in the `Example` class of `meta.py`.
#
# Vocabulary:
#
# - LANG: Language's name (with correct cases e.g. MATLAB)
# - WEB: Online docs root URL 
# - OL: Name for ordered lists
# - UL: Name for unordered lists
# - OL2D: Name for ordered lists
# - NAN: Name in code for Not-a-Numbers
#
# ------------------------------------------------------------------------------

table = dict(
    python = dict(
        LANG = 'python',
        WEB = 'https://plot.ly/python/',
        OL = 'list or 1d numpy array',
        UL = 'dictionary',
        OL2D = 'list of lists or 2d numpy array',
        NAN = '`numpy.nan`'
    ),
    matlab = dict(
        LANG = 'MATLAB',
        WEB = 'https://plot.ly/matlab/',
        OL = 'array',
        UL = 'structure',
        NAN = '`NaN`'
    ),
    r = dict(
        LANG = 'R',
        OL = 'array',
        NAN = '`NaN`'
    ),
    nodejs = dict(
        LANG = 'Node.js',
    ),
    julia = dict(
        LANG = 'Julia',
    )
)
