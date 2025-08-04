import matplotlib.pyplot as plt
import numpy as np

# Datos de fecha (Año/Mes)
fechas = ["2022/04", "2022/05", "2022/06", "2022/07", "2022/08", "2022/09", "2022/10", "2022/11", "2022/12",
          "2023/01", "2023/02", "2023/03", "2023/04", "2023/05", "2023/06", "2023/07", "2023/08", "2023/09",
          "2023/10", "2023/11", "2023/12", "2024/01", "2024/02", "2024/03", "2024/04", "2024/05", "2024/06",
          "2024/07", "2024/08", "2024/09", "2024/10", "2024/11", "2024/12", "2025/01", "2025/02", "2025/03",
          "2025/04"]
# Precio mayorista ponderado promedio de productos acuáticos (yuan/kg)
precios = [24.68, 24.40, 23.71, 23.68, 23.35, 24.38, 23.38, 23.19, 22.39, 23.31, 23.55, 22.78, 22.79, 23.13, 23.31,
           23.20, 23.43, 23.91, 23.70, 23.20, 22.89, 23.24, 23.97, 23.22, 23.26, 23.20, 23.26, 23.00, 23.20, 23.75,
           23.57, 22.90, 22.61, 22.73, 22.80, 22.37, 22.42]

x = np.arange(len(fechas))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 6))
# Dibujar un gráfico de líneas
linea, = ax.plot(x, precios, marker='o', color='orange', label='Precio mayorista ponderado promedio de productos acuáticos (yuan/kg)')

# Agregar anotaciones numéricas
for i, precio in enumerate(precios):
    ax.text(x[i], precio, f'{precio}', ha='center', va='bottom', fontsize=8)

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(fechas, rotation=45, fontsize=8)
ax.set_ylabel('Precio (yuan/kg)')
ax.set_title('Precio mayorista ponderado promedio de productos acuáticos en China desde abril de 2022 a abril de 2025')
ax.legend()

plt.tight_layout()
plt.show()