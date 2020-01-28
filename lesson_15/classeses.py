class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'x = {}, y = {}'.format(self.__x, self.__y)

    def print_point(self):
        return 'x = {}, y = {}'.format(self.__x, self.__y)

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self, x):
        return self.__x

    def get_y(self, y):
        return self.__y


class Figure:
    def __init__(self, name):
        self.__name = name
        self.__picks = []

    def add_point(self, pt):
        if not pt:
            self.__picks.append(pt)

    def print_fig(self):
        for pt in self.__picks:
            x = pt.get_x()
            y = pt.get_y()