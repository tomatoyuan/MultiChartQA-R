import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
etiquetas = ["Gráfico", "Video corto", "Transmisión en vivo", "Actividad fuera de línea", "Curso de voz"]
porcentajes = [81.9, 75.5, 40.3, 40.4, 27.9]
colores = ["#FFA500"] * len(etiquetas)  # Naranja uniforme

# Inicializar el gráfico
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 100)
ax.set_ylim(0, len(etiquetas) * 2)
ax.set_axis_off()  # Ocultar los ejes

for i, (etiqueta, porc, color) in enumerate(zip(etiquetas, porcentajes, colores)):
    # Dibujar la barra de progreso naranja
    ax.barh(i * 2 + 1, porc, height=1.5, left=15, color=color, alpha=0.8)
    # Dibujar la etiqueta
    ax.text(10, i * 2 + 1.75, etiqueta, fontsize=12, va="center")
    # Dibujar el valor del porcentaje
    ax.text(15 + porc + 2, i * 2 + 1.75, f"{porc}%", fontsize=12, va="center", ha="left")

ax.set_title("Preferencias de formatos de información de la población china en etapa de planificación de embarazo en 2023", fontsize=14, y=1.05)
plt.tight_layout()
plt.show()