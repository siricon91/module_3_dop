def calculate_structure_sum(data):
    full_amount = 0

    if isinstance(data, int):
        full_amount += data
    elif isinstance(data, str):
        full_amount += len(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            full_amount += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            full_amount += calculate_structure_sum(key)
            full_amount += calculate_structure_sum(value)
    return full_amount

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)