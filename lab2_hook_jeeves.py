# вариант 8

# Метод Хука-Дживса: на каждом шаге выполняем исследующий поиск (пробные шаги по координатам для поиска лучшей точки),
# затем делаем шаг по образцу (двигаемся в направлении от предыдущей точки к найденной) для ускорения сходимости.

import math
from lab1_golden_section import golden_section

def f(x, y):
    return (30 - (x - 2) * math.exp(-(x - 2)) - (y - 3) * math.exp(-(y - 3)))

def hook_jeeves(x0, dx, eps, alpha=0.5, max_iter=1000):
    n = 2
    x = x0.copy() # текущая базовая точка (где мы сейчас)
    x_prev = x0.copy() # предыдущая базовая точка (откуда пришли)
    dx_curr = dx.copy() # текущий шаг

    for k in range(max_iter):
        # исследующий поиск
        improved = False
        x_trial = x.copy() # пробная точка (лучшая точка, найденная в окрестности)

        for i in range(n):
            # шаг вперед
            x_test = x_trial.copy()
            x_test[i] += dx_curr[i]
            if f(x_test[0], x_test[1]) < f(x_trial[0], x_trial[1]):
                x_trial = x_test
                improved = True
            else:
                # шаг назад
                x_test = x_trial.copy()
                x_test[i] -= dx_curr[i]
                if f(x_test[0], x_test[1]) < f(x_trial[0], x_trial[1]):
                    x_trial = x_test
                    improved = True

        # проверка успеха исследующего поиска
        if improved:
            # направление ускоряющего шага
            direction = [x_trial[i] - x_prev[i] for i in range(n)]

            # одномерная минимизация вдоль ускоряющего направления
            def f_lambda(lmbda):
                x_new = [x_trial[i] + lmbda * direction[i] for i in range(n)]
                return f(x_new[0], x_new[1])

            a = -10
            b = 10

            # оптимальный шаг
            lambda_opt, _ = golden_section(f_lambda, a, b, eps)

            # новая точка после ускоряющего шага
            x_new = [x_trial[i] + lambda_opt * direction[i] for i in range(n)]

            x_prev = x.copy()
            x = x_new.copy()

            # Проверка сходимости
            diff = math.sqrt((x[0] - x_prev[0]) ** 2 + (x[1] - x_prev[1]) ** 2)
            if diff < eps:
                break
        else:
            # уменьшение шагов, где альфа - коэффициент уменьшения шага
            dx_curr = [d * alpha for d in dx_curr]
            if max(dx_curr) < eps: # если шаг и так маленький, то мы уже рядом с минимумом
                break
            # возвращение к предыдущей базовой точке
            x = x_prev.copy()
    return x

x_opt = hook_jeeves([0, 0], [0.5, 0.5], 1e-6)
print(f"x1 = {x_opt[0]:.2f}, x2 = {x_opt[1]:.2f}")
print(f"Значение функции: {f(x_opt[0], x_opt[1]):.6f}")