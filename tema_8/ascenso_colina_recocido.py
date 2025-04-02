import numpy as np
import matplotlib.pyplot as plt

def objective_function(x):
    return np.sin(3 * x) + np.sin(5 * x)

# Parámetros del recocido simulado
T_initial = 1.0
alpha = 0.997  # Enfriamiento más lento
max_iter = 500
step_size = 0.1
x_bounds = (0, 2 * np.pi)

# Inicio forzado
x_current = 1.5
f_current = objective_function(x_current)
T = T_initial

trajectory = [(x_current, f_current)]
temperatures = [T]

# Recocido Simulado
for i in range(max_iter):
    x_new = x_current + np.random.uniform(-step_size, step_size)
    x_new = np.clip(x_new, *x_bounds)
    f_new = objective_function(x_new)

    delta = f_new - f_current

    if delta > 0 or np.exp(delta / T) > np.random.rand():
        x_current = x_new
        f_current = f_new

    T *= alpha
    trajectory.append((x_current, f_current))
    temperatures.append(T)

trajectory = np.array(trajectory)
x_vals = np.linspace(*x_bounds, 1000)
y_vals = objective_function(x_vals)

# Gráficas
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(x_vals, y_vals, label='f(x)')
plt.plot(trajectory[:, 0], trajectory[:, 1], 'ro-', markersize=2, label='Trayectoria')
plt.axvline(x=1.5, color='gray', linestyle='--', label='Inicio en x=1.5')
plt.title("Recorrido con enfriamiento lento (α = 0.997)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(temperatures, label='Temperatura')
plt.title("Evolución de la Temperatura (α = 0.997)")
plt.xlabel("Iteración")
plt.ylabel("Temperatura")
plt.legend()

plt.tight_layout()
plt.show()
