import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
provincias = ["Guangdong", "Jiangsu", "Shandong", "Beijing", "Henan"]
atencion_fraude = [11, 9, 6.5, 5.2, 4]
pib_2015 = [9.5, 7.5, 4, 1.2, 2.2]

# Crear un lienzo y subgráficos
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(provincias))
ancho = 0.35

# Establecer colores degradados
colores1 = plt.cm.Oranges(np.linspace(0.6, 0.9, len(provincias)))
colores2 = plt.cm.Greens(np.linspace(0.6, 0.9, len(provincias)))

# Dibujar un gráfico de barras con colores degradados
rects1 = ax.bar(x - ancho/2, atencion_fraude, ancho, 
                label='Atención al fraude telefónico en cada provincia', color=colores1, 
                edgecolor='black', linewidth=0.5)

rects2 = ax.bar(x + ancho/2, pib_2015, ancho, 
                label='PIB de cada provincia en 2015', color=colores2, 
                edgecolor='black', linewidth=0.5)

# Añadir etiquetas numéricas (optimizar posición y estilo)
def add_labels(rects, ax, is_top=False):
    for rect in rects:
        altura = rect.get_height()
        pos_y = altura + 0.3 if not is_top else altura - 0.3
        va = 'bottom' if not is_top else 'top'
        ax.annotate(f'{altura}',
                    xy=(rect.get_x() + rect.get_width() / 2, pos_y),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va=va,
                    fontsize=10, fontweight='bold')

add_labels(rects1, ax)
add_labels(rects2, ax, is_top=True)

# Establecer el título del gráfico y las etiquetas de los ejes
ax.set_title("Comparación de la atención al fraude telefónico y el PIB de cada provincia en 2015", 
             fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Valor (Unidad: 100 millones de yuanes/Índice de atención)", fontsize=12, labelpad=10)

# Establecer los estilos de los ejes x e y
ax.set_xticks(x)
ax.set_xticklabels(provincias, fontsize=12, fontweight='bold')
ax.set_ylim(0, 13)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Embelezar la leyenda
leyenda = ax.legend(fontsize=10, frameon=True, loc='upper right')
frame = leyenda.get_frame()
frame.set_facecolor('white')
frame.set_edgecolor('gray')
frame.set_alpha(0.8)

# Añadir descripción de texto en la parte inferior (optimizar la tipografía)
plt.figtext(0.5, 0.01, 
            "Los cinco primeros en atención a la prevención del fraude: Guangdong, Shandong, Jiangsu, Beijing, Henan\n"
            "Los cinco primeros en ranking del PIB de cada provincia en 2015: Guangdong, Jiangsu, Shandong, Zhejiang, Henan", 
            ha="center", fontsize=10, color='dimgray')

# Añadir color de fondo para distinguir áreas
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

# Ajustar el diseño
plt.tight_layout(pad=3)
plt.show()