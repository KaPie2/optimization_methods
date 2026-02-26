import time
start_time = time.time()

# вариант 8

def F(n):
    if n <= 1:
        return 1
    return F(n - 1) + F(n - 2)

def find_n(a, b, eps):
    n = 2
    while F(n) < ((b - a) / eps):
        n += 1
    return n

def f(x):
    return x**3 - x

def fibonacci_method(a, b):
    n = find_n(a, b, 0.01)
    while n > 2:
        L = abs(b - a)

        x1 = a + (F(n - 1) / F(n)) * L
        x2 = b - (F(n - 1) / F(n)) * L

        f1 = f(x1)
        f2 = f(x2)

        if f1 > f2:
            b = x1
            f1 = f2
            x1 = x2

            x2 = a + (b - x1)
            f2 = f(x2)
        else:
            a = x2
            f2 = f1
            x2 = x1

            x1 = b - (x2 - a)
            f1 = f(x1)
        n = n - 1
    x_min = (a + b) / 2
    print(f'x_min = {x_min}')
    print(f'f(x_min) = {f(x_min)}')

fibonacci_method(0, 1)

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.4f} секунд")