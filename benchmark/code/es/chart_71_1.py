import matplotlib.pyplot as plt
import numpy as np

# Categorías y datos
categorias = [
    "Fabricación de artículos deportivos y productos relacionados", "Venta de artículos deportivos y productos relacionados", "Gestión de instalaciones y lugares deportivos",
    "Educación y capacitación deportiva", "Actividades de fitness y recreación deportiva", "Otros servicios deportivos",
    "Actividades de gestión deportiva", "Servicios de medios y información deportiva", "Agentes y representación deportiva",
    "Actividades de competición y actuación deportiva", "Construcción de instalaciones y lugares deportivos"
]
datos = np.array([44.9, 16.5, 7.9, 7.4, 5.8, 5.7, 3.2, 3.1, 1.2, 1.0, 3.5])

# Construir un eje de tiempo pseudo
x = np.linspace(0, 10, 100)
datos_apilados = np.array([np.ones_like(x) * v for v in datos])

# Mejora de color (colorido + suave)
colores = [
    "#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF",
    "#A0C4FF", "#BDB2FF", "#FFC6FF", "#FFFFFC", "#D0F4DE", "#B0D0D3"
]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de área apilada
apilado = ax.stackplot(x, datos_apilados, labels=categorias, colors=colores, alpha=0.95)

# Calcular la posición de altura media (para agregar texto)
suma_acumulada = np.cumsum(datos_apilados, axis=0)
altura_media = suma_acumulada - datos_apilados / 2

# Agregar texto de porcentaje, dispuesto alternativamente a la izquierda y a la derecha
for i in range(len(categorias)):
    y_media = altura_media[i, len(x) // 2]  # Obtener la altura en el punto medio
    alineacion = 'right' if i % 2 == 0 else 'left'
    x_pos = 2 if i % 2 == 0 else 8  # Distribución izquierda - derecha

    ax.text(
        x_pos, y_media,
        f"{datos[i]}% {categorias[i]}",
        fontsize=9,
        ha=alineacion,
        va='center',
        color='black',
        fontweight='bold'
    )

# Título y leyenda
ax.set_title("Composición de la industria deportiva de China en 2020 (Gráfico de área apilada)", fontsize=14, fontweight="bold", pad=20)
ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.1), fontsize=9, frameon=False)

# Embellir el gráfico
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()