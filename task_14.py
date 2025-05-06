class EvenNumbers():
    def __init__(self, n):
        self.current = -2
        self.steps_left = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.steps_left != 0:
            self.current += 2
            self.steps_left -= 1
            return self.current
        raise StopIteration

evens = EvenNumbers(10)
for num in evens:
    print(num) # Должно вывести 0, 2, 4, 6, 8