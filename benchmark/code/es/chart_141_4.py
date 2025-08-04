import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ["Control prenatal", "Productos de salud prenatal", "Dieta prenatal", "Prueba de embarazo", "Libros de prenatalidad", "Electrodomésticos", "Automóviles", "Otros"]
porcentajes = [78.5, 77.4, 74.7, 58.1, 31.7, 15.5, 5.7, 0.4]

x = np.arange(len(categorias))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, porcentajes, color='orange', label='Proporción de nuevo consumo (%)')
ax.set_ylabel('Proporción de nuevo consumo (%)')
ax.set_xlabel('Categorías de consumo')
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=45, ha='right')
ax.set_title('Distribución de categorías de nuevo consumo entre la población china en etapa de pre - embarazo en 2023')

# Agregar anotaciones numéricas
for i, porcentaje in enumerate(porcentajes):
    ax.text(i, porcentaje + 1, f'{porcentaje}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()