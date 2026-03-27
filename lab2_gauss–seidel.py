# вариант 8

# Основная идея метода состоит в том, что на
# каждом шаге фиксируются все переменные, кроме одной, которая выбирается
# так, чтобы минимизировать функцию.

import math
from lab1_golden_section import golden_section

def f(x, y):
    return (30 - (x - 2) * math.exp(-(x - 2)) - (y - 3) * math.exp(-(y - 3)))

def gauss_seidel(x0, eps, max_iter=1000):
    n = 2
    x = x0.copy()
    for k in range(max_iter):
        x_prev = x.copy()
        y = x.copy() # обновление координаты
        for j in range(n):
            a = y[j] - 10
            b = y[j] + 10
            if j == 0:
                y1_fixed = y[1] # фиксируем y (двигаемся по x)
                def f_lambda_x(t):
                    return f(t, y1_fixed)

                lambda_opt, _ = golden_section(f_lambda_x, a, b, eps) # передаем объект функции, а не ее результат
                y[0] = lambda_opt # обновляем x
            else:
                y0_fixed = y[0] # фиксируем x (двигаемся по y)
                def f_lambda_y(t):
                    return f(y0_fixed, t)

                lambda_opt, _ = golden_section(f_lambda_y, a, b, eps)
                y[1] = lambda_opt
        x = y.copy()
        diff = math.sqrt((x[0] - x_prev[0])**2 + (x[1] - x_prev[1])**2)
        if diff < eps:
            break
    return x

x_opt = gauss_seidel([0, 0], 1e-5)
print(f"x1 = {x_opt[0]:.2f}, x2 = {x_opt[1]:.2f}")
print(f"Значение функции: {f(x_opt[0], x_opt[1]):.6f}")