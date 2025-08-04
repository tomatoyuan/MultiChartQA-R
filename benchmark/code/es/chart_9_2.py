import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, PathPatch
from matplotlib.path import Path

# Configuración de datos (combinar grupos de género y edad)
data = {
    "genero": {
        "grupos": ["Hombre", "Mujer"],
        "tgi": [120, 93],
        "color_exterior": "#D9D9D9",  # Color del anillo dentado exterior
        "colores_interiores": ["#4CAD8F", "#4CAD8F"],  # Colores del círculo interior (oscuro para hombres, claro para mujeres)
        "titulo": "Por género",
        "posicion_etiqueta": [(-2.2, 0.5), (2.2, 0.5)],  # Posiciones de las etiquetas (distribuidas a la izquierda y derecha)
        "anotacion": "Atención (TGI)"  # Texto de anotación
    },
    "edad": {
        "grupos": ["18-24", "25-34", "35-44", ">45 años"],
        "tgi": [104, 117, 95, 82],
        "color_exterior": "#D9D9D9",  # Color del anillo dentado exterior
        "colores_interiores": ["#4DA6FF", "#4DA6FF", "#4DA6FF", "#4DA6FF"],  # Azul
        "titulo": "Por grupo de edad",
        "posicion_etiqueta": [(-2.2, 1.2), (2.2, 1.2), (-2.2, -0.8), (2.2, -1.8)],  # Posiciones de las etiquetas
        "anotacion": ""  # No repetir la anotación para los grupos de edad
    }
}

# Crear un lienzo (ajustar la altura para acomodar dos grupos)
fig = plt.figure(figsize=(6, 8), facecolor='white')  # Aumentar la altura del lienzo
ax = fig.add_subplot(111)

# Función principal para dibujar un marco exterior dentado
def dibujar_anillo_dentado(centro, radio, color, num_dientes=30):
    """
    Dibujar un marco exterior fijo con dientes
    :param centro: Coordenadas del centro del círculo (x, y)
    :param radio: Radio del marco exterior
    :param color: Color del marco exterior
    :param num_dientes: Número de dientes (controla la estética)
    """
    theta = np.linspace(0, 2 * np.pi, num_dientes * 2, endpoint=False)
    radios = np.array([radio, radio * 0.95] * num_dientes)
    datos_camino = []
    for t, r in zip(theta, radios):
        x = centro[0] + r * np.cos(t)
        y = centro[1] + r * np.sin(t)
        datos_camino.append((Path.MOVETO if t == 0 else Path.LINETO, (x, y)))
    
    # Cerrar el camino
    datos_camino.append((Path.CLOSEPOLY, (centro[0], centro[1])))
    codigos, vertices = zip(*datos_camino)
    camino = Path(vertices, codigos)
    parche = PathPatch(camino, facecolor='none', edgecolor=color, lw=2)
    ax.add_patch(parche)

# Función para dibujar un círculo interior dinámico
def dibujar_circulo_interior_dinamico(centro, tgi, color, max_tgi=120):
    """
    Dibujar un círculo interior que cambia dinámicamente con el TGI
    :param centro: Coordenadas del centro del círculo (x, y)
    :param tgi: Valor del TGI
    :param color: Color del círculo interior
    :param max_tgi: TGI máximo (utilizado para la normalización)
    """
    # Calcular el radio del círculo interior según la proporción del TGI
    proporcion_radio = np.sqrt(tgi / max_tgi)
    radio_base = 0.9  # Radio base (en relación con el radio del marco exterior de 1.0)
    radio = radio_base * proporcion_radio
    
    circulo_interior = Circle(centro, radio, color=color, zorder=2)
    ax.add_artist(circulo_interior)
    
    # Agregar texto del TGI
    ax.text(
        centro[0], centro[1], 
        f"{tgi}", 
        ha='center', 
        va='center', 
        fontsize=14, 
        fontweight='bold', 
        color='#333333',
        zorder=3
    )

