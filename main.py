"""ЛР №4, вариант 2: filter, reduce, logging, memoization, parameterized decorator."""
from functools import reduce, wraps


def filter_evens(values):
    """Среднее №2: filter для чётных чисел."""
    return list(filter(lambda value: value % 2 == 0, values))


def factorial(n):
    """Среднее №4: факториал с reduce."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n должно быть неотрицательным целым")
    return reduce(lambda acc, number: acc * number, range(1, n + 1), 1)


def log_calls(func):
    """Среднее №7: декоратор логирования вызовов."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__}: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат {func.__name__}: {result}")
        return result
    return wrapper


def memoize(func):
    """Повышенное №2: сохранение результатов для одинаковых аргументов."""
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    return wrapper


def repeat(times):
    """Повышенное №6: декоратор с параметром числа повторений."""
    if not isinstance(times, int) or times < 1:
        raise ValueError("times должен быть положительным целым")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@log_calls
def double(number):
    return number * 2


@memoize
def fibonacci(n):
    if n < 0:
        raise ValueError("n >= 0")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@repeat(3)
def greet(name):
    print(f"Привет, {name}!")


if __name__ == "__main__":
    print("Чётные:", filter_evens(range(1, 11)))
    print("Факториал 5:", factorial(5))
    double(7)
    print("Число Фибоначчи F(20):", fibonacci(20))
    greet("Герман")
