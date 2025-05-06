def is_palindrome(string) -> bool:
    processed_string = str(string).strip().lower()
    for i in ".,:;?!()“”'\"- ":
        processed_string = processed_string.replace(i, '')
    return processed_string == processed_string[::-1]

print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra"))  # => False
