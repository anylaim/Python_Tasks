my_dict = {'Alex': 2002, 'Mike': 1998, 'Lisa': 2000, 'John': 2000, 'Emma': 2003}
print(my_dict)
print(my_dict['Emma'])
print(my_dict.get('Nastya'))
my_dict['Nastya'] = 2006
del my_dict['Mike']
my_dict.pop('Lisa')
print(my_dict)

my_set = {'String', False, 123, 4.56, (1, 2), 0, 'String', (1, 2)}
print(my_set)
my_set.add('new string')
my_set.add((1, 3))
my_set.discard('String')
print(my_set)