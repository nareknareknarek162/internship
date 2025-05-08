import time


def cached(max_size=None, seconds=None):
    max_size = None if not isinstance(max_size, int) else max_size
    seconds = None if not isinstance(seconds, int) else seconds
    def real_cache(func):
        calculated = {}
        def wrapper(*args, **kwargs):
            nonlocal calculated
            calculated = {i[0]: i[1] for i in list(calculated.items()) if time.time() - i[1][1] < seconds} \
                if seconds is not None else calculated
            if args not in calculated:
                if max_size is not None and len(calculated) > max_size:
                    calculated = dict(list(calculated.items())[1:]) # Это будет работать только в python 3.7+
                calculated[args] = (func(*args, **kwargs), time.time())
            return calculated[args][0]
        return wrapper
    return real_cache

''''
@cached(None, 2)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2

'''

'''
#size tests
print(slow_function(3))
print(slow_function(5))
print(slow_function(7))
print(slow_function(9))
print(slow_function(3))
print(slow_function(5))
print(slow_function(10))
print(slow_function(11))
print(slow_function(3))
print(slow_function(5))
'''

'''
#seconds test
# Первый вызов — вычисляется
print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
# Повторный вызов с теми же аргументами — берётся из кэша
print(slow_function(2)) # Вывод: 4 (без вычисления)
# Через 15 секунд кэш устареет, и будет новое вычисление
time.sleep(15)
print(slow_function(2))
# Вывод: "Вычисляю для 2..." → 4
time.sleep(3)
print(slow_function(2)) # 4
'''

'''
print(slow_function(5))
time.sleep(2)
print(slow_function(5))
'''