import matplotlib.pyplot as plt

# Datos
etiquetas = ['Comprar seguro', 'Solicitar cita médica', 'Buscar remedios caseros', 'Rezar a los dioses', 'Otros']
tamaños = [43, 18, 18, 21, 0]  # Proporciones de cada parte, la suma es 100, se pueden ajustar según sea necesario
colores = ['#FFA07A', '#90EE90', '#FFC0CB', '#87CEFA', '#D3D3D3']  # Colores de cada parte, se pueden personalizar

# Dibujar un gráfico circular
fig, ax = plt.subplots()
ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Asegurar que el gráfico circular sea un círculo perfecto

# Agregar un título
plt.title('Comportamientos posteriores de pacientes con cáncer')

# Mostrar el gráfico
plt.show()