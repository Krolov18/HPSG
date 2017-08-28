# coding: utf-8


class Feature(object):
    __names = set()

    def __init__(self, name: str, pole: bool):
        self.__name = name
        self.__pole = pole
        self.__names.add(name)

    def __str__(self): return repr(self)

    def __repr__(self):
        return "({}, {})".format(self.__name.upper(), '+' if self.__pole else '-')

    def __hash__(self): return 1

    def get_features(self):
        return self.__names

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        pass

    @property
    def pole(self):
        return self.__pole

    @pole.setter
    def pole(self, value):
        pass


def main():
    x = Feature('haut', True)
    print(x)

if __name__ == '__main__':
    main()
