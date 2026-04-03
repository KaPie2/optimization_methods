# вариант 8

import sympy as sp

# Определяем переменные
x1, x2, lam = sp.symbols('x1 x2 lam')

# Целевая функция и ограничение
f = x1**2 - x2**2
phi = 2*x1 + x2 - 3

# Функция Лагранжа
L = f + lam * phi

# Частные производные
dL_dx1 = sp.diff(L, x1)
dL_dx2 = sp.diff(L, x2)
dL_dlam = sp.diff(L, lam)

# Решаем систему уравнений
solution = sp.solve([dL_dx1, dL_dx2, dL_dlam], [x1, x2, lam])


print("\nФункция Лагранжа: L =", L)

print("\nЧастные производные:")
print(f"∂L/∂x1 = {dL_dx1}")
print(f"∂L/∂x2 = {dL_dx2}")
print(f"∂L/∂λ = {dL_dlam}")

print("\nРешение:")
print(solution)
