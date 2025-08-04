import matplotlib.pyplot as plt

# Datos
tamaños = [8.24, 91.66]

# Colores, más cercanos a la imagen original
colores_ordenador = ["#1976d2", "#e3f2fd"]  # Colores del ordenador: azul oscuro y azul claro
colores_movil = ["#f57c00", "#ffebee"]    # Colores del móvil: naranja y naranja claro

# Crear un lienzo y dos subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.subplots_adjust(top=0.85, bottom=0.15)  # Ajustar márgenes superior e inferior

# Dibujar el gráfico de proporción de búsquedas desde el ordenador (ajustar color de la etiqueta)
wedges1, texts1, autotexts1 = ax1.pie(
    [tamaños[0], 100 - tamaños[0]],
    labels=["Ordenador", ""],  # Simplificar etiquetas
    autopct=lambda p: f'{p:.2f}%\n' if p >= 3 else '',
    startangle=90,
    pctdistance=0.8,
    colors=colores_ordenador,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Dibujar el gráfico de proporción de búsquedas desde el móvil (ajustar color de la etiqueta)
wedges2, texts2, autotexts2 = ax2.pie(
    [tamaños[1], 100 - tamaños[1]],
    labels=["Móvil", ""],  # Simplificar etiquetas
    autopct=lambda p: f'{p:.2f}%\n' if p >= 3 else '',
    startangle=90,
    pctdistance=0.8,
    colors=colores_movil,
    wedgeprops=dict(width=0.3, edgecolor='w')
)

# Establecer el color de las etiquetas (consistente con los colores del gráfico circular correspondiente)
for text in texts1:
    text.set_color(colores_ordenador[0])  # Color de la etiqueta del ordenador es azul oscuro
for text in texts2:
    text.set_color(colores_movil[0])    # Color de la etiqueta del móvil es naranja oscuro

# Establecer el color del texto de porcentaje en negro
for text in autotexts1 + autotexts2:
    text.set_color('black')
    text.set_fontsize(14)

# Eliminar los ejes para que el gráfico sea un círculo perfecto
ax1.axis('equal')
ax2.axis('equal')

# Establecer subtítulos (debajo del gráfico)
ax1.text(0.5, -0.1, "Proporción de Búsquedas desde el Ordenador", 
         ha='center', va='center', transform=ax1.transAxes, fontsize=14)
ax2.text(0.5, -0.1, "Proporción de Búsquedas desde el Móvil", 
         ha='center', va='center', transform=ax2.transAxes, fontsize=14)

# Establecer el título principal
fig.suptitle("Distribución de Dispositivos de Búsqueda en la Industria de la Leche Materna Artificial en Febrero", fontsize=16, fontweight='bold')

plt.tight_layout()  # Ajustar el diseño para evitar solapamiento
plt.show()