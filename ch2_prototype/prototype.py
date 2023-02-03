from abc import ABCMeta,abstractmethod
from copy import deepcopy
class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass