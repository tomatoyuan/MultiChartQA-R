import matplotlib.pyplot as plt
import numpy as np

# Datos del gráfico circular izquierdo
etiquetas_pastel = ["Dos años", "Tres años", "Cuatro años o más", "Dentro de un año"]
tamaños_pastel = [49.0, 33.7, 9.3, 8.0]
colores_pastel = ["#8B4513", "#FFA07A", "#32CD32", "#FF8C00"]

# Datos del gráfico de barras derecho
factores_barra = ["Rendimiento", "Tamaño de pantalla", "Duración de la batería", "Marca", "RAM", "Precio", "Función de cámara", "Capacidad de almacenamiento", "Otros"]
proporciones_barra = [57.6, 57.0, 54.2, 47.2, 41.8, 38.4, 34.3, 31.1, 0.2]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Gráfico circular izquierdo
porciones, textos, textos_automaticos = ax1.pie(tamaños_pastel, labels=etiquetas_pastel, colors=colores_pastel, autopct="%1.1f%%", startangle=90)
for texto_automatico in textos_automaticos:
    texto_automatico.set_color("white")
ax1.set_title("Frecuencia de reemplazo de teléfonos móviles por parte de los consumidores chinos")

# Gráfico de barras derecho
x = np.arange(len(factores_barra))
barras = ax2.bar(x, proporciones_barra, color="#FF8C00")
for i, proporcion in enumerate(proporciones_barra):
    ax2.text(i, proporcion + 1, f"{proporcion}%", ha="center", va="bottom")
ax2.set_ylabel("Proporción (%)")
ax2.set_xlabel("Factores de consideración")
ax2.set_xticks(x)
ax2.set_xticklabels(factores_barra, rotation=45)
ax2.set_title("Factores considerados por los consumidores chinos al elegir teléfonos móviles")

plt.tight_layout()
plt.show()