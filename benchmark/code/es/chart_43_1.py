import matplotlib.pyplot as plt
import numpy as np

# Datos de años
años = np.arange(2015, 2025)
# Ventas minoristas totales de bienes de consumo correspondientes a cada año (en miles de millones de yuanes). Los datos se estiman aproximadamente según el gráfico y se pueden reemplazar con precisión según sea necesario.
ventas_minoristas = [290000, 310000, 340000, 370000, 400000, 390000, 430000, 435000, 460000, 480000]

# Crear un lienzo y subgráfico
fig, ax = plt.subplots()

# Dibujar un gráfico de barras
barras = ax.bar(años, ventas_minoristas, color='cyan', label='Ventas Minoristas Totales')

# Calcular la línea de tendencia
z = np.polyfit(años, ventas_minoristas, 1)
p = np.poly1d(z)
ax.plot(años, p(años), 'blue', label='Línea de Tendencia')

# Establecer las marcas del eje x para mostrar los años
plt.xticks(años)

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2., altura + 1000,
            f'{altura}',
            ha='center', va='bottom', rotation=0)

# Agregar un título y etiquetas de los ejes
ax.set_title('Tendencia de las Ventas Minoristas Totales de Bienes de Consumo en China de 2015 a 2024 (en miles de millones de yuanes)')
ax.set_xlabel('Año')
ax.set_ylabel('Ventas Minoristas Totales (en miles de millones de yuanes)')

# Agregar una leyenda
ax.legend()

# Mostrar el gráfico
plt.show()