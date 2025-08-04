import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2007", "2009", "2011", "2013", "2015", "2017", "2019"]
# Proporciones de diversos destinos (datos simulados, tratando de aproximar la tendencia en el gráfico original)
empleo = [54, 46, 56, 55, 59, 58, 51]    # Empleo
estudios_avanzados = [20, 25, 19, 19, 27, 29, 33] # Estudios avanzados o intención de continuar estudios
esperando = [26, 30, 25, 26, 15, 13, 16]       # Esperando empleo y otros

# Configuración de colores (tratando de aproximar el gráfico original)
colors = ["#A4C639", "#8EBF8F", "#87CEEB"]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras apiladas
bottom = np.zeros(len(years))
for i, (label, data, color) in enumerate(zip(["Empleo", "Estudios avanzados o intención de continuar estudios", "Esperando empleo y otros"], 
                                            [empleo, estudios_avanzados, esperando], 
                                            colors)):
    ax.bar(years, data, bottom=bottom, color=color, label=label)
    bottom += data

    # Agregar etiquetas de datos
    for x, y in zip(years, data):
        ax.annotate(f'{y}%',
                    xy=(x, bottom[i] - y/2),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

# Establecer la escala del eje y (0 - 100%)
ax.set_ylim(0, 100)
# Establecer el título
ax.set_title("Destinos de graduación de estudiantes universitarios chinos desde 2007 hasta 2019", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend(loc='lower right')

# Embelezar: Ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()