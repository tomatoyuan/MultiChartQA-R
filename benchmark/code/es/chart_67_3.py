import matplotlib.pyplot as plt
import numpy as np

# Nombres de las ciudades
ciudades = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen"]
# Datos de la tasa de vacancia de los distritos comerciales centrales
vacancia_core = [9.8, 9.9, 7.6, 18.8]
# Datos de la tasa de vacancia de los edificios de oficinas de alta calidad en toda la ciudad
vacancia_ciudad = [17.1, 16.6, 11.9, 16.6]

# Crear un lienzo y subgráficos
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar la línea de la tasa de vacancia de los distritos comerciales centrales
linea_core, = ax.plot(ciudades, vacancia_core, marker='o', color='#A4C639', label='Tasa de vacancia de los distritos comerciales centrales (%)', linewidth=2)
# Dibujar la línea de la tasa de vacancia de los edificios de oficinas de alta calidad en toda la ciudad
linea_ciudad, = ax.plot(ciudades, vacancia_ciudad, marker='o', color='#64B5F6', label='Tasa de vacancia de los edificios de oficinas de alta calidad en toda la ciudad (%)', linewidth=2)

# Agregar etiquetas de datos (distritos comerciales centrales)
for x, y in zip(ciudades, vacancia_core):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, 5),  # Ajustar la posición de la etiqueta
                textcoords='offset points',
                ha='center', va='bottom',
                color='#A4C639')

# Agregar etiquetas de datos (edificios de oficinas de alta calidad en toda la ciudad)
for x, y in zip(ciudades, vacancia_ciudad):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, 5),  # Ajustar la posición de la etiqueta
                textcoords='offset points',
                ha='center', va='bottom',
                color='#64B5F6')

# Establecer el título
ax.set_title('Tasa de vacancia de los edificios de oficinas de alta calidad en ciudades de primer nivel de China en 2021', fontsize=14, fontweight='bold')
# Agregar una leyenda
ax.legend()

# Embelezar el gráfico ocultando los bordes superior y derecho
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()