##Q10

class canvas:
    def __init__(self, width, height, bg=" "):
        self.width=width
        self.height=height
        self.bg=bg
        self.grid = []

        i = 0
        while i<height:
            row = [bg]*width
            self.grid.append(row)
            i = i+1

    def set_pixel(self, x, y, char="*"):
        if x>=0 and x<self.width and y>=0 and y<self.height:
            self.grid[y][x] = char

    def show(self):
        y = 0
        while y<self.height:
            x = 0
            line=""
            while x<self.width:
                line = line+self.grid[y][x]
                x = x+1
            print(line)
            y = y+1


class shape:
    def area(self):
        print("Not implemented")

    def perimeter(self):
        print("Not implemented")

    def points(self):
        print("Not implemented")
        return []

    def contains(self, x, y):
        print("Not implemented")
        return False

    def overlaps(self, other):
        print("Not implemented")
        return False


class rectangle(shape):
    def __init__(self, length, width, x, y):
        self.__length = length
        self.__width = width
        self.__x = x
        self.__y = y

    def points(self):
        pts = []

        x1 = self.__x
        y1 = self.__y

        x2 = self.__x+self.__length
        y2 = self.__y

        x3 = self.__x+self.__length
        y3 = self.__y+self.__width

        x4 = self.__x
        y4 = self.__y+self.__width

        pts.append((x1, y1))
        pts.append((x2, y2))
        pts.append((x3, y3))
        pts.append((x4, y4))

        return pts


class circle(shape):
    def __init__(self, radius, x, y):
        self.__radius = radius
        self.__x = x
        self.__y = y

    def points(self):
        pts = []

        r = self.__radius
        x = self.__x
        y = self.__y

        pts.append((x+r, y))
        pts.append((x-r, y))
        pts.append((x, y+r))
        pts.append((x, y-r))

        return pts


class triangle(shape):
    def __init__(self, base, height, x, y):
        self.__base = base
        self.__height = height
        self.__x = x
        self.__y = y

    def points(self):
        pts = []

        x1 = self.__x
        y1 = self.__y

        x2 = self.__x+self.__base
        y2 = self.__y

        x3 = self.__x
        y3 = self.__y+self.__height

        pts.append((x1, y1))
        pts.append((x2, y2))
        pts.append((x3, y3))

        return pts


def paint_shape(canvas, obj, char):
    pts = obj.points()

    i = 0
    while i<len(pts):
        x = pts[i][0]
        y = pts[i][1]
        canvas.set_pixel(x, y, char)
        i = i+1


class CompoundShape:
    def __init__(self):
        self.items = []

    def add(self, obj):
        self.items.append(obj)

    def paint(self, canvas, char):
        i = 0
        while i<len(self.items):
            paint_shape(canvas, self.items[i], char)
            i = i+1

##Q11:

class RasterDrawing:
    def __init__(self, width, height, bg=" "):
        self.c = canvas(width, height, bg)
        self.items = []

    def add_shape(self, obj, char):
        self.items.append((obj, char))
        return self

    def remove_shape(self, index):
        if index >= 0 and index < len(self.items):
            self.items.pop(index)

    def paint(self):
        self.c = canvas(self.c.width, self.c.height, self.c.bg)
        i=0
        while i < len(self.items):
            obj = self.items[i][0]
            ch = self.items[i][1]
            paint_shape(self.c, obj, ch)
            i = i + 1

    def show(self):
        self.c.show()

    def __repr__(self):
        s = "RasterDrawing(" + repr(self.c.width) + "," + repr(self.c.height) + "," + repr(self.c.bg) + ")"
        i = 0
        while i < len(self.items):
            obj = self.items[i][0]
            ch = self.items[i][1]
            s = s + ".add_shape(" + repr(obj) + "," + repr(ch) + ")"
            i = i + 1

        return s

    def save(self, filename):
        f = open(filename, "w")
        f.write(repr(self))
        f.close()


def load_raster(filename):
    f = open(filename, "r")
    text = f.read()
    f.close()
    return eval(text)


##Q12

class rectangle(shape):
    def __init__(self, length, width, x, y):
        self.__length=length
        self.__width=width
        self.__x=x
        self.__y=y

    def points(self):
        pts=[]

        x1=self.__x
        y1=self.__y

        x2=self.__x + self.__length
        y2=self.__y

        x3=self.__x + self.__length
        y3=self.__y + self.__width

        x4=self.__x
        y4=self.__y + self.__width

        pts.append((x1, y1))
        pts.append((x2, y2))
        pts.append((x3, y3))
        pts.append((x4, y4))

        return pts

    def __repr__(self):
        return "rectangle(" + repr(self.__length) + "," + repr(self.__width) + "," + repr(self.__x) + "," + repr(self.__y) + ")"


class circle(shape):
    def __init__(self, radius, x, y):
        self.__radius=radius
        self.__x=x
        self.__y=y

    def points(self):
        pts=[]

        r=self.__radius
        x=self.__x
        y=self.__y

        pts.append((x+r, y))
        pts.append((x-r, y))
        pts.append((x, y+r))
        pts.append((x, y-r))

        return pts

    def __repr__(self):
        return "circle(" + repr(self.__radius) + "," + repr(self.__x) + "," + repr(self.__y) + ")"


class triangle(shape):
    def __init__(self, base, height, x, y):
        self.__base=base
        self.__height=height
        self.__x=x
        self.__y=y

    def points(self):
        pts=[]

        x1=self.__x
        y1=self.__y

        x2=self.__x + self.__base
        y2=self.__y

        x3=self.__x
        y3=self.__y + self.__height

        pts.append((x1, y1))
        pts.append((x2, y2))
        pts.append((x3, y3))

        return pts

    def __repr__(self):
        return "triangle(" + repr(self.__base) + "," + repr(self.__height) + "," + repr(self.__x) + "," + repr(self.__y) + ")"