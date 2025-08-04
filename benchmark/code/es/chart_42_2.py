import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2014, 2025)
# Datos de ingresos (billones de yuanes), 2024 es el valor pronosticado (P)
revenues = [2.5, 2.8, 3.2, 4.4, 5.4, 6.9, 7.4, 8.0, 8.3, 8.6, 9.0]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(12, 7))

# Establecer el estilo de la cuadrícula
plt.grid(True, linestyle='--', alpha=0.7)

# Crear un gráfico de barras con colores degradados
colors = plt.cm.Blues(np.linspace(0.5, 0.9, len(years)))
bars = ax.bar(years, revenues, color=colors, edgecolor='black', linewidth=0.5)

# Establecer el título y las etiquetas de los ejes
ax.set_title('Ingresos generales y pronóstico de la industria de la gran salud en China desde 2014 hasta 2024', fontsize=16, pad=20)
ax.set_xlabel('Año', fontsize=14, labelpad=10)
ax.set_ylabel('Ingresos (billones de yuanes)', fontsize=14, labelpad=10)

# Establecer las marcas de los ejes x e y
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 10, 1))

# Modificar la etiqueta del eje x para 2024 a 2024P
xticks_labels = [str(year) for year in years]
xticks_labels[-1] = '2024P'
ax.set_xticklabels(xticks_labels)

# Agregar etiquetas numéricas a cada barra
for bar, revenue in zip(bars, revenues):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{revenue}', ha='center', va='bottom', fontsize=10)

# Resaltar el valor pronosticado
prediction_bar = bars[-1]
prediction_bar.set_color('lightgreen')
prediction_bar.set_edgecolor('black')

# Agregar una leyenda
ax.legend([bars[0], prediction_bar], ['Valor real', 'Valor pronosticado'], loc='upper left')

# Establecer el rango del eje y
plt.ylim(0, 10)

# Mejorar la apariencia del gráfico
plt.tight_layout()

# Mostrar el gráfico
plt.show()