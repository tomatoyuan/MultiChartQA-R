import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2020", "2022", "2023", "Estimado 2025"]
# Consumo anual per cápita de café en los años correspondientes
data = [9.1, 11.3, 16.74, 20]
# Establece un color diferente para los datos estimados de 2025, aquí se utiliza naranja, que se puede ajustar según las necesidades reales
colors = ["#1f77b4", "#1f77b4", "#1f77b4", "#ff7f0e"]  

x = np.arange(len(years))  # Posiciones del eje x

fig, ax = plt.subplots()
# Dibuja un gráfico de barras
bars = ax.bar(x, data, color=colors)  

# Establece las etiquetas de las marcas en el eje x
ax.set_xticks(x)
ax.set_xticklabels(years)

# Agrega un título
ax.set_title("Consumo anual per cápita de café en China (tazas)")

# Agrega etiquetas de datos a cada barra
for bar, value in zip(bars, data):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f"{value}",
            ha='center', va='bottom')

# Muestra el gráfico
plt.show()