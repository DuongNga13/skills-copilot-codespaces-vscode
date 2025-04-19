import math

# Lớp Point
class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        tmp = input()
        self.__x, self.__y = map(int, tmp.split())

    def print(self):
        print(f"({self.__x}, {self.__y})", end='')

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self, other=None):
        if other is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        return math.sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2)


# Lớp ColorPoint kế thừa Point
class ColorPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__()
            self.__color = "xanh"
        elif len(args) == 1 and isinstance(args[0], ColorPoint):
            cp = args[0]
            super().setXY(cp.getX(), cp.getY())
            self.__color = cp.__color
        elif len(args) == 3:
            x, y, color = args
            super().__init__(x, y)
            self.__color = color

    def read(self):
        tmp = input()
        parts = tmp.strip().split()
        x, y = int(parts[0]), int(parts[1])
        color = ' '.join(parts[2:])
        self.setXY(x, y)
        self.__color = color

    def print(self):
        super().print()
        print(f": {self.__color}")

    def setColor(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color


# Lớp kiểm thử
class C002454:
    @staticmethod
    def testCase1():
        a = ColorPoint(5, 10, "trắng")
        a.print()

    @staticmethod
    def testCase2():
        b = ColorPoint()
        b.read()
        b.move(10, 8)
        b.print()

    @staticmethod
    def testCase3():
        c = ColorPoint(6, 3, "đen")
        d = ColorPoint(c)
        d.print()
        d.setColor("vàng")
        d.print()
        c.print()

    @staticmethod
    def main(*args):
        C002454.testCase1()
        C002454.testCase2()
        C002454.testCase3()
C002454.main()
