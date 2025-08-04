import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Una vez al día o más', '2 - 3 veces a la semana', '2 - 3 veces al mes', 'Ocasionalmente (≤1 vez al mes)']
valores = [32, 47, 17, 4]

# Esquema de colores optimizado con colores modernos
colores = ['#4a86e8', '#4a86e8', '#b7b7b7', '#e6e6e6']

# Crear figura y subgráfico con tamaño adecuado
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de barras con bordes y transparencia
barras = ax.bar(etiquetas, valores, color=colores, edgecolor='black', alpha=0.85, width=0.6)

# Agregar etiquetas de valor con posición y estilo optimizados
for barra in barras:
    altura = barra.get_height()
    ax.text(
        barra.get_x() + barra.get_width() / 2, 
        altura + 0.5,  # Ajustar finamente la posición de la etiqueta
        f'{altura}%',
        ha='center', 
        va='bottom',
        fontsize=12,
        fontweight='bold'
    )

# Establecer el título con estilo
ax.set_title('Frecuencia de consumo de café de los consumidores en el distrito de Jing\'an, Shanghái', fontsize=16, fontweight='bold', pad=20)

# Establecer la etiqueta y el rango del eje y
ax.set_ylabel('Porcentaje (%)', fontsize=12, labelpad=10)
ax.set_ylim(0, max(valores) * 1.15)  # Ajustar el rango del eje y para dejar espacio

# Embelezar los ejes
ax.tick_params(axis='x', rotation=0, labelsize=11)  # Mantener las etiquetas del eje x horizontales
ax.tick_params(axis='y', labelsize=10)

# Establecer las líneas de cuadrícula (solo horizontales)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ocultar las espinas derecha y superior, resaltar las espinas izquierda y inferior
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Ajustar el diseño
plt.tight_layout(pad=2)

# Mostrar el gráfico
plt.show()