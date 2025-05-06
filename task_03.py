def max_odd(array: list):
    mx = None
    for i in filter(lambda x: isinstance(x, (float, int)) and not isinstance(x, bool), array):
        if int(i) == i and i % 2 != 0 and (mx is None or mx < i):
            mx = i
    return mx


print(max_odd([1, 2, 3, 4, 4]))  # => 3
print(max_odd([21.0, 2, 3, 4, 4]))  # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))  # => 3
print(max_odd(['ololo', 'fufufu']))  # => None
print(max_odd([2, 2, 4]))  # => None

# убедимся
print(max_odd([[21.00, 5], None, 13.0012, 46, 24, 'abcdef', True, 3 / 4]))
print(max_odd([[21.00, [5]], None, 13.0012, 46, 24, 'abcdef', False, 3 / 4, 17.000000]))
