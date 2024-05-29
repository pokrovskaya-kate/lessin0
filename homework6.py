my_dict = {'Kate': 1995, 'Max': 1990}
print(my_dict)
print(my_dict['Kate'])
my_dict['Anna'] = 1993
print(my_dict['Anna'])
my_dict.update({'Olga': 1996, 'Nick': 1991})
print(my_dict)
a = my_dict.pop('Max')
print(my_dict)
print(a)
print(my_dict)

my_set = {1, 2, 7, 4, 3, 'Sun', 31.12}
print(my_set)
my_set.update({'Sky', 19})
print(my_set)
print(my_set.discard(3))
print(my_set)