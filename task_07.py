def combine_anagrams(words_array):
    groups = dict()
    for i in words_array:
        key_word = ''.join(sorted(i))
        if key_word not in groups:
            groups[key_word] = list()
        groups[key_word].append(i)
    return list(groups.values())


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
