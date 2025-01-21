x = input("Число 1: ")
y = input("Число 2: ")
z = input("Число 3: ")

if x == y and x == z :
    print(3)
elif x == y or y == z or z == x :
    print(2)
else :
    print(0)
