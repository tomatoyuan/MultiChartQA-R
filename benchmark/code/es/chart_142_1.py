import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2018", "2019", "2020", "2021", "2022", "Primer semestre 2023"]
exportacion = [6116, 7981, 10850, 13918, 15321, 8254]  # Exportación (mil millones de yuanes)
importacion = [4441, 4922, 5370, 5319, 5278, 2771]    # Importación (mil millones de yuanes)
total = [10557, 12903, 16220, 19237, 20599, 11025] # Total de importación y exportación (mil millones de yuanes)

x = np.arange(len(años))

fig, ax = plt.subplots(figsize=(12, 7))

# Dibujar un gráfico de barras apiladas (de abajo hacia arriba: total de importación y exportación, importación, exportación, correspondiente al orden de la figura original)
ax.bar(x, total, color='#8B4513', label='Total de importación y exportación (mil millones de yuanes)')
ax.bar(x, importacion, bottom=total, color='#FF8C69', label='Importación (mil millones de yuanes)')
ax.bar(x, exportacion, bottom=np.array(total) + np.array(importacion), color='#FFDAB9', label='Exportación (mil millones de yuanes)')

ax.set_ylabel('Monto (mil millones de yuanes)')
ax.set_xlabel('Año')
ax.set_xticks(x)
ax.set_xticklabels(años)
ax.legend()
ax.set_title('Escala de importación y exportación del comercio electrónico transfronterizo de China desde 2018 hasta 2023')

# Agregar anotaciones numéricas (anotar los valores de total de importación y exportación, importación y exportación respectivamente)
for i in range(len(años)):
    # Anotar el valor total de importación y exportación
    ax.text(i, total[i] / 2, f'{total[i]}', ha='center', va='center', color='white', fontweight='bold')
    # Anotar el valor de importación
    ax.text(i, total[i] + importacion[i] / 2, f'{importacion[i]}', ha='center', va='center', color='white', fontweight='bold')
    # Anotar el valor de exportación
    suma_inferior = total[i] + importacion[i]
    ax.text(i, suma_inferior + exportacion[i] / 2, f'{exportacion[i]}', ha='center', va='center', color='white', fontweight='bold')

plt.tight_layout()
plt.show()