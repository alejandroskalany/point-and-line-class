import sys,math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)
        self.printer = ("(" + str(x) + "," + str(y) + ")")

    def __repr__(self):
        coord = (self.x, self.y)
        return coord

    def __str__(self):
        return str(self.printer)


#testing points
#a_point = Point(1,2)
#another_point = Point(2,3)


class Line:
    def __init__(self, p1, p2):

        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def __str__(self):
        x1, y1 = self.p1.x,self.p1.y
        x2, y2 - self.p2.x,self.p2.y
        line = "((%f,%f),(%f,%f))" % (x1,y1,x2,y2)
        return line

if __name__ == "__main__":

    #print(a_point)
    #print(another_point)
    print("Line maker")
    x1 = input('Enter an x1 value: ')
    x2 = input('Enter a y1 value: ')
    p1 = Point(x1, y1)
    print(p1)

    x2 = input("Enter an x2 value: ")
    y2 = input("Enter a y2 value: ")
    p2 = Point(x2, y2)
    print(p2)

    line = Line(p1,p2)