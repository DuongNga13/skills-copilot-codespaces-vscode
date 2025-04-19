from Bai1 import Point
import math

class LineSegment:
    __d1 = Point()
    __d2 = Point(0)

    def __init__(self, *args):
        if len(args)==0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

        if len(args)==2:
            if not (isinstance(args[0], Point) and isinstance(args[1], Point)):
                raise TypeError("Point should be used!")
            self.__d1 = args[0]
            self.__d2 = args[1]

        if len(args)==4:
            if not all(isinstance(item, Point) for item in args):
                raise TypeError("Only Intergers can be added!")
            self.__d1 = Point((args[0], args[1]))
            self.__d2 = Point((args[2], args[3]))

        if len(args)==1:
            if not(isinstance(args[0], LineSegment)):
                raise TypeError("Only a line segment can be added!")
            self.__d1 = Point(args[0].__d1.getX(), args[0].__d1.getY(), )
            self.__d2 = Point(args[0].__d2.getX(), args[0].__d1.getY(), )

    def read(self):
        tmp = input("Nhap vao doan thang (x1 y1 x2 y2): ").split()
        x1, y1, x2, y2 = map(int, tmp)
        self.__d1 = Point(x1, y1)
        self.__d2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.__d1.getX()}, {self.__d1.getY()}); ({self.__d2.getX()}, {self.__d2.getY()})]"

    def move(self, dx=0, dy=0):
        self.__d1.move(dx,dy)
        self.__d2.move(dx,dy)

    def length(self):
        return self.__d1.distance(self.__d2)
    
    def angle(self):
        return int(math.atan2(self.__d2.getY()-self.__d1.getY()),self.__d2.getX()-self.__d1.getX()) 
    
class LineSegmentTest:
    def testCase1(self):
        diemA = Point(2,5)
        diemB = Point(20,35)
        doanAB = LineSegment(diemA, diemB)
        doanAB.move(35, 51)
        print("Doan AB: ", doanAB)

    def testCase2(self):
        doanCD = LineSegment()
        doanCD.read()
        print("|CD| = {:.2f}".format(doanCD.length()))

    def testCase3(self):
        n = int(input("Nhap n(so doan thang):"))
        danhsach = []

        for i in range(n):
            l1 = LineSegment()
            l1.read()
            danhsach.append(l1)

        for item in danhsach:
            print(item)
            print(item.length())

        danhsach.sort(key = lambda dist: dist.length())
        for item in danhsach:
            print(item)
            print(item.length())

def main():
    while True:
        s = input("Case 1/2/3: ")
        if s == '1':
            LineSegmentTest().testCase1()
        elif s == '2':
            LineSegmentTest().testCase2()
        elif s == '3':
            LineSegmentTest().testCase3()

main()
