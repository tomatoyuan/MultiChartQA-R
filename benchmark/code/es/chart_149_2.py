import matplotlib.pyplot as plt
import numpy as np

# --------------------- Datos del gráfico circular para "Frecuencia de compra" a la izquierda ---------------------
etiquetas_frecuencia = [
    "Casi todos los días", "3 - 4 veces a la semana", "1 - 2 veces a la semana", 
    "1 - 2 veces al mes", "Irregular", "Rara vez"
]
tamaños_frecuencia = [11.9, 29.5, 38.3, 7.9, 10.7, 1.7]  # Porcentaje
colores_frecuencia = ["coral", "gold", "green", "brown", "olive", "darkgreen"]

# --------------------- Datos del gráfico de barras horizontales para "Actividades de promoción preferidas" a la derecha ---------------------
etiquetas_promocion = [
    "Ganar un premio al abrir la botella", "Segunda botella a mitad de precio", "Descuento", "Regalos pequeños gratis"
]
proporciones_promocion = [59.2, 55.8, 50.5, 44.8]  # Porcentaje
colores_promocion = ["coral"] * len(etiquetas_promocion)  # Naranja uniforme

# --------------------- Crear un lienzo (una fila, dos columnas) ---------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Dibujar el gráfico circular para "Frecuencia de compra" a la izquierda ---------------------
wedges, texts, autotexts = ax1.pie(
    tamaños_frecuencia, 
    colors=colores_frecuencia, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.8  # Ajustar la posición de la etiqueta para evitar superposiciones
)
ax1.set_title('Frecuencia de compra de bebidas sin azúcar por consumidores chinos en 2023', fontsize=14)
# Ajustar la posición de la leyenda (fuera del gráfico a la derecha)
ax1.legend(
    wedges, 
    etiquetas_frecuencia, 
    title="Frecuencia de compra", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5)
)
# Optimizar el color del texto de la etiqueta (usar texto blanco para sectores oscuros y negro para los claros)
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Dibujar el gráfico de barras horizontales para "Actividades de promoción preferidas" a la derecha ---------------------
x_promocion = np.arange(len(etiquetas_promocion))
ax2.barh(x_promocion, proporciones_promocion, color=colores_promocion)
ax2.set_title('Actividades de promoción preferidas para bebidas sin azúcar por consumidores chinos en 2023', fontsize=14)
ax2.set_xlabel('Porcentaje (%)')
ax2.set_ylabel('Tipos de actividades de promoción')
ax2.set_yticks(x_promocion)
ax2.set_yticklabels(etiquetas_promocion)
ax2.set_xlim(0, 70)  # Ajustar el rango del eje x para ajustarse a la proporción máxima (59.2%)

# Agregar etiquetas numéricas a la derecha
for i, prop in enumerate(proporciones_promocion):
    ax2.text(prop + 1, i, f'{prop}%', ha='left', va='center', color='black', fontsize=11)

# --------------------- Agregar descripción de la fuente de la muestra ---------------------
fig.text(0.5, -0.05, 'Fuente de la muestra: Sistema de encuesta y cálculo de datos de Strawberry Pie', 
         fontsize=10, ha='center')

plt.tight_layout()
plt.show()