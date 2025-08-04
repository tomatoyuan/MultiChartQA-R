import matplotlib.pyplot as plt
import numpy as np

# Categorías
categorias = ["Estandar Mínimo", "De 6 - 9 años", "De 10 - 13 años", "De 14 - 17 años"]
# Datos (mínimos), correspondientes al gráfico
datos = [120, 64.3, 55.5, 44.9]
# La parte que alcanza el promedio en cada categoría (valor esquemático, que coincide con el efecto visual del gráfico)
partes_promedio = [120, 30, 25, 20]
# Configuración de colores
colores = ["#A4C639", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
linea_promedio_y = 54.9  # Duración promedio

# Crear un lienzo
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de barras
x = np.arange(len(categorias))
ancho_barra = 0.6
for i in range(len(categorias)):
    # Dibujar la parte inferior (gris o verde)
    rect = ax.bar(x[i], datos[i], width=ancho_barra, color=colores[i])
    # Dibujar la "parte del promedio" cubierta en la parte superior (solo el estándar mínimo no necesita ser cubierto porque es verde y supera el promedio)
    if categorias[i] != "Estandar Mínimo":
        ax.bar(x[i], datos[i] - partes_promedio[i], bottom=partes_promedio[i], width=ancho_barra, color=colores[0])
    # Agregar etiquetas de datos
    ax.text(x[i], datos[i] + 2, f'{datos[i]}min', ha='center', va='bottom', color='black')

# Dibujar una línea punteada amarilla para la duración promedio
ax.axhline(y=linea_promedio_y, color='yellow', linestyle='--', linewidth=2)
ax.text(3.2, linea_promedio_y + 2, f'Promedio {linea_promedio_y}min', ha='left', va='bottom', color='gold', fontweight='bold')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias)
# Ocultar las marcas del eje y
ax.set_yticks([])
# Establecer el título
ax.set_title('Situación de deportes al aire libre de niños y adolescentes chinos en 2018', fontsize=14, fontweight='bold')

# Embelezar: ocultar los bordes superior, derecho e inferior
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()