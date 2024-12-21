x = int(input('Введите число: '))

arr2 = []
for i in range(1, x // 2) :
    for j in range(1, x) :
        if x % (i + j) == 0 and i + j > 2 and i < j :
            arr2.append(str(i)) # str для дальнейшего преобразования
            arr2.append(str(j))

arr2 = "".join(arr2) # преобразование из списка в строку
arr2 = int(arr2) # обратно в число
print(arr2) # arr2 теперь число, над которым можно совершать действия (если шифр был бы сложнее)

print("--------------------------------------------------------")

# или если нужно чтоб пары подбирались строго до 20 для текущего числа

arr1 = []
for i in range(1, 10) :
    for j in range(1, 20) :
        if x % (i + j) == 0 and i + j > 2 and i < j :
            arr1.append(i)
            arr1.append(j)

print(*arr1)