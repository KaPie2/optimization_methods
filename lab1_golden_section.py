import math
# вариант 8
def f(x):
    return x ** 3 - x

def golden_section(f, a, b, eps):
    iteration = 1
    tau = 0.618

    L = b - a
    x1 = a + L * tau
    x2 = b - L * tau

    f1 = f(x1)
    f2 = f(x2)

    print(f"Начальные точки:")
    print(f"  L = {L:.6f}")
    print(f"  x1 = {x1:.6f}, f1 = {f1:.10f}")
    print(f"  x2 = {x2:.6f}, f2 = {f2:.10f}")

    while (b - a) > eps:
        print(f"\nИтерация {iteration}:")
        print(f"  a = {a:.6f}, b = {b:.6f}, L = {b - a:.6f}")

        if f1 > f2:
            b = x1
            f1 = f2
            x1 = x2
            L = b - a
            x2 = b - L * tau
            f2 = f(x2)
            print(f"  f1 > f2 - сужаем справа")
        else:
            a = x2
            f2 = f1
            x2 = x1
            L = b - a
            x1 = a + L * tau
            f1 = f(x1)
            print(f"  f1 <= f2 - сужаем слева")

        print(f"  x1 = {x1:.6f}, x2 = {x2:.6f}")
        print(f"  f1 = {f1:.10f}, f2 = {f2:.10f}")

        iteration += 1

    x_min, f_min = (x1, f1) if f1 < f2 else (x2, f2)

    print("\n" + "=" * 60)
    print(f"Ответ:")
    print(f"  x_min = {x_min:.10f}")
    print(f"  f(x_min) = {f_min:.10f}")

    return x_min, f_min

x_min, f_min = golden_section(f, 0, 1, 0.01)
