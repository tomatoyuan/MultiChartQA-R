import matplotlib.pyplot as plt

# Datos
tamaños = [4.12, 95.88]

# Colores, más cercanos a la imagen original
colores_pc = ["#1976d2", "#e3f2fd"]  # Colores de computadora: azul oscuro y azul claro
colores_movil = ["#f57c00", "#ffebee"]  # Colores de móvil: naranja y naranja claro

# Crear un lienzo y dos subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.subplots_adjust(top=0.85, bottom=0.15)  # Ajustar márgenes superior e inferior

# Dibujar el gráfico de proporción de recuperación del lado de la computadora (ajustar color de etiqueta)
wedges1, texts1, autotexts1 = ax1.pie(
    [tamaños[0], 100 - tamaños[0]],
    labels=["Computadora", ""],  # Simplificar etiquetas
    autopct=lambda p: f'{p:.2f}%\n' if p >= 3 else '',
    startangle=90,
    pctdistance=0.8,
    colors=colores_pc,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Dibujar el gráfico de proporción de recuperación del lado del móvil (ajustar color de etiqueta)
wedges2, texts2, autotexts2 = ax2.pie(
    [tamaños[1], 100 - tamaños[1]],
    labels=["Móvil", ""],  # Simplificar etiquetas
    autopct=lambda p: f'{p:.2f}%\n' if p >= 3 else '',
    startangle=90,
    pctdistance=0.8,
    colors=colores_movil,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Establecer colores de etiqueta (consistentes con los colores del gráfico circular correspondiente)
for text in texts1:
    text.set_color(colores_pc[0])  # Color de etiqueta de computadora es azul oscuro
for text in texts2:
    text.set_color(colores_movil[0])  # Color de etiqueta de móvil es naranja oscuro

# Establecer el color del texto de porcentaje a negro
for text in autotexts1 + autotexts2:
    text.set_color('black')
    text.set_fontsize(14)

# Eliminar los ejes para que el gráfico sea un círculo perfecto
ax1.axis('equal')
ax2.axis('equal')

# Establecer subtítulos (debajo de los gráficos)
ax1.text(0.5, -0.1, "Proporción de recuperación del lado de la computadora", 
         ha='center', va='center', transform=ax1.transAxes, fontsize=14)
ax2.text(0.5, -0.1, "Proporción de recuperación del lado del móvil", 
         ha='center', va='center', transform=ax2.transAxes, fontsize=14)

# Establecer el título principal
fig.suptitle("Distribución de dispositivos de recuperación de la industria de estética médica en mayo", fontsize=16, fontweight='bold')

plt.tight_layout()  # Ajustar el diseño para evitar superposiciones
plt.show()