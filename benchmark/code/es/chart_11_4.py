import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Fuerza de la escuela', 'Interés profesional', 'Ubicación geográfica', 'Otros']
valores = [24, 36, 13, 27]
colores = ['#FF7F0E', '#2CA02C', '#FFD700', '#1F77B4']  # Colores correspondientes

# Crear un lienzo y ejes
fig, ax = plt.subplots()

# Dibujar un gráfico de barras horizontales
ax.barh(etiquetas, valores, color=colores)

# Agregar etiquetas de datos
for i, v in enumerate(valores):
    ax.text(v + 1, i, str(v) + '%', va='center')

# Establecer el título
ax.set_title('¿Qué más te preocupa cuando tienes múltiples escuelas para elegir?')

# Mostrar el gráfico
plt.show()