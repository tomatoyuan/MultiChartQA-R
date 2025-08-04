import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Períodos de tiempo (datos del eje x)
horas = np.arange(0, 25, 4)
# Calor de búsqueda (datos del eje y, unidad: diez mil)
valores_calor = [1100, 1100, 3000, 1200, 3000, 1100, 1000]

# Crear un lienzo
plt.figure(figsize=(8, 5), facecolor="#f5f5f5")

# Utilizar interpolación spline cúbica para generar una curva suave
x_suave = np.linspace(horas.min(), horas.max(), 300)
spl = make_interp_spline(horas, valores_calor, k=3)  # k=3 significa spline cúbica
y_suave = spl(x_suave)

# Dibujar la curva suave
plt.plot(x_suave, y_suave, color="#0077b6", linewidth=2.5)
# Dibujar los puntos de datos
plt.scatter(horas, valores_calor, color="#023e8a", s=60, zorder=5)

# Establecer el título
plt.title("El período de tiempo con mayor calor de búsqueda de la Copa del Mundo", fontsize=16, fontweight="bold", color="#03045e")
# Establecer la etiqueta del eje x
plt.xlabel("Período de tiempo", fontsize=12, color="#333333")
# Establecer la etiqueta del eje y
plt.ylabel("Calor de búsqueda (diez mil)", fontsize=12, color="#333333")

# Establecer las marcas del eje x
plt.xticks(horas)
# Establecer las marcas del eje y
plt.yticks([1000, 2000, 3000])

# Agregar líneas de cuadrícula
plt.grid(True, linestyle="--", alpha=0.7)

# Mejorar la apariencia del gráfico
plt.tight_layout()  # Ajustar automáticamente el diseño
plt.ylim(0, 3500)   # Establecer el rango del eje y

# Mostrar el gráfico
plt.show()