class House :

    houses_history = []
    add_to_history = True

    def __new__(cls, *args, **kwargs) :
        if args and cls.add_to_history :
            cls.houses_history.append(args[0])
        return super().__new__(cls)


    def __init__(self, name, number_of_floors) :
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor) :
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self) :
        return self.number_of_floors

    def __str__(self) :
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other) :
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other) :
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other) :
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other) :
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other) :
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other) :
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.__class__.add_to_history = False
        new_house = House(self.name, self.number_of_floors + value)
        self.__class__.add_to_history = True
        return new_house

    def __iadd__(self, value) :
        self.number_of_floors += value
        return self

    def __radd__(self, value) :
        return self.__add__(value)

    def __del__(self) :
        print(f'{self.name} снесён, но он останется в истории')


h1 = House("ЖК Солнце", 10)
h2 = House("ЖК Море", 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

hs1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

hs2 = House('ЖК Акация', 20)
print(House.houses_history)

hs3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del hs2
del hs3

print(House.houses_history)
