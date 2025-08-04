import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ['Antes', '2024']
valores = [100, 117]
x = np.arange(len(categorias))

# Crear una figura
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
ancho_barra = 0.6
rects1 = ax.bar(x[0], valores[0], width=ancho_barra, color='#6aa84f', label='Ingresos de Ventas Anteriores', 
                edgecolor='black', linewidth=0.8)
rects2 = ax.bar(x[1], valores[1], width=ancho_barra, color='#3d85c6', label='Ingresos de Ventas 2024', 
                edgecolor='black', linewidth=0.8)

# Añadir etiquetas de datos
def add_labels(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate(f'{altura}',
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=12)

add_labels(rects1)
add_labels(rects2)

# Añadir una anotación de flecha horizontal de crecimiento
ax.annotate('Crecimiento del 17%', 
            xy=(0.8, 105),  # Punto de inicio de la flecha
            xytext=(0.2, 105),  # Punto de fin de la flecha
            arrowprops=dict(facecolor='black', shrink=0.02, width=1.5, headwidth=8, connectionstyle="arc3"),
            ha='center', va='center', fontsize=12)

# Establecer el estilo del gráfico
ax.set_ylim([0, 140])
ax.set_ylabel('Ingresos de Ventas (Miles de Millones)', fontsize=14)
ax.set_title('Crecimiento de los Ingresos de Ventas de la Industria de Alimentos Saludables en 2024', fontsize=16, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(categorias, fontsize=12)
ax.legend(fontsize=12, loc='upper left')

# Añadir líneas de cuadrícula
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ajustar el borde
for spine in ax.spines.values():
    spine.set_color('gray')

# Emprolijar el estilo general
plt.tight_layout()

# Mostrar el gráfico
plt.show()