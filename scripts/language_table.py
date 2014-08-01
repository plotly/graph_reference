# -------------------------------------------------------------------------------
#
# Set language-specific vocabulary here.
#
# This table in imported in `meta.py` and `meta_shortcut.py`
#
# Vocabulary:
#
# - LANG: The language's name (with correct cases e.g. MATLAB)
# - OLIST: Name for ordered lists
# - ULIST: Name for unordered lists
# - NAN: Name in code for Not-a-Numbers
# -
#
# ------------------------------------------------------------------------------

table = dict(
    python = dict(
        LANG = 'python',
        OLIST = 'list or numpy array',
        NAN = '`numpy.nan`'
    ),
    matlab = dict(
        LANG = 'MATLAB',
        OLIST = 'array',
        NAN = '`NaN`'
    ),
)
