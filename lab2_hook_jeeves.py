# вариант 8

import math
from lab1_golden_section import golden_section

def f(x, y):
    return (30 - (x - 2) * math.exp(-(x - 2)) - (y - 3) * math.exp(-(y - 3)))

def hook_jeeves(x0, dx, eps, alpha=0.5, max_iter=1000):
    n = 2
    x_base = x0.copy()
    x_prev = x0.copy()
    dx_curr = dx.copy()

    for k in range(max_iter):
        # Исследующий поиск
        improved = False
        x_trial = x_base.copy()

        for i in range(n):
            # Шаг вперед
            x_test = x_trial.copy()
            x_test[i] += dx_curr[i]
            if f(x_test[0], x_test[1]) < f(x_trial[0], x_trial[1]):
                x_trial = x_test
                improved = True
            else:
                # Шаг назад
                x_test = x_trial.copy()
                x_test[i] -= dx_curr[i]
                if f(x_test[0], x_test[1]) < f(x_trial[0], x_trial[1]):
                    x_trial = x_test
                    improved = True

        # Проверка успеха исследующего поиска
        if improved:
            # Направление ускоряющего шага
            direction = [x_trial[i] - x_prev[i] for i in range(n)]

            # Одномерная минимизация вдоль ускоряющего направления
            def f_lambda(t):
                x_new = [x_trial[i] + t * direction[i] for i in range(n)]
                return f(x_new[0], x_new[1])

            a = -10
            b = 10
            # Находим оптимальный шаг методом золотого сечения
            lambda_opt, _ = golden_section(f_lambda, a, b, eps)

            # Новая точка после ускоряющего шага
            x_new = [x_trial[i] + lambda_opt * direction[i] for i in range(n)]

            x_prev = x_base.copy()
            x_base = x_new.copy()

            # Проверка сходимости
            diff = math.sqrt((x_base[0] - x_prev[0]) ** 2 + (x_base[1] - x_prev[1]) ** 2)
            if diff < eps:
                break
        else:
            # Уменьшаем шаги
            dx_curr = [d * alpha for d in dx_curr]
            if max(dx_curr) < eps:
                break
            # Возвращаемся к предыдущей базовой точке
            x_base = x_prev.copy()

    return x_base

x_opt = hook_jeeves([0, 0], [0.5, 0.5], 1e-6)
print(f"x1 = {x_opt[0]:.2f}, x2 = {x_opt[1]:.2f}")
print(f"Значение функции: {f(x_opt[0], x_opt[1]):.6f}")