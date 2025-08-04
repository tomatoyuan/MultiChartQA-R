import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Datos de fecha, utilizando números seriales para representar fechas (el 7 de mayo es el día 0, y así sucesivamente)
x = np.arange(0, 20, 1)
# Datos simulados del índice de transacciones, simulando aproximadamente la tendencia de la curva original
y = [10, 120, 140, 160, 170, 180, 190, 200, 210, 220, 250, 280, 310, 320, 330, 340, 350, 360, 370, 380]

# Crear puntos de datos más densos en el eje x para una curva suave
x_smooth = np.linspace(x.min(), x.max(), 300)

# Utilizar interpolación cúbica spline para crear una curva suave
spl = make_interp_spline(x, y, k=3)  # k = 3 significa spline cúbico
y_smooth = spl(x_smooth)

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Agregar el título principal
plt.title('Gráfico de la tendencia del índice de transacciones de la promoción 618', fontsize=16, pad=20)

# Dibujar la curva suave, establecer el color cercano al gradiente del gráfico original
line, = ax.plot(x_smooth, y_smooth, color='pink', linewidth=3)
# Rellenar el área debajo de la curva con un color de gradiente
ax.fill_between(x_smooth, y_smooth, color='pink', alpha=0.3)

# Establecer las marcas y etiquetas del eje x, correspondientes a fechas reales
x_labels = ['7 de mayo', '', '', '', '', '13 de mayo', '', '', '', '', '', '16 de mayo', '', '', '', '', '', '', '', '26 de mayo']
ax.set_xticks(np.arange(0, 20, 1))
ax.set_xticklabels(x_labels, rotation=0, ha='center')

# Agregar texto de anotación
ax.text(5, 50, 'Proporción del presupuesto de la primera ola: 60%\nGanar la ventaja de tráfico de la primera ola', fontsize=12, ha='center')
ax.text(5, 30, 'Fecha de inicio de la pre - venta', fontsize=10, ha='center', color='red')
ax.text(15, 120, 'Ventas de pre - compra del 618', fontsize=12, ha='center', color='red')

# Anotar puntos de datos clave
highlight_indices = [0, 5, 10, 15, 19]  # Seleccionar los índices de los puntos de datos a anotar
for i in highlight_indices:
    # Anotar en la posición del punto de datos original, no en la posición suavizada
    ax.annotate(f'{y[i]}',  # El contenido de texto de la anotación
                xy=(x[i], y[i]),  # El punto de datos a anotar
                xytext=(x[i], y[i]+15),  # La posición del texto (por encima del punto de datos)
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),  # Estilo de la flecha
                ha='center',  # Alineación horizontal
                fontsize=10)  # Tamaño de fuente

# Establecer la etiqueta del eje y
ax.set_ylabel('Índice de transacciones')

# Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Mostrar el gráfico
plt.tight_layout()
plt.show()