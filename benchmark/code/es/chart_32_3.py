import matplotlib.pyplot as plt
import numpy as np

# Grupos de edad
grupos_edad = ['≤18 años', '19 - 24 años', '25 - 34 años', '35 - 49 años', '≥50 años']
# Datos de porcentaje de mujeres (simulados, complementados razonablemente según la tendencia del gráfico y los datos conocidos)
porcentajes_mujer = [60, 71, 57, 55, 52]
# Datos de porcentaje de hombres (simulados, complementados razonablemente según la tendencia del gráfico y los datos conocidos)
porcentajes_hombre = [40, 29, 43, 45, 48]

x = np.arange(len(grupos_edad))  # Posiciones en el eje x
ancho = 0.35  # Ancho de las barras

fig, ax = plt.subplots()
# Dibujar barras de mujeres
rects1 = ax.bar(x - ancho/2, porcentajes_mujer, ancho, label='Mujer', color='pink')
# Dibujar barras de hombres
rects2 = ax.bar(x + ancho/2, porcentajes_hombre, ancho, label='Hombre', color='blue')

# Añadir título y etiquetas
ax.set_ylabel('Porcentaje (%)')
ax.set_title('Porcentajes de hombres y mujeres que buscan "Certificado de Calificación de Maestro" en diferentes grupos de edad')
ax.set_xticks(x)
ax.set_xticklabels(grupos_edad, rotation=45, ha='right')
ax.legend()

# Anotar valores en las barras
def autolabel(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate('{}%'.format(altura),
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 3),  # Distancia vertical de la etiqueta del valor desde la barra
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()