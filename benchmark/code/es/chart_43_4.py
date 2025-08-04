import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ["Equipamiento audiovisual (Altavoces inteligentes, Auriculares inteligentes)", "Productos educativos electrónicos (Máquinas de aprendizaje, etc.)", "Hardware de computadora/Monitores/Periféricos de computadora", 
              "Productos de fotografía y videografía", "Consolas de juegos y accesorios (Switch, PS, etc.)", "Nunca ha comprado"]
porcentajes = [51.1, 36.4, 34.2, 23.0, 17.5, 13.1]

# Crear una figura y ejes
fig, ax = plt.subplots()

# Dibujar un gráfico de barras
barras = ax.bar(categorias, porcentajes, color='cyan')

# Establecer el título y las etiquetas
ax.set_title('Proporción de mujeres que compraron varios productos digitales 3C en el último año', pad=50)
ax.set_ylabel('Proporción (%)')

# Rotar las etiquetas del eje x para evitar solapamiento
plt.xticks(rotation=45, ha='right')

# Agregar etiquetas numéricas sobre cada barra
for barra, porcentaje in zip(barras, porcentajes):
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2., altura + 0.5,
            f'{porcentaje}%', ha='center', va='bottom')

# Mostrar el gráfico
plt.tight_layout()
plt.show()