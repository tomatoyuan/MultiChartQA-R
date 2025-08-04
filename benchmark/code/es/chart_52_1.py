import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
elementos = [
    {"nombre": "Aprender Cursos Profesionales", "porcentaje": 69.3, "color": "#a8e6cf"},
    {"nombre": "Completar la Tesis de Graduación", "porcentaje": 64.0, "color": "#dcedc1"},
    {"nombre": "Obtener Experiencia en Prácticas", "porcentaje": 51.1, "color": "#ffd3b6"},
    {"nombre": "Realizar Exámenes Externos", "porcentaje": 50.8, "color": "#c8e6c9"},
    {"nombre": "Participar en Prácticas en el Campus", "porcentaje": 42.5, "color": "#e8eaf6"},
]

# Coordenadas de los nodos del camino
coordenadas_nodos = [
    (0.1, 0.8),   # Aprender Cursos Profesionales
    (0.3, 0.65),  # Completar la Tesis de Graduación
    (0.5, 0.5),   # Obtener Experiencia en Prácticas
    (0.7, 0.6),   # Realizar Exámenes Externos
    (0.9, 0.3),   # Participar en Prácticas en el Campus
]

# Orden de conexión
conexiones = [(0, 1), (1, 2), (2, 3), (3, 4)]

fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Dibujar conexiones
for inicio, fin in conexiones:
    x1, y1 = coordenadas_nodos[inicio]
    x2, y2 = coordenadas_nodos[fin]
    ax.plot([x1, x2], [y1, y2], color='gray', linestyle='--', linewidth=1.5)

# Dibujar burbujas y texto
for i, elemento in enumerate(elementos):
    x, y = coordenadas_nodos[i]

    # Dibujar burbuja
    burbuja = plt.Circle((x + 0.05, y), 0.05, color=elemento["color"], zorder=2)
    ax.add_artist(burbuja)

    # Dibujar texto
    texto = f"{elemento['porcentaje']}%\n{elemento['nombre']}"
    ax.text(x + 0.12, y, texto,
            ha='left', va='center',
            fontsize=10, color='black')

# Título
ax.text(0.5, 0.92, "Las 5 Cosas Más Importantes en la Universidad",
        ha='center', va='center',
        fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()