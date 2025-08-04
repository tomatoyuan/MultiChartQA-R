import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ['El producto tiene fuertes atributos de salud', 'Tiene empaque de regalo listo, más práctico', 'Es bastante útil para la persona que recibe el regalo', 'Relación calidad - precio, hacer mucho con poco dinero', 'Es preciado, da buena impresión al darlo']
valores = [87, 71, 70, 58, 41]

# Crear un gráfico de barras con degradado de color
fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(categorias, valores)

# Aplicar degradado de color (simulado a través de la transparencia del color)
for i, barra in enumerate(barras):
    barra.set_facecolor((0.6, 0, 0, 0.3 + 0.7 * valores[i] / 100))  # Canal de color rojo fijo, la transparencia aumenta con el valor

# Agregar etiquetas de valores
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazar hacia arriba 3 puntos
                textcoords="offset points",
                ha='center', va='bottom')

# Mejorar la apariencia del gráfico
ax.set_ylabel('Proporción de atención (%)')
ax.set_title('Distribución de puntos de atención al comprar regalos de Año Nuevo (con degradado de color)')
ax.set_ylim(0, 100)
plt.xticks(rotation=20)
plt.tight_layout()

plt.show()