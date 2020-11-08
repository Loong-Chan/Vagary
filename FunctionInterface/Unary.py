import abc


class Unary(object):
    def __init__(self, x: float):
        self.x = x

    def value(self) -> float:
        raise NotImplementedError


class fact():

    def __init__(self, x: float):
        pass

    def fact(self) -> float:
        return 1

    def __dir__(self):
        return 1


print(fact(33))
