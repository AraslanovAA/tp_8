import xmlrpc.server
import  math

import xmlrpc.server
from abc import ABCMeta, abstractmethod

server = xmlrpc.server.SimpleXMLRPCServer(('localhost',8000))
class figure():
    """parent class"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def reckon(self):
        """return square"""


class rectangle(figure):
    """class for calculate area of the rectangle"""

    def __init__(self, a, b):
        self.l = a
        self.B = b

    def reckon(self):
        """return square of rectangle"""
        S = self.l * self.B
        return S


class square(figure):
    """class for calculate area of the square"""

    def __init__(self, a):
        self.l = a

    def reckon(self):
        """return area of square"""
        S = self.l * self.l
        return S


class circle(figure):
    """class for calculate area of the circle"""

    def __init__(self, r):
        self.l = r

    def reckon(self):
        """return square of circle"""
        S = self.l * self.l * math.pi
        return S

def evaluate(str,num2,num3 = 0) :
    try:
        count = float(num2)
        count2 = float(num3)
    except ValueError:
        return "ErrType"
    if str == "Круг" :
        if count > 0:
            c = circle(count)
            return c.reckon()
        else:
            return "ErrZero"
    if str == "Прямоугольник" :
        if ((count > 0) and (count2 > 0)) :
            r = rectangle(count,count2)
            return  r.reckon()
        else :
            return "ErrZero"
    if str == "Квадрат" :
        if count > 0:
            s = square(count)
            return s.reckon()
        else:
            return "ErrZero"



server.register_function(evaluate)
server.register_introspection_functions()
print("[Соединение с сервером успешно установлено]")
print("[Сервер в ожидании выражения]")
server.serve_forever()
