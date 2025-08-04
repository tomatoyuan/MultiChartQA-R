import matplotlib.pyplot as plt
import numpy as np

# Años
años = [2007, 2013, 2017, 2020]
tasas_diabetes = [9.7, 10.4, 11.2, 11.9]
tasas_colesterol = [3.1, 6.0, 8.0, 8.2]

# Configuración de colores
color_diabetes = "#6ab04c"      # Verde oliva suave
color_colesterol = "#45aaf2"   # Azul claro brillante

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar el gráfico de área
ax.fill_between(
    años, tasas_diabetes, 
    color=color_diabetes, alpha=0.3, label="Prevalencia de diabetes entre adultos (%)"
)
ax.plot(años, tasas_diabetes, color=color_diabetes, linewidth=2.5, marker="o")

ax.fill_between(
    años, tasas_colesterol, 
    color=color_colesterol, alpha=0.3, label="Prevalencia de hipercolesterolemia entre adultos (%)"
)
ax.plot(años, tasas_colesterol, color=color_colesterol, linewidth=2.5, marker="o")

# Agregar etiquetas de datos
for x, y in zip(años, tasas_diabetes):
    ax.text(x, y - 0.8, f"{y}%", ha='center', va='bottom', fontsize=10, color=color_diabetes)

for x, y in zip(años, tasas_colesterol):
    ax.text(x, y - 0.8, f"{y}%", ha='center', va='top', fontsize=10, color=color_colesterol)

# Configurar los ejes
ax.set_xticks(años)
ax.set_ylabel("Prevalencia (%)")
ax.set_title("Prevalencia de diabetes e hipercolesterolemia entre adultos chinos de 2007 a 2020", fontsize=14, fontweight='bold')

# Leyenda
ax.legend(loc="upper left", fontsize=10)

# Mejorar la apariencia
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.grid(alpha=0.2)

plt.tight_layout()
plt.show()