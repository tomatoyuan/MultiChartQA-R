import matplotlib.pyplot as plt
import numpy as np

# Nombres de las ciudades
ciudades = ['Beijing', 'Shenzhen', 'Chengdu', 'Shanghai', 'Hangzhou']
# Porcentajes de búsqueda correspondientes a cada ciudad (estimados según el gráfico, puedes reemplazarlos con datos precisos)
porcentajes = [5.5, 3.5, 2.9, 2.8, 2.7]  

x = np.arange(len(ciudades))  # Coordenadas del eje x

fig, ax = plt.subplots()
# Dibujar un gráfico de barras y establecer el color de las barras a azul
rects = ax.bar(x, porcentajes, color='blue')  

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(ciudades)
# Establecer el rango del eje y
ax.set_ylim([0, 6])  
# Establecer las marcas del eje y
ax.set_yticks(np.arange(0, 7, 1))  
# Agregar un título al gráfico
ax.set_title('Top 5 Ciudades para Búsquedas en la Industria de Servicios Legales en Mayo')  
# Agregar una etiqueta al eje y
ax.set_ylabel('Porcentaje de Búsqueda (%)')  

# Anotar los valores en las barras (opcional, para hacer la información del gráfico más intuitiva)
for rect in rects:
    altura = rect.get_height()
    ax.annotate('{}'.format(altura),
                xy=(rect.get_x() + rect.get_width() / 2, altura),
                xytext=(0, 3),  # Distancia vertical de la anotación del valor desde la barra
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()