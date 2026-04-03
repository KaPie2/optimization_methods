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

def project_onto_constraint(x):
    # Проекция точки на прямую 2x1 + x2 = 3 (для начальной точки)
    # Решаем систему: минимизируем |x - x0|^2 при 2x1 + x2 = 3
    # Аналитическое решение через метод множителей Лагранжа
    a, b = 2, 1  # коэффициенты ограничения
    c = 3
    denominator = a ** 2 + b ** 2
    t = (c - (a * x[0] + b * x[1])) / denominator
    return [x[0] + a * t, x[1] + b * t]

def zoitendijk(x0, eps, max_iterations=100):
    x = x0[:]

    # Проецируем начальную точку на ограничение
    x = project_onto_constraint(x)
    print(f"Начальная точка (после проекции): {x}")
    print(f"phi(x) = {phi(x)}")

    for i in range(max_iterations):
        # 1) Проверка условий Куна-Таккера
        # Для ограничения-равенства условие Куна-Таккера:
        # grad_f + v * grad_phi = 0
        # Пытаемся найти v
        # grad_f = [2x1, -2x2], grad_phi = [2, 1]
        # Решаем (систему): 2x1 + 2v = 0,
        #                  -2x2 + v = 0
        # => v = 2x2,
        #    2x1 + 4x2 = 0
        # => x1 + 2x2 = 0

        if abs(x[0] + 2 * x[1]) < eps and abs(phi(x)) < eps:
            print(f"Условия Куна-Таккера выполнены")
            break

        # 2) Находим возможное направление (касательное к ограничению)
        # Условие: grad_phi^T * s = 0 => 2*s1 + s2 = 0
        # Направление касательной
        # нужно найти вектор s = (s1, s2) такой, что
        tangent = [1, -2]  # т.к. 2*1 + (-2) = 0
        # нормировка
        norm_t = math.sqrt(tangent[0] ** 2 + tangent[1] ** 2)
        tangent = [tangent[0] / norm_t, tangent[1] / norm_t]

        grad = grad_f(x)
        # Проекция антиградиента на касательную
        dot = grad[0] * tangent[0] + grad[1] * tangent[1]
        s = [-tangent[0] * dot, -tangent[1] * dot]  # направление спуска

        # Нормализуем направление
        norm_s = math.sqrt(s[0] ** 2 + s[1] ** 2)
        if norm_s > eps:
            s = [s[0] / norm_s, s[1] / norm_s]

        # Проверяем, что это направление спуска
        directional_derivative = grad[0] * s[0] + grad[1] * s[1]
        if directional_derivative >= 0:
            # Пробуем противоположное направление
            s = [-s[0], -s[1]]
            directional_derivative = grad[0] * s[0] + grad[1] * s[1]

        if abs(directional_derivative) < eps:
            print(f"Направление не найдено")
            break

        # 3) Линейный поиск вдоль направления s с учетом ограничения
        # Для ограничения-равенства ищем alpha, чтобы phi(x + alpha * s) = 0
        # phi(x + alpha * s) = 2(x1+alpha*s1) + (x2+alpha*s2) - 3 = phi(x) + alpha*(2*s1 + s2)
        # Так как 2*s1 + s2 = 0 (касательное направление), phi остается константой

        # поэтому шаг выбираем из условия минимизации f вдоль направления
        def f_1d(alpha):
            x_new = [x[0] + alpha * s[0], x[1] + alpha * s[1]]
            return f(x_new)

        # Выполняем одномерную минимизацию
        alpha_opt, _ = golden_section(f_1d, -10, 10, eps / 10)

        x_new = [x[0] + alpha_opt * s[0], x[1] + alpha_opt * s[1]]

        delta = math.sqrt((x_new[0] - x[0]) ** 2 + (x_new[1] - x[1]) ** 2)
        if delta < eps:
            x = x_new
            break

        x = x_new
        print(f"x={[round(xi, 6) for xi in x]}, f={f(x)}, phi={phi(x)}")

    return x

x0 = [0.0, 0.0]
eps = 1e-6
x_opt = zoitendijk(x0, eps)

print(f"\nРезультат:")
print(f"Оптимальная точка: x = {x_opt}")
print(f"f(x_opt) = {f(x_opt)}")
print(f"phi(x_opt) = {phi(x_opt)}")

print("Задача не имеет минимума (функция не ограничена снизу)")
print("Метод Зойтендейка будет бесконечно двигаться в сторону уменьшения f")