import matplotlib.pyplot as plt
import numpy as np

# Datos (ejemplo de valores de popularidad, se pueden reemplazar con datos reales)
categorias = ["Cena de Nochevieja", "Saludos de Año Nuevo", "Ver el Espectáculo de Festival de Primavera / Dinero de Suerte / Quedar despierto hasta tarde", "Dinero de Suerte", "Poner fuegos artificiales / Adorar a los dioses y pedir bendiciones"]
norte = [85, 70, 65, 90, 75]  # Valores de popularidad en el norte (datos de ejemplo)
sur = [95, 60, 70, 80, 55]  # Valores de popularidad en el sur (datos de ejemplo)

y = np.arange(len(categorias))  # Coordenadas del eje y
valor_maximo = max(max(norte), max(sur))  # Obtener el valor máximo de popularidad para establecer el rango del eje x

# Crear un lienzo
fig, ax = plt.subplots(figsize=(12, 6))

# Dibujar el gráfico de barras horizontales para el norte (a la izquierda, extendiéndose en dirección negativa)
ax.barh(y, [-n for n in norte], height=0.4, label="Norte", color="#1E88E5")
# Dibujar el gráfico de barras horizontales para el sur (a la derecha, extendiéndose en dirección positiva)
ax.barh(y, sur, height=0.4, label="Sur", color="#FF5722")

# Establecer las etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(categorias, fontsize=12)

# Establecer el rango y las etiquetas del eje x
ax.set_xlim(-valor_maximo - 10, valor_maximo + 10)
ax.set_xticks([-100, -75, -50, -25, 0, 25, 50, 75, 100])
ax.set_xticklabels(['100', '75', '50', '25', '0', '25', '50', '75', '100'])
ax.set_xlabel('Valor de Popularidad', fontsize=12)

# Establecer el título y la leyenda
ax.set_title('Comparación de la popularidad de atención de los "Rituales de Festival de Primavera" entre el Norte y el Sur', fontsize=16, pad=20)
ax.legend(loc='upper right')

# Agregar etiquetas de datos
for i, v in enumerate(norte):
    ax.text(-v - 5, i, str(v), va='center', ha='right', color='black')
for i, v in enumerate(sur):
    ax.text(v + 5, i, str(v), va='center', ha='left', color='black')

# Ocultar los bordes superior y derecho, ajustar la posición del borde inferior
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_position('center')

plt.tight_layout()
plt.show()