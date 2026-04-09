# вариант 5
import numpy as np
from scipy.optimize import minimize

def f(x):
    return (x[0] - 2) ** 2 + (x[1] - 1) ** 2

def g1(x):
    # g1 >= 0
    return x[1] - x[0] ** 2

def g2(x):
    # g2 >= 0
    return 2 - x[0] - x[1]


def find_feasible_point(x0):
    def penalty(x):
        return max(0, -g1(x)) ** 2 + max(0, -g2(x)) ** 2

    result = minimize(penalty, x0, method='BFGS')
    return result.x

def barrier_method(x0, eps, r0=1.0, alpha=10, max_iter=50):
    x = np.array(x0, dtype=float)
    r = r0

    for k in range(max_iter):
        # барьерная функция: P(x) = f(x) - r * (ln(g1) + ln(g2))
        def barrier(x_curr):
            g1_val = g1(x_curr)
            g2_val = g2(x_curr)

            # проверка допустимости (все g > 0 для логарифма)
            if g1_val <= 0 or g2_val <= 0:
                return 1e10  # большой штраф за выход из области

            return f(x_curr) - r * (np.log(g1_val) + np.log(g2_val))

        # минимизация барьерной функции
        result = minimize(barrier, x, method='BFGS', options={'gtol': 1e-10, 'disp': False})

        x_new = result.x
        g1_val = g1(x_new)
        g2_val = g2(x_new)
        f_val = f(x_new)
        min_g = min(g1_val, g2_val)

        # проверка сходимости (все ограничения выполнены с запасом)
        if min_g > 0 and abs(f_val - f(x)) < eps:
            return x_new, f_val

        # уменьшение барьерного параметра (r -> 0)
        r /= alpha
        x = x_new

    return x_new, f_val

x0 = [2,2]

# поиск допустимой начальной точки
x_feasible = find_feasible_point(x0)
print(f"допустимая точка: {x_feasible}")

x_opt, f_opt = barrier_method(x0=x_feasible, eps=0.01, r0=1, alpha=10)

print("Метод барьерных поверхностей")
print(f"x = {x_opt}, f = {f_opt}")
