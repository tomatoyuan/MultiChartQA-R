import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", 
         "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "Ene - Nov 2023"]
ventas_minoristas = [4.2, 4.7, 5.1, 5.8, 6.6, 7.7, 9.1, 11.1, 12.8, 15.2, 18.0, 20.6, 23.2, 25.9, 28.7, 31.6, 
                34.7, 37.8, 40.8, 39.2, 44.1, 44.0, 42.8]
tasa_de_crecimiento = [0, 11.6, 8.9, 13.1, 14.6, 15.5, 18.0, 22.5, 15.6, 18.5, 18.2, 14.3, 13.0, 11.7, 10.4, 10.2, 
               10.0, 8.8, 8.0, -3.9, 12.5, -0.2, -0.5]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Dibujar un gráfico de barras de las ventas minoristas totales de bienes de consumo
ax1.bar(x, ventas_minoristas, color='orange', label='Ventas Minoristas Totales de Bienes de Consumo (Billones de Yuanes)')
ax1.set_ylabel('Ventas Minoristas Totales de Bienes de Consumo (Billones de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años, rotation=45, ha='right')
ax1.legend(loc='upper left')

# Crear un eje y secundario y dibujar un gráfico de línea de la tasa de crecimiento interanual
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='brown', label='Tasa de Crecimiento Interanual (%)', linewidth=2)
ax2.set_ylabel('Tasa de Crecimiento Interanual (%)')
ax2.legend(loc='lower left')

# Añadir etiquetas de valor para las ventas minoristas totales de bienes de consumo
for i, ventas in enumerate(ventas_minoristas):
    ax1.text(i, ventas + 0.5, f'{ventas}', ha='center', va='bottom')

# Añadir etiquetas de valor para la tasa de crecimiento interanual
for i, tasa in enumerate(tasa_de_crecimiento):
    ax2.text(i, tasa + 0.5, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Ventas Minoristas Totales de Bienes de Consumo y Tasa de Crecimiento en China desde 2001 hasta los primeros 11 meses de 2023')

plt.tight_layout()
plt.show()