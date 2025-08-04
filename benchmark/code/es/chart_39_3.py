import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ["Visita frecuentemente, la cultura de estilo shanghaines es muy distintiva", "Ha visitado, ha experimentado la cultura del café de la antigua Shanghái", "No ha visitado, pero está bastante interesado", "No quiere visitar, no está muy interesado"]
tamaños = [31, 50, 16, 3]  # Los datos pueden ser aproximadamente los mismos
# Colores, tratar de estar cerca de la imagen original y se pueden ajustar según la situación real
colores = ["#E67E22", "#F1C40F", "#BDC3C7", "#95A5A6"]

# Dibujar un gráfico circular
fig, ax = plt.subplots()
ax.pie(tamaños, labels=etiquetas, autopct="%1.1f%%", startangle=140, colors=colores)

# Establecer el título
ax.set_title("Voluntad de los consumidores para experimentar los cafés de estilo shanghaines")

# Mostrar el gráfico
plt.show()