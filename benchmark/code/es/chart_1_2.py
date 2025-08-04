import matplotlib.pyplot as plt
import numpy as np

# Grupos de edad
grupos_edad = ['Menos de 18', '18 - 24', '25 - 34', '35 - 44', 
               '45 - 54', '55 - 64', 'Más de 65']
# Datos simulados, generalmente en línea con las proporciones del diagrama, se pueden ajustar según la situación real
datos = [22, 28, 14, 10, 7, 6, 5]  

# Establecer un esquema de colores moderno - degradado de azul oscuro a azul claro
colores = plt.cm.viridis(np.linspace(0.2, 0.8, len(grupos_edad)))
# Resaltar el grupo de edad de 18 - 24
colores[1] = plt.cm.magma(0.6)

x = np.arange(len(grupos_edad))  # Posiciones de las marcas en el eje x

# Crear una figura y ejes, usar un lienzo más ancho
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor('#ffffff')  # Fondo blanco
ax.set_facecolor('#f5f5f5')  # Fondo de los ejes en gris claro

# Dibujar un gráfico de barras para agregar sensación de tres dimensiones
barras = ax.bar(x, datos, width=0.7, color=colores, alpha=0.85, 
                edgecolor='#333333', linewidth=0.6)

# Agregar etiquetas de datos sobre cada barra y agregar un efecto de sombra
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2., altura + 0.4,
            f'{altura}', ha='center', va='bottom', 
            fontsize=11, fontweight='bold', color='black',
            bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.2'))

# Establecer las etiquetas de las marcas en el eje x para que se muestren horizontalmente
ax.set_xticks(x)
ax.set_xticklabels(grupos_edad, fontsize=12, fontweight='medium')

# Establecer el rango y la etiqueta del eje y, ocultar las marcas del eje y
ax.set_ylim(0, max(datos) * 1.2)
ax.set_ylabel('Proporción de búsquedas (%)', fontsize=13, fontweight='medium', labelpad=10)
ax.tick_params(axis='y', which='both', length=0)

# Agregar líneas de cuadrícula horizontales, usar un color más claro
ax.grid(axis='y', linestyle='-', alpha=0.3, color='lightgray')

# Establecer el título y el subtítulo del gráfico
ax.set_title('Distribución por edad de la población que busca información sobre accidentes cerebrovasculares', fontsize=18, pad=20, fontweight='bold')
ax.text(0.5, 0.96, 'El grupo de edad de 18 - 24 tiene el mayor volumen de búsquedas', transform=ax.transAxes, 
        ha='center', va='top', fontsize=13, color='#555555')

# Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Ajustar el color y el grosor de los bordes izquierdo y inferior
ax.spines['left'].set_color('#cccccc')
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_color('#cccccc')
ax.spines['bottom'].set_linewidth(1.5)

# Agregar una flecha de anotación apuntando a la barra más alta
ax.annotate('Mayor proporción', xy=(1, 30), xytext=(1, 32),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
            ha='center', fontsize=12)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()