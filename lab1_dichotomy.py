# вариант 8

import time
start_time = time.time()

def f(x):
    return x ** 3 - x

def dichotomy(f, a, b, eps):
    while (b - a) > 2 * eps:
        x = (a + b) / 2

        x1 = x - eps / 2
        x2 = x + eps / 2

        f1 = f(x1)
        f2 = f(x2)

        if f1 > f2:
            a = x1
        else:
            b = x2

    x_min = (a + b) / 2
    f_min = f(x_min)

    print("Ответ:")
    print(f"  x_min = {x_min}")
    print(f"  f(x_min) = {f_min}")

    return x_min, f_min

x_min, f_min = dichotomy(f, 0, 1, 0.01)

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.4f} секунд")
