import matplotlib.pyplot as plt

# Datos
etiquetas = ["Sí", "No"]
tamaños = [39, 61]
# Colores para cada parte del gráfico circular, se pueden ajustar según sea necesario
colores = ["#87E8DE", "#FF6B6B"]  

# Crear un gráfico circular
fig, ax = plt.subplots()
ax.pie(tamaños, labels=etiquetas, autopct="%1.1f%%", startangle=90, colors=colores)
# Establecer el título
ax.set_title("¿Revisará tus calificaciones del examen con tus padres?")
# Asegurarse de que el gráfico circular sea un círculo perfecto
ax.axis("equal")  

# Mostrar el gráfico
plt.show()