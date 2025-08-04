import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Número de juegos/aplicaciones no VR
no_vr = [3935, 5844, 8028, 7522, 8924, 10827, 11620, 13765]
# Número de juegos/aplicaciones VR
vr = [735, 1105, 872, 612, 822, 562, 945, 689]

x = np.arange(len(años))

fig, ax = plt.subplots(figsize=(12, 7))

# Dibujar la parte no VR (naranja)
ax.bar(x, no_vr, color='orange', label='Juegos/Aplicaciones no VR')
# Dibujar la parte VR (amarillo, apilada sobre la no VR)
ax.bar(x, vr, bottom=no_vr, color='gold', label='Juegos/Aplicaciones VR')

# Añadir etiquetas para la cantidad no VR
for i, nv in enumerate(no_vr):
    ax.text(i, nv / 2, f'{nv}', ha='center', va='center', color='white')

# Añadir etiquetas para la cantidad VR
for i, v in enumerate(vr):
    ax.text(i, no_vr[i] + v / 2, f'{v}', ha='center', va='center', color='black')

ax.set_ylabel('Cantidad (unidades)')
ax.set_xlabel('Año')
ax.set_xticks(x)
ax.set_xticklabels(años)
ax.legend()
ax.set_title('Número de juegos/aplicaciones recién agregados en la plataforma Steam anualmente desde 2016 - 2023')

plt.tight_layout()
plt.show()