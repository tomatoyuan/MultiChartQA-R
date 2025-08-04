import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Datos
etiquetas = ["Inversión Total", "Negocios, Transferencias, Boletos", "Gastos de Contratación de Jugadores Extranjeros"]
valores = [41, 30.9, 34.3]
colores = ["#2E7D32", "#2E7D32", "#B71C1C"]  # Verde y Rojo
color_resaltado = "#FFC107"  # Resaltado amarillo

# Crear el lienzo con altura aumentada para evitar superposiciones
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')  # Aumentar el ancho del lienzo
ax.set_ylim(0, 1.2)  # Ampliar el rango del eje y
ax.set_xlim(0, len(valores) * 3)  # Ampliar el rango del eje x, para dar más espacio a las etiquetas inclinadas
ax.axis('off')

# Dibujar la cuadrícula de fondo
for i in range(1, 10):
    ax.axhline(y=i*0.1, color='#e9ecef', linestyle='-', alpha=0.5)

# Dibujar los bloques de datos con más espaciado
for i in range(len(valores)):
    # Agregar efecto de sombra
    sombra = patches.FancyBboxPatch(
        (i * 3 + 0.1, 0.3), 1.8, 0.6,  # Aumentar el ancho y el intervalo de posición de los bloques
        boxstyle=patches.BoxStyle("Round", pad=0.02),
        facecolor='black', alpha=0.2
    )
    ax.add_patch(sombra)
    
    # Dibujar el bloque principal
    rect = patches.FancyBboxPatch(
        (i * 3, 0.35), 1.8, 0.6,  # Aumentar el ancho del bloque
        boxstyle=patches.BoxStyle("Round", pad=0.02),
        facecolor=colores[i], edgecolor="none", alpha=0.9
    )
    ax.add_patch(rect)
    
    # Agregar resaltado del borde
    resaltado = patches.FancyBboxPatch(
        (i * 3, 0.35), 1.8, 0.6,  # Aumentar el ancho del bloque
        boxstyle=patches.BoxStyle("Round", pad=0.02),
        facecolor='none', edgecolor=color_resaltado, 
        linewidth=2, alpha=0.8
    )
    ax.add_patch(resaltado)
    
    # Dibujar el texto del valor
    ax.text(
        i * 3 + 0.9, 0.65, f"{valores[i]}",  # Ajustar la posición del valor
        ha="center", va="center", fontsize=28, 
        color="white", fontweight='bold',
        bbox=dict(facecolor='none', edgecolor='none')
    )

# Agregar el título
ax.text(
    (len(valores) * 3) / 2, 1.1, "Resumen de los Datos Financieros de los Clubes de la Superliga China", 
    ha="center", va="center", fontsize=20, 
    color="#212529", fontweight='bold'
)

# Agregar el subtítulo
ax.text(
    (len(valores) * 3) / 2, 1.0, "Unidad: Miles de Millones de Yuanes", 
    ha="center", va="center", fontsize=14, 
    color="#6c757d"
)

# Dibujar las etiquetas con una rotación de 30 grados
for i, etiqueta in enumerate(etiquetas):
    ax.text(
        i * 3 + 0.9, 0.25, etiqueta,  # Ajustar la posición de la etiqueta
        ha="center", va="center", fontsize=12, 
        color="#333333", fontweight='bold',
        rotation=30  # Establecer el ángulo de inclinación
    )

# Ajustar la posición de la leyenda
ax.text(
    1.5, 0.1, "■ Ítems de Ingreso",  # Ajustar la posición de la leyenda
    ha="center", va="center", fontsize=12, 
    color="#2E7D32"
)
ax.text(
    4.5, 0.1, "■ Ítems de Gasto",  # Ajustar la posición de la leyenda
    ha="center", va="center", fontsize=12, 
    color="#B71C1C"
)

# Ajustar la posición de la fuente de datos
ax.text(
    (len(valores) * 3) - 1.5, 0.1, "Fuente de Datos: Ejemplo Ficticio", 
    ha="right", va="center", fontsize=10, 
    color="#6c757d"
)

# Ajustar finamente el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()