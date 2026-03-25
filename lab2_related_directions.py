# вариант 8

import math
from lab1_golden_section import golden_section

def f(x, y):
    return (30 - (x - 2) * math.exp(-(x - 2)) - (y - 3) * math.exp(-(y - 3)))

def related_directions(x0, eps, max_iter=1000):
    n = 2
    x = x0.copy()
    s = [[1, 0], [0, 1]]
    for k in range(max_iter):
        x_prev = x.copy()

        for v in s:
            x_fixed = x.copy()
            v_fixed = v.copy()
            # Создаем функцию одной переменной вдоль направления d
            def f_lambda(t):
                x_new = [x_fixed[0] + t * v_fixed[0], x_fixed[1] + t * v_fixed[1]]
                return f(x_new[0], x_new[1])

            # Находим интервал поиска
            a = -10
            b = 10

            # Находим оптимальный шаг
            lambda_opt, _ = golden_section(f_lambda, a, b, eps / 100)

            # Обновляем точку
            x = [x[0] + lambda_opt * v[0], x[1] + lambda_opt * v[1]]

        s_new = [x[0] - x_prev[0], x[1] - x_prev[1]]

        x_fixed = x.copy()
        s_new_fixed = s_new.copy()
        # Шаг 3: Минимизация по новому направлению
        def f_lambda_new(t):
            x_new = [x_fixed[0] + t * s_new_fixed[0], x_fixed[1] + t * s_new_fixed[1]]
            return f(x_new[0], x_new[1])

        a = -10
        b = 10
        lambda_opt, _ = golden_section(f_lambda_new, a, b, eps / 100)

        x_new = [x[0] + lambda_opt * s_new[0], x[1] + lambda_opt * s_new[1]]

        # Шаг 4: Обновляем набор направлений (сдвигаем, отбрасывая самое старое)
        s = [s[1], s_new]

        # Шаг 5: Обновляем текущую точку
        x = x_new

        # Шаг 6: Проверка сходимости
        diff = math.sqrt((x[0] - x_prev[0])**2 + (x[1] - x_prev[1])**2)

        if diff < eps:
            break
    return x

x_opt = related_directions([0,0], 1e-6)
print(f"x1 = {x_opt[0]:.2f}, x2 = {x_opt[1]:.2f}")
print(f"Значение функции: {f(x_opt[0], x_opt[1]):.6f}")