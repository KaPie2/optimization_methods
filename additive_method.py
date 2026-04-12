import numpy as np
import scipy.optimize as opt
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

pareto_points = []
alpha_list = []

# Генерируем 10 точек, меняя весовые коэффициенты
for i in range(10):
    # Меняем веса: от (0.8, 0.1, 0.1) до (0.1, 0.1, 0.8)
    alpha1 = 0.8 - i * 0.07
    alpha2 = 0.1
    alpha3 = 0.1 + i * 0.07
    alpha_list.append((alpha1, alpha2, alpha3))

    # Свертка
    def F(x):
        return alpha1 * f1(x) + alpha2 * f2(x) + alpha3 * f3(x)

    res = opt.minimize(F, x0=[0, 0], method='BFGS')
    pareto_points.append(res.x)

pareto_points = np.array(pareto_points)

print("Множество Парето (10 точек):")
for i, p in enumerate(pareto_points):
    print(f"x{i + 1} = ({p[0]:.4f}, {p[1]:.4f})")

# График
plt.figure(figsize=(10, 8))

# Центры f1, f2, f3
plt.plot(b1, d1, 'bo', markersize=10, label='Центр f1')
plt.plot(b2, d2, 'go', markersize=10, label='Центр f2')
plt.plot(b3, d3, 'yo', markersize=10, label='Центр f3')

# Соединяем центры друг с другом
plt.plot([b1, b2], [d1, d2], 'k-', linewidth=1, alpha=0.5)
plt.plot([b2, b3], [d2, d3], 'k-', linewidth=1, alpha=0.5)
plt.plot([b1, b3], [d1, d3], 'k-', linewidth=1, alpha=0.5)

# Парето-точки
plt.scatter(pareto_points[:, 0], pareto_points[:, 1], c='red', s=50, zorder=5)
plt.plot(pareto_points[:, 0], pareto_points[:, 1], 'r-', linewidth=2, label='Множество Парето')

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Метод аддитивной свертки (10 точек Парето)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.show()
