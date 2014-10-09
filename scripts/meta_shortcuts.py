from meta_examples import MakeExamples

# -------------------------------------------------------------------------------
#
# A set of shortcuts used in meta.MakeMeta()
#
# - Define shortcuts for value types in ValTypes()
# - Define required conditions in RequiredCond()
# - Define shortcuts to keymeta field in Make()
#
# -------------------------------------------------------------------------------

class ValTypes(str):
    '''@ValTypes@ -- Inventory of value types
    '''
    
    def __init__(self):
        '''@val_types@'''
        self = ''

    def bool(self):
        return "a boolean: {TRUE} | {FALSE}"
    
    def string(self):
        return "a string"

    def color(self):
        return "a string describing color"

    def number(self, lt=None, le=None, gt=None, ge=None, is_list=False):
        if any((all((lt is not None, le is not None)),
                all((gt is not None, ge is not None)))):
            raise Exception("over-constrained number definition")
        if [lt, le, gt, ge] == [None, None, None, None]:
            out = "number"
        elif lt is not None and ([ge, gt] == [None, None]):
            out = "number: x < {lt}".format(lt=lt)
        elif le is not None and ([ge, gt] == [None, None]):
            out = "number: x <= {le}".format(le=le)
        elif gt is not None and ([le, lt] == [None, None]):
            out = "number: x > {gt}".format(gt=gt)
        elif ge is not None and ([le, lt] == [None, None]):
            out = "number: x >= {ge}".format(ge=ge)
        elif (lt is not None) and (gt is not None):
            out = "number: x in ({gt}, {lt})".format(gt=gt, lt=lt)
        elif (lt is not None) and (ge is not None):
            out = "number: x in [{ge}, {lt})".format(ge=ge, lt=lt)
        elif (le is not None) and (gt is not None):
            out = "number: x in ({gt}, {le}]".format(gt=gt, le=le)
        elif (le is not None) and (ge is not None):
            out = "number: x in [{ge}, {le}]".format(le=le, ge=ge)
        if is_list:
            return out+", or list of these numbers"
        else:
            return out

    def number_array(self):
        return "{OL} of numbers"

    def data_array(self):
        return "{OL} of numbers, strings, datetimes"

    def string_array(self):
        return "{OL} of strings"

    def color_array(self):
        return "{OL} of string describing color"

    def matrix(self):
        return "{OL2D} of numbers"

    def object(self):
        return "{ULlike}"

    def object_list(self):
        return "{OLlike} of one or several {ULlike}"

# -------------------------------------------------------------------------------

class RequiredCond(str):  
    '''@RequiredCond@ -- Inventory of required conditions
    '''

    def __init__(self):
        '''@required_cond@'''
        self = ''

    def keys(self, keys):
        '''@required_cond.keys@ -- conditions involving keys
        '''
        if type(keys)==str:
            to_be = 'is'
        if all([type(keys)==list, len(keys)==1]):
            to_be = 'is'
            keys = keys[0]
        elif type(keys)==list:
            keys=','.join(keys[0:-1]) + ' and ' + keys[-1]
            to_be = 'are'
        return " when {keys} {to_be} unset".format(keys=keys,to_be=to_be)
    
    def plottype(self, plottype):
        '''@required_cond.plottype@ -- conditions involving plot type
        '''
        return " when making a {plottype}".format(plottype=plottype)

# -------------------------------------------------------------------------------

