import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Esquema de colores de los packs de emojis (correspondiendo estrictamente a los tipos)
mapa_colores = {
    'Emojis de celebridades': '#FF5252',
    'Emojis de texto': '#00E5FF',
    'Emojis integrados en QQ y WeChat': '#FFD740',
    'Emojis de estilo de ancianos': '#9C27B0',
    'Iconos de emojis': '#00E676',
    'Emojis de cómic': '#2979FF',
}

# Definición de datos (mantener la lógica original)
categorias = ['Emojis de celebridades', 'Emojis de texto', 'Emojis integrados en QQ y WeChat', 
              'Emojis de estilo de ancianos', 'Iconos de emojis', 'Emojis de cómic']
porcentajes = [43, 27, 21, 16, 25, 41]

# Relaciones de la cadena de desprecio (correspondencia clara de tipos para facilitar el mapeo de colores)
conexiones = [
    ('Emojis de celebridades', 'Emojis de cómic', 3.5),   # Celebridades → Cómic
    ('Emojis de cómic', 'Emojis de texto', 3),    # Cómic → Texto
    ('Emojis de texto', 'Iconos de emojis', 2.5),       # Texto → Emoji
    ('Iconos de emojis', 'Emojis integrados en QQ y WeChat', 2),    # Emoji → QQ
    ('Emojis integrados en QQ y WeChat', 'Emojis de estilo de ancianos', 1.5),  # QQ → Ancianos
]

# Crear un lienzo y configuraciones básicas
fig, ax = plt.subplots(figsize=(14, 12), facecolor='#FAFAFA')
ax.set_facecolor('#FAFAFA')
ax.grid(True, linestyle='--', alpha=0.3, color='#EEEEEE')

# Dibujar un gráfico circular (mejorar la sombra y el borde)
porciones, textos, textos_porcentaje = ax.pie(
    porcentajes, 
    labels=categorias, 
    autopct=lambda p: f'{p:.1f}%\n({int(p * sum(porcentajes) / 100)})',
    colors=[mapa_colores[c] for c in categorias],
    startangle=140,
    pctdistance=0.75,
    explode=[0.04] * 6,
    shadow=True,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'antialiased': True},
    textprops={'fontsize': 12, 'weight': 'bold', 'color': '#212121'}
)

# Máscara blanca en el centro (mejorar la sensación de jerarquía)
circulo_centro = plt.Circle((0, 0), 0.4, color='#FAFAFA', linewidth=0, zorder=1)
ax.add_artist(circulo_centro)

# Optimizar el estilo de las etiquetas de porcentaje (con un cuadro de fondo blanco)
for a in textos_porcentaje:
    a.set_bbox(dict(boxstyle="round,pad=0.3", fc="white", ec="#BDBDBD", alpha=0.85))

# Establecer el título
ax.set_title('Versión de los nacidos después del 2000: Lógica de desprecio - Relación entre celebridades y anime', 
             fontsize=22, 
             fontweight='bold', 
             color='#212121',
             pad=25)

# Dibujar flechas de la cadena de desprecio (el color corresponde estrictamente al color principal del pack de emojis)
for categoria_inicio, categoria_fin, grosor in conexiones:
    # Encontrar el ángulo del sector correspondiente
    porcion_inicio = [w for w, l in zip(porciones, categorias) if l == categoria_inicio][0]
    porcion_fin = [w for w, l in zip(porciones, categorias) if l == categoria_fin][0]
    
    angulo_inicio = (porcion_inicio.theta2 + porcion_inicio.theta1) / 2
    angulo_fin = (porcion_fin.theta2 + porcion_fin.theta1) / 2
    
    # Calcular coordenadas (radio unificado para evitar confusión)
    radio = 0.65
    inicio_x = np.cos(np.radians(angulo_inicio)) * radio
    inicio_y = np.sin(np.radians(angulo_inicio)) * radio
    fin_x = np.cos(np.radians(angulo_fin)) * radio
    fin_y = np.sin(np.radians(angulo_fin)) * radio
    
    # Dibujar una flecha (color único, consistente con el color del pack de emojis de inicio)
    ax.annotate(
        '', 
        xy=(fin_x, fin_y), 
        xytext=(inicio_x, inicio_y),
        arrowprops=dict(
            arrowstyle='-|>', 
            color=mapa_colores[categoria_inicio],  # Usar el color del tipo de inicio
            lw=grosor,
            connectionstyle="arc3,rad=0.2"
        )
    )

# Construir una leyenda (dividida en dos grupos: tipos + relaciones)
leyenda_tipo = [
    Line2D([0], [0], color=mapa_colores[c], lw=4, label=c) 
    for c in categorias
]

leyenda_flecha = [
    Line2D([0], [0], color=mapa_colores[inicio], lw=grosor, label=f'{inicio} → {fin}') 
    for inicio, fin, grosor in conexiones
]

# Combinar las leyendas (tipos primero, luego relaciones)
leyenda1 = ax.legend(
    handles=leyenda_tipo, 
    loc='upper right', 
    title="Tipos de packs de emojis", 
    fontsize=11, 
    frameon=True,
    framealpha=0.9, 
    facecolor='white', 
    edgecolor='#BDBDBD'
)
ax.add_artist(leyenda1)

ax.legend(
    handles=leyenda_flecha, 
    loc='lower right', 
    title="Relaciones de la cadena de desprecio", 
    fontsize=10, 
    frameon=True,
    framealpha=0.9, 
    facecolor='white', 
    edgecolor='#BDBDBD'
)

# Nota al pie
plt.figtext(
    0.15, 0.02, 
    "Nota: Este gráfico es para divertirse y los datos no representan resultados estadísticos reales, solo para entretenimiento y debate.", 
    ha="left", 
    fontsize=10, 
    bbox={"facecolor":"white", "alpha":0.8, "pad":6}
)

# Ajustar el diseño
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()