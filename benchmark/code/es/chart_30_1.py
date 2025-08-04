import matplotlib.pyplot as plt
import numpy as np

# Datos
años = [2015, 2016, 2017, 2018]
# Atención en cada trimestre (Trimestre 1 - 4)
t1 = [1000, 1200, 5000, 4000]
t2 = [800, 1300, 4800, 5000]
t3 = [600, 1100, 4600, 4500]
t4 = [1200, 1500, 8000, 1500]
# Nuevas infecciones por VIH reportadas
nuevas_infecciones = [115465, 124555, 134512, 160000]

# Desplazamiento para graficar múltiples gráficos de barras en el mismo eje X
x = np.arange(len(años))
ancho = 0.2

# Crear un lienzo y subgráficos
fig, ax1 = plt.subplots(figsize=(8, 5))

# Graficar gráficos de barras para la atención en cada trimestre
ax1.bar(x - 1.5*ancho, t1, ancho, label='Trimestre 1', color='#f78b9b')
ax1.bar(x - 0.5*ancho, t2, ancho, label='Trimestre 2', color='#ff5e2d')
ax1.bar(x + 0.5*ancho, t3, ancho, label='Trimestre 3', color='#d4b17c')
ax1.bar(x + 1.5*ancho, t4, ancho, label='Trimestre 4', color='#3b3b3b')

# Establecer el título del eje Y izquierdo (Atención)
ax1.set_ylabel('Atención', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear el eje Y derecho para graficar el gráfico de línea de las nuevas infecciones por VIH reportadas
ax2 = ax1.twinx()
line, = ax2.plot(x, nuevas_infecciones, marker='o', color='#8bc34a', label='Nuevas infecciones por VIH reportadas')

# Agregar etiquetas de datos al gráfico de línea
for i, (x_val, y_val) in enumerate(zip(x, nuevas_infecciones)):
    # Convertir el número de infecciones a una cadena con separadores de miles
    y_text = f"{y_val:,}"
    ax2.annotate(y_text,  # Texto de la anotación
                 (x_val, y_val),  # Posición del punto de datos
                 textcoords="offset points",  # Coordenadas del texto en relación con el punto de datos
                 xytext=(0, 10),  # Desplazamiento en las direcciones X e Y
                 ha='center',  # Alineación horizontal
                 fontsize=9)  # Tamaño de la fuente

ax2.set_ylabel('Nuevas infecciones por VIH reportadas', fontsize=12)
ax2.legend(loc='upper right')

# Título del gráfico
plt.title('Atención a la información relacionada con "SIDA" y nuevas infecciones por VIH reportadas (2015 - 2018)', fontsize=14, pad=20)

# Ajustar el diseño
plt.tight_layout()
# Mostrar el gráfico
plt.show()