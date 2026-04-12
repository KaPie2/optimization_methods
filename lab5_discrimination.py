import numpy as np
import matplotlib.pyplot as plt

a1, b1, c1, d1 = 2, 5, 3, 5
a2, b2, c2, d2 = 3, -7, 1, -2
a3, b3, c3, d3 = 1, 8, 2, -4

def f1(x):
    return a1 * (x[0] - b1) ** 2 + c1 * (x[1] - d1) ** 2

def f2(x):
    return a2 * (x[0] - b2) ** 2 + c2 * (x[1] - d2) ** 2

def f3(x):
    return a3 * (x[0] - b3) ** 2 + c3 * (x[1] - d3) ** 2

# минимизируем f1 на сетке при ограничениях по f2 и f3
def discrimination_step(a2_level, a3_level, x1_min=-10, x1_max=10, x2_min=-10, x2_max=10, n=301):

    x1_vals = np.linspace(x1_min, x1_max, n)
    x2_vals = np.linspace(x2_min, x2_max, n)

    best_x = None
    best_f1 = float('inf')

    for x1 in x1_vals:
        for x2 in x2_vals:
            x = np.array([x1, x2])
            if f2(x) <= a2_level and f3(x) <= a3_level:
                val_f1 = f1(x)
                if val_f1 < best_f1:
                    best_f1 = val_f1
                    best_x = x.copy()

    return best_x, best_f1

def generate_pareto_discrimination():
    points = []

    # уровни для ограничений
    levels = [50, 80, 110, 140, 170, 200, 230, 260, 290, 320]

    for a3_level in levels:
        # немного «строже» ограничиваем f2
        a2_level = 1.5 * a3_level

        x, val_f1 = discrimination_step(a2_level, a3_level)
        if x is not None:
            # проверка, чтобы точки сильно не совпадали
            is_unique = True
            for p in points:
                if np.linalg.norm(p - x) < 0.1:
                    is_unique = False
                    break
            if is_unique:
                points.append(x)
            if len(points) >= 10:
                break

    return np.array(points)

pareto_points = generate_pareto_discrimination()

print("Множество Парето (10 точек):")
for i, p in enumerate(pareto_points):
    print(f"x{i + 1} = ({p[0]:.4f}, {p[1]:.4f})")

# График в том же стиле
plt.figure(figsize=(10, 8))

# Центры f1, f2, f3 (те же, что в других методах)
plt.plot(b1, d1, 'bo', markersize=10, label='Центр f1')
plt.plot(b2, d2, 'go', markersize=10, label='Центр f2')
plt.plot(b3, d3, 'yo', markersize=10, label='Центр f3')

# Соединяем центры
plt.plot([b1, b2], [d1, d2], 'k-', linewidth=1, alpha=0.5)
plt.plot([b2, b3], [d2, d3], 'k-', linewidth=1, alpha=0.5)
plt.plot([b1, b3], [d1, d3], 'k-', linewidth=1, alpha=0.5)

# Парето‑точки
plt.scatter(pareto_points[:, 0], pareto_points[:, 1], c='red', s=50, zorder=5)
plt.plot(pareto_points[:, 0], pareto_points[:, 1], 'r-', linewidth=2, label='Множество Парето')

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Дискриминационный метод (10 точек Парето)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.show()