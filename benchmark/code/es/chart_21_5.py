import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Tasa de éxito en un intento', 'Tasa de éxito en dos intentos', 'Tasa de éxito después de tres o más intentos']
valores = [8, 27, 65]

# Crear una figura
fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar el ancho del gráfico

# Dibujar un gráfico de barras
ax.bar(etiquetas, valores, color=['lightblue', 'lightgreen', 'lightcoral'])

# Configurar la rotación de las etiquetas del eje x en 30 grados
plt.xticks(rotation=30, ha='right', fontsize=10)  # Inclinar 30 grados y alinear a la derecha

# Agregar etiquetas numéricas
for i, v in enumerate(valores):
    ax.text(i, v + 1, f'{v}%', ha='center')

# Establecer el título y las etiquetas de los ejes (ajustar según sea necesario)
ax.set_ylabel('Porcentaje')
# Agregar un título
ax.set_title('Distribución de las tasas de éxito de entrada del código de verificación de 12306 durante el período de viaje de la Fiesta de Primavera en 2016')

# Mostrar la figura
plt.tight_layout()  # Ajustar el diseño
plt.show()