import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Esquema de colores de los packs de emojis (estrictamente correspondiente a los tipos)
mapa_colores = {
    'Emoji de celebridades': '#FF5252',
    'Emoji de texto': '#00E5FF',
    'Emoji integrados en QQ y WeChat': '#FFD740',
    'Emoji de personas mayores': '#9C27B0',
    'Emoji': '#00E676',
    'Emoji de cómic': '#2979FF',
}

# Definición de datos (mantener la lógica original)
categorias = ['Emoji integrados en QQ y WeChat', 'Emoji de personas mayores', 'Emoji de texto',
              'Emoji de celebridades', 'Emoji de cómic', 'Emoji']
porcentajes = [42, 30, 25, 15, 29, 33]

# Relaciones de la cadena de desprecio (claramente correspondientes a los tipos para el mapeo de colores)
conexiones = [
    ('Emoji integrados en QQ y WeChat', 'Emoji de personas mayores', 3.5),  # QQ y WeChat → Personas mayores
    ('Emoji de personas mayores', 'Emoji de texto', 3),       # Personas mayores → Texto
    ('Emoji de texto', 'Emoji', 2.5),           # Texto → Emoji
    ('Emoji', 'Emoji de cómic', 2),            # Emoji → Cómic
    ('Emoji de cómic', 'Emoji de celebridades', 1.5),        # Cómic → Celebridades
]

# Crear el lienzo y configuraciones básicas
fig, ax = plt.subplots(figsize=(14, 12), facecolor='#FAFAFA')
ax.set_facecolor('#FAFAFA')
ax.grid(True, linestyle='--', alpha=0.3, color='#EEEEEE')

# Dibujar el gráfico circular (mejorar la sombra y el borde)
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
ax.set_title('Lógica de desprecio de la edición de los 80s: Conveniencia',
             fontsize=22,
             fontweight='bold',
             color='#212121',
             pad=25)

# Dibujar las flechas de la cadena de desprecio (colores que corresponden estrictamente al color principal del pack de emojis)
for categoria_inicio, categoria_fin, grosor in conexiones:
    # Encontrar el ángulo del sector correspondiente
    porcion_inicio = [w for w, l in zip(porciones, categorias) if l == categoria_inicio][0]
    porcion_fin = [w for w, l in zip(porciones, categorias) if l == categoria_fin][0]

    angulo_inicio = (porcion_inicio.theta2 + porcion_inicio.theta1) / 2
    angulo_fin = (porcion_fin.theta2 + porcion_fin.theta1) / 2

    # Calcular las coordenadas (radio unificado para evitar confusiones)
    radio = 0.65
    inicio_x = np.cos(np.radians(angulo_inicio)) * radio
    inicio_y = np.sin(np.radians(angulo_inicio)) * radio
    fin_x = np.cos(np.radians(angulo_fin)) * radio
    fin_y = np.sin(np.radians(angulo_fin)) * radio

    # Dibujar la flecha (de un solo color, consistente con el color del pack de emojis de inicio)
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

# Construir la leyenda (dividida en dos grupos: tipos + relaciones)
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
    fontsize=11,
    frameon=True,
    framealpha=0.9,
    facecolor='white',
    edgecolor='#BDBDBD'
)

# Anotación en la parte inferior
plt.figtext(
    0.15, 0.02,
    "Nota: Este gráfico es una muestra divertida. Los datos no representan resultados estadísticos reales y son solo para entretenimiento y discusión.",
    ha="left",
    fontsize=10,
    bbox={"facecolor": "white", "alpha": 0.8, "pad": 6}
)

# Ajustar el diseño
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()