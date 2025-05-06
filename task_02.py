def coincidence(list=[], range=()) -> list:
    if list and range:
        return [i for i in list if isinstance(i, (float, int)) and range[0] <= i <= range[-1]]
    return []

print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
print(coincidence()) # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4))) # => [1, 2, 2.5]