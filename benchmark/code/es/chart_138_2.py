import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]
# Datos de producción de varios tipos (Unidad: 10,000 toneladas), orden: Verduras, Carne, Productos acuáticos
vegetable = [67434.2, 69192.7, 70346.7, 72102.6, 74912.9, 77549.0, 80000.0]
meat = [8628.3, 8654.4, 8624.6, 7758.8, 7748.4, 8990.0, 9328.4]
aquatic = [6379.5, 6445.3, 6457.7, 6480.4, 6549.0, 6690.0, 6549.0]

x = np.arange(len(years))  # Coordenadas del eje x
bar_width = 0.3  # Ancho de cada gráfico de barras de cada categoría

fig, ax = plt.subplots(figsize=(12, 8))

# Dibujar el gráfico de barras para la producción de verduras (en la parte inferior)
ax.bar(x, vegetable, width=bar_width, label='Producción de Verduras (10,000 toneladas)', color='#CD5C5C')
# Dibujar el gráfico de barras para la producción de carne (encima de la producción de verduras)
ax.bar(x, meat, width=bar_width, bottom=vegetable, label='Producción de Carne (10,000 toneladas)', color='#FFA07A')
# Dibujar el gráfico de barras para la producción de productos acuáticos (encima de la producción de carne)
ax.bar(x, aquatic, width=bar_width, bottom=np.array(vegetable) + np.array(meat), 
       label='Producción Total de Productos Acuáticos (10,000 toneladas)', color='#FFDAB9')

# Agregar etiquetas numéricas para los diferentes tipos de producción
# Etiquetar la producción de verduras
for i, v in enumerate(vegetable):
    ax.text(i, v / 2, f'{v}', ha='center', va='center', color='white', fontweight='bold')
# Etiquetar la producción de carne
for i, (v, m) in enumerate(zip(vegetable, meat)):
    ax.text(i, v + m / 2, f'{m}', ha='center', va='center', color='white', fontweight='bold')
# Etiquetar la producción de productos acuáticos
for i, (v, m, a) in enumerate(zip(vegetable, meat, aquatic)):
    bottom_sum = v + m
    ax.text(i, bottom_sum + a / 2, f'{a}', ha='center', va='center', color='white', fontweight='bold')

ax.set_ylabel('Producción (10,000 toneladas)')
ax.set_xlabel('Año')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('Producción de Materias Primas de Ingredientes para Fondue en China de 2016 - 2022')

plt.tight_layout()
plt.show()