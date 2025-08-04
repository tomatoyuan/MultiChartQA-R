import matplotlib.pyplot as plt
import numpy as np

# Escenarios de uso
escenarios = [
    "Ir y volver del trabajo", "Recoger y dejar a los niños", "Tour en automóvil de corta distancia",
    "Reunirse con familiares y amigos", "Ir de compras en centros comerciales/supermercados", "Tour en automóvil de larga distancia", "Visitar a familiares de larga distancia"
]
# Datos de proporción simulados (lo más cercano posible a la figura original)
porcentajes = [67.8, 61.2, 59.6, 45.6, 44.7, 44.0, 32.7]
# Configuración de color (verde cercano a la figura original)
color = "#A4C639"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(escenarios))
altura_barra = 0.6
barras = ax.barh(y, porcentajes, height=altura_barra, color=color)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + altura_barra/2),
                xytext=(5, 0),  # Posición de la etiqueta: desplazamiento de 5 hacia la derecha
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(escenarios)
# Establecer las marcas del eje x (0 - 70%)
ax.set_xlim(0, 70)
# Establecer el título
ax.set_title("Escenarios de uso de vehículos MPV", fontsize=14, fontweight="bold")

# Ocultar los bordes superior y derecho
for espina in ["top", "right"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()
plt.show()