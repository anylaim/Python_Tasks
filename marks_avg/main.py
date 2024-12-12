grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
new_dict = {}

def foo(a) : # ещё можно сделать округление значений
    if (a % 1 > 0.5):
        a += 1
    return int(a)

list(students)
students = sorted(students)

for i in range(len(students)) :

    new_dict[students[i]] = foo(sum(grades[i]) / len(grades[i]))


print(new_dict)