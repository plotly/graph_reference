
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
        self.python = ['']
        self.matlab = ['']
        self.r = ['']
        self.nodejs = ['']
        self.julia = ['']

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
            "'hsla(120,100%,50%,0.3)'"
        ])
        return self
    
    def colorscale(self):
        '''@colorscale@'''
        self.python = [
            "'Greys'", 
            "[[0, 'rgb(0,0,0)'],\n" 
            "[0.5, 'rgb(65, 182, 196)'],\n"
            "[1, 'rgb(255,255,255)']]"
        ]
        return self

    def range_xy(self):
        '''@range_xy@'''
        self.python = [
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
        return self

    def domain(self):
        '''@domain@'''
        self.python = [
            "[0,0.4], [0.6, 1]"
        ]
        return self

    def Area(self):  # TODO!
        '''@Area@'''
        self.python = ['']
        return self

    def Bar(self):
        '''@Bar@'''
        self.python = [
            "py.plot([Bar(x=['yesterday', 'today', 'tomorrow'], y=[5, 4, 10])])"
        ]
        return self

    def Box(self):
        '''@Box@'''
        self.python = [
            "py.plot([Box(name='boxy', y=[1,3,9,2,4,2,3,5,2])])"
        ]
        return self

    def Contour(self):
        self.python = [
            "z = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]",
            "y = ['a', 'b', 'c']",
            "x = [1, 2, 3, 4, 5]"
            "py.plot([Contour(z=z, x=x, y=y)])"
        ]
        return self
    
    def Heatmap(self):
        self.python = [
            "z = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]]",
            "y = ['a', 'b', 'c']",
            "x = [1, 2, 3, 4, 5]"
            "py.plot([Contour(z=z, x=x, y=y)])"
        ]
        return self

    def Histogram(self):
        self.python = [
            "py.plot([Histogram(x=[1,1,2,3,2,3,3])]) # along bins along x-axis",
            "py.plot([Histogram(y=[1,1,2,3,2,3,3])]) # along bins along y-axis",
        ]
        return self

    def Histogram2d(self):
        self.python = [
            "import numpy as np",
            "x = np.random.randn(500)",
            "y = np.random.randn(500)+1",
            "py.iplot([Histogram2d(x=x, y=y)])"
        ]
        return self

    def Histogram2dContour(self):
        self.python = [
            "import numpy as np",
            "x = np.random.randn(500)",
            "y = np.random.randn(500)+1",
            "py.iplot([Histogram2dContour(x=x, y=y)])"
        ]
        return self

    def Scatter(self):
        self.python = [
            "py.plot([Scatter(name='tacters', x=[1,4,2,3], y=[1,6,2,1])])"
        ]
        return self

    def AngularAxis(self): # TODO!
        self.python = ['']
        return self

    def RadialAxis(self): # TODO!
        self.python = ['']
        return self
    
    def Annotation(self):
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

    def ColorBar(self):
        self.python = [''] # TODO!
        return self

    def Contours(self):
        self.python = [''] # TODO!
        return self
        
    def ErrorY(self):
        self.python = [''] # TODO!
        return self

    def ErrorX(self):
        self.python = [''] # TODO!
        return self

    def Figure(self):
        self.python = [''] # TODO!
        return self

    def Font(self):
        self.python = [''] # TODO!
        return self

    def Layout(self):
        self.python = [''] # TODO!
        return self
        
    def Legend(self):
        self.python = [''] # TODO!
        return self

    def Line(self):
        self.python = [''] # TODO!
        return self

    def Marker(self):
        self.python = [''] # TODO!
        return self

    def Margin(self):
        self.python = [''] # TODO!
        return self

    def Stream(self):
        self.python = [''] # TODO!
        return self

    def XAxis(self):
        self.python = [''] # TODO!
        return self

    def XBins(self):
        self.python = [''] # TODO!
        return self

    def YAxis(self):
        self.python = [''] # TODO!
        return self

    def YBins(self):
        self.python = [''] # TODO!
        return self

    def Data(self):
        self.python = [
            "Data([Bar(x=[1,2], y=[4,5]), Scatter(x=[1,2],y[2,3])])"
        ]
        return self

    def Annotations(self):
        self.python = [''] # TODO!
        return self

# -------------------------------------------------------------------------------
