# вариант 8

import time
start_time = time.time()

def f(x):
    return x ** 3 - x

def golden_section(f, a, b, eps):
    tau = 0.618

    L = b - a
    x1 = a + L * tau
    x2 = b - L * tau

    f1 = f(x1)
    f2 = f(x2)

    while (b - a) > eps:
        if f1 > f2:
            b = x1
            f1 = f2
            x1 = x2
            L = b - a
            x2 = b - L * tau
            f2 = f(x2)
        else:
            a = x2
            f2 = f1
            x2 = x1
            L = b - a
            x1 = a + L * tau
            f1 = f(x1)

    x_min, f_min = (x1, f1) if f1 < f2 else (x2, f2)

    print(f"Ответ:")
    print(f"  x_min = {x_min}")
    print(f"  f(x_min) = {f_min}")

    return x_min, f_min

x_min, f_min = golden_section(f, 0, 1, 0.01)

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.4f} секунд")
