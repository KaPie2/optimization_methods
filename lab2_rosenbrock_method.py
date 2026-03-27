import math
import numpy as np

# вариант 8
A = 30
a = 2
b = 3

def f(x, y):
    return A - (x - a) * math.exp(-(x - a)) - (y - b) * math.exp(-(y - b))

def gram_schmidt(s, alpha):
    n = len(s)
    new_s = []

    for j in range(n):
        # вычисляем z^j
        if abs(alpha[j]) < 1e-12:  # alpha_j ≈ 0
            z = s[j].copy()
        else:
            z = np.zeros_like(s[0])
            for i in range(j, n):
                z = z + alpha[i] * s[i]

        # вычисляем g^j (ортогонализация)
        if j == 0:
            g = z.copy()
        else:
            g = z.copy()
            for i in range(j):
                # Вычитаем проекцию на уже построенные направления
                proj = np.dot(z, new_s[i]) * new_s[i]
                g = g - proj

        # нормируем
        norm_g = np.linalg.norm(g)
        new_s.append(g / norm_g)

    return new_s


def rosenbrock_method(x_start, eps=1e-6, eta=2.0, beta=-0.5, max_iter=100):
    n = 2
    # Начальные направления: координатные оси
    s = [np.array([1.0, 0.0]), np.array([0.0, 1.0])]
    # Начальные шаги
    delta = [1.0, 1.0]
    # Начальная точка
    x_k = np.array(x_start, dtype=float)
    y = x_k.copy()

    for iteration in range(max_iter):
        x_prev = x_k.copy()

        # Проход по всем направлениям
        for j in range(n):
            y_new = y + delta[j] * s[j]

            if f(y_new[0], y_new[1]) < f(y[0], y[1]):
                # Успешный шаг
                y = y_new
                delta[j] = eta * delta[j]
            else:
                # Неудачный шаг
                delta[j] = beta * delta[j]

        # Проверяем, было ли улучшение
        if f(y[0], y[1]) < f(x_k[0], x_k[1]):
            x_k = y.copy()

            # Проверка остановки
            if np.linalg.norm(x_k - x_prev) < eps:
                break

            # Вычисляем alpha
            diff = x_k - x_prev
            alpha = [np.dot(diff, s[j]) for j in range(n)]

            # Строим новые направления
            s = gram_schmidt(s, alpha)

            # Сбрасываем y
            y = x_k.copy()
        else:
            # Не было успешных спусков
            if all(abs(d) < eps for d in delta):
                break
            y = x_k.copy()

    return x_k


# Запуск
x0 = [0, 0]
x_opt = rosenbrock_method(x0, eps=1e-6)

print(f"x1 = {x_opt[0]:.2f}, x2 = {x_opt[1]:.2f}")
print(f"Значение функции: {f(x_opt[0], x_opt[1]):.6f}")
