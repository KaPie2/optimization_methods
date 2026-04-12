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

# Этап 1 минимизация f1
res1 = opt.minimize(f1, x0=[0, 0])
f1_star = f1(res1.x)

pareto_points = []

# Генерируем 10 точек
for Delta1 in np.linspace(5, 100, 10):
    # Этап 2 минимизация f2 с ограничением от f1
    cons2 = ({'type': 'ineq', 'fun': lambda x: Delta1 - (f1(x) - f1_star)})
    res2 = opt.minimize(f2, x0=[0, 0], method='SLSQP', constraints=cons2)
    f2_star = f2(res2.x)

    # Этап 3 минимизация f3 с ограничением от f1 и f2
    cons3 = [
        {'type': 'ineq', 'fun': lambda x: Delta1 - (f1(x) - f1_star)},
        {'type': 'ineq', 'fun': lambda x: 100 - (f2(x) - f2_star)}
    ]
    res3 = opt.minimize(f3, x0=[0, 0], method='SLSQP', constraints=cons3)
    pareto_points.append(res3.x)

pareto_points = np.array(pareto_points)

print("Множество Парето (10 точек):")
for i, p in enumerate(pareto_points):
    print(f"x{i + 1} = ({p[0]:.4f}, {p[1]:.4f})")

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
plt.title('Метод последовательных уступок')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.show()
