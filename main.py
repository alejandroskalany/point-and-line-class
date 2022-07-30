class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.printer = ("(" + str(x) + "," + str(y) + ")")

    def __str__(self):
        return str(self.printer)

a_point = Point(1,2)
another_point = Point(2,3)


#class Line:





if __name__ == "__main__":

    print(a_point)
    print(another_point)
