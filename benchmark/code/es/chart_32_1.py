import matplotlib.pyplot as plt
import numpy as np

# Datos
años = np.arange(2016, 2021)
# Calor de búsqueda simulado (solo para reproducir la tendencia, no son datos reales, se pueden reemplazar)
calor_de_busqueda = [10, 30, 50, 70, 100]

# Graficado
plt.figure(figsize=(6, 4))
# Gráfico de barras de color degradado (simulación simple, se puede hacer una personalización más refinada con colormap)
barras = plt.bar(años, calor_de_busqueda, color=plt.cm.get_cmap('Purples')(np.linspace(0.3, 0.9, len(años))))

# Anotación de datos
for barra, calor in zip(barras, calor_de_busqueda):
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura + 2,
             f'{calor}', ha='center', va='bottom', fontsize=10)

# Título y etiquetas
plt.title('¡En 2020, la búsqueda de certificados de enseñanza se disparó! ¡Ser profesor se hace más atractivo!', fontsize=12)
plt.xlabel('Año')
plt.ylabel('Calor de Búsqueda (Simulado)')

# Optimizar visualización
plt.xticks(años)
# Ocultar los bordes superior y derecho
for borde in ['top', 'right']:
    plt.gca().spines[borde].set_visible(False)

plt.show()