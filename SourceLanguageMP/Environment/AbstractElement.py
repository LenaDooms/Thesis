from abc import ABC, abstractmethod


class MPPElemAbstract(ABC):
    def __init__(self, c, m, gamma, e):
        self.c = c
        self.m = m
        self.gamma = gamma
        self.e = e

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def equals(self, element):
        pass


class MPGCElemAbstract(ABC):
    def __init__(self,  m, tcList, tc, sigma):
        self.m = m
        self.tcList = tcList
        self.tc = tc
        self.sigma = sigma

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def equals(self, element):
        pass

    @abstractmethod
    def elaborate(self, gc):
        pass


class MPGammaElem(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def equals(self, element):
        pass

    @abstractmethod
    def elaborate(self, gc):
        pass
