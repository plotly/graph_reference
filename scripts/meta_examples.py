
# -------------------------------------------------------------------------------
#
# Define short (code snippet) examples in Examples()
#
# * Meta examples are represented as class variables. 
#   They need to be retrieved using getattr(<instance-of-Examples>, <language>)
#
# -------------------------------------------------------------------------------

class MakeExamples(list):
    '''@Examples@'''

    def __init__(self):
        '''@examples@'''
        self.python = []
        self.matlab = []
        self.r = []
        self.nodejs = []
        self.julia = []

    def _for_all(self, _examples):
        '''@for_all@ -- set same example for all languages'''
        self.python = _examples
        self.matlab = _examples
        self.r = _examples
        self.nodejs = _examples
        self.julia = _examples

    def color(self):
        '''@color@'''
        self._for_all([
            "'green'", 
            "'rgb(0, 255, 0)'",
            "'rgba(0, 255, 0, 0.3)'",
            "'hsl(120,100%,50%)'",
            "'hsla(120,100%,50%,0.3)'",
            "'#434F1D'"
        ])
        return self
    
    def colorscale(self):
        '''@colorscale@'''
        self.python = [
            "'Greys'", 
            "[[0, 'rgb(0,0,0)'], " 
            "[0.5, 'rgb(65, 182, 196)'], "
            "[1, 'rgb(255,255,255)']]"
        ]
        self.matlab = [
            "'Greys'", 
            "{ { {0, 'rgb(0,0,0)'}, " 
            "{0.5, 'rgb(65, 182, 196)'}, "
            "{1, 'rgb(255,255,255)'} } }"
        ]
        self.r = [
            "'Greys'", 
            "list(c(0, 'rgb(0,0,0)'), " 
            "list(0.5, 'rgb(65, 182, 196)'), "
            "list(1, 'rgb(255,255,255)'))"
        ]
        self.nodejs = [
            "'Greys'", 
            "[[0, 'rgb(0,0,0)'], " 
            "[0.5, 'rgb(65, 182, 196)'], "
            "[1, 'rgb(255,255,255)']]"
        ]
        self.julia = [
            "'Greys'", 
            "{[0, 'rgb(0,0,0)'], " 
            "[0.5, 'rgb(65, 182, 196)'], "
            "[1, 'rgb(255,255,255)']}"
        ]
        return self

    def range_xy(self):
        '''@range_xy@'''
        self.python = [
            "[-13, 20]",
            "[0, 1]"
        ]
        self.matlab = [
            "[-13, 20]",
            "[0, 1]"
        ]
        self.r = [
            "c(-13, 20)",
            "c(0, 1)"
        ]
        self.nodejs = [
            "[-13, 20]",
            "[0, 1]"
        ]
        self.julia = [
            "[-13, 20]",
            "[0, 1]"
        ]
        return self

    def range_polar(self):
        '''@range_polar@'''
        self.python = [
            "[0, 180]",
            "[0, 6.2831]"
        ]
        self.matlab = [
            "[0, 180]",
            "[0, 6.2831]"
        ]
        self.r = [
            "c(0, 180)",
            "c(0, 6.2831)"
        ]
        self.nodejs = [
            "[0, 180]",
            "[0, 6.2831]"
        ]
        self.julia = [
            "[0, 180]",
            "[0, 6.2831]"
        ]
        return self

    def domain(self):
        '''@domain@'''
        self.python = [
            "[0, 0.4]",
            "[0.6, 1]"
        ]
        self.matlab = [
            "[0, 0.4]",
            "[0.6, 1]"
        ]
        self.r = [
            "c(0, 0.4)",
            "c(0.6, 1)"
        ]
        self.nodejs = [
            "[0, 0.4]",
            "[0.6, 1]"
        ]
        self.julia = [
            "[0, 0.4]",
            "[0.6, 1]"
        ]
        return self

    def text(self):
        '''@text@'''
        self._for_all([
           "'regular text'", 
           "'an annotation<br>spanning two lines'",
           "'<b>bold text</b>'", 
           "'<a href='https://plot.ly/'>a link to plot.ly</a>'"
        ])
        return self

    def area(self):  # TODO!
        '''@area@'''
        self.python = []
        return self

    def bar(self):
        '''@bar@'''
        self.python = [
            "py.plot([Bar(x=['yesterday', 'today', 'tomorrow'], y=[5, 4, 10])])"
        ]
        return self

    def box(self):
        '''@box@'''
        self.python = [
            "py.plot([Box(name='boxy', y=[1,3,9,2,4,2,3,5,2])])"
        ]
        return self

    def contour(self):
        '''@contour@'''
        self.python = [
            "z = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]",
            "y = ['a', 'b', 'c']",
            "x = [1, 2, 3, 4, 5]"
            "py.plot([Contour(z=z, x=x, y=y)])"
        ]
        return self
    
    def heatmap(self):
        '''@heatmap'''
        self.python = [
            "z = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]",
            "y = ['a', 'b', 'c']",
            "x = [1, 2, 3, 4, 5]"
            "py.plot([Contour(z=z, x=x, y=y)])"
        ]
        return self

    def histogram(self):
        '''@histogram@'''
        self.python = [
            "py.plot([Histogram(x=[1,1,2,3,2,3,3])]) # bins along x-axis",
            "py.plot([Histogram(y=[1,1,2,3,2,3,3])]) # bins along y-axis",
        ]
        return self

    def histogram2d(self):
        '''@histogram2d@'''
        self.python = [
            "import numpy as np",
            "x = np.random.randn(500)",
            "y = np.random.randn(500)+1",
            "py.iplot([Histogram2d(x=x, y=y)])"
        ]
        return self

    def histogram2dcontour(self):
        '''@histogram2dcontour@'''
        self.python = [
            "import numpy as np",
            "x = np.random.randn(500)",
            "y = np.random.randn(500)+1",
            "py.iplot([Histogram2dContour(x=x, y=y)])"
        ]
        return self

    def scatter(self):
        '''@scatter@'''
        self.python = [
            "py.plot([Scatter(name='tacters', x=[1,4,2,3], y=[1,6,2,1])])"
        ]
        return self

    def angularaxis(self): # TODO!
        '''@angularaxis@'''
        self.python = []
        return self

    def radialaxis(self): # TODO!
        '''@radialaxis@'''
        self.python = []
        return self
    
    def annotation(self):
        '''@annotation@'''
        self.python = [
            "annotation = Annotation(\n"
            "     text='what i want this to say is:<br>THIS!',\n"
            "     x=0,\n"
            "     y=0,\n"
            "     xref='paper',\n"
            "     yref='paper,\n"
            "     yanchor='bottom',\n"
            "     xanchor='left')"
        ]
        return self

    def colorbar(self):
        '''@colorbar@'''
        self.python = [] # TODO!
        return self

    def contours(self):
        '''@contours@'''
        self.python = [] # TODO!
        return self
        
    def error_y(self):
        '''@error_y@'''
        self.python = [] # TODO!
        return self

    def error_x(self):
        '''@error_x@'''
        self.python = [] # TODO!
        return self

    def figure(self):
        '''@figure@'''
        self.python = [] # TODO!
        return self

    def font(self):
        '''@font@'''
        self.python = [] # TODO!
        return self

    def layout(self):
        '''@layout@'''
        self.python = [] # TODO!
        return self
        
    def legend(self):
        '''@legend@'''
        self.python = [] # TODO!
        return self

    def line(self):
        '''@line@'''
        self.python = [] # TODO!
        return self

    def marker(self):
        '''@marker@'''
        self.python = [] # TODO!
        return self

    def margin(self):
        '''@margin@'''
        self.python = [] # TODO!
        return self

    def stream(self):
        '''@stream@'''
        self.python = [] # TODO!
        return self

    def xaxis(self):
        '''@xaxis@'''
        self.python = [] # TODO!
        return self

    def xbins(self):
        '''@xbins@'''
        self.python = [] # TODO!
        return self

    def yaxis(self):
        '''@yaxis@'''
        self.python = [] # TODO!
        return self

    def ybins(self):
        '''@ybins@'''
        self.python = [] # TODO!
        return self

    def data(self):
        '''@data@'''
        self.python = [
            "Data([Bar(x=[1,2], y=[4,5]), Scatter(x=[1,2],y[2,3])])"

        ]
        return self

    def annotations(self):
        '''@annotations@'''
        self.python = [
            "Annotations([Annotation(x=0, y=1, text='look!'),\n"
            "    Annotation(x=1, y=2, text='See the data at the URL below, showarrow=False),\n"
            "    Annotation(x=10, y=20, text='this point is an outlier)])"
        ]
        return self

# -------------------------------------------------------------------------------
