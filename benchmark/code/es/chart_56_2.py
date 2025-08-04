import matplotlib.pyplot as plt
import numpy as np

# Crear una figura y un objeto de eje
fig, ax = plt.subplots(figsize=(10, 10))
# Establecer la relación de aspecto del eje para que sea igual
ax.set_aspect('equal')
# Desactivar el eje
ax.axis('off')

# ✅ Reducir el tamaño del círculo principal
# Crear el círculo principal exterior
circulo_principal_exterior = plt.Circle((0, 0), 0.6, color='white', ec='black', lw=2.5, zorder=3)
# Crear el círculo principal interior
circulo_principal_interior = plt.Circle((0, 0), 0.45, color='white', ec='black', lw=2.5, zorder=4)
# Añadir el círculo principal exterior al eje
ax.add_artist(circulo_principal_exterior)
# Añadir el círculo principal interior al eje
ax.add_artist(circulo_principal_interior)
# Añadir texto al centro del círculo principal
ax.text(0, 0.06, '1.11 mil millones', ha='center', va='center', fontsize=17, fontweight='bold')
# Añadir texto debajo del texto central
ax.text(0, -0.22, 'Usuarios de Internet Nacionales (2024)', ha='center', fontsize=12)

# Parámetros para los sub - círculos (finamente ajustados)
posiciones = [(-1.4, 1.0), (1.4, -1.0), (-1.4, -1.0)]
colores = ['#76C7C0', '#58A4B0', '#4C8C9D']
etiquetas = ['Usuarios de videos cortos', 'Usuarios de transmisión en vivo', 'Usuarios de compras en línea']
usuarios = ['1.04 mil millones', '0.83 mil millones', '0.97 mil millones']
tasas = ['CAGR¹ = 4.5%', 'CAGR¹ = 7.8%', 'CAGR¹ = 5.6%']
porcentajes = ['× 93.8%', '× 75.2%', '× 87.9%']

r_exterior = 0.22
r_interior = 0.18

for i in range(3):
    x, y = posiciones[i]
    color = colores[i]

    # Dibujar los sub - círculos
    exterior = plt.Circle((x, y), r_exterior, color='white', ec=color, lw=2.5, zorder=3)
    interior = plt.Circle((x, y), r_interior, color='white', ec=color, lw=2.5, zorder=4)
    ax.add_artist(exterior)
    ax.add_artist(interior)

    # Dibujar la línea de conexión y añadir la proporción
    ax.plot([0, x], [0, y], color='gray', lw=1, zorder=1)
    ax.text(x * 0.5, y * 0.5, porcentajes[i], ha='center', va='center', fontsize=12, color=color)

    # Añadir descripciones para los sub - círculos
    ax.text(x, y - 0.28, usuarios[i], ha='center', va='top', fontsize=12, fontweight='bold')
    ax.text(x, y - 0.42, etiquetas[i], ha='center', va='top', fontsize=12, color=color)
    ax.text(x, y - 0.56, tasas[i], ha='center', va='top', fontsize=10)

# ✅ Mover el título hacia abajo, más cerca del centro de la figura
ax.text(0, 1.6, 'Análisis del espacio de crecimiento de los usuarios de comercio electrónico en transmisión en vivo', ha='center', fontsize=18, fontweight='bold')
ax.text(0, -2.2, '¹ CAGR: Tasa de crecimiento anual compuesto', ha='center', fontsize=10, color='gray')

# Ajustar automáticamente el diseño
plt.tight_layout()
# Mostrar el gráfico
plt.show()