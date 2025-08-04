import matplotlib.pyplot as plt
import numpy as np

# Datos
años = [f"{y} 01" for y in range(2014, 2025)]
usuarios = [1869, 2094, 2320, 2804, 3212, 3478, 3726, 4214, 4632, 4770, 5036]
crecimiento = [12.0, 10.8, 20.9, 14.5, 8.3, 7.1, 13.1, 9.9, 3.0, 5.6]

fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Dibujar el gráfico de barras
barras = ax.bar(años, usuarios, color='#419D83', width=0.6)

# Agregar etiquetas de número de usuarios en la parte superior de las barras
for barra, valor in zip(barras, usuarios):
    ax.text(barra.get_x() + barra.get_width()/2, valor + 100,
            f"{valor:,}", ha='center', va='bottom', color='white', fontsize=11)

# Agregar etiquetas de tasa de crecimiento (simuladas con un círculo de fondo blanco)
for i, (barra, pct) in enumerate(zip(barras[1:], crecimiento)):
    # x = barra.get_x() + barra.get_width() / 2
    x = barra.get_x() - barra.get_width() / 3
    y = 200  # Establecer en la parte inferior sin comprimir el gráfico principal
    ax.text(x, y, f"+{pct:.1f}%", ha='center', va='center',
            fontsize=10, color='black',
            bbox=dict(boxstyle="circle,pad=0.3", facecolor='white', edgecolor='none'))

# Mejorar los ejes
ax.set_ylim(0, 5500)
ax.set_xlim(-0.5, len(años)-0.5)
ax.set_yticks([])
ax.set_xticks(np.arange(len(años)))
ax.set_xticklabels(años, color='white', fontsize=11)
ax.spines[['left', 'top', 'right']].set_visible(False)
ax.spines['bottom'].set_color('white')
ax.tick_params(axis='x', colors='white')

# Caja del título principal en la esquina superior izquierda
plt.text(-0.5, 5300, "202401", fontsize=12, color='white',
         bbox=dict(facecolor='#1E6E57', boxstyle="round,pad=0.4"))
plt.title("Número de usuarios de redes sociales a lo largo de los años", fontsize=16, color='white', loc='left', pad=20)

# Fuente de los datos
plt.text(-0.5, -600, "*Fuente de datos: We Are Social", color='white', fontsize=10)

plt.tight_layout()
plt.show()