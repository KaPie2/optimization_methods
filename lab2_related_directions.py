# вариант 8

# на каждой итерации алгоритма поиск осуществляется вдоль системы сопряжённых направлений

import math
from lab1_golden_section import golden_section

def f(x, y):
    return (30 - (x - 2) * math.exp(-(x - 2)) - (y - 3) * math.exp(-(y - 3)))

def related_directions(x0, eps, max_iter=1000):
    # n = 2
    x = x0.copy()
    s = [[1, 0], [0, 1]] # набор направлений (координатные оси)
    for k in range(max_iter):
        x_prev = x.copy()

        for v in s:
            x_fixed = x.copy() # фиксируем текущую точку
            v_fixed = v.copy() # фиксируем направление

            def f_lambda(lmbda):
                x_new = [x_fixed[0] + lmbda * v_fixed[0], x_fixed[1] + lmbda * v_fixed[1]]
                return f(x_new[0], x_new[1])

            # интервал поиска лямбда
            a = -10
            b = 10

            # оптимальный шаг
            lambda_opt, _ = golden_section(f_lambda, a, b, eps)

            # "шагаем"
            x = [x[0] + lambda_opt * v[0], x[1] + lambda_opt * v[1]]

        s_new = [x[0] - x_prev[0], x[1] - x_prev[1]] # суммарное перемещение за проход по всем текущим направлениям

        x_fixed = x.copy()
        s_new_fixed = s_new.copy()

        # минимизация по новому направлению
        def f_lambda_new(lmbda):
            x_new = [x_fixed[0] + lmbda * s_new_fixed[0], x_fixed[1] + lmbda * s_new_fixed[1]]
            return f(x_new[0], x_new[1])

        a = -10
        b = 10

        lambda_opt, _ = golden_section(f_lambda_new, a, b, eps)

        x_new = [x[0] + lambda_opt * s_new[0], x[1] + lambda_opt * s_new[1]]

        # обновление набора направлений (сдвигаем, отбрасывая самое старое)
        s = [s[1], s_new]

        x = x_new

        # проверка сходимости
        diff = math.sqrt((x[0] - x_prev[0])**2 + (x[1] - x_prev[1])**2)

        if diff < eps:
            break
    return x

x_opt = related_directions([0,0], 1e-6)
print(f"x1 = {x_opt[0]:.2f}, x2 = {x_opt[1]:.2f}")
print(f"Значение функции: {f(x_opt[0], x_opt[1]):.6f}")