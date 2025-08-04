import matplotlib.pyplot as plt
import numpy as np

# Categorías de nivel educativo
etiquetas = ['Posgrado y superior', 'Grado', 'Bachillerato', 'Secundaria', 'Inferior a secundaria']
# Proporción hipotética de personas interesadas en cada nivel de educación (reemplazar con datos reales, este es solo un ejemplo)
tamaños = [10, 30, 25, 20, 15]  

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops establece el ancho del donut
ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90,
       wedgeprops={'width': 0.3})  
ax.axis('equal')  # Asegurar que el gráfico de pastel (donut) se dibuje como un círculo

plt.title('Distribución del nivel educativo de la población interesada')
plt.show()