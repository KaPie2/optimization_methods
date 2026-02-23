import math
# вариант 8
def f(x):
    return x ** 3 - x

def dichotomy(f, a, b, eps):
    iteration = 1

    while (b - a) > 2 * eps:
        x = (a + b) / 2

        x1 = x - eps / 2
        x2 = x + eps / 2

        f1 = f(x1)
        f2 = f(x2)

        print(f"\nИтерация {iteration}:")
        print(f"  a = {a:.6f}, b = {b:.6f}, b - a = {b - a:.6f}")
        print(f"  x = {x:.6f}, x1 = {x1:.6f}, x2 = {x2:.6f}")
        print(f"  f1 = {f1:.10f}, f2 = {f2:.10f}")

        if f1 > f2:
            a = x1
            print(f"  f1 > f2 => a = {a:.6f}")
        else:
            b = x2
            print(f"  f1 <= f2 => b = {b:.6f}")

        iteration += 1

    x_min = (a + b) / 2
    f_min = f(x_min)

    print("\nОтвет:")
    print(f"  x_min = {x_min:.10f}")
    print(f"  f(x_min) = {f_min:.10f}")

    return x_min, f_min

x_min, f_min = dichotomy(f, 0, 1, 0.01)
