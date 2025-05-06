def sort_list(list):
    if not list:
        return []
    max_el = max(list)
    min_el = min(list)
    for i in range(len(list)):
        if list[i] == max_el:
            list[i] = min_el
        elif list[i] == min_el:
            list[i] = max_el
    return list + [min_el]


print(sort_list([])) # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1])) # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]

