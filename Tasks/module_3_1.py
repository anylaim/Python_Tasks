x = input('Enter string: ')

call = 0

def count_calls() :
    global call
    call += 1


def string_info (string) :
    count_calls()
    var = (len(string), string.upper(), string.lower())
    return var

arr = ['Apple', 'Coconut', 'Sweet', 'Grape', 'Ball']

def is_contains (string, list) :
    count_calls()
    for i in range(len(list)) :

        if string.casefold() == list[i].casefold() :
            return True
    return False

print(string_info(x))
print(is_contains(x, arr))
print(call)
