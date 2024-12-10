immutable_var = (12.34, 56, True, 'string', [False, 12, 34])
print(immutable_var)

## immutable_var[1] = 123

immutable_var[4][0] = True
print(immutable_var)


mutable_list = [12.34, 56, True, 'string', [False, 12, 34]]
mutable_list[1] = 65
mutable_list[4][2] = 21
mutable_list[3] = 'string*'

print(mutable_list)