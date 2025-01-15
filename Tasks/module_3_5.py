def get_multiplied_digits(numbers) :
    str_number = str(numbers)
    first = int(str_number[0])
    if len(str_number) > 1 :
        return first * get_multiplied_digits(int(str_number[1:]))
    elif first != 0 :
        return first
    else :
        return 1


print(get_multiplied_digits(50436))
print(get_multiplied_digits(12345))
print(get_multiplied_digits(402030))