from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color = (255, 255, 255), *sides) :
        self.__sides = list(sides)
        if self.__is_valid_color(*color):
            self.__color = color
        else :
            self.__color = (255, 255, 255)
        self.filled = False

    def get_color(self) :
        return self.__color

    def __is_valid_color(self, r, g, b) :
        return all(isinstance(color, int) and 0 <= color <= 255 for color in (r, g, b))

    def set_color(self, r, g, b) :
        if self.__is_valid_color(r, g, b) :
            self.__color = (r, g, b)
            self.filled = True

    def get_sides(self) :
        return self.__sides

    def __is_valid_sides(self, *sides) :
        return len(sides) == len(self.__sides) and all(isinstance(side, int) and side > 0 for side in sides)

    def set_sides(self, *new_sides) :
        if self.__is_valid_sides(*new_sides) :
            self.__sides = list(new_sides)

    def __len__(self) :
        return sum(self.__sides)

class Circle(Figure) :
    sides_count = 1

    def __init__(self, color, *side) :
        super().__init__(color, side)
        side = list(*self.get_sides())
        self.__radius = side[0] / (2 * pi)

    def get_square(self) :
        return self.__radius * (pi ** 2)

    def get_radius(self) :
        return self.__radius

class Triangle(Figure) :
    sides_count = 3

    def __init__(self, color, *sides) :
        if len(sides) == 3 and ((sides[0] + sides[1] > sides[2]) or
                                (sides[1] + sides[2] > sides[0]) or
                                (sides[2] + sides[0] > sides[1])):
            super().__init__(color, sides)
        else :
            super().__init__(color, 1, 1, 1)

    def get_square(self) :
        sides = list(*self.get_sides())
        p = (sides[0] + sides[1] + sides[2]) / 2
        return sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

class Cube(Figure) :
    sides_count = 12

    def __init__(self, color, *side) :
        sides = []
        for i in range(12) :
            if len(side) == 1 :
                sides.append(*side)
            else :
                sides.append(1)
        super().__init__(color, sides)


    def get_volume(self) :
        side = list(*self.get_sides())
        return side[0] ** 3





circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)




circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())




cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())


print(len(circle1))


print(cube1.get_volume())