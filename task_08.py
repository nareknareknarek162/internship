from functools import reduce


def multiply_numbers(inputs=None):
    return None if inputs is None \
        else reduce(lambda x, y: x * y, map(int, filter(lambda x: x in '0123456789', str(inputs))), 1)


print(multiply_numbers())  # => None
print(multiply_numbers('ss'))  # => None
print(multiply_numbers('1234'))  # => 24
print(multiply_numbers('sssdd34'))  # => 12
print(multiply_numbers(2.3))  # => 6
print(multiply_numbers([5, 6, 4]))  # => 120
