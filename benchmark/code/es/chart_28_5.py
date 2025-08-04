import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
generos = ["Mujer", "Hombre"]
porcentajes_genero = [45, 55]
colores_genero = ['#FF7E79', '#7EB0D5']

# Crear un lienzo
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(111)

# Dibujar un gráfico de barras segmentado horizontal embellecido
altura_barra = 0.4
ax.barh(0, porcentajes_genero[0], color=colores_genero[0], 
         height=altura_barra, edgecolor='white', linewidth=1.5, label=generos[0])
ax.barh(0, porcentajes_genero[1], left=porcentajes_genero[0], color=colores_genero[1], 
         height=altura_barra, edgecolor='white', linewidth=1.5, label=generos[1])

# Agregar etiquetas de datos
ax.text(porcentajes_genero[0]/2, 0, f"{porcentajes_genero[0]}%", 
         ha='center', va='center', fontsize=14, color='white', fontweight='bold')
ax.text(porcentajes_genero[0] + porcentajes_genero[1]/2, 0, f"{porcentajes_genero[1]}%", 
         ha='center', va='center', fontsize=14, color='white', fontweight='bold')

# Establecer el estilo del gráfico de barras
ax.set_xlim(0, 100)
ax.set_yticks([])  # Eliminar el eje y
ax.set_xlabel("Porcentaje (%)", fontsize=12, labelpad=10)
ax.set_title("Proporción de atención de hombres y mujeres de 25 - 34 años al 11.11", fontsize=14, pad=20, fontweight='bold')

# Personalizar las marcas del eje x
ax.set_xticks([0, 25, 50, 75, 100])
ax.tick_params(axis='x', which='major', labelsize=10)

# Agregar una leyenda
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), 
           ncol=2, frameon=False, fontsize=12)

# Agregar líneas de cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Agregar un borde
for spine in ax.spines.values():
    spine.set_color('#cccccc')

# Agregar una línea diagonal en el punto de división - la línea de separación entre hombres y mujeres
divider_y = np.linspace(-altura_barra/2, altura_barra/2, 100)
divider_x = np.ones_like(divider_y) * porcentajes_genero[0]
ax.plot(divider_x, divider_y, color='white', linewidth=1.5, linestyle='--')

# Ajustar el diseño
plt.tight_layout(pad=3)

# Guardar el gráfico (opcional)
# plt.savefig('distribucion_genero.png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico
plt.show()