# Función para dibujar una línea separadora
def dibujar_linea_separadora(y_pos, longitud=6, color='#E0E0E0', estilo_linea='-', ancho_linea=1.5):
    """
    Dibujar una línea separadora horizontal
    :param y_pos: Posición de la coordenada Y de la línea separadora
    :param longitud: Longitud de la línea separadora
    :param color: Color de la línea separadora
    :param estilo_linea: Estilo de la línea
    :param ancho_linea: Ancho de la línea
    """
    x_inicio = -longitud / 2
    x_fin = longitud / 2
    ax.plot([x_inicio, x_fin], [y_pos, y_pos], color=color, linestyle=estilo_linea, linewidth=ancho_linea, zorder=1)

# Dibujar todos los grupos
for tipo_grupo, datos_grupo in data.items():
    # Desplazamiento vertical (grupo de género arriba, grupo de edad abajo)
    desplazamiento_y = -3.5 if tipo_grupo == "edad" else 0  # Ajustar el desplazamiento vertical
    
    # Dibujar todos los círculos para cada grupo
    for i, (grupo, tgi, color) in enumerate(zip(
        datos_grupo["grupos"], 
        datos_grupo["tgi"], 
        datos_grupo["colores_interiores"]
    )):
        # Calcular la posición del centro (alternar izquierda y derecha)
        centro = (1.5 if i % 2 == 1 else -1.5, desplazamiento_y + (1.0 if i < 2 else -1.0))
        
        # Dibujar el marco exterior dentado
        dibujar_anillo_dentado(centro, radio=1.0, color=datos_grupo["color_exterior"])
        
        # Dibujar el círculo interior dinámico
        dibujar_circulo_interior_dinamico(centro, tgi, color)
        
        # Agregar etiquetas de grupo
        etiqueta_x, etiqueta_y = datos_grupo["posicion_etiqueta"][i]
        ax.text(
            etiqueta_x, etiqueta_y + desplazamiento_y, 
            grupo, 
            ha='center', 
            va='center', 
            fontsize=12, 
            fontweight='bold', 
            color='#333333',
            bbox=dict(facecolor='white', edgecolor='none', pad=2),
            zorder=4
        )
    
    # Mover el título del grupo hacia arriba
    titulo_y = 2.5 + desplazamiento_y
    ax.text(
        -2.5, titulo_y, 
        datos_grupo["titulo"], 
        ha='left', 
        va='center', 
        fontsize=16, 
        fontweight='bold', 
        color='#333333',
        zorder=5
    )
    
    # Mover la flecha de anotación hacia arriba
    if datos_grupo["anotacion"]:
        ax.annotate(
            datos_grupo["anotacion"], 
            xy=(-0.5, 0.5 + desplazamiento_y), 
            xytext=(-1.2, 1.8 + desplazamiento_y),
            arrowprops=dict(arrowstyle='->', color='#666666'),
            fontsize=12, 
            color='#666666',
            zorder=6
        )

# Agregar el título general
ax.text(
    0, 4.0,  # Mover el título general hacia arriba
    "Atención a las nuevas marcas chinas por género y grupo de edad (TGI)", 
    ha='center', 
    va='center', 
    fontsize=18, 
    fontweight='bold', 
    color='#333333',
    zorder=7
)

# Mover el texto de descripción inferior hacia abajo
ax.text(
    0, -8.0,  # Mover el texto inferior más hacia abajo
    "TGI: Mide la atención. Un valor superior a 100 indica que la atención del grupo de usuarios es mayor que el nivel promedio.\n"
    "El área del círculo es proporcional al valor del TGI", 
    ha='center', 
    va='center', 
    fontsize=12, 
    color='#666666',
    zorder=8
)

# Dibujar tres líneas separadoras
dibujar_linea_separadora(y_pos=3.0)  # Separar el título y el grupo de género
dibujar_linea_separadora(y_pos=-0.5)  # Separar el grupo de género y el grupo de edad
dibujar_linea_separadora(y_pos=-6.4)  # Separar el grupo de edad y la anotación inferior

# Establecer el rango de los ejes
ax.set_xlim(-3, 3)
ax.set_ylim(-9, 4.5)  # Expandir el rango del eje Y para acomodar todo el contenido
ax.axis('off')  # Ocultar los ejes

# Ajustar el diseño
plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.25)
plt.show()