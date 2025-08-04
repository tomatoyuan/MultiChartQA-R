import matplotlib.pyplot as plt
import numpy as np

# Nombres de las empresas
empresas = [
    "SAIC Motor", "BYD", "Great Wall Motor", "Changan Automobile", 
    "GAC Group", "FAW Jiefang", "Foton Motor", "Jianghuai Automobile", 
    "CNHTC", "SERES"
]
# Ingresos en 2022 (en decenas de miles de millones de yuanes)
ingresos_2022 = [74.41, 42.41, 13.73, 12.13, 11.03, 3.83, 4.64, 3.66, 2.88, 3.41]
# Ingresos en 2023 (en decenas de miles de millones de yuanes)
ingresos_2023 = [74.47, 60.23, 17.32, 15.13, 12.97, 6.39, 5.61, 4.50, 4.21, 3.58]
# Tasas de crecimiento (%)
tasas_de_crecimiento = [0.09, 42.04, 26.12, 24.78, 17.62, 66.71, 20.78, 23.07, 45.96, 5.09]

x = np.arange(len(empresas))

fig, ax = plt.subplots(figsize=(14, 8))

# Dibujar el gráfico de barras de ingresos para 2022 (naranja)
ax.bar(x - 0.2, ingresos_2022, width=0.4, color='orange', label='Ingresos en 2022 (en decenas de miles de millones de yuanes)')
# Dibujar el gráfico de barras de ingresos para 2023 (azul)
ax.bar(x + 0.2, ingresos_2023, width=0.4, color='blue', label='Ingresos en 2023 (en decenas de miles de millones de yuanes)')

# Agregar etiquetas de valor de ingresos para 2022
for i, ing in enumerate(ingresos_2022):
    ax.text(x[i] - 0.2, ing + 0.5, f'{ing}', ha='center', va='bottom')

# Agregar etiquetas de valor de ingresos para 2023
for i, ing in enumerate(ingresos_2023):
    ax.text(x[i] + 0.2, ing + 0.5, f'{ing}', ha='center', va='bottom')

# Agregar etiquetas de valor de tasa de crecimiento (a la derecha)
for i, tasa in enumerate(tasas_de_crecimiento):
    ax.text(len(empresas) + 0.5, x[i], f'{tasa}%', ha='center', va='center', color='black')
    # Dibujar una flecha hacia arriba (simplificada como una flecha de texto, o usar matplotlib.patches para dibujar una flecha gráfica)
    ax.text(len(empresas) + 0.2, x[i], '↑', ha='center', va='center', color='orange', fontsize=16)

ax.set_ylabel('Ingresos (en decenas de miles de millones de yuanes)')
ax.set_xlabel('Nombres de las empresas')
ax.set_xticks(x)
ax.set_xticklabels(empresas)
ax.legend()
ax.set_title('Las 10 principales empresas cotizadas de fabricación de vehículos eléctricos de la bolsa A en China en términos de ingresos operativos en 2023')

# Ajustar el rango del eje x para dejar espacio para las etiquetas de tasa de crecimiento
ax.set_xlim(-0.5, len(empresas) + 1)

plt.tight_layout()
plt.show()