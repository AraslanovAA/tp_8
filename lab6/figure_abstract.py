from abc import ABCMeta, abstractmethod
class figure():
    """parent class"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def reckon(self):
        """return square"""