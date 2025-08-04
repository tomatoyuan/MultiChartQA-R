import matplotlib.pyplot as plt
import numpy as np

# Datos
meses = ['2302', '2303', '2304', '2305', '2306', '2307', '2308', '2309',
         '2310', '2311', '2312', '2402', '2403']
x = np.arange(len(meses))

ventas_minoristas_sociales_yoy = [3.5, 10.6, 18.4, 12.7, 3.1, 2.5, 4.6, 5.5, 7.6, 10.1, 7.4, 5.5, 3.1]
ventas_minoristas_en_red_yoy = [5.3, 7.3, 10.4, 11.8, 10.8, 10.0, 9.5, 8.9, 8.4, 8.3, 8.4, 14.4, 11.6]

# Canvas
plt.figure(figsize=(12, 6))

# Gráfico de líneas
plt.plot(x, ventas_minoristas_sociales_yoy, marker='o', label='Ventas minoristas sociales YoY', color='#1976d2', linewidth=2)
plt.plot(x, ventas_minoristas_en_red_yoy, marker='s', label='Ventas minoristas en red de bienes físicos acumuladas YoY', color='#26a69a', linewidth=2)

# Agregar etiquetas de datos
for i, (y1, y2) in enumerate(zip(ventas_minoristas_sociales_yoy, ventas_minoristas_en_red_yoy)):
    plt.text(x[i], y1 + 0.7, f'{y1:.1f}%', ha='center', fontsize=9, color='#1976d2')
    plt.text(x[i], y2 - 1.2, f'{y2:.1f}%', ha='center', fontsize=9, color='#26a69a')

# Configurar ejes y título
plt.xticks(x, meses)
plt.ylabel('Tasa de crecimiento interanual (%)')
plt.title('Tendencia de ventas minoristas sociales y en red, 202301 - 202403')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()

# Agregar fuente de datos y explicación
plt.figtext(0.01, 0, "Fuente de datos: Magic Mirror Insight; Sina Finance\nExplicación de datos: La tasa interanual de ventas minoristas en red es la tasa interanual acumulada hasta el mes correspondiente;",
            ha='left', fontsize=9, linespacing=1.5)

plt.tight_layout()
plt.ylim(2, 20)

plt.subplots_adjust(bottom=0.2)
plt.show()