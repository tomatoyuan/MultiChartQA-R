import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ["Encontrado innecesario después de la compra", "El producto no coincide con la descripción", "El tamaño o modelo no coincide", "Mercancía falsa o de mala calidad", "Mala actitud del servicio al cliente", "Mala calidad de los regalos gratuitos", "Difícil servicio postventa", "Retraso en la entrega express"]
valores = [10, 3, 2, 1, 1, 1, 0.5, 0.3]  # Los valores son simulados y se pueden ajustar según la situación real

x = np.arange(len(etiquetas))  # Posiciones de las marcas en el eje x

# Crear un gráfico
fig, ax = plt.subplots()
rectangulos = ax.bar(x, valores, color=['pink', 'pink', 'pink', 'orange', 'orange', 'orange', 'lightblue', 'lightblue'])

# Establecer las etiquetas de las marcas en el eje x
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, rotation=45, ha='right')

# Añadir un título
ax.set_title('Razones de arrepentimiento en el Día 11.11', fontsize=14, fontweight='bold')

# Añadir etiquetas numéricas a cada barra
for rectangulo in rectangulos:
    altura = rectangulo.get_height()
    ax.annotate('{}'.format(altura),
                xy=(rectangulo.get_x() + rectangulo.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazamiento de 3 píxeles
                textcoords="offset points",
                ha='center', va='bottom')

# Mostrar el gráfico
plt.tight_layout()
plt.show()