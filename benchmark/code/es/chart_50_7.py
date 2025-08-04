import matplotlib.pyplot as plt
import numpy as np

# Marcas de gafas AI
marcas = ["Huawei", "Xiaomi", "Google", "Rokid", "Meta", "Xingzhe Wujiang", "LeiShen Technology", "Yiwen Technology", "Star Meizu", "Baidu"]
# Porcentajes correspondientes de las marcas (%), los datos se simulan aproximadamente y se pueden ajustar según la situación real
porcentajes = [23.8, 17.3, 15.3, 7.7, 6.5, 5.8, 4.0, 3.0, 2.9, 2.2]

x = np.arange(len(marcas))  # Posiciones de las marcas en el eje x

fig, ax = plt.subplots()

# Dibujar un gráfico de barras con un color verde similar
barras = ax.bar(x, porcentajes, color='greenyellow')

# Agregar un título
ax.set_title('Marcas de gafas AI conocidas por los encuestados generales (TOP10)')

# Establecer las etiquetas de las marcas en el eje x
ax.set_xticks(x)
ax.set_xticklabels(marcas, rotation=45, ha='right')  # Rotar las etiquetas para evitar solapamiento

# Agregar etiquetas numéricas a cada barra
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer la etiqueta del eje y (se puede agregar según sea necesario)
ax.set_ylabel('Porcentaje de la marca (%)')

plt.tight_layout()  # Ajustar automáticamente el diseño para evitar solapamiento de etiquetas
plt.show()