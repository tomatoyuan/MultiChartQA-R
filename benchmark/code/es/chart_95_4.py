import matplotlib.pyplot as plt
import numpy as np

# Datos de la dirección de desarrollo de especialidad
etiquetas_habilidad = ["Solo por pasión\nNo es necesario ganar dinero", "Espero que sea\nun trabajo principal o secundario"]
tamaños_habilidad = [32, 68]
colores_habilidad = ["#D3D3D3", "#87CEEB"]

# Datos de la ciudad de vida futura
etiquetas_ciudad = ["Ciudades de primer nivel", "Ciudades de segundo nivel", "Ciudades por debajo del tercer nivel", "Aún no decidido"]
tamaños_ciudad = [36, 42, 16, 6]
colores_ciudad = ["#A4C639", "#A4C639", "#A4C639", "#A4C639"]  # Esquema de color verde uniforme, se puede ajustar

# Crear un lienzo (diseño de dos columnas)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Dibujar un gráfico circular para la dirección de desarrollo de especialidad
ax1.pie(tamaños_habilidad, labels=etiquetas_habilidad, colors=colores_habilidad, startangle=90,
        wedgeprops=dict(width=0.3, edgecolor='white'))  # Gráfico circular en forma de donut
ax1.set_title("Dirección de Desarrollo de Especialidad", fontsize=12, fontweight="bold", y=-0.1)  # Mover el título hacia abajo

# Dibujar un gráfico de barras para las ciudades de vida futura
x = np.arange(len(etiquetas_ciudad))
ancho_barra = 0.6
ax2.bar(x, tamaños_ciudad, color=colores_ciudad, width=ancho_barra)

# Agregar etiquetas de datos al gráfico de barras de ciudades
for bar in ax2.patches:
    altura = bar.get_height()
    ax2.annotate(f'{altura}%',
                 xy=(bar.get_x() + ancho_barra/2, altura),
                 xytext=(0, 3),  # Posición de la etiqueta: desplazamiento de 3 puntos hacia arriba
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color='black')

# Establecer las marcas y etiquetas del eje x para el gráfico de barras de ciudades
ax2.set_xticks(x)
ax2.set_xticklabels(etiquetas_ciudad, rotation=10, ha="right")
ax2.set_title("Ciudad de Vida Futura", fontsize=12, fontweight="bold", y=-0.2)  # Mover el título hacia abajo

# Embellir: Ocultar los bordes del gráfico circular y del gráfico de barras
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

# Ajustar el espaciado entre subgráficos
plt.subplots_adjust(wspace=0.5)

plt.show()