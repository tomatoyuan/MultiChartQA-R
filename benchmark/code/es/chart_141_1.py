import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ["Suplemento nutricional", "Ajuste de trabajo y descanso", "Conocimientos sobre embarazo y parto", "Técnicas de relaciones sexuales para concepción", "Productos para la maternidad", "Recuperación postpartum", "Otros"]
porcentajes = [88.7, 78.1, 67.9, 66.0, 52.8, 48.3, 2.3]
colores = ["#FF9933"] * len(etiquetas)  # Naranja uniforme, similar al estilo de la imagen original

x = np.arange(len(etiquetas))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de barras horizontales
barras = ax.barh(x, porcentajes, color=colores)
ax.set_ylabel('Contenido de interés')
ax.set_xlabel('Porcentaje de atención (%)')
ax.set_yticks(x)
ax.set_yticklabels(etiquetas)
ax.invert_yaxis()  # Colocar "Suplemento nutricional" en la parte superior, similar al orden de la imagen original

# Agregar anotaciones numéricas
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1, barra.get_y() + barra.get_height() / 2, 
            f'{ancho}%', ha='left', va='center')

ax.set_title('Distribución de intereses entre la población china en edad preconcepcional en 2023')

plt.tight_layout()
plt.show()