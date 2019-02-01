import math
from typing import Any, Union
import figure_abstract

class circle(figure_abstract.figure):
    """class for calculate area of the circle"""
    def __init__(self, r):
        self.l = r

    reckon = lambda self: self.l * self.l * math.pi
    """return square of circle"""
    """
    def reckon(self) :
        
        S = self.l * self.l * math.pi
        return S
    """





