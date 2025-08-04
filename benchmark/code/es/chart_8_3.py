import matplotlib.pyplot as plt
import numpy as np

# Niveles de ciudades
niveles_ciudades = ['Ciudades de primer nivel', 'Ciudades de segundo nivel', 'Ciudades de tercer nivel', 'Ciudades de cuarto nivel']
# Datos de proporción (para el gráfico de barras)
proporcion = [52, 15, 14, 10]
# Datos de tasa de crecimiento (para el gráfico de línea)
tasa_crecimiento = [3, -18, -30, -18]

x = np.arange(len(niveles_ciudades))  # Índices del eje X

fig, ax1 = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño del gráfico

# Dibujar el gráfico de barras (proporción)
barras = ax1.bar(x, proporcion, color='blue', label='Proporción')
ax1.set_ylabel('Proporción (%)', color='blue')
ax1.set_xlabel('Niveles de ciudades')
ax1.set_xticks(x)
ax1.set_xticklabels(niveles_ciudades)
ax1.tick_params(axis='y', labelcolor='blue')

# Agregar etiquetas de datos al gráfico de barras
for barra in barras:
    altura = barra.get_height()
    ax1.annotate(f'{altura}%',
                 xy=(barra.get_x() + barra.get_width() / 2, altura),
                 xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                 textcoords="offset points",
                 ha='center',
                 va='bottom',
                 color='blue')

# Crear un segundo eje Y para dibujar el gráfico de línea (tasa de crecimiento)
ax2 = ax1.twinx()
linea, = ax2.plot(x, tasa_crecimiento, color='orange', label='Tasa de crecimiento', marker='o', markersize=6)
ax2.set_ylabel('Tasa de crecimiento (%)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Agregar etiquetas de datos al gráfico de línea
for i, tasa in enumerate(tasa_crecimiento):
    ax2.annotate(f'{tasa}%',
                 xy=(x[i], tasa),
                 xytext=(5, 5) if tasa >= 0 else (5, -5),  # Ajustar la posición según sea positivo o negativo
                 textcoords="offset points",
                 ha='left',
                 va='bottom' if tasa >= 0 else 'top',
                 color='orange',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))

# Agregar una leyenda
lineas_1, etiquetas_1 = ax1.get_legend_handles_labels()
lineas_2, etiquetas_2 = ax2.get_legend_handles_labels()
ax1.legend(lineas_1 + lineas_2, etiquetas_1 + etiquetas_2, loc='upper right')

# Establecer el título
plt.title('Proporción de atención y tasa de crecimiento de la industria de litigios de divorcio por nivel de ciudad en mayo')

# Agregar líneas de cuadrícula
ax1.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()  # Asegurar que todos los elementos quepan en el área del gráfico
plt.show()