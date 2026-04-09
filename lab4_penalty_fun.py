# вариант 8
import numpy as np
from scipy.optimize import minimize

def f(x):
    return x[0] ** 2 + x[1] ** 2 - 3 * x[0] + 15 * x[1]

def limitation(x):
    # h(x) = 0
    return (x[0] + x[1]) ** 2 - 4 * (x[0] - x[1])

def penalty_fun(x0, eps, r0=1, alpha=10, max_iter=100):
    # начальный штрафной коэффициент - r
    # коэффициент увеличения штрафа - alpha

    x = np.array(x0)
    r = r0

    for k in range(max_iter):
        # штрафная функция: P(x) = f(x) + r * h(x)^2
        def penalty(x_curr):
            h = limitation(x_curr)
            return f(x_curr) + r * h ** 2

        # минимизация штрафной функции
        result = minimize(penalty, x, method='BFGS', options={'gtol': 1e-10, 'disp': False})

        x_new = result.x
        h_val = limitation(x_new)
        f_val = f(x_new)

        # проверка сходимости
        if abs(h_val) < eps:
            return x_new, f_val

        # увеличение штрафного коэффициента
        r *= alpha

    return x_new, f_val

x0 = [1, 1]
eps = 0.01

x_opt_pen, f_opt_pen = penalty_fun(x0, eps)
print("Метод штрафных функций")
print(f"x = {x_opt_pen}, f = {f_opt_pen}")