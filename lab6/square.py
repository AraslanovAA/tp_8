import figure_abstract
class square(figure_abstract.figure):
    """class for calculate area of the square"""
    def __init__(self, a):
        self.l =a

    def reckon(self):
        """return area of square"""
        S = self.l*self.l
        return  S