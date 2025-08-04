import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
etiquetas = ["Cine/Conciertos al aire libre", "Salones de networking", "Rincón de idiomas", "Baile"]
porcentajes = [76.4, 67.7, 40.3, 27.3]
# Usar texto para simular iconos (puedes personalizar símbolos más apropiados)
iconos = ["Cine/Conciertos al aire libre", "Salones de networking", "Rincón de idiomas", "Baile"]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, len(etiquetas) * 2)
ax.set_axis_off()

for i, (etiqueta, perc, icono) in enumerate(zip(etiquetas, porcentajes, iconos)):
    # Dibujar el icono (en forma de texto)
    # ax.text(10, i * 2 + 1, icono, fontsize=20, va="center")
    # Dibujar la etiqueta
    ax.text(20, i * 2 + 1, etiqueta, fontsize=12, va="center")
    # Dibujar el porcentaje
    ax.text(90, i * 2 + 1, f"{perc}%", fontsize=12, va="center", ha="right")
    # Dibujar la barra de progreso
    ax.barh(i * 2 + 1, perc, left=20, height=1.5, color="#FF9933", alpha=0.8)

ax.set_title("Expectativas de los principales grupos de consumo en las zonas universitarias chinas para la adición\n de servicios de valor en los distritos comerciales de las zonas universitarias en el futuro en 2023", fontsize=14, y=1.05)
plt.tight_layout()
plt.show()