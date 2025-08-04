import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
# Escala de financiación en China (en miles de millones de yuanes), los datos pueden ser aproximadamente los mismos
china = [0, 0, 0, 0, 0, 0, 0, 10, 30, 0]  # Datos de muestra, se pueden ajustar según la situación real
# Escala de financiación en el extranjero (en miles de millones de yuanes), los datos pueden ser aproximadamente los mismos
overseas = [1, 10, 7, 21, 11, 31, 55, 71, 277, 75]  # Datos de muestra, se pueden ajustar según la situación real

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras agrupadas (China y el extranjero apiladas)
x = np.arange(len(years))
bar_width = 0.6
# Primero dibujar el extranjero (azul)
overseas_bars = ax.bar(x, overseas, width=bar_width, color="#64B5F6", label="Escala de financiación en el extranjero (en miles de millones de yuanes)")
# Luego dibujar China (verde, apilada sobre el extranjero)
china_bars = ax.bar(x, china, width=bar_width, color="#C68439", label="Escala de financiación en China (en miles de millones de yuanes)")

# Agregar etiquetas de datos (extranjero)
for bar in overseas_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Agregar etiquetas de datos (China)
for bar in china_bars:
    height = bar.get_height()
    if height > 0:
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Ajustar la posición de la etiqueta
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='white')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(years)
# Establecer la etiqueta del eje y
ax.set_ylabel("Escala de financiación (en miles de millones de yuanes)")
# Establecer el título
ax.set_title("Escala de financiación de la industria de aprendizaje digital empresarial global desde 2013 hasta el primer semestre de 2022", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embelezar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()