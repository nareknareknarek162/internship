def connect_dicts(dict1: dict, dict2: dict) -> dict:
    priority_dict = dict1 if sum(dict1.values()) > sum(dict2.values()) else dict2
    other_dict = dict2 if sum(dict1.values()) > sum(dict2.values()) else dict1
    for i in other_dict:
        if i not in priority_dict and other_dict[i] >= 10:
            priority_dict[i] = other_dict[i]
    return dict(filter(lambda y: y[1] >= 10, sorted(priority_dict.items(), key=lambda x: x[1])))


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))  # =>{ "c": 11, "b": 12 }
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  # =>{ d: 11, "c": 12, "a": 13 }
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  # =>{ "c": 11, "b": 12, "a": 15 }
