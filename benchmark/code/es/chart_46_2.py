import matplotlib.pyplot as plt

# Datos - En el orden del gráfico: Sillas ergonómicas, Lámparas protectoras de ojos, Mesas para trabajar de pie; Orden generacional: Post - 05s → Post - 00s → Post - 95s → Post - 90s → Post - 85s → Post - 80s
categorias = ["Sillas ergonómicas", "Lámparas protectoras de ojos", "Mesas para trabajar de pie"]
generaciones = ["Post - 05s", "Post - 00s", "Post - 95s", "Post - 90s", "Post - 85s", "Post - 80s"]
# 1 significa que el cuadrado está lleno, 0 significa que no, correspondiente al gráfico
datos = {
    "Sillas ergonómicas": [0, 0, 1, 1, 1, 1],  
    "Lámparas protectoras de ojos": [1, 0, 0, 0, 1, 1],     
    "Mesas para trabajar de pie": [1, 0, 1, 0, 1, 0]      
}

# Porcentajes totales (consistentes con el gráfico)
porcentajes_totales = {
    "Sillas ergonómicas": 66,
    "Lámparas protectoras de ojos": 55,
    "Mesas para trabajar de pie": 53
}

# Colores personalizados (similares al esquema de color naranja original)
colores = {
    "Sillas ergonómicas": "#F8C4B4",  # Naranja claro, similar al color de las sillas ergonómicas en el gráfico original
    "Lámparas protectoras de ojos": "#F8C4B4",    # Naranja claro, color para las lámparas protectoras de ojos
    "Mesas para trabajar de pie": "#F8C4B4"     # Naranja claro, color para las mesas para trabajar de pie
}

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 5))  # Ajustar el tamaño del lienzo

# Establecer parámetros de la cuadrícula
tamaño_cuadro = 0.8   # Tamaño del cuadrado
espacio = 0.2     # Espacio entre cuadrados
ancho_etiqueta = 2   # Ancho del área de la etiqueta izquierda

# Dibujar el contenido
for i, cat in enumerate(categorias):
    # Fondo de la etiqueta izquierda (naranja claro semi - transparente)
    rect_bg = plt.Rectangle(
        (0, i * (tamaño_cuadro + espacio)),
        ancho_etiqueta, tamaño_cuadro,
        facecolor=colores[cat],
        alpha=0.3,
        edgecolor='none'
    )
    ax.add_patch(rect_bg)
    
    # Nombre del artículo
    ax.text(
        ancho_etiqueta * -0.1,  
        i * (tamaño_cuadro + espacio) + tamaño_cuadro/2,
        cat,
        ha='left',
        va='center',
        color='black',
        fontweight='bold',
        fontsize=12
    )
    
    # Etiqueta de porcentaje
    ax.text(
        ancho_etiqueta * 1.3,  
        i * (tamaño_cuadro + espacio) + tamaño_cuadro/2,
        f'{porcentajes_totales[cat]}%',
        ha='right',
        va='center',
        color='black',
        fontweight='bold',
        fontsize=12
    )
    
    # Dibujar cuadrados de datos
    for j, valor in enumerate(datos[cat]):
        if valor == 1:  # Dibujar un cuadrado si hay un valor
            rect = plt.Rectangle(
                (ancho_etiqueta + j * (tamaño_cuadro + espacio), i * (tamaño_cuadro + espacio)),
                tamaño_cuadro, tamaño_cuadro,
                facecolor=colores[cat],
                edgecolor='white',
                alpha=1
            )
            ax.add_patch(rect)

# Establecer el rango del eje
ax.set_xlim(0, ancho_etiqueta + len(generaciones) * (tamaño_cuadro + espacio))
ax.set_ylim(0, len(categorias) * (tamaño_cuadro + espacio))

# Etiquetas del eje X (generaciones)
ticks_x = [ancho_etiqueta + j * (tamaño_cuadro + espacio) + tamaño_cuadro/2 for j in range(len(generaciones))]
ax.set_xticks(ticks_x)
ax.set_xticklabels(generaciones, fontsize=11, rotation=0)

# Título
ax.set_title('Muebles que los consumidores más quieren equipar en su estudio (Las partes resaltadas con TGI>100 indican alta preferencia)', fontsize=14, pad=20)

# Ocultar bordes innecesarios, mantener etiquetas del eje X
ax.yaxis.set_visible(False)  # Ocultar el eje Y
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Ajustar el diseño para evitar recortes
plt.tight_layout()
plt.show()