import matplotlib.pyplot as plt
import numpy as np

# Nombres de las series de televisión
labels = ["La Justicia del Pueblo", "Yo Soy el Maestro del Destino", "Funcionarios del Estado", "Acción Pública del Estado", "Poder Absoluto"]
# Porcentaje de hombres
male_percents = [64, 70, 70, 74, 75]
# Porcentaje de mujeres
female_percents = [36, 30, 30, 26, 25]

x = np.arange(len(labels))  # Posiciones en el eje x
width = 0.35  # Ancho de las barras

fig, ax = plt.subplots(figsize=(8, 5))
# Dibujar las barras del porcentaje de hombres
rects_male = ax.barh(x - width/2, male_percents, width, label='Hombres', color='#8B4513')  
# Dibujar las barras del porcentaje de mujeres
rects_female = ax.barh(x + width/2, female_percents, width, label='Mujeres', color='red')  

# Agregar etiquetas y título
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.set_xlabel('Porcentaje (%)')
ax.set_title('Análisis de género de usuarios de series de televisión populares')
ax.legend()

# Agregar etiquetas de valores a las barras
def label_bars(rects):
    for rect in rects:
        length = rect.get_width()
        ax.text(length + 1, rect.get_y() + rect.get_height()/2,
                f'{length}%', va='center')

label_bars(rects_male)
label_bars(rects_female)

plt.tight_layout()
plt.show()