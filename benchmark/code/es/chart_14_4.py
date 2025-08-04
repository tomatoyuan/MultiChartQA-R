import matplotlib.pyplot as plt
import numpy as np

# Datos
grupos = ['Adultos mayores', 'Niños/Bebes', 'Mujeres', 'Mascotas']
nivel_de_influencia = [8, 7, 6, 5]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))

# Establecer el color de fondo y la cuadrícula
ax.set_facecolor('#FFF8E7')  # Fondo naranja claro cálido
ax.grid(axis='y', linestyle='--', alpha=0.3, color='gray')

# Dibujar un gráfico de barras embellecido
colores = plt.cm.Reds(np.linspace(0.6, 0.9, len(grupos)))  # Color de gradiente
barras = ax.bar(grupos, nivel_de_influencia, color=colores, width=0.6, 
              edgecolor='black', linewidth=0.5)

# Añadir un título y un subtítulo
ax.set_title('Grupos propensos a la "Enfermedad del Aire Acondicionado"', fontsize=18, pad=20, fontweight='bold')

# Ajustar los ejes
ax.set_ylim(0, 10)  # Fijar el rango del eje y para una comparación más intuitiva
ax.set_yticks([])  # Ocultar las marcas de graduación del eje y
ax.set_xlabel('Tipos de Grupos', fontsize=12, labelpad=10)

# Embellecer las etiquetas del eje x
ax.tick_params(axis='x', which='major', labelsize=12, pad=10)

# Ocultar los ejes superior, derecho e izquierdo
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Añadir una breve descripción encima de cada barra
for barra, grupo in zip(barras, grupos):
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2., altura + 0.3,
            f'{grupo}', ha='center', va='bottom', fontweight='bold', fontsize=12)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()