people_weight_dict = { 
    'john': 134,
    'mike': 170,
    'robert': 165,
    'items': ['orange', {'k1': 'some value'}],
    'tuple': (1, 2, 3, 4, 5)
}

tuple_removed = people_weight_dict.pop('tuple')

print(tuple_removed)