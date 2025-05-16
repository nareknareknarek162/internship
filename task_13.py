import time


def cached(max_size=None, seconds=None):
    max_size = None if not isinstance(max_size, int) else max_size
    seconds = None if not isinstance(seconds, int) else seconds

    def real_cache(func):
        calculated = {}

        def wrapper(*args, **kwargs):
            nonlocal calculated

            key = args
            for i in kwargs:
                key += (i, kwargs[i])  # key is ordered set or args and kwargs

            calculated = {i[0]: i[1] for i in list(calculated.items()) if time.time() - i[1][1] < seconds} \
                if seconds is not None else calculated
            if key not in calculated:
                if max_size is not None and len(calculated) >= max_size:
                    calculated = dict(list(calculated.items())[1:])  # Это будет работать только в python 3.7+
                calculated[args] = (func(*args, **kwargs), time.time())
            return calculated[args][0]

        return wrapper

    return real_cache