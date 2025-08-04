import matplotlib.pyplot as plt

# Datos
etiquetas = ['19 años - 34 años', '≤18 años', 'Otros']
tamaños = [83, 13, 4]  # Suponemos que "otros" representa el 4%, se puede ajustar según los datos reales exactos
colores = ['pink', 'blue', 'lightcoral']

# Dibujar el gráfico circular
fig, ax = plt.subplots()
ax.pie(tamaños, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Asegurar que el gráfico circular sea un círculo perfecto

# Agregar título
plt.title('Proporción de búsqueda de "Certificado de Docencia" en diferentes rangos de edad')

# Mostrar el gráfico
plt.show()