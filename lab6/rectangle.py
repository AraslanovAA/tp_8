import figure_abstract
class rectangle(figure_abstract.figure):
    """class for calculate area of the rectangle"""
    def __init__(self, a, b):
        self.l = a
        self.B = b

    reckon = lambda self: self.l * self.l
    """return square of rectangle"""
    """
    def reckon(self):
        
        S = self.l*self.B
        return S
    """