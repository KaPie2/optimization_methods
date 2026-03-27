import math
import numpy as np
from lab1_golden_section import golden_section

# вариант 8
A = 30
a = 2
b = 3

def f(x, y):
    return A - (x - a) * math.exp(-(x - a)) - (y - b) * math.exp(-(y - b))

def grad_f(x, y):
    df_dx = -((x - a) - 1) * math.exp(-(x - a))
    df_dy = -((y - b) - 1) * math.exp(-(y - b))
    return np.array([df_dx, df_dy])

def steepest_descent(x0, eps, max_iter=1000):
    x = np.array(x0, dtype=float)

    for k in range(max_iter):
        grad = grad_f(x[0], x[1])  # вектор градиента
        grad_norm = np.linalg.norm(grad)  # длина вектора градиента

        if grad_norm < eps:
            break

        S = -grad / grad_norm

        def f_along(alpha):
            return f(x[0] + alpha * S[0], x[1] + alpha * S[1])

        alpha_opt, _ = golden_section(f_along, -10, 10, eps)
        x = x + alpha_opt * S

    return x

x0 = [0, 0]
x_opt = steepest_descent(x0, eps=1e-6)

print(f"x1 = {x_opt[0]:.2f}, x2 = {x_opt[1]:.2f}")
print(f"Значение функции: {f(x_opt[0], x_opt[1]):.6f}")
