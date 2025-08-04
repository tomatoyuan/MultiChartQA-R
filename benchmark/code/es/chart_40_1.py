import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Datos
tipos_picantes = ["Picante", "Ácido - Picante", "Pimentón"]
porcentajes_preferencia = [45, 35, 30]
unidades_scoville = [250, 750, 1250]  # Valor medio de picante
orígenes = ["China, Corea del Sur, etc.", "Tailandia, Malasia, etc.", "EE. UU., México, etc."]
platos_representativos = [
    ["Hot Pot Picante", "Kimchi Picante", "Tortitas de Arroz Salteadas Picantes"],
    ["Tom Yum Goong", "Ensalada de Papaya Verde", "Asam Laksa"],
    ["Barbacoa de Texas", "Carne Picante Ahumada", "Chili Mexicano"]
]

# Definición de colores
colores = ['#FF5722', '#FF9800', '#FFC107']
colores_claros = ['#FFCCBC', '#FFE0B2', '#FFF9C4']

# Crear un lienzo
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1.5])

# 1. Gráfico circular de porcentajes de preferencia
ax1 = fig.add_subplot(gs[0, 0])
ax1.pie(porcentajes_preferencia, labels=tipos_picantes, autopct='%1.1f%%',
        startangle=90, colors=colores, wedgeprops={'edgecolor': 'w', 'linewidth': 2})
ax1.set_title('Porcentaje de Preferencias por los 3 Sabores Picantes Más Populares del Mundo', fontsize=14, pad=15)
ax1.axis('equal')  # Asegurar que el gráfico circular sea redondo

# 2. Gráfico de barras de comparación de picante
ax2 = fig.add_subplot(gs[0, 1])
barras = ax2.bar(tipos_picantes, unidades_scoville, color=colores_claros, edgecolor=colores, linewidth=1.5)
ax2.set_title('Picante Promedio de Diferentes Sabores Picantes (SHU)', fontsize=14, pad=15)
ax2.set_xlabel('Tipos de Sabores Picantes', fontsize=12)
ax2.set_ylabel('Picante (SHU)', fontsize=12)
ax2.set_ylim(0, 1600)

# Agregar etiquetas numéricas a cada barra
for barra in barras:
    altura = barra.get_height()
    ax2.text(barra.get_x() + barra.get_width()/2., altura + 30,
             f'{altura} SHU', ha='center', va='bottom', fontweight='bold')

# 3. Tabla de información de tipos de sabores picantes
ax3 = fig.add_subplot(gs[1, :])
ax3.axis('off')

# Datos de la tabla
datos_tabla = []
for i, (tipo_picante, porcentaje, scoville, origen, platos) in enumerate(zip(
    tipos_picantes, porcentajes_preferencia, unidades_scoville, orígenes, platos_representativos
)):
    datos_tabla.append([
        f'{tipo_picante} ({porcentaje}%)', 
        f'{scoville} SHU', 
        origen,
        '\n'.join([f'• {plato}' for plato in platos])
    ])

# Crear la tabla
tabla = ax3.table(
    cellText=datos_tabla,
    colLabels=['Tipos de Sabores Picantes', 'Picante', 'Origen', 'Platos Representativos'],
    loc='center',
    cellLoc='left',
    colWidths=[0.15, 0.15, 0.25, 0.45]
)

# Establecer el estilo de la tabla
tabla.set_fontsize(12)
tabla.scale(1, 2)  # Ajustar el tamaño de la tabla

for i in range(len(tipos_picantes)):
    tabla[(i+1, 0)].set_facecolor(colores_claros[i])
    tabla[(i+1, 0)].set_text_props(weight='bold', color='black')

for j in range(4):
    tabla[(0, j)].set_facecolor('#f0f0f0')
    tabla[(0, j)].set_text_props(weight='bold')

# 4. Mapa simplificado de rastreo de origen de sabores picantes
ax4 = fig.add_subplot(gs[2, :])
ax4.set_title('Mapa de Rastreo de Origen de Sabores Picantes', fontsize=14, pad=15)
ax4.set_xlim(0, 10)
ax4.set_ylim(0, 6)
ax4.axis('off')

# Dibujar el contorno del mapa mundial simplificado
mapa_mundial = plt.Rectangle((1, 1), 8, 4, fill=False, edgecolor='#CCCCCC', linewidth=2)
ax4.add_patch(mapa_mundial)

# Dibujar los puntos de origen y de intersección de los sabores picantes
puntos_origen = [
    (2, 2, "Sudamérica", colores[0]),  # Origen del sabor picante
    (8, 2, "Southeast Asia", colores[1]),  # Origen del sabor ácido - picante
    (5, 4, "Asia Central", colores[2])     # Punto de intersección de sabores picantes
]

# Agregar marcadores de origen
for x, y, nombre, color in puntos_origen:
    ax4.plot(x, y, 'o', markersize=12, color=color)
    ax4.text(x, y-0.3, nombre, ha='center', va='top', fontweight='bold', color=color)

# Agregar líneas de conexión
ax4.plot([2, 5], [2, 4], '--', color='#DDDDDD')
ax4.plot([8, 5], [2, 4], '--', color='#DDDDDD')

# Agregar leyenda
elementos_leyenda = [
    Patch(facecolor=colores[0], edgecolor='w', label='Origen del Sabor Picante'),
    Patch(facecolor=colores[1], edgecolor='w', label='Origen del Sabor Ácido - Picante'),
    Patch(facecolor=colores[2], edgecolor='w', label='Punto de Intersección de Sabores Picantes')
]
ax4.legend(handles=elementos_leyenda, loc='lower right')

# Agregar texto descriptivo
ax4.text(5, 0.5, "Nota: Este mapa es un diagrama esquemático simplificado que muestra los principales orígenes y puntos de intersección de tres sabores picantes.", 
         ha='center', va='center', fontsize=10, color='#666666')

# Ajustar el diseño
plt.tight_layout()
plt.subplots_adjust(hspace=0.3)

# Mostrar el gráfico
plt.show()