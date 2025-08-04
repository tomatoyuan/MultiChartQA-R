import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2019", "2020", "2021", "2022", "2023", "2024", "2025e", "2026e"]
# Ingresos de prima de cada tipo de seguro (en miles de millones de yuanes), los datos se simulan aproximadamente y se pueden ajustar según las situaciones reales
premium_data = np.array([
    [22754, 11649, 7066, 1000],    # 2019
    [23982, 11929, 8173, 1100],    # 2020
    [23572, 11671, 8447, 1200],    # 2021
    [24519, 12712, 8653, 1300],    # 2022
    [27646, 13607, 9035, 1400],    # 2023
    [31917, 14331, 9773, 1500],    # 2024
    [33736, 14918, 10174, 1600],   # 2025e
    [35659, 15530, 10591, 1700]    # 2026e
])

# Colores correspondientes a cada tipo de seguro
colors = ['green', 'limegreen', 'mediumseagreen', 'lightseagreen']
# Nombres de los tipos de seguro
insurance_types = ["Seguro de Vida (Miles de Millones de Yuanes)", "Seguro de Propiedad (Miles de Millones de Yuanes)", "Seguro de Salud (Miles de Millones de Yuanes)", "Seguro de Accidentes (Miles de Millones de Yuanes)"]

x = np.arange(len(years))  # Posiciones de las marcas en el eje x
bar_width = 0.6  # Ancho de las barras

fig, ax = plt.subplots(figsize=(14, 9))  # Aumentar aún más el tamaño del gráfico

# Dibujar un gráfico de barras apiladas
bottom = np.zeros(len(years))
for i in range(premium_data.shape[1]):
    bars = ax.bar(x, premium_data[:, i], width=bar_width, bottom=bottom, color=colors[i], label=insurance_types[i])
    bottom += premium_data[:, i]
    
    # Agregar etiquetas de datos encima de cada barra
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if height > 500:  # Mostrar solo etiquetas con altura suficiente para evitar la sobrecarga
            ax.text(
                bar.get_x() + bar.get_width()/2., 
                bar.get_y() + height/2,
                f'{int(height)}',
                ha='center', va='center',
                color='black', fontsize=8, fontweight='bold'
            )

# Agregar un título
ax.set_title('Ingreso de Prima Original y Tasa de Crecimiento de la Industria de Seguros China de 2019 a 2026', fontsize=16, pad=15)

# Establecer las etiquetas de las marcas en el eje x
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)

# Agregar una etiqueta al eje y
ax.set_ylabel('Ingreso de Prima (Miles de Millones de Yuanes)', fontsize=13)

# Agregar una leyenda
ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=11)

# Calcular la prima total para cada año
total_premiums = premium_data.sum(axis=1)

# Agregar anotaciones de prima total
for i, total in enumerate(total_premiums):
    ax.text(x[i], total + 1000,  # Ajustar la posición vertical para evitar superposición con las barras
            f'{int(total)}', 
            ha='center', va='bottom', 
            fontsize=9, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.7, pad=2.0))

# Función de anotación de CAGR
def add_cagr_annotation(start_idx, end_idx, cagr_value, ax, x, total_premiums):
    """Agregar anotación de polilínea de CAGR"""
    start_x = x[start_idx]
    end_x = x[end_idx]
    start_y = total_premiums[start_idx]
    end_y = total_premiums[end_idx]
    
    # Calcular la posición del punto medio
    mid_x = (start_x + end_x) / 2
    mid_y1 = start_y + (end_y - start_y) * 0.3
    mid_y2 = start_y + (end_y - start_y) * 0.7
    
    # Dibujar una polilínea
    ax.plot([start_x, end_x], [start_y, end_y], 
            'gray', linestyle='--', linewidth=1.2)
    
    # Agregar texto de CAGR
    text_x = mid_x
    text_y = mid_y2 + (end_y - start_y) * 0.25
    ax.text(text_x, text_y, f'CAGR = {cagr_value}%', 
            ha='center', va='bottom', fontsize=12, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', pad=3.0))

# Agregar anotación de CAGR de 2019 a 2024
add_cagr_annotation(0, 5, 6, ax, x, total_premiums)

# Agregar anotación de CAGR de 2024 a 2026
add_cagr_annotation(5, 7, 5, ax, x, total_premiums)

# Embelezar el gráfico
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Agregar líneas de cuadrícula horizontales
plt.tight_layout()  # Ajustar automáticamente el diseño

plt.show()