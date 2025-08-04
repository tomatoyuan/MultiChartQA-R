import matplotlib.pyplot as plt
import numpy as np

# Propósitos para que las empresas utilicen humanos digitales de IA
propositos = [
    "Mejorar la eficiencia y calidad del trabajo", "Mejorar el nivel de digitalización de la empresa", "Reducir costos laborales",
    "Patrocinio de productos y ventas en directo", "Reducir costos económicos", "Mejorar la interacción y experiencia del cliente",
    "Mejorar la imagen corporativa", "Recopilación y análisis de datos", "Demostración de aplicación de tecnología innovadora"
]
# Proporciones correspondientes (%)
proporciones = [48.80, 43.09, 36.44, 35.37, 27.13, 23.80, 23.14, 16.22, 8.11]

x = np.arange(len(propositos))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 7))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas en el centro por encima de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center', va='center', fontsize=9)

# Establecer las marcas y etiquetas del eje x, girar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(propositos, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Propósitos de las empresas chinas para utilizar humanos digitales de IA en 2025')

plt.tight_layout()
plt.show()