import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Años y categorías de vacaciones
years = ["2020", "2021", "2022"]
holidays_2020 = ["Festival de Rastrillo", "Día del Trabajo", "Festival del Bote del Dragón", "Festival del Medio Otoño y Día Nacional", "Fiesta de la Primavera"]
holidays_2021 = ["Fiesta de la Primavera", "Festival de Rastrillo", "Día del Trabajo", "Festival del Bote del Dragón", "Festival del Medio Otoño", "Día Nacional"]
holidays_2022 = ["Fiesta de la Primavera", "Festival de Rastrillo", "Día del Trabajo", "Festival del Bote del Dragón"]

# Datos
revenue_2020 = [19.3, 32.3, 31.2, 69.9, 56.7]
revenue_2021 = [77.0, 74.8, 78.6, 59.9, 56.3, 68.0]
revenue_2022 = [36.2, 44.0, 65.6, 58.0]

person_times_2020 = [38.6, 47.2, 50.9, 79.0, 94.5]
person_times_2021 = [103.2, 98.7, 87.2, 70.1, 73.9, 85.0]
person_times_2022 = [68.0, 66.8, 86.8, 75.0]

# Crear figura y subgráficos con tamaño ajustado
fig, axes = plt.subplots(1, 3, figsize=(15, 6), sharey=False)
fig.suptitle("Recuperación de los datos turísticos de cada fiesta desde 2020 hasta 2022", fontsize=14, fontweight="bold", y=0.95)

# Graficar datos de 2020
ax_2020 = axes[0]
x_2020 = np.arange(len(holidays_2020))
ax_2020.plot(x_2020, revenue_2020, marker='o', color='#A4C639', 
             label='Recuperación de los ingresos turísticos respecto a 2019 (%)', linewidth=2)
ax_2020.plot(x_2020, person_times_2020, marker='o', color='#64B5F6', 
             label='Recuperación de las visitas turísticas respecto a 2019 (%)', linewidth=2)
ax_2020.set_xticks(x_2020)
ax_2020.set_xticklabels(holidays_2020, rotation=45, ha='right', fontsize=9)
ax_2020.set_title("2020")
ax_2020.yaxis.set_major_locator(MaxNLocator(integer=True))  # Asegurar marcas enteras

# Agregar etiquetas de datos de 2020
for x, y1, y2 in zip(x_2020, revenue_2020, person_times_2020):
    ax_2020.annotate(f'{y1}%', (x, y1), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)
    ax_2020.annotate(f'{y2}%', (x, y2), textcoords="offset points", xytext=(0, -12), ha='center', color='#64B5F6', fontsize=8)

# Graficar datos de 2021
ax_2021 = axes[1]
x_2021 = np.arange(len(holidays_2021))
ax_2021.plot(x_2021, revenue_2021, marker='o', color='#A4C639', linewidth=2)
ax_2021.plot(x_2021, person_times_2021, marker='o', color='#64B5F6', linewidth=2)
ax_2021.set_xticks(x_2021)
ax_2021.set_xticklabels(holidays_2021, rotation=45, ha='right', fontsize=9)
ax_2021.set_title("2021")
ax_2021.yaxis.set_major_locator(MaxNLocator(integer=True))

# Agregar etiquetas de datos de 2021
for x, y1, y2 in zip(x_2021, revenue_2021, person_times_2021):
    ax_2021.annotate(f'{y1}%', (x, y1), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)
    ax_2021.annotate(f'{y2}%', (x, y2), textcoords="offset points", xytext=(0, -12), ha='center', color='#64B5F6', fontsize=8)

# Graficar datos de 2022
ax_2022 = axes[2]
x_2022 = np.arange(len(holidays_2022))
ax_2022.plot(x_2022, revenue_2022, marker='o', color='#A4C639', linewidth=2)
ax_2022.plot(x_2022, person_times_2022, marker='o', color='#64B5F6', linewidth=2)
ax_2022.set_xticks(x_2022)
ax_2022.set_xticklabels(holidays_2022, rotation=45, ha='right', fontsize=9)
ax_2022.set_title("2022")
ax_2022.yaxis.set_major_locator(MaxNLocator(integer=True))

# Agregar etiquetas de datos de 2022
for x, y1, y2 in zip(x_2022, revenue_2022, person_times_2022):
    ax_2022.annotate(f'{y1}%', (x, y1), textcoords="offset points", xytext=(0, 5), ha='center', fontsize=8)
    ax_2022.annotate(f'{y2}%', (x, y2), textcoords="offset points", xytext=(0, -12), ha='center', color='#64B5F6', fontsize=8)

# Agregar cuadro de información
ax_info = fig.add_axes([0.82, 0.8, 0.15, 0.2])
ax_info.axis('off')
ax_info.text(0, 1, "H1 2022 VS. H1 2021", fontsize=10, fontweight='bold')
ax_info.text(0, 0.8, "Turismo de residentes urbanos: -16.6%", color='#64B5F6', fontsize=9)
ax_info.text(0, 0.6, "Turismo de residentes rurales: -35.4%", color='#E57373', fontsize=9)

# Combinar leyendas
lines, labels = axes[0].get_legend_handles_labels()
fig.legend(lines, labels, loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.11), fontsize=10)

# Ocultar bordes superior y derecho de todos los ejes
for ax in axes:
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

# Ajustar el diseño
plt.subplots_adjust(left=0.05, right=0.8, bottom=0.2, top=0.85, wspace=0.3)
plt.show()