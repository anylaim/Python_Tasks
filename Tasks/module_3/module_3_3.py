def print_params(a = 1, b = 'строка', c = True) :
    print(a, b, c)

print_params()
print_params("string", 25, [1, 2, 3])

values_list = [('string', False, 123), [321, "str", True], "qwerty"]
values_dict = {'a' : "zxc", 'b' : 456, 'c' : False}

print_params(**values_dict)
print_params(*values_list)

values_list_2 = ['str', False]
print_params(*values_list_2, 987)
