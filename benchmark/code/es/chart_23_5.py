import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ["Parece imposible encontrar una pareja", "Habilidades de comunicación deficientes dificultan las citas", "Participar activamente en citas a ciegas", "Disfrutar de la cultura del soltería", "Otros"]
tamaños = [40, 20, 19, 7.8, 13.2]  # La proporción de "Otros" se calcula como 100 - 40 - 20 - 19 - 7.8, que es 13.2
colores = ["#f78199", "#a06cd5", "#ffe66d", "#ff4b5c", "#c3eaf4"]

# Crear un gráfico de donut
fig, ax = plt.subplots()
ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.1f%%", startangle=90, pctdistance=0.85)

# Agregar un círculo blanco en el centro para crear el efecto de gráfico de donut
circulo_centro = plt.Circle((0, 0), 0.70, fc="white")
fig.gca().add_artist(circulo_centro)

# Establecer el título
ax.set_title("Entre aquellos que evitan entrar en una relación")

# Ajustar el diseño y mostrar el gráfico
plt.tight_layout()
plt.show()