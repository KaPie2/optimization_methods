# вариант 8

def F(n):
    if n == 0 or n == 1:
        return 1
    return F(n - 1) + F(n - 2)

def f(x):
    return x**3 - x

def fibonacci_method(a, b, n):
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
    print(min(f1, f2))

fibonacci_method(0, 1, 12)