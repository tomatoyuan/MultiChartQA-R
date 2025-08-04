import matplotlib.pyplot as plt
import numpy as np

# Datos
comidas = ["Camarones de río", "Barbacoa", "Pato picante", "Cerveza", "Cola", "Edamame", "Palomitas de maíz", "Carne a la parrilla"]
valores = [2264, 1030, 827, 804, 521, 462, 442, 352]

# Crear un lienzo y un sub - gráfico (establecer un tamaño y resolución más grandes)
fig, ax = plt.subplots(figsize=(12, 7), dpi = 300)

# Establecer colores degradados (de azul oscuro a azul claro)
colores = plt.cm.Blues(np.linspace(0.6, 0.95, len(comidas)))

# Dibujar un gráfico de barras con esquinas redondeadas (establecer el borde mediante edgecolor y linewidth)
barras = ax.bar(
    x = np.arange(len(comidas)),
    height = valores,
    width = 0.65,
    color = colores,
    edgecolor = 'black',
    linewidth = 0.8,
    capstyle = 'round'
)

# Agregar etiquetas numéricas encima del gráfico de barras
for barra, valor in zip(barras, valores):
    altura = barra.get_height()
    ax.text(
        barra.get_x() + barra.get_width()/2., 
        altura + 30,  # La posición de la etiqueta está ligeramente por encima de la parte superior de la barra
        f'{valor}',
        ha = 'center', 
        va = 'bottom',
        fontsize = 10,
        fontweight = 'bold'
    )

# Establecer las etiquetas de las marcas del eje x (girar 30 grados para mejorar la legibilidad)
ax.set_xticks(np.arange(len(comidas)))
ax.set_xticklabels(comidas, rotation = 30, ha = 'right', fontsize = 11)

# Agregar un título y etiquetas de los ejes (aumentar el tamaño de fuente y la negrita)
ax.set_title('Atención a los alimentos durante la Copa de Europa', fontsize = 16, fontweight = 'bold', pad = 20)
ax.set_xlabel('Tipos de alimentos', fontsize = 13, labelpad = 10)
ax.set_ylabel('Valor de atención', fontsize = 13, labelpad = 10)

# Establecer el rango del eje y (dejar algo de espacio en la parte superior)
ax.set_ylim(0, max(valores) * 1.1)

# Agregar líneas de cuadrícula para mejorar la legibilidad
ax.grid(axis = 'y', linestyle = '--', alpha = 0.7)

# Embellir el borde del gráfico
for spine in ax.spines.values():
    spine.set_color('gray')
    spine.set_linewidth(0.5)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()