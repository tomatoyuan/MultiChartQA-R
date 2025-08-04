import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ["Por debajo de 200 yuanes", "201 - 500 yuanes", "501 - 1000 yuanes", "1001 - 1500 yuanes", "1501 - 2000 yuanes", "Por encima de 2000 yuanes"]
porcentajes = [15.0, 34.4, 38.9, 8.9, 1.6, 1.2]

x = np.arange(len(categorias))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, porcentajes, color='orange', label='Proporción de consumo (%)')
ax.set_ylabel('Proporción de consumo (%)')
ax.set_xlabel('Rango de gasto promedio mensual')
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=15, ha='right')
ax.set_title('Encuesta sobre el consumo mensual promedio de cosméticos de los consumidores chinos en 2023')

# Agregar anotaciones numéricas
for i, porcentaje in enumerate(porcentajes):
    ax.text(i, porcentaje + 1, f'{porcentaje}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()