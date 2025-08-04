import matplotlib.pyplot as plt
import numpy as np

# Categorías de escala empresarial y sus datos de proporción
etiquetas = ["Empresas pequeñas", "Empresas medianas", "Microempresas", "Empresas grandes"]
tamaños = [60.47, 25.64, 10.47, 3.42]
# Colores correspondientes
colores = ['blue', 'green', 'orange', 'purple']
# Información descriptiva para cada categoría (utilizada para las anotaciones)
descripciones = [
    "Empresas pequeñas (Número de empleados: 20 ≤ X < 300 o Ingreso operativo: 300 ≤ Y < 2000 millones de yuanes)",
    "Empresas medianas (Número de empleados: 300 ≤ X < 1000 o Ingreso operativo: 2000 ≤ Y < 40000 millones de yuanes)",
    "Microempresas (Número de empleados: X < 20 o Ingreso operativo: Y < 300 millones de yuanes)",
    "Empresas grandes (Número de empleados: X ≥ 1000 o Ingreso operativo: Y ≥ 40000 millones de yuanes)"
]

# Construir las coordenadas de los vértices del polígono del gráfico de embudo (simulación aproximada, se puede ajustar según sea necesario)
# Suponer que el embudo es simétrico horizontalmente y se divide en capas verticalmente
posiciones_y = [0.8, 0.6, 0.4, 0.2]  # Posiciones verticales de cada capa
anchos = [1, 0.6, 0.3, 0.1]  # Anchos de cada capa, disminuyendo de arriba hacia abajo para simular un embudo
lista_vertices = []
for y, w in zip(posiciones_y, anchos):
    izquierda = -w / 2
    derecha = w / 2
    vertices = [(izquierda, y), (derecha, y), (derecha, y - 0.1), (izquierda, y - 0.1)]
    lista_vertices.append(vertices)

fig, ax = plt.subplots(figsize=(10, 6))

for i in range(len(lista_vertices)):
    # Dibujar cada capa del polígono (capas del embudo)
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
ax.set_title('Escala de las empresas de transformación digital chinas en 2025')

plt.tight_layout()
plt.show()