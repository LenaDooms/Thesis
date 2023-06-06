from abc import ABC, abstractmethod


class MPConstraint(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def equals(self, constraint):
        pass

    @abstractmethod
    def elaborate(self, gc):
        pass


class MPAbstractQ(MPConstraint):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def wellFormed(self, gamma, gc):
        pass

    @abstractmethod
    def substitute(self, tau, a):
        pass

    @abstractmethod
    def entails(self, p, gc, gamma):
        pass

    @abstractmethod
    def getDictionary(self, p, gc, gamma):
        pass


class MPAbstractC(MPConstraint):
    def __init__(self, aList, qList, q):
        super().__init__()
        self.aList = aList
        self.qList = qList
        self.q = q

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def wellFormed(self, gamma, gc):
        pass

    @abstractmethod
    def unambiguous(self):
        pass
