def count_words(string) -> dict:
    processed_string = str(string).strip().lower()
    for i in ".,:;?!()“”'\"-":
        processed_string = processed_string.replace(i, '')
    return {i: processed_string.split().count(i) for i in set(processed_string.split())}

print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))