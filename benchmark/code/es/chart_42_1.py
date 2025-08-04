import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2014, 2025)
# Datos de ingresos (trillones de yuanes), el valor para 2024 es la previsión (E)
revenues = [2.5, 2.8, 3.2, 4.4, 5.4, 6.9, 7.4, 8.0, 8.3, 8.6, 9.0]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(12, 7))

# Establecer el estilo de la cuadrícula
plt.grid(True, linestyle='--', alpha=0.7)

# Crear un gráfico de barras con colores degradados
colors = plt.cm.Blues(np.linspace(0.5, 0.9, len(years)))
bars = ax.bar(years, revenues, color=colors, edgecolor='black', linewidth=0.5)

# Establecer el título y las etiquetas de los ejes
ax.set_title('Ingresos generales y previsión de la industria de la gran salud de China desde 2014 hasta 2024', fontsize=16, pad=20)
ax.set_xlabel('Año', fontsize=14, labelpad=10)
ax.set_ylabel('Ingresos (Trillones de Yuanes)', fontsize=14, labelpad=10)

# Establecer las marcas de los ejes x e y
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 10, 1))

# Añadir etiquetas numéricas a cada barra
for bar, revenue in zip(bars, revenues):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{revenue}', ha='center', va='bottom', fontsize=10)

# Resaltar el valor de la previsión
prediction_bar = bars[-1]
prediction_bar.set_color('lightgreen')
prediction_bar.set_edgecolor('black')
ax.text(prediction_bar.get_x() + prediction_bar.get_width()/2., 
        prediction_bar.get_height() + 0.4,
        f'{revenues[-1]} (Previsión)', ha='center', va='bottom', fontsize=10, weight='bold')

# Añadir una leyenda
ax.legend([bars[0], prediction_bar], ['Valor real', 'Previsión (E)'], loc='upper left')

# Establecer el rango del eje y
plt.ylim(0, 10)

# Mejorar la apariencia del gráfico
plt.tight_layout()

# Mostrar el gráfico
plt.show()