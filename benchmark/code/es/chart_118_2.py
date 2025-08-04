import matplotlib.pyplot as plt
import numpy as np

# Categorías de tamaño de empresa y sus proporciones
etiquetas = ["Pequeñas empresas", "Empresas medianas", "Microempresas", "Grandes empresas"]
tamaños = [58.78, 20.35, 17.02, 3.85]
# Colores correspondientes
colores = ['blue', 'green', 'orange', 'purple']
# Información descriptiva para cada categoría (usada para las anotaciones)
descripciones = [
    "Pequeñas empresas (Número de empleados: 20 ≤ X < 300 o Ingreso operativo: 300 ≤ Y < 2000 millones de yuanes)",
    "Empresas medianas (Número de empleados: 300 ≤ X < 1000 o Ingreso operativo: 2000 ≤ Y < 40000 millones de yuanes)",
    "Microempresas (Número de empleados < 20 o Ingreso operativo < 300 millones de yuanes)",
    "Grandes empresas (Número de empleados X ≥ 1000 o Ingreso operativo Y ≥ 40000 millones de yuanes)"
]

fig, ax = plt.subplots(figsize=(10, 7))
# Construir las coordenadas de los vértices del polígono del gráfico de embudo (simulación aproximada, se puede ajustar según sea necesario)
# Suponemos que el embudo es simétrico horizontalmente y basado en capas verticales
posiciones_y = [0.8, 0.6, 0.4, 0.2]  # Posiciones verticales de cada capa
anchos = [1, 0.6, 0.3, 0.1]  # Anchos de cada capa, decreciendo para simular un embudo
lista_vertices = []
for i in range(len(etiquetas)):
    y = posiciones_y[i]
    w = anchos[i]
    izquierda = -w / 2
    derecha = w / 2
    vertices = [(izquierda, y), (derecha, y), (derecha, y - 0.1), (izquierda, y - 0.1)]
    lista_vertices.append(vertices)

# Dibujar cada capa del polígono y agregar anotaciones
for i in range(len(etiquetas)):
    poligono = plt.Polygon(lista_vertices[i], color=colores[i])
    ax.add_patch(poligono)
    # Agregar anotaciones de proporción y descripción, ubicadas en el centro de la capa
    centro_x = 0
    centro_y = posiciones_y[i] - 0.05
    ax.text(centro_x, centro_y, f'{etiquetas[i]}\n{descripciones[i]}\nProporción: {tamaños[i]}%',
            ha='center', va='center', fontsize=9)

ax.set_xlim(-0.6, 0.6)
ax.set_ylim(0, 1)
ax.axis('off')  # Ocultar los ejes
ax.set_title('Tamaño de las empresas entre los usuarios de humanos digitales AI en China en 2025')

plt.tight_layout()
plt.show()