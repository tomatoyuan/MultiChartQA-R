import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Proporción de recuperación en computadora', 'Proporción de recuperación en móvil']
tamaños = [12.03, 87.97]
# Colores, se pueden ajustar según sea necesario
colores = ['#b3d1ff', '#ff9966']  

# Crear una figura y un subgráfico
fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops se utiliza para establecer el ancho del anillo
ax.pie(tamaños, labels=etiquetas, autopct='%1.2f%%', startangle=90, colors=colores,
       wedgeprops={'width': 0.3})  

# Establecer el título (opcional, agregarlo según sea necesario)
ax.set_title('Distribución de la proporción de recuperación en la industria de litigios de divorcio')  

plt.show()