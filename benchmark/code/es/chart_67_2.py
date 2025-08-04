import matplotlib.pyplot as plt
import numpy as np

# Nombres de las industrias
industrias = ["Tecnología", "Finanzas", "Servicios Profesionales", "Manufactura", "Inmuebles", "Farmacéutica y Ciencias de la Vida"]
# Datos correspondientes (porcentaje)
datos = [33.6, 21.9, 8.8, 8.2, 6.0, 4.1]
# Configuración de colores, similar al esquema de color verde original
colores = ["#A4C639"] * len(industrias)

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(industrias))
altura_barra = 0.6
barras = ax.barh(y, datos, height=altura_barra, color=colores, edgecolor="white")

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(industrias)
# Ocultar las marcas del eje x
ax.set_xticks([])
# Establecer el título
ax.set_title("Participación de la Demanda de Arrendamiento de los Principales Inquilinos de Edificios de Oficinas en 2021", fontsize=14, fontweight="bold")

# Embellir el gráfico ocultando los bordes superior, derecho e inferior
for espina in ["top", "right", "bottom"]:
    ax.spines[espina].set_visible(False)

plt.show()