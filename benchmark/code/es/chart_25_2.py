import matplotlib.pyplot as plt

# Datos
etiquetas = ['De 25 a 34 años', 'Menores de 19 años', 'De 19 a 24 años', 'Mayores de 35 años']
tamaños = [37, 28, 18, 17]

# Dibujar un gráfico de pastel
fig, ax = plt.subplots()
ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Asegurar que el gráfico de pastel sea un círculo perfecto

# Agregar un título
ax.set_title('Proporción de edad de las personas preocupadas por el "Sentido del Ritual de la Fiesta de Primavera"')

# Mostrar el gráfico
plt.show()