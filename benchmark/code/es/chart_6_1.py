import matplotlib.pyplot as plt
import numpy as np

# Lista de fechas
fechas = ["5/1", "5/2", "5/3", "5/4", "5/5", "5/6", "5/7", "5/8", "5/9", "5/10", 
          "5/11", "5/12", "5/13", "5/14", "5/15", "5/16", "5/17", "5/18", "5/19", 
          "5/20", "5/21", "5/22", "5/23", "5/24", "5/25", "5/26", "5/27", "5/28", 
          "5/29", "5/30", "5/31"]
# Volumen de búsqueda de servicios legales (gráfico de barras, eje izquierdo)
servicio_legal = [1200000, 1100000, 1200000, 1300000, 1400000, 1800000, 2000000, 
                  1900000, 1950000, 1900000, 1800000, 1850000, 1500000, 
                  1400000, 1300000, 1800000, 1700000, 1750000, 1400000, 
                  1350000, 1300000, 2200000, 1200000, 1350000, 1800000, 
                  1850000, 1900000, 1500000, 1400000, 1450000, 2000000]
# Lista de proporción de disputas de propiedad (aproximadamente %)
disputa_propiedad = [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 
                     0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 
                     0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5]
# Lista de proporción de demandas de divorcio (aproximadamente %)
demanda_divorcio = [5.2, 5.0, 4.9, 4.8, 4.7, 4.6, 5.5, 5.0, 4.6, 4.5, 
                    4.4, 4.3, 3.2, 3.3, 3.4, 3.5, 3.4, 3.3, 3.0, 3.1, 
                    3.2, 5.0, 4.5, 4.0, 3.2, 3.3, 3.4, 4.5, 4.3, 4.2, 4.0]

# Crear un lienzo y ejes dobles
fig, ax1 = plt.subplots(figsize=(14, 8))  # Eje primario (eje izquierdo)
ax2 = ax1.twinx()  # Eje secundario (eje derecho, proporción)

# Dibujar servicios legales (gráfico de barras, eje izquierdo)
x = np.arange(len(fechas))  # Índice de coordenadas X
barras = ax1.bar(x, servicio_legal, color='blue', label='Servicio Legal', width=0.6)
ax1.set_ylabel('Volumen de Búsqueda', color='blue', fontsize=12)
ax1.set_ylim(0, 2500000)  # Coincidir con el rango del eje izquierdo de la figura original
ax1.tick_params(axis='y', labelcolor='blue')

# Dibujar disputa de propiedad y demanda de divorcio (gráfico de líneas, eje derecho)
linea1, = ax2.plot(x, disputa_propiedad, color='orange', label='Disputa de Propiedad', marker='o', linestyle='-', linewidth=2)
linea2, = ax2.plot(x, demanda_divorcio, color='green', label='Demanda de Divorcio', marker='o', linestyle='-', linewidth=2)
ax2.set_ylabel('Proporción (%)', color='black', fontsize=12)
ax2.set_ylim(0, 6)  # Coincidir con el rango del eje derecho de la figura original (0% - 6%)
ax2.tick_params(axis='y', labelcolor='black')

# Configuración de las coordenadas X y la leyenda
ax1.set_xticks(x)
ax1.set_xticklabels(fechas, rotation=45, fontsize=10)  # Inclinar las fechas para evitar solapamiento
ax1.set_title('Tendencia de Atención de Búsqueda en Mayo de la Industria de Servicios Legales y Proporción de Sub - industrias', fontsize=14, pad=20)

# Agregar etiquetas de datos al gráfico de barras (volumen de búsqueda)
for i, barra in enumerate(barras):
    altura = barra.get_height()
    # Mostrar etiquetas cada 3 días para evitar sobrecrowding
    if i % 3 == 0:
        ax1.annotate(f'{altura:,}',
                     xy=(barra.get_x() + barra.get_width() / 2, altura),
                     xytext=(0, 5),  # Desplazamiento hacia arriba de 5 puntos
                     textcoords="offset points",
                     ha='center', va='bottom',
                     fontsize=9,
                     color='blue',
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", alpha=0.7))

# Agregar etiquetas de datos al gráfico de líneas de disputa de propiedad
for i, (x_val, y_val) in enumerate(zip(x, disputa_propiedad)):
    # Etiquetar solo puntos con cambios y nodos clave
    if y_val != 0.3 or i % 7 == 0 or i == len(x)-1:
        ax2.annotate(f'{y_val}%',
                     xy=(x_val, y_val),
                     xytext=(0, -15),  # Desplazamiento hacia abajo
                     textcoords="offset points",
                     ha='center', va='top',
                     fontsize=9,
                     color='orange',
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))

# Agregar etiquetas de datos al gráfico de líneas de demanda de divorcio
for i, (x_val, y_val) in enumerate(zip(x, demanda_divorcio)):
    # Etiquetar solo picos, valles y nodos clave
    if i == 0 or i == len(x)-1 or i % 5 == 0 or \
       (i > 0 and i < len(x)-1 and 
        (y_val > demanda_divorcio[i-1] and y_val > demanda_divorcio[i+1]) or 
        (y_val < demanda_divorcio[i-1] and y_val < demanda_divorcio[i+1])):
        ax2.annotate(f'{y_val}%',
                     xy=(x_val, y_val),
                     xytext=(0, 10),  # Desplazamiento hacia arriba
                     textcoords="offset points",
                     ha='center', va='bottom',
                     fontsize=9,
                     color='green',
                     bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="green", alpha=0.7))

# Combinar leyendas (mostrar leyendas de ejes dobles juntas)
lineas_1, etiquetas_1 = ax1.get_legend_handles_labels()
lineas_2, etiquetas_2 = ax2.get_legend_handles_labels()
ax1.legend(lineas_1 + lineas_2, etiquetas_1 + etiquetas_2, loc='upper left', fontsize=10)

# Agregar líneas de cuadrícula para mejorar la legibilidad
ax1.grid(True, linestyle='--', alpha=0.3)

# Optimizar el diseño
plt.tight_layout()
plt.show()