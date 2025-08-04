import matplotlib.pyplot as plt
import numpy as np

# Datos
niveles_ciudad = ["Ciudades de primer nivel", "Ciudades de segundo nivel", "Ciudades de tercer nivel", "Ciudades de cuarto nivel"]
proporcion = [38, 19, 17, 12]  # Datos de proporción
tasa_crecimiento = [-6, -4, -8, -9]  # Datos de tasa de crecimiento

x = np.arange(len(niveles_ciudad))  # Posiciones de las marcas en el eje x

# Crear un gráfico
fig, ax1 = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño del gráfico

# Establecer el estilo de fondo - Usar un estilo incorporado de Matplotlib
plt.style.use('ggplot')  # Cambiar a un estilo incorporado de Matplotlib

# Dibujar un gráfico de barras (proporción) - Usar colores de gradiente
colores_barras = ['#4A86E8', '#6AA1E8', '#8ABBE8', '#AAD5E8']  # Gradiente azul
barras = ax1.bar(x, proporcion, color=colores_barras, label='Proporción', width=0.6, edgecolor='black', linewidth=0.5)
ax1.set_ylabel('Proporción (%)', color='#4A86E8', fontsize=12)
ax1.set_xlabel('Nivel de ciudad', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(niveles_ciudad, fontsize=11)
ax1.tick_params(axis='y', labelcolor='#4A86E8')

# Agregar etiquetas de datos encima del gráfico de barras
for barra in barras:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2., altura + 0.5,
             f'{altura}%', ha='center', va='bottom', fontsize=10)

# Crear un segundo eje y y dibujar un gráfico de línea (tasa de crecimiento)
ax2 = ax1.twinx()
color_linea = '#FF9900'  # Naranja
ax2.plot(x, tasa_crecimiento, color=color_linea, label='Tasa de crecimiento', linewidth=2.5, marker='o', markersize=8)
ax2.set_ylabel('Tasa de crecimiento (%)', color=color_linea, fontsize=12)
ax2.tick_params(axis='y', labelcolor=color_linea)
ax2.set_ylim([-10, 0])  # Establecer el rango del eje de la tasa de crecimiento

# Agregar etiquetas de datos en el gráfico de línea
for i, txt in enumerate(tasa_crecimiento):
    ax2.annotate(f'{txt}%', (x[i], tasa_crecimiento[i]), textcoords="offset points", 
                 xytext=(0,10), ha='center', fontsize=10, color=color_linea)

# Agregar una leyenda - Usar un estilo más bonito
lineas_1, etiquetas_1 = ax1.get_legend_handles_labels()
lineas_2, etiquetas_2 = ax2.get_legend_handles_labels()
ax1.legend(lineas_1 + lineas_2, etiquetas_1 + etiquetas_2, loc='upper right', 
           frameon=True, framealpha=0.9, edgecolor='black', fancybox=True)

# Agregar un título al gráfico
plt.title('Proporción de atención de la industria de la formación profesional por nivel de ciudad en mayo', fontsize=16, fontweight='bold', pad=20)

# Agregar líneas de cuadrícula para mejorar la legibilidad
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.grid(axis='x', visible=False)
ax2.grid(visible=False)

# Ajustar el diseño del gráfico
plt.tight_layout()

# Mostrar el gráfico
plt.show()