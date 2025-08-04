import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# -------------------- Definición de Datos --------------------
# Información de nodos: nombre, porcentaje, color
nodos = [
    {"name": "Texto corto e imagen", "percent": 82.9, "color": "#a5d65d", "desc": "Como publicar estados diarios, fotos favoritas, emoticonos/GIFs de Internet"},
    {"name": "Video corto/mini - video", "percent": 74.0, "color": "#81c784", "desc": "Contenido de video de aproximadamente 5 minutos o menos"},
    {"name": "Texto largo", "percent": 33.2, "color": "#4dd0e1", "desc": "Publicaciones de blog largas, novelas en línea, artículos de cuentas oficiales, etc."},
    {"name": "Música y audio", "percent": 25.8, "color": "#ffe082", "desc": "Como música original, covers de karaoke, producción de programas de audio, etc."},
    {"name": "Video de duración mediana - larga", "percent": 29.1, "color": "#87de87", "desc": "Más de 5 minutos, como vlogs de vida, compartir experiencias, etc."}
]

# Relaciones de conexión (simulando una conexión circular)
aristas = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 0)
]

# -------------------- Crear Estructura de Grafo --------------------
G = nx.Graph()
# Agregar nodos
for i, nodo in enumerate(nodos):
    G.add_node(i, 
               name=nodo["name"], 
               percent=nodo["percent"], 
               color=nodo["color"],
               desc=nodo["desc"])
# Agregar aristas
G.add_edges_from(aristas)

# -------------------- Configuración de Diseño (Diseño Circular) --------------------
pos = nx.circular_layout(G, scale=0.8)  # Diseño circular, aumentar la escala para dispersar los nodos

# -------------------- Crear Canvas --------------------
fig, ax = plt.subplots(figsize=(8, 8))

# -------------------- Dibujar Nodos (con color y tamaño) --------------------
tamaños_nodos = [n["percent"] * 48 for n in nodos]  # El tamaño del nodo está positivamente correlacionado con el porcentaje
colores_nodos = [n["color"] for n in nodos]

nx.draw_networkx_nodes(
    G, pos,
    node_size=tamaños_nodos,
    node_color=colores_nodos,
    alpha=0.8,
    ax=ax
)

# -------------------- Dibujar Aristas (Líneas de Conexión Grises) --------------------
nx.draw_networkx_edges(
    G, pos,
    width=2,
    edge_color="#cccccc",
    ax=ax
)

# -------------------- Agregar Anotaciones de Nodos (Nombre, Porcentaje, Descripción) --------------------
for i, nodo in enumerate(nodos):
    # Anotar el nombre y el porcentaje (dentro del nodo)
    ax.text(
        pos[i][0], pos[i][1], 
        f"{nodo['name']}\n{nodo['percent']}%",
        ha="center", va="center",
        fontsize=8,
        color="blue",
        fontweight="bold"
    )
    # Anotar la información de descripción (fuera del nodo, ajustar el desplazamiento)
    desc_x = pos[i][0] + (1.5 if pos[i][0] > 0 else -1.5) * 0.1  # Desplazamiento horizontal
    desc_y = pos[i][1] + (1.5 if pos[i][1] > 0 else -1.5) * 0.1  # Desplazamiento vertical
    ax.text(
        desc_x, desc_y, 
        nodo["desc"],
        ha="left" if pos[i][0] > 0 else "right",
        va="center",
        fontsize=9,
        color="#424242"
    )

# -------------------- Embelezar la Gráfica --------------------
# Ocultar los ejes
ax.axis("off")

# Agregar un título
ax.set_title(
    "Tipos de Contenido Original Publicado por Usuarios de Aplicaciones de Retrato de Belleza Chinas en 2022",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()