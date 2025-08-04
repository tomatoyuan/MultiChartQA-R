import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2019", "2020", "2021", "2022"]
crecimiento_exportacion = [30.5, 39.2, 28.3, 10.1]  # Tasa de crecimiento interanual del volumen de exportación (%)
crecimiento_importacion = [10.8, 9.1, -0.9, 0.8]    # Tasa de crecimiento interanual del volumen de importación (%)
crecimiento_total = [22.2, 25.7, 18.6, 7.1]    # Tasa de crecimiento interanual del volumen de importación y exportación (%)

x = np.arange(len(años))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de líneas
ax.plot(x, crecimiento_total, marker='o', color='blue', label='Tasa de crecimiento interanual del volumen de importación y exportación (%)', linewidth=2)
ax.plot(x, crecimiento_importacion, marker='o', color='orange', label='Tasa de crecimiento interanual del volumen de importación (%)', linewidth=2)
ax.plot(x, crecimiento_exportacion, marker='o', color='green', label='Tasa de crecimiento interanual del volumen de exportación (%)', linewidth=2)

ax.set_ylabel('Tasa de crecimiento interanual (%)')
ax.set_xlabel('Año')
ax.set_xticks(x)
ax.set_xticklabels(años)
ax.legend()
ax.set_title('Tasa de crecimiento interanual del volumen de comercio electrónico transfronterizo de China desde 2019 hasta 2022')

# Agregar anotaciones numéricas
for i in range(len(años)):
    # Anotar el valor interanual del volumen de importación y exportación
    ax.text(i, crecimiento_total[i] + 1, f'{crecimiento_total[i]}', ha='center', va='bottom', color='blue')
    # Anotar el valor interanual del volumen de importación
    ax.text(i, crecimiento_importacion[i] + 1, f'{crecimiento_importacion[i]}', ha='center', va='bottom', color='orange')
    # Anotar el valor interanual del volumen de exportación
    ax.text(i, crecimiento_exportacion[i] + 1, f'{crecimiento_exportacion[i]}', ha='center', va='bottom', color='green')

plt.tight_layout()
plt.show()