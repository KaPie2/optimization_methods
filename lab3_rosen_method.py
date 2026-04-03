# вариант 8

import math
from lab1_golden_section import golden_section

def f(x):
    return x[0] ** 2 - x[1] ** 2

def grad_f(x):
    return [2 * x[0], -2 * x[1]]

def phi(x):
    return 2 * x[0] + x[1] - 3

def grad_phi(x):
    return [2, 1]

def compute_projection_matrix():
    # Вычисляем матрицу P = I - A^T (A A^T)^{-1} A
    A1, A2 = 2, 1
    AAT_inv = 1.0 / (A1 * A1 + A2 * A2)

    P = [[1 - A1 * AAT_inv * A1, 0 - A1 * AAT_inv * A2],
         [0 - A2 * AAT_inv * A1, 1 - A2 * AAT_inv * A2]]

    return P

def rosen_method(x_start, eps=1e-6, max_iter=100):
    # Матрица P
    P = compute_projection_matrix()
    print(f"Матрица проектирования P:")
    print(f"  [{P[0][0]:.2f}, {P[0][1]:.2f}]")
    print(f"  [{P[1][0]:.2f}, {P[1][1]:.2f}]\n")

    # Допустимая начальная точка
    x = x_start

    for k in range(max_iter):
        # Направление спуска S = -P * grad_f
        g = grad_f(x)
        S = [-(P[0][0] * g[0] + P[0][1] * g[1]),
             -(P[1][0] * g[0] + P[1][1] * g[1])]

        norm_S = math.sqrt(S[0] ** 2 + S[1] ** 2)

        # Проверка на оптимальность
        if norm_S <= eps:
            A1, A2 = 2, 1
            AAT_inv = 1.0 / (A1 * A1 + A2 * A2)
            lambda_val = AAT_inv * (A1 * g[0] + A2 * g[1])
            print(f"\n|S| = {norm_S:.2e} <= eps, оптимальная точка найдена")
            print(f"Множитель Лагранжа λ = {lambda_val:.6f}")
            break

        # Нормализуем направление
        S = [S[0] / norm_S, S[1] / norm_S]

        # Одномерный поиск
        def f_alpha(a):
            return f([x[0] + a * S[0], x[1] + a * S[1]])

        # Находим интервал для поиска
        a = 1.0
        f0 = f_alpha(0)
        while a < 1000 and f_alpha(a) < f0:
            a *= 2

        alpha_opt, _ = golden_section(f_alpha, -a, a, eps / 10)

        # Новая точка
        x_new = [x[0] + alpha_opt * S[0],
                 x[1] + alpha_opt * S[1]]

        print(f"x={[round(xi, 6) for xi in x_new]}, f={f(x_new)}, phi={phi(x_new)}")
        x = x_new

    return x

x_opt = rosen_method([0, 3], eps=1e-6)

print(f"\nРезультат:")
print(f"Оптимальная точка: x = {x_opt}")
print(f"f(x_opt) = {f(x_opt)}")
print(f"phi(x_opt) = {phi(x_opt)}")


print("\nЗадача не имеет минимума (функция не ограничена снизу)")
print("Метод Розена будет бесконечно двигаться в сторону уменьшения f")
