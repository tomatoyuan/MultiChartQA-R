import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ["La IA aumenta la tasa de clics del grupo objetivo aproximadamente",
             "La IA aumenta la tasa de conversión del grupo objetivo aproximadamente",
             "La eficiencia de selección del grupo objetivo aumenta aproximadamente"]
valores = [20, 30, 100]  # Valores en porcentaje
colores = ["#FF99CC", "#FF99CC", "#FF99CC"]  # Colores rosados similares
ancho_barra = 0.5  # Ancho del gráfico de barras
x = np.arange(len(etiquetas))  # Posiciones en el eje x

# Crear una figura
fig, ax = plt.subplots(figsize=(8, 4))  # Ajustar el tamaño del lienzo, similar a la proporción del gráfico original

# Dibujar el gráfico de barras
barras = ax.bar(x, valores, width=ancho_barra, color=colores, edgecolor="white")

# Agregar un título
ax.set_title("¿Cuál es el uso de la 'Selección de audiencia por IA'?", fontsize=14, fontweight="bold", y=1.1)  # Posicionar el título un poco más alto

# Agregar etiquetas de datos
for barra, valor in zip(barras, valores):
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, altura, f"{valor}%",
            ha="center", va="bottom", fontsize=12, color="pink")

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, fontsize=10, rotation=45, ha='right')

# Ocultar el eje y (El gráfico original no muestra el eje y)
ax.yaxis.set_visible(False)

# Ocultar los bordes (Para lograr un estilo más sencillo similar al gráfico original)
for spine in ax.spines.values():
    spine.set_visible(False)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()