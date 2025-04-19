class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy


class ColorPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__()
            self.color = "xanh"
        elif len(args) == 3:
            x, y, color = args
            super().__init__(x, y)
            self.color = color
        elif len(args) == 1 and isinstance(args[0], ColorPoint):
            cp = args[0]
            super().__init__(cp.getX(), cp.getY())
            self.color = cp.color

    def read(self):
        print("Nhap toa do x, y va mau cua diem:")
        tmp = input()
        parts = tmp.strip().split()
        x, y = int(parts[0]), int(parts[1])
        color = " ".join(parts[2:])
        self.setXY(x, y)
        self.color = color

    def print(self):
        print(f"({self.getX()}, {self.getY()}): {self.color}")

    def setColor(self, color):
        self.color = color


class C002454:
    @staticmethod
    def testCase1():
        print("\n Test case 1:")
        A = ColorPoint(5, 10, "trắng")
        print("In ra A:")
        A.print()

    @staticmethod
    def testCase2():
        print("\n Test case 2:")
        B = ColorPoint()
        B.read()
        print("Di chuyen B them (10, 8)...")
        B.move(10, 8)
        print("Diem B sau di chuyen:")
        B.print()

    @staticmethod
    def testCase3():
        print("\nTest case 3:")
        C = ColorPoint(6, 3, "đen")
        D = ColorPoint(C)
        print("Diem D duoc sao chep tu diem C:")
        D.print()
        print("Mau diem D -> 'Vang'")
        D.setColor("vang")
        print("Diem D khi doi mau:")
        D.print()
        print("Diem C:")
        C.print()

    @staticmethod
    def main():
        print("Bat dau kiem thu")
        C002454.testCase1()
        C002454.testCase2()
        C002454.testCase3()
        print("\nKet thuc")

C002454.main()
