import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# --------------------- Preparación de datos ---------------------
# Distribución de género
etiquetas_genero = ["Mujer", "Hombre"]
tamaños_genero = [60, 40]
colores_genero = ["pink", "lightblue"]

# Distribución de edad
etiquetas_edad = ["21 años o menos", "22 - 30", "31 - 40", "41 - 50", "51 - 59", "60 años o más"]
tamaños_edad = [4.0, 35.5, 46.6, 10.9, 2.4, 0.6]
colores_edad = ["coral", "gold", "green", "brown", "gray", "olive"]

# Distribución de ingresos mensuales
etiquetas_ingresos = ["5000 o menos", "5001 - 10000", "10001 - 15000", "15001 - 20000", 
                      "20001 - 25000", "25001 - 30000", "Más de 30000"]
tamaños_ingresos = [20.0, 37.2, 26.5, 10.2, 2.9, 1.3, 1.9]
colores_ingresos = ["sienna", "orange", "darkorange", "coral", "lightcoral", "pink", "palevioletred"]

# --------------------- Crear el lienzo ---------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 6))

# --------------------- Dibujar la distribución de género (en forma de bloques) ---------------------
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 20)
ax1.axis('off')  # Ocultar los ejes

# Dibujar bloques de mujeres
bloques_mujer = int(tamaños_genero[0] / 2)  # Cada bloque representa el 2%
for i in range(bloques_mujer):
    ax1.add_patch(Rectangle((i * 2, 5), 2, 10, color=colores_genero[0]))

# Dibujar bloques de hombres
bloques_hombre = int(tamaños_genero[1] / 2)
for i in range(bloques_hombre):
    ax1.add_patch(Rectangle((i * 2, 5), 2, 10, color=colores_genero[1], alpha=0.8))

# Agregar etiquetas de género y porcentajes
ax1.text(10, 2, f"{etiquetas_genero[0]}: {tamaños_genero[0]}%", fontsize=12, ha='center')
ax1.text(10 + tamaños_genero[0], 2, f"{etiquetas_genero[1]}: {tamaños_genero[1]}%", fontsize=12, ha='center')

ax1.set_title('Distribución de género', fontsize=14)

# --------------------- Dibujar el gráfico circular de distribución de edad ---------------------
wedges, texts, autotexts = ax2.pie(tamaños_edad, colors=colores_edad, autopct='%1.1f%%', startangle=90)
ax2.set_title('Distribución de edad', fontsize=14)
ax2.legend(wedges, etiquetas_edad, title="Rango de edad", loc="center left", bbox_to_anchor=(1, 0.5))

# Ajustar el color del texto de anotación
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Dibujar el gráfico circular de distribución de ingresos mensuales ---------------------
wedges, texts, autotexts = ax3.pie(tamaños_ingresos, colors=colores_ingresos, autopct='%1.1f%%', startangle=90)
ax3.set_title('Distribución de ingresos mensuales', fontsize=14)
ax3.legend(wedges, etiquetas_ingresos, title="Rango de ingresos", loc="center left", bbox_to_anchor=(1, 0.5))

# Ajustar el color del texto de anotación
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('Perfil de los consumidores chinos de bebidas sin azúcar: Género/Edad/Ingresos', fontsize=16, y=1.03)
plt.tight_layout()
plt.show()