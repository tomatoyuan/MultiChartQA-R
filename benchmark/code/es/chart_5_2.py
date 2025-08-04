import matplotlib.pyplot as plt
import numpy as np

# Construir datos de fecha para el eje horizontal correspondientes a las fechas del gráfico original
fechas = ["2.1", "2.3", "2.5", "2.7", "2.9", "2.11", 
          "2.13", "2.15", "2.17", "2.19", "2.21", 
          "2.23", "2.25", "2.27"]
# Construir datos aproximados de atención de búsqueda para el eje vertical siguiendo la tendencia del gráfico original
valores = [150000, 200000, 250000, 380000, 370000, 390000, 
           360000, 430000, 440000, 410000, 560000, 
           430000, 420000, 340000]  

# Crear un lienzo y establecer su tamaño
fig, ax = plt.subplots(figsize=(10, 6))  

# Dibujar un gráfico de líneas, establecer el color de la línea en azul y ajustar el grosor de la línea para un mejor efecto visual
linea, = ax.plot(fechas, valores, color="#4285F4", linewidth=2.5)  

# Establecer el título del gráfico, poner en negrita la fuente
ax.set_title("Tendencia de atención de búsqueda de la industria de la leche en polvo en febrero", fontsize=16, fontweight="bold")  

# Establecer la etiqueta del eje vertical, el rango y las marcas
ax.set_ylabel("Atención", fontsize=12)
ax.set_ylim(100000, 600000)  
ax.set_yticks([100000, 200000, 300000, 400000, 500000, 600000])  
# Formatear las etiquetas de las marcas del eje vertical con separadores de miles
ax.set_yticklabels([f"{tick:,}" for tick in ax.get_yticks()])  

# Establecer las marcas del eje horizontal utilizando los datos de fecha construidos
ax.set_xticks(fechas)  

# Agregar líneas de cuadrícula en estilo discontinuo para mejorar la legibilidad del gráfico
ax.grid(linestyle="--", color="gray", alpha=0.3)  

# Agregar anotaciones a los puntos de datos
for x, y in zip(fechas, valores):
    # Formatear el valor numérico con un separador de miles
    valor_str = f"{y:,}"
    
    # Ajustar la posición de la anotación para evitar solapamientos
    if y > 400000:  # Anotación por encima del punto
        ax.annotate(valor_str, 
                    (x, y), 
                    textcoords="offset points",
                    xytext=(0, 10), 
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#4285F4", alpha=0.8))
    else:  # Anotación por debajo del punto
        ax.annotate(valor_str, 
                    (x, y), 
                    textcoords="offset points",
                    xytext=(0, -15), 
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#4285F4", alpha=0.8))

# Resaltar los valores máximo y mínimo
valor_max = max(valores)
valor_min = min(valores)
for x, y in zip(fechas, valores):
    if y == valor_max or y == valor_min:
        ax.scatter(x, y, color='red', s=50, zorder=5)
        ax.annotate(f"{y:,}", 
                    (x, y), 
                    textcoords="offset points",
                    xytext=(0, 15), 
                    ha='center',
                    fontsize=10,
                    fontweight='bold',
                    color='red',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", alpha=0.8))

# Agregar una leyenda
ax.legend([linea], ["Atención de búsqueda"], loc='upper left')

# Agregar una descripción de la fuente de datos
plt.figtext(0.1, 0.01, 'Fuente de datos: Datos ficticios solo para ejemplo', ha="left", fontsize=9, bbox={"facecolor":"white", "alpha":0.5, "pad":5})

# Optimizar el diseño para evitar solapamiento de elementos
plt.tight_layout()  

# Mostrar el gráfico
plt.show()