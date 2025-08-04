import matplotlib.pyplot as plt
import numpy as np

# 数据
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
datos_2022 = [47.4, 46.6, 47.3, 46.2, 47.2, 47.5, 47.9, 47.9, 47.7, 47.8, 47.6, 47.8]
datos_2023 = [47.8, 47.8, 48.6, 48.7, 48.5, 48.6, 48.6, 48.6, 48.8, 48.7, 48.9, 48.9]
datos_2024 = [48.9, 48.0] + [None] * 10

x = np.arange(len(meses))
ancho = 0.25

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(x - ancho, datos_2022, width=ancho, label='Año 2022', color='#f1c232')
ax.bar(x, datos_2023, width=ancho, label='Año 2023', color='#3c78d8')
ax.bar(x + ancho, [v if v is not None else 0 for v in datos_2024], width=ancho, label='Año 2024', color='red')

# Agregar etiquetas de valores
for i, v in enumerate(datos_2022):
    ax.text(x[i] - ancho, v + 0.1, f"{v}", ha='center', va='bottom', fontsize=9)
for i, v in enumerate(datos_2023):
    ax.text(x[i], v + 0.1, f"{v}", ha='center', va='bottom', fontsize=9)
for i, v in enumerate(datos_2024):
    if v is not None:
        ax.text(x[i] + ancho, v + 0.1, f"{v}", ha='center', va='bottom', fontsize=9)

ax.set_xticks(x)
ax.set_xticklabels(meses)
ax.set_ylim(44, 51)
ax.set_ylabel('Horas/semana')
ax.set_title('Tiempo de trabajo semanal promedio de los empleados de empresas en China de 2022 a 2024')

ax.legend()
plt.tight_layout()
plt.show()