class Make(dict):
    '''@Make@ -- Inventory of meta generators for repeated keys
    '''

    def __init__(self):
        '''@make@'''
        self = dict()
        global val_types        # N.B no need to type self.val_types(...)
        val_types = ValTypes()   
        global required_cond
        required_cond = RequiredCond()

    def _output(self,_required, _key_type, _val_types, _description, **kwargs):
        '''@output@ -- Format the keys' values into a dictionary
        Outputs a dictionary of key-value pairs, given the keys.
        (pos. arg. 1) _required: value of 'required' key
        (pos. arg. 2) _key_type: value of 'key_type' key
        (pos. arg. 3) _val_types: value of 'val_types' key
        (pos. arg. 4) _description: value of 'description' key
        (keyword args) kwargs: dictionary of additional key-value pairs
        '''
        _dict = dict(
            required= _required,
            key_type= _key_type,
            val_types= _val_types,
            description= _description)
        if len(kwargs):
            for k, v in kwargs.iteritems():
                _dict[k] = v
        return _dict

    def x(self,obj):
        '''@x@'''
        _required = dict(
            scatter=required_cond.keys(["'y'","'r'","'t'"]),
            bar=required_cond.keys(["'y'"]),
            histogram=required_cond.keys(["'y'"]),
            box=False,
            heatmap=False,
            contour=False,
            histogram2d=True,
            histogram2dcontour=True,
            scatter3d=True,
            surface=False
        )
        _key_type = 'data'
        _val_types = val_types.data_array()
        _description = dict(
            scatter=(
                "Sets the x coordinates of the points of this scatter trace. "
                "If 'x' is linked to {a_OL} of strings, "
                "then the x coordinates are integers, 0, 1, 2, 3, ..., labeled "
                "on the x-axis by the {OL} of strings linked to 'x'."
            ),
            bar=(
                "Sets the x coordinates of the bars. "
                "If 'x' is linked to {a_OL} of strings, "
                "then the x coordinates are integers, 0, 1, 2, 3, ..., labeled "
                "on the x-axis by the {OL} of strings linked to 'x'. "
                "If 'y' is not set, the bars are plotted horizontally, "
                "with their length determined by the {OL} linked to 'x'."
            ),
            histogram=(
                "Sets the data sample to be binned (done by Plotly) on the x-axis "
                "and plotted as vertical bars."
            ),
            box=(
                "Usually, you do not need to set this value as "
                "plotly will handle box locations for you. However "
                "this allows you to have fine control over the "
                "location data for the box. Unlike making a bar, "
                "a box plot is made of many y values. Therefore, "
                "to give location data to the values you place in "
                "'y', the length of 'x' must equal the length of 'y'. "
                "when making multiple box plots, you can concatenate "
                "the data sets for each box into a single 'y' array. "
                "then, the entries in 'x' define which box plot each "
                "entry in 'y' belongs to. When making a single box "
                "plot, you must set each entry in 'x' to the same "
                "value, see 'x0' for a more practical way to handle "
                "this case. If you don't include 'x', the box will "
                "simply be assigned a location."
            ),
            heatmap=(
                "Sets the horizontal coordinates "
                "referring to the columns of the {OL2D} linked to 'z'. "
                "if strings, the x-labels are spaced evenly. "
                "If the dimensions of the {OL2D} linked to 'z' are (n x m), "
                "the length of the 'x' array should equal m."
            ),
            histogram2d=(
                "Sets the data sample to be binned on the x-axis and "
                "whose distribution (computed by Plotly) will correspond "
                "to the x-coordinates of this 2D histogram trace."
           ),
           scatter3d=(
               "Sets the x coordinates of the points of this 3D scatter trace. "
               "If 'x' is linked to {a_OL} of strings, "
               "then the x coordinates are integers, 0, 1, 2, 3, ..., labeled "
               "on the x-axis by the {OL} of strings linked to 'x'."
           ),
        )
        _description['contour'] =  _description['heatmap']
        _description['histogram2dcontour'] =  _description['histogram2d']
        _description['surface'] = _description['heatmap']
        _streamable=True
        return self._output(_required[obj],_key_type,_val_types,_description[obj],
                            streamable=_streamable)
    
    def y(self,obj):
       '''@y@'''
       _required = dict(
            scatter=required_cond.keys(["'x'","'r'","'t'"]),
            bar=required_cond.keys(["'x'"]),
            histogram=required_cond.keys(["'x'"]),
            box=True,
            heatmap=False,
            contour=False,
            histogram2d=True,
            histogram2dcontour=True,
            scatter3d=True,
            surface=False
        )
       _key_type = 'data'
       _val_types = val_types.data_array()
       _description = dict(
           scatter=(
               "Sets the y coordinates of the points of this scatter trace. "
               "If 'y' is linked to {a_OL} of strings, "
               "then the y coordinates are integers, 0, 1, 2, 3, ..., labeled "
               "on the y-axis by the {OL} of strings linked to 'y'."
           ),
           bar=(
               "Sets the y coordinates of the bars. "
               "If 'y' is linked to {a_OL} of strings, "
               "then the y coordinates are integers, 0, 1, 2, 3, ..., labeled "
               "on the y-axis by the {OL} of strings linked to 'y'. "
               "If 'x' is not set, the bars are plotted vertically, "
               "with their length determined by the {OL} linked to 'y'."
           ),
           histogram=(
               "Sets the data sample to be binned (done by Plotly) on the y-axis "
               "and plotted as horizontal bars."
           ),
           box=(
               "This array is used to define an individual "
               "box plot, or, a concatenation of multiple box plots. "
               "Statistics from these numbers define the bounds of "
               "the box, the length of the whiskers, etc. For "
               "details on defining multiple boxes with locations "
               "see 'x'. Each box spans from the first quartile to the third. "
               "The second quartile is marked by a line inside the box. "
               "By default, the whiskers are correspond to box' edges "
               "+/- 1.5 times "
               "the interquartile range. See also 'boxpoints' for more info"
           ),
           heatmap=(
               "Sets the vertical coordinates "
               "referring to the rows of the {OL2D} linked to 'z'. "
               "If strings, the y-labels are spaced evenly. "
               "If the dimensions of the {OL2D} linked to 'z' are (n x m), "
               "the length of the 'y' array should equal n."
           ),
           histogram2d=(
               "Sets the data sample to be binned on the y-axis and "
               "whose distribution (computed by Plotly) will correspond "
               "to the y-coordinates of this 2D histogram trace."
          ),
          scatter3d=(
              "Sets the y coordinates of the points of this 3D scatter trace. "
              "If 'y' is linked to {a_OL} of strings, "
              "then the y coordinates are integers, 0, 1, 2, 3, ..., labeled "
              "on the y-axis by the {OL} of strings linked to 'y'."
          ),
       )
       _description['contour'] = _description['heatmap']
       _description['histogram2dcontour'] = _description['histogram2d']
       _description['surface'] = _description['heatmap']
       _streamable = True
       return self._output(_required[obj],_key_type,_val_types,_description[obj],
                          streamable=_streamable)
    
    def z(self,obj):
        '''@z@'''
        _required = True
        _key_type = 'data'
        _val_types = val_types.matrix()
        if (obj=='scatter3d' or obj=='surface'):
            _val_types = val_types.data_array()
        _description = dict(
            heatmap=(
                "Sets the data that describes the heatmap mapping. "
                "Say the dimensions of the {OL2D} linked to 'z' has "
                "n rows and m columns then the resulting heatmap will show "
                "n partitions along the y-axis and m partitions along the "
                "x-axis. Therefore, the ith row/ jth column cell in the "
                "{OL2D} linked to 'z' is mapped to "
                "the ith partition of the y-axis (starting from the bottom "
                "of the plot) and the jth partition of the x-axis "
                "(starting from the left of the plot). "
            ),
            scatter3d=(
                "Sets the z coordinates of the points of this scatter trace. "
                "If 'z' is linked to {a_OL} of strings, "
                "then the z coordinates are integers, 0, 1, 2, 3, ..., labeled "
                "on the z-axis by the {OL} of strings linked to 'z'."
            ),
            surface=(
                "Sets the surface coordinates. "
                "Say the dimensions of the {OL2D} linked to 'z' has "
                "n rows and m columns then the resulting contour will have "
                "n coordinates along the y-axis and m coordinates along the "
                "x-axis. Therefore, the ith row/ jth column cell in the "
                "{OL2D} linked to 'z' is mapped to "
                "the ith partition of the y-axis "
                "and the jth partition of the x-axis "
            )
        )
        _description['contour'] = _description['heatmap'].replace('heatmap',
                                                                  'contour map')
        _streamable=True
        return self._output(_required,_key_type,_val_types,_description[obj],
                            streamable=_streamable)
    
    def r(self,obj):
        '''@r@'''
        _required=dict(
            scatter=required_cond.plottype("Polar Chart"),
            bar=required_cond.plottype("Polar Chart"),
            area=True
        )
        _key_type='data'
        _val_types=val_types.number_array() # Q? Should this support string too?
        _description=dict(  
            scatter=(
                "For Polar charts only. "
                "Sets the radial coordinates of the points in this "
                "polar scatter trace about the origin."
            ),
            bar=(
                "For Polar charts only. "
                "Sets the radial coordinates of the bars in this polar bar trace "
                "about the original; that is, the radial extent of each bar."
            ),
            area=(
                "Sets the radial coordinates of the circle sectors in this "
                "polar area trace about the origin; that is, the radial extent of "
                "each circle sector."
           )
        )
        _streamable=True
        return self._output(_required[obj],_key_type,_val_types,_description[obj],
                            streamable=_streamable)
    
    def t(self,obj):
        '''@t@'''
        _required=dict(
            scatter=required_cond.plottype("Polar Chart"),
            bar=required_cond.plottype("Polar Chart"),
            area=True
        )
        _key_type='data'
        _val_types=val_types.data_array()
        _description=dict(
            scatter=(
                "For Polar charts only. "
                "Sets the angular coordinates of the points in this "
                "polar scatter trace."
            ),
            bar=(
                "For Polar charts only. "
                "Sets the angular coordinates of the bars "
                "in this polar bar trace."
            ),
            area=(
                "Sets the angular coordinates of the circle sectors in this "
                "polar area trace. There are as many sectors as coordinates "
                "linked to 't' and 'r'. Each sector is drawn about the "
                "coordinates linked to 't', where they spanned symmetrically "
                "in both the positive and negative angular directions. "
                "The angular extent of each sector is equal to the angular range "
                "(360 degree by default) divided by the number of sectors. "
                "Note that the sectors are drawn in order; coordinates at the end "
                "of the array may overlay the coordinates at the start."
           )
        )
        for k in _description.keys():
            _description[k]+=(
                " By default, the angular coordinates "
                "are in degrees (0 to 360) where the angles "
                "are measured clockwise about the right-hand "
                "side of the origin. To change this "
                "behavior, modify 'range' in 'angularaxis' "
                "or/and 'direction' in 'layout'. "
                "If 't' is linked to {a_OL} of "
                "strings, then the angular coordinates are "
                "0, 360\N, 2*360/N, ... where N is the "
                "number of coordinates given labeled by the "
                "{OL} of strings linked to 't'."
            )  
        _streamable=True
        return self._output(_required[obj],_key_type,_val_types,_description[obj],
                            streamable=_streamable)
    
    def x0y0(self,obj,x_or_y=False):
        '''@x0y0@ | @x0@ | @y0@'''

        S={'x':['x',], 'y':['y',], False:['',]}
        s=S[x_or_y]
    
        _required=False
        _key_type='plot_info'  
        _val_types=val_types.number()
        _description=dict( # TODO Add scatter?
            box=(
                "The location of this box. When 'y' defines a single "
                "box, 'x0' can be used to set where this box is "
                "centered on the x-axis. If many boxes are set to "
                "appear at the same 'x0' location, they will form a "
                "box group."
            ),
            heatmap=(
                "The location of the first coordinate of the {S0}-axis. "
                "Use with 'd{S0}' an alternative to an '{S0}' {{OL}}. "
                "Has no effect if '{S0}' is set."
            ).format(S0=s[0])
        )
        _description['contour']= _description['heatmap']
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def dxdy(self,obj,x_or_y=False):
        '''@dxdy@ | @dx@ | @dy@'''
        S={'x':['x',], 'y':['y',], False:['',]}
        s=S[x_or_y]
    
        _required=False
        _key_type='plot_info'  
        _val_types=val_types.number()
        _description=dict( # TODO Add scatter?
            heatmap=(
                "Spacing between {S0}-axis coordinates. "
                "Use with '{S0}0' an alternative to an '{S0}' {{OL}}. "
                "Has no effect if '{S0}' is set."
            ).format(S0=s[0]),
        )
        _description['contour']= _description['heatmap']
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def xytype(self,obj,x_or_y):
        '''@xytype@ | @xtype@ | @ytype@'''
        S={'x':['x','horizontal'], 'y':['y','vertical'], False:['',]}
        s=S[x_or_y]
    
        _required=False
        _key_type='plot_info'    
        _val_types="'array' | 'scaled'"
        _description=dict(
            heatmap=(
                "If set to 'scaled' and '{S0}' is linked to {{a_OL}}, "
                "then the {S1} labels are scaled to {{a_OL}} "
                "of integers of unit step "
                "starting from 0."
           ).format(S0=s[0],S1=s[1])
        )
        _description['contour']= _description['heatmap']
        return self._output(_required,_key_type,_val_types,_description[obj])
    

    def text(self, obj):
        '''@text@'''
        S = '(x,y,z)' if obj=='scatter3d' else '(x,y)'
        _required=False
        _key_type='data'
        _val_types=val_types.string_array()
        _description=dict(
            scatter=(
                "The text elements associated with each {S} pair in "
                "this scatter trace. If the scatter 'mode' does not "
                "include 'text' then text elements will appear on hover only. "
                "In contrast, if 'text' is included in 'mode', "
                "the entries in 'text' "
                "will be rendered on the plot at the locations "
                "specified in part by their corresponding {S} coordinate pair "
                "and the 'textposition' key."
            ).format(S=S),
            bar=(
                "The text elements associated with each bar in this trace. "
                "The entries in 'text' will appear on hover only, in a text "
                "box located at the top of each bar."
            )
        )
        _description['histogram']=_description['bar']
        _description['scatter3d']=_description['scatter']
        _streamable=True
        return self._output(_required,_key_type,_val_types,_description[obj],
                            streamable=_streamable)

    
    def error(self, obj, which_axis):
        '''@error@ | @error_y@ | @error_x@'''
        S = {'x':['horizontal','x'],
             'y':['vertical','y'],
             'z':['','z']}
        s = S[which_axis]
        _required = False
        _key_type = 'object'
        _val_types = val_types.object()
        _description = dict(
            scatter=(
                "Links {{a_ULlike}} describing "
                "the {S0} error bars (i.e. along the {S1}-axis) "
                "that can be drawn "
                "from the (x,y) coordinates of this scatter trace."
            ).format(S0=s[0],S1=s[1]),
            bar=(
                "Links {{a_ULlike}} describing the {S0} error bars "
                "(i.e. along the {S1}-axis) that can "
                "be drawn from bar tops."
           ).format(S0=s[0],S1=s[1]),
           scatter3d=(
               "Links {{a_ULlike}} describing "
               "the {S1}-axis error bars "
               "that can be drawn "
               "from the (x,y,z) coordinates of this 3D scatter trace."
           ).format(S1=s[1]),
        )
        _description['histogram']= _description['bar']
        _streamable=True
        return self._output(_required,_key_type,_val_types,_description[obj],
                            streamable=_streamable)
    
    def orientation(self,obj):
        '''@orientation@'''
        _required=False
        _key_type='plot_info' 
        _val_types="'v' | 'h'"
        _description=dict(
            bar=(
                "Sets the direction of the bars. "
                "If set to 'v', the length of each bar will run vertically. "
                "If set to 'h', the length of each bar will run horizontally"
            ),
            histogram=( # ARTIFACT
                "Web GUI Artifact. Histogram orientation is determined "
                "by which of 'x' or 'y' the data sample is linked to."
            )
        )
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def marker(self, obj):
        '''@marker@'''
        _required=False
        _key_type='object'
        _val_types=val_types.object()
        _description=dict(
            scatter=(
                "Links {a_ULlike} containing marker style "
                "parameters for this scatter trace. "
                "Has an effect only if 'mode' contains 'markers'."
            ),
            bar=(
                "Links {a_ULlike} containing marker style "
                "parameters for this bar trace, for example, "
                "the bars' fill color, border width and border color."
            ),
            box=(
                "Links {a_ULlike} containing marker style "
                "parameters for this the boxpoints of box trace. "
                "Has an effect only 'boxpoints' is set to 'outliers', "
                "'suspectedoutliers' or 'all'."
            ),
            area=(
                "Links {a_ULlike} containing marker style "
                "of the area sectors of this trace, for example the sector fill "
                "color and sector boundary line width and sector boundary color."
           ),
           scatter3d=(
                "Links {a_ULlike} containing marker style "
                "parameters for this 3D scatter trace. "
                "Has an effect only if 'mode' contains 'markers'."
           )
        )
        _description['histogram']= _description['bar']
        _streamable=True
        return self._output(_required,_key_type,_val_types,_description[obj],
                            streamable=_streamable)
    
    def line(self, obj):
        '''@line@'''
        _required=False
        _key_type='object'
        _val_types=val_types.object()
        _description=dict(
            scatter=(
                "Links {a_ULlike} containing line "
                "parameters for this scatter trace. "
                "Has an effect only if 'mode' contains 'lines'."
            ),
            box=(
                "Links {a_ULlike} containing line "
                "parameters for the border of this box trace "
                "(including the whiskers)."
            ),
            scatter3d=(
                "Links {a_ULlike} containing line "
                "parameters for this 3D scatter trace. "
                "Has an effect only if 'mode' contains 'lines'."
            ),
            contour=(
                "Links {a_ULlike} containing line "
                "parameters for contour lines of this contour trace "
                "(including line width, dash, color and smoothing level). "
                "Has no an effect if 'showlines' is set to {FALSE} in 'contours'."
            ),
            marker=(
                "Links {a_ULlike} containing line parameters for the line "
                "segments associated with this marker. "
                "For example, the line segments around each marker point "
                "in a scatter trace or the line segments around each bar in a "
                "bar trace."
           )
        )
        _description['histogram2dcontour']= _description['contour']
        _streamable=True
        return self._output(_required,_key_type,_val_types,_description[obj],
                            streamable=_streamable)
    

    def textposition(self, is_3d=False):
        '''@textposition@'''
        S = '(x,y,z)' if is_3d else '(x,y)'

        _required = False
        _key_type = 'style'
        _val_types = (
            "'top left' | 'top' (or 'top center')| 'top right' | "
            "'left' (or 'middle left') | '' (or 'middle center') |"
            "'right' (or 'middle right') |"
            "'bottom left' | 'bottom' (or 'bottom center') |"
            "'bottom right'"
        )
        _description = (
                    "Sets the position of the text elements "
                    "in the 'text' key with respect to the data points. "
                    "By default, the text elements are plotted directly "
                    "at the {S} coordinates."
        ).format(S=S)
        return self._output(_required, _key_type, _val_types, _description)


    def opacity(self, marker=False):
        '''@opacity@'''
        _required=False
        _key_type="style"
        if not marker:
            _val_types=val_types.number(ge=0, le=1)
            _description=(
                 "Sets the opacity, or transparency, "
                 "of the entire object, "
                 "also known as the alpha channel of colors. "
                 "If the object's color is given in terms of "
                 "'rgba' color "
                 "model, 'opacity' is redundant."
            )
        else:
            _val_types=val_types.number(ge=0, le=1, is_list=True)
            _description=(
                "Sets the opacity, or transparency "
                "also known as the alpha channel of colors) "
                "of the marker points. "
                "If the marker points' "
                "color is given in terms of 'rgba' "
                "color model, this does not need to be defined. "
                "If 'opacity' is linked to a list or an array "
                "of numbers, opacity values are mapped to "
                "individual marker points in the "
                "same order as in the 'x', 'y' (or 'z') {OL}."
            )
        return self._output(_required,_key_type,_val_types,_description)
    
    def textfont(self, obj):
        '''@textfont@'''
        _required=False
        _key_type='object'
        _val_types=val_types.object()
        _description=dict(
            scatter=(
                "Links {a_ULlike} describing the font style "
                "of this scatter trace's text elements. Has only "
                "an effect if 'mode' is set and includes 'text'."
            ),
            bar="Not currently supported, has no effect." # ARTIFACT
        )
        _description['histogram']= _description['bar']
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def font(self, obj):
        '''@font@'''
        _required=False
        _key_type='object'
        _val_types=val_types.object()
        _description=dict(
            legend=(
                "Links {a_ULlike} describing the font "
                "settings within the legend."
            ),
            annotation=(
                "Links {a_ULlike} describing the font "
                "settings within this annotation."
            ),
            layout=(
                "Links {a_ULlike} describing the global font "
                "settings for this figure (e.g. all axis titles and labels)."
            )
        )
        return self._output(_required,_key_type,_val_types,_description[obj])
    

    def name(self, is_3d=False):
        '''@name@'''
        _required = False
        _key_type = 'data'
        _val_types = val_types.string()
        if not is_3d:
            _description = (
                "The label associated with this trace. "
                "This name will appear in the legend, on hover and "
                "in the column header in the online spreadsheet."
            )
        else:
            _description = (
                "The label associated with this trace. "
                "This name will appear "
                "in the column header in the online spreadsheet."
            )
        return self._output(_required, _key_type, _val_types, _description)

    def mode(self, is_3d=False):
        '''@mode@'''
        S = '3D ' if is_3d else ''

        _required = False
        _key_type = 'style'
        _val_types = (
            "'lines' | 'markers' | 'text' | 'lines+markers' | "
            "'lines+text' | 'markers+text' | 'lines+markers+text'"
        )
        _description = (
            "Plotting mode for this {S}scatter trace. If the "
            "mode includes 'text' then the 'text' will appear at "
            "the (x,y) points, otherwise it will appear on "
            "hover."
        ).format(S=S)
        return self._output(_required, _key_type, _val_types, _description)
    
    def stream(self):
        '''@stream@'''
        return dict(
            required=False,
            key_type='object',
            val_types=val_types.object(),
            description=(
                "Links {a_ULlike} that initializes this trace as "
                "a writable-stream, for use with the streaming API."
            )
        )
    
    def visible(self):
        '''@visible@'''
        return dict(
            required=False,
            key_type='plot_info',
            val_types=val_types.bool(),
            description=(
                "Toggle whether or not this object will be "
                "visible on the rendered figure."
            )
        )
    
    def showlegend(self, trace=False, layout=False):
        '''@showlegend@'''
        _required=False
        _key_type='style'
        _val_types=val_types.bool()
        if trace:
            _description=(
                "Toggle whether or not this trace will be "
                "labeled in the legend."
            )
        elif layout:
            _description=(
                "Toggle whether or not the legend will "
                "be shown in this figure."
            )
        return self._output(_required,_key_type,_val_types,_description)
    

    def axis(self, which_axis, trace=False, layout=False, scene=False):
        '''@axis@ | @xaxis@ | @yaxis@'''
        S = {'x':['x','horizontal', '{xaxis}'],
             'y':['y','vertical' ,'{yaxis}'],
             'z':['z','','']}
        s = S[which_axis]
        _required = False
        if trace:
            _key_type = 'plot_info'
            _val_types = "'{S0}1' | '{S0}2' | '{S0}3' | etc.".format(S0=s[0])
            _description = (
                "This key determines which {S0}-axis "
                "the {S0}-coordinates of this trace will "
                "reference in the figure.  Values '{S0}1' "
                "and '{S0}' reference to '{S0}axis' in 'layout', "
                "'{S0}2' references to '{S0}axis2' in 'layout', and "
                "so on. Note that '{S0}1' will always refer to "
                "'{S0}axis' or '{S0}axis1' in 'layout', "
                "they are the same."
            ).format(S0=s[0])
        elif layout or scene:
            _key_type = 'object'
            _val_types = val_types.object()
            _description = (
                "Links {{a_ULlike}} describing an "
                "{S0}-axis (i.e. an {S1} axis). "
                "The first {S2} object can be entered into "
                "'layout' by linking it to '{S0}axis' OR "
                "'{S0}axis1', both keys are identical to Plotly.  "
                "To create references other than {S0}-axes, "
                "you need to define them in 'layout' "
                "using keys '{S0}axis2', '{S0}axis3' and so on. "
                "Note that in 3D plots, {S2} objects must be "
                "linked from a {{scene}} object."
            ).format(S0=s[0], S1=s[1], S2=s[2])
            if scene:
                _description = (
                    "Links {{a_ULlike}} describing an "
                    "{S0}-axis of a particular 3D scene."
                ).format(S0=s[0])
        return self._output(_required,_key_type,_val_types,_description)

    
    def type(self, trace):
        '''@type@'''
        _required=False
        _key_type='plot_info'
        _val_types="'{trace}'".format(trace=trace)
        _description=(
            "Plotly identifier for this data's trace type. "
        )
        return self._output(_required,_key_type,_val_types,_description)
    
    def histnorm(self):
        '''@histnorm@'''
        return dict(
            required=False,
            key_type='style',
            val_types=(
                "'' (or 'count') | 'percent' | 'probability' | 'density' | "
                "'probability density'"
            ),
            description=(
                "Sets the type of normalization for this histogram trace. "
                "If 'histnorm' is not specified, or set to '' "
                "(empty string) or set to 'count', the height of each bar "
                "displays the frequency of occurrence, i.e., "
                "the number of times this "
                "value was found in the corresponding bin. "
                "If set to 'percent', the height of each bar "
                "displays the percentage of total occurrences found within the "
                "corresponding bin. If set to 'probability', the height "
                "of each bar displays the probability that an event will "
                "fall into the corresponding bin. If set to 'density', "
                "the height of each bar is equal to the number of "
                "occurrences in a bin divided by the size of the bin "
                "interval such that summing the area of all bins will "
                "yield the total number of occurrences. If set to "
                "'probability density', the height of each bar "
                "is equal to the number of probability that an event will "
                "fall into the corresponding bin divided by the size of "
                "the bin interval such that summing the area of all bins "
                "will yield 1."
           )
        )
    
    def autobin(self, x_or_y):
        '''@autobin@ | @autobinx@ | @autobiny@'''
        _required=False
        _key_type='style'
        _val_types=val_types.bool()
        _description=(
            "Toggle whether or not the {0}-axis bin parameters "
            "are picked automatically by Plotly. "
            "Once 'autobin{0}' is set to {{FALSE}}, the {0}-axis "
            "bins parameters can be declared "
            "in '{0}bins' object."
        ).format(x_or_y)
        return self._output(_required,_key_type,_val_types,_description)
    
    def nbins(self, x_or_y):
        '''@nbins@ | @nbinsx@ | @nbinsy@'''
        _required=False
        _key_type='style'
        _val_types=val_types.number(gt=0)
        _description=(
            "Specifies the number of {0}-axis bins. "
            "No need to set 'autobin{0}' to {{FALSE}} "
            "for 'nbins{0}' to apply."
        ).format(x_or_y)
        return self._output(_required,_key_type,_val_types,_description)
    
    def bins(self, x_or_y):
        '''@bins@ | @xbins@ | @ybins@'''
        _required=False
        _key_type='object'
        _val_types=val_types.object()
        _description=(
            "Links {{a_ULlike}} defining the parameters "
            "of {0}-axis bins of this trace, for example, "
            "the bin width and the bins' starting and  "
            "ending value. Has an effect only if "
            "'autobin{0}' is set to {{FALSE}}."
        ).format(x_or_y)
        return self._output(_required,_key_type,_val_types,_description)
    
    def colorbar(self):
        '''@colorbar@'''
        return dict(
            required=False,
            key_type='object',
            val_types=val_types.object(),
            description=(
                "Links {a_ULlike} defining the parameters of "
                "the color bar associated with this trace "
                "(including its title, length and width)."
           )
        )
    
    def colorscale(self, z_or_color):
        '''@colorscale@'''
        S={'c': ['color', 'c'], 'z': ['z', 'z']}
        s = S[z_or_color]
        _required=False
        _key_type="style"
        _val_types=(
            "{OL} of value-color pairs | "
            "'Greys' | 'Greens' | 'Bluered' | 'Hot' | "
            "'Picnic' | 'Portland' | 'Jet' | 'RdBu' | 'Blackbody' | "
            "'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'"
        )
        _description=(
            "Sets and/or defines the color scale for this trace. "
            "The string values are pre-defined color "
            "scales. For custom color scales, define {{a_OL}}"
            "color-value pairs where, by default, the first "
            "element of the pair "
            "corresponds to a normalized value of {S0} from 0-1, "
            "i.e. ({S1}-{S1}min)/ ({S1}max-{S1}min), and the "
            "second element of pair corresponds to a color. "
            "Use with '{S1}auto', '{S1}min' and "
            "'{S1}max to fine-tune the map from '{S0}' to "
            "rendered colors."
        ).format(S0=s[0],S1=s[1])
        return self._output(_required,_key_type,_val_types,_description,
                            examples=MakeExamples.colorscale(MakeExamples()))
    
    def zcauto(self, z_or_c):
        '''@zcauto@ | @zauto@ | @cauto@'''
        _required=False
        _key_type='style'
        _val_types=val_types.bool()
        _description=(
            "Toggle whether or not the default values "
            "of '{}max' and '{}max' can be overwritten."
        ).format(z_or_c, z_or_c)
        return self._output(_required,_key_type,_val_types,_description)
    
    def zcminmax(self, min_or_max, z_or_color):
        '''@zcminmax@ | @zmin@ | @zmax@ | @cmin@ | @cmax@'''

        S={'min': 'minimum', 'max': 'maximum'}
        s=S[min_or_max]
    
        _required=False
        _key_type='style'
        _val_types=val_types.number()
        _description=(
            "Sets the {S0} '{z_or_color}' data value to be "
            "resolved by the color scale. "
            "Its default value is the {S0} of the "
            "'{z_or_color}' data values. "
            "This value will be used as the {S0} in the color scale "
            "normalization. For more info see 'colorscale'."
        ).format(S0=s,z_or_color=z_or_color)
        if z_or_color=='color':
            _description+=(
                " Has only an effect if 'color' is linked "
                "to {a_OL} nd 'colorscale' is set."
            )
        return self._output(_required,_key_type,_val_types,_description)
    
    def reversescale(self):
        '''@reversescale@'''
        return dict(
            required=False,
            key_type='style',
            val_types=val_types.bool(),
            description=(
                "Toggle whether or not the color scale will be reversed."
            )
        )
    
    def showscale(self):
        '''@showscale@'''
        return dict(
            required=False,
            key_type='style',
            val_types=val_types.bool(),
            description=(
                "Toggle whether or not the color scale associated with "
                "this mapping will be shown alongside the figure."
            )
        )
    
    def zsmooth(self):
        '''@zsmooth@'''
        return dict(
            required=False,
            key_type='style',
            val_types="{FALSE} | 'best' | 'fast'",
            description=( # TODO Describe the 2 algorithms
                "Choose between algorithms ('best' or 'fast') "
                "to smooth data linked to 'z'. "
                "The default value is {FALSE} "
                "corresponding to no smoothing."
            )
        )
    
    def autocontour(self):
        '''@autocontour@'''
        return dict(
            required=False,
            key_type='style',
            val_types=val_types.bool(),
            description=(
                "Toggle whether or not the contour parameters are picked "
                "automatically by Plotly. "
                "If {FALSE}, declare the contours parameters "
                "in 'contours'."
            )
        )
    
    def ncontours(self):
        '''@ncontours@'''
        return dict(
            required=False,
            key_type='style',
            val_types=val_types.number(gt=1),
            description=(
                "Specifies the number of contours lines "
                "in the contour plot. "
                "No need to set 'autocontour' to False for 'ncontours' "
                "to apply."
            )
        )
    
    def contours(self):
        '''@contours@'''
        return dict(
            required=False,
            key_type='object',
            val_types=val_types.object(),
            description=(
                "Links {a_ULlike} defining the parameters of "
                "the contours of this trace."
            )
        )
    
    def color(self,obj):
        '''@color@'''
        _required=False
        _key_type='style' #Q? 'data' in bubble charts (i.e. if linked to array)
        if obj=='marker':
            _val_types=val_types.color_array()  #Q? Add "or 'data_array'" 
        else:
            _val_types=val_types.color()
        _description=dict(
            marker=(
                "Sets the color of the face of the marker object. "
                "If 'color' is linked to {a_OL} of color strings, "
                "color values are mapped to individual marker points "
                "in the same order as in the data lists or arrays. "
                "To set the color of the marker's bordering line, "
                "use 'line' in 'marker'. "
                "The 'color' key can also accept {OL} of numbers, "
                "where each number is then mapped to a color using the "
                "color scale set in 'colorscale'."
            ),
            line=(
                "Sets the color of the line object. "
                "If linked within 'marker', sets the color of the marker's "
                "bordering line. "
                "If linked within, 'contours', sets the color of the "
                "contour lines."
            ),
            font=(
                "Sets the color of the text font. "
                "If linked directly from 'layout', set the "
                "color of the global font."
            ),
            error="Sets the color of the error bars."
        )
        _streamable=True
        return self._output(
            _required,_key_type,_val_types,_description[obj],
            streamable=_streamable,examples=MakeExamples.color(MakeExamples()))
    
    def fillcolor(self,obj):
        '''@fillcolor@'''
        _required=False
        _key_type='style'
        _val_types=val_types.color()
        _description=dict(
            scatter=(
                "Sets the color that will appear "
                "in the specified fill area (set in 'fill'). "
                "Has no effect if 'fill' is set to 'none'."
            ),
            box="Sets the color of the box interior."
        )
        return self._output(_required,_key_type,_val_types,_description[obj],
                            examples=MakeExamples.color(MakeExamples()))
    
    def outlinecolor(self,obj):
        '''@outlinecolor@'''
        _required=False
        _key_type='style'
        _val_types=val_types.color()
        _description=dict(
            font="For polar chart only. Sets the color of the text's outline.",
            colorbar="The color of the outline surrounding this colorbar."
        )
        return self._output(_required,_key_type,_val_types,_description[obj],
                            examples=MakeExamples.color(MakeExamples()))
    
    def bgcolor(self, obj):
        '''@bgcolor@'''
        _required = False
        _key_type = 'style'
        _val_types = val_types.color()
        _description = dict(
            legend="Sets the background (bg) color of the legend.",
            colorbar="Sets the background (bg) color of this colorbar.",
            annotation="Sets the background (bg) color of this annotation.",
            scene=(
                "Sets the background (bg) color of this scene "
                "(i.e. of the plotting surface and the margins)."
            )
        )
        return self._output(_required,_key_type,_val_types,_description[obj],
                            examples=MakeExamples.color(MakeExamples()))
    
    def bordercolor(self,obj):
        '''@bordercolor@'''
        _required=False
        _key_type='style'
        _val_types=val_types.color()
        _description=dict(
            legend="Sets the enclosing border color for the legend.",
            colorbar="Sets the color of the enclosing boarder of this colorbar.",
            annotation="The color of the enclosing boarder of this annotation."
        )
        return self._output(_required,_key_type,_val_types,_description[obj],
                            examples=MakeExamples.color(MakeExamples()))
    
    def size(self, obj, x_or_y=False):
        '''@size@'''
        S={'x': ['x',], 'y': ['y',], False:['',]}
        s=S[x_or_y]
    
        _required=False
        _key_type='style'   #Q? 'data' in bubble charts (i.e. if linked to array)
        if obj=='marker':
            _val_types=val_types.number(gt=0,is_list=True)
        else:
            _val_types=val_types.number(gt=0)
        _description=dict(
            marker=(
                "Sets the size of the markers (in pixels). "
                "If 'size' is linked to {a_OL} of numbers, "
                "size values are mapped to individual marker points "
                "in the same order as in the 'x', 'y (or 'z') {OL}. "
                "In this case, use 'size' in conjunction "
                "with 'sizeref' and 'sizemode' "
                "to fine-tune the map from the numbers linked to 'size' "
                "and the marker points' rendered sizes."
            ),
            font=(
                "Sets the size of text font. "
                "If linked directly from 'layout', set the "
                "size of the global font."
            ),
            bins=(
                "Sets the size (i.e. their width) of each "
                "{S0}-axis bin."
            ).format(S0=s[0]),
            contours="Sets the size of each contour level."
        )
        _streamable=True
        return self._output(_required,_key_type,_val_types,_description[obj],
                            streamable=_streamable)
    
    def startend(self, obj, start_or_end, x_or_y=False):
        '''@startend@ | @start@ | @end@'''
        S_se={'start':['first','starting'], 'end':['last','end']}
        s_se=S_se[start_or_end]
        S_xy={'x': ['x',], 'y': ['y',], False:['',]}
        s_xy=S_xy[x_or_y]
    
        _required=False
        _key_type='style'
        _val_types=val_types.number(gt=0)
        _description=dict(
            bins=(
                "Sets the {S_se1} point on the {S_xy0}-axis for the {S_se0} "
                "bin."
            ).format(S_se0=s_se[0],S_se1=s_se[1],S_xy0=s_xy[0]),
            contours=(
                "Sets the value of the {S_se0} "
                "contour level."
            ).format(S_se0=s_se[0])
        )
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def width(self, obj):
        '''@width@'''
        _required=False
        _key_type='style'
        _val_types=val_types.number(ge=0)
        _description = dict(
            line="Sets the width (in pixels) of the line segments in question.",
            error=(
                "Sets the width (in pixels) of the cross-bar at both ends of "
                "the error bars."
            )
        )
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def thickness(self, obj, which_axis=False):
        '''@thickness@'''
        _required = False
        _key_type = 'style'
        _val_types = val_types.number(ge=0)
        S = {'x':['x',], 'y':['y',], 'z':['z',], False:['',]}
        s = S[which_axis]
        _description = dict(
            error=(
                "Sets the line thickness of the {S0} error bars."
            ).format(S0=s[0]),
            colorbar="Sets the thickness of the line surrounding the colorbar."
        )
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def borderwidth(self, obj):
        '''@borderwidth@'''
        _required=False
        _key_type='style'
        _val_types=val_types.number(ge=0)
        _description=dict(
            legend="Sets the width of the border enclosing for the legend.",
            colorbar="Sets the width of the boarder enclosing this colorbar",
            annotation="Sets the width of the boarder enclosing this annotation"
        )
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def title(self, obj, x_or_y=False):
        '''@title@'''
        _required=False
        _key_type='plot_info'
        _val_types=val_types.string()
        _description=dict(
                axis="The {S}-axis title.".format(S=x_or_y),
                colorbar="The title of the colorbar.",
                layout="The title of the figure."
        )
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def titlefont(self, obj, x_or_y=False):
        '''@titlefont@'''
        _required=False
        _key_type='object'
        _val_types=val_types.object()
        _description=dict(
                axis=(
                    "Links {{a_ULlike}} describing the font "
                    "settings of the {S}-axis title."
                ).format(S=x_or_y),
                colorbar=(
                    "Links {a_ULlike} describing the font "
                    "settings of the colorbar title."
                ),
                layout=(
                    "Links {a_ULlike} describing the font "
                    "settings of the figure's title."
                )
        )
        return self._output(_required,_key_type,_val_types,_description[obj])
    
    def range(self, what_axis):
        '''@range@'''
        _required = False
        _key_type = 'style'
        _val_types = "number array of length 2" # TODO generalize ValType.number
        _description = (
            "Defines the start and end point of "
            "this {S} axis."
        ).format(S=what_axis)
        _examples = MakeExamples.range_xy(MakeExamples())
        if what_axis=='angular':
            _description+=(
                " By default, 'range' is set to [0,360]. "
                "Has no effect if 't' is linked to "
                "{a_OL} of strings."
        )
            _examples = MakeExamples.range_polar(MakeExamples())
        return self._output(_required,_key_type,_val_types,_description,
                            examples=_examples)
    
    def domain(self, what_axis):
        '''@domain@'''
        _required=False
        _key_type='plot_info'
        _val_types="number array of length 2"
        _description=(
            "Sets the domain of this {S} axis; "
            "that is, the available space "
            "for this {S} axis to live in. "
            "Domain coordinates are given in normalized "
            "coordinates with respect to the paper."
        ).format(S=what_axis)
        if what_axis in ['radial','angular']:
            _description=(
                "Polar chart subplots are not supported yet. "
                "This key has currently no effect."
            )
            return self._output(_required,_key_type,_val_types,_description)
        else:
            _examples = MakeExamples.domain(MakeExamples())
            return self._output(_required,_key_type,_val_types,_description,
                                examples=_examples)
    
    def showline(self, what_axis):
        '''@showline@'''
        _required=False
        _key_type='style'
        _val_types=val_types.bool()
        _description=(
            "Toggle whether or not the line bounding this "
            "{S} axis will "
            "be shown on the figure."
        ).format(S=what_axis)
        if what_axis=='angular':
            _description+=(
                " If 'showline' is set to {TRUE}, "
                "the bounding line starts from the origin and "
                "extends to the edge of radial axis."
            )
        return self._output(_required,_key_type,_val_types,_description)
    
    def autotick(self, axis_or_colorbar):
        '''@autotick@'''
        _required=False
        _key_type='style'
        _val_types=val_types.bool()
        _description=(
            "Toggle whether or not the {S} ticks parameters "
            "are picked automatically by Plotly. "
            "Once 'autotick' is set to {{FALSE}}, "
            "the {S} ticks parameters can be declared "
            "with 'ticks', 'tick0', 'dtick0' and other "
            "tick-related key in this {S} object."
        ).format(S=axis_or_colorbar)
        return self._output(_required,_key_type,_val_types,_description)
    
    def nticks(self, axis_or_colorbar):
        '''@nticks@'''
        _required=False
        _key_type='style'    
        _val_types=val_types.number(gt=0)
        _description=(
            "Sets the number of {S} ticks. "
            "No need to set 'autoticks' to {{FALSE}} "
            "for 'nticks' to apply."
        ).format(S=axis_or_colorbar)
        return self._output(_required,_key_type,_val_types,_description)
    
    def showticklabels(self, what_ticks):
        '''@showticklabels@'''
        _required=False
        _key_type='style'
        _val_types=val_types.bool()
        _description=(
            "Toggle whether or not the {} ticks "
            "will feature tick labels."
        ).format(what_ticks)
        return self._output(_required,_key_type,_val_types,_description)
    
    def xyref(self, x_or_y):
        '''@xyref@ | @xref@ | @yref@'''

        S={'x': ['x','left','right'], 'y':['y','bottom','top']}
        s=S[x_or_y]
    
        _required=False
        _key_type='plot_info'
        _val_types="'paper' | '{S0}1' | '{S0}2' | etc".format(S0=s[0])
        _description=(
            "Sets the {S0} coordinate system which this object "
            "refers to. If you reference an axis, e.g., "
            "'{S0}2', the object will move with pan-and-zoom "
            "to stay fixed to this point. If you reference "
            "the 'paper', it remains fixed regardless of "
            "pan-and-zoom. In other words, if set to 'paper', "
            "the '{S0}' location refers to the distance from "
            "the left side of the plotting area in normalized "
            "coordinates where 0 is '{S1}' and 1 is '{S2}'. "
            "If set to refer to an {S0}axis' , e.g., "
            "'{S0}1', '{S0}2', '{S0}3', etc., the "
            "'{S0}' location will refer to the location in "
            "terms of this axis."
        ).format(S0=s[0],S1=s[1],S2=s[2])
        return self._output(_required,_key_type,_val_types,_description)
    
    def xyanchor(self, obj, x_or_y):
        '''@xyanchor@ | @xanchor@ | @yanchor@'''

        S = {
            'x': ['x','left','right','horizontal'], 
            'y':['y','bottom','top','vertical']
        }
        s = S[x_or_y]
    
        _required = False
        _key_type = 'plot_info'
        _val_types = {
            'x':"'auto' | 'left' | 'center' | 'right'",
            'y':"'auto' | 'bottom' | 'middle' | 'top'"
        }
        _description = (
            "Sets the {S3} position anchor of this {obj}. "
            "That is, bind the position set with the '{S0}' key "
            "to the {val_types} of this {obj}."
        ).format(S0=s[0], S3=s[3], obj=obj, 
                 val_types=_val_types[x_or_y].replace("'auto' | ",'')).replace('|','or')
        if obj in ['legend','annotation']:
            _description += (
                " For example, if '{S0}' is set to 1, "
                "'{S0}ref' to 'paper', and '{S0}anchor' to '{S2}', "
                "the {S2}-most portion of this object will line "
                "up with the {S2}-most edge of the plotting area."
            ).format(S0=s[0], S2=s[2])
        return self._output(_required,_key_type,_val_types[x_or_y],_description)
    
    def xy_layout(self, obj, x_or_y):
        '''@xy_layout@ | @x_layout@ | @y_layout@'''
        _required = False
        _key_type = 'plot_info'
        _val_types = val_types.number()
        _description = (
            "Sets the '{x_or_y}' position of this {obj}."
        ).format(x_or_y=x_or_y, obj=obj)
        if obj in ['legend','annotation']:
            _description += (
                "Use in conjunction with '{x_or_y}ref' and "
                "'{x_or_y}anchor' to fine-tune the location of "
                "this {obj}."
            ).format(x_or_y=x_or_y, obj=obj)
        return self._output(_required,_key_type,_val_types,_description)
    
# -------------------------------------------------------------------------------
