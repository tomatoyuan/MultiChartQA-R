import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# Nombres de los jugadores
jugadores = ["Messi", "Neymar", "Salah", "Ronaldo", "Ramos", "Iniesta", "Kane", "Pogba", "Griezmann", "Cheryshev"]
# Datos de popularidad
popularidades = [80, 33, 27, 20, 15, 12, 13.1, 13.1, 13, 6.4]
# Generar índices para mapear las marcas del eje x a los jugadores
x = np.arange(len(jugadores))  

# Crear una figura
fig, ax = plt.subplots()
# Dibujar un gráfico de barras con un color degradado de púrpura a rosa
barras = ax.bar(x, popularidades, color=plt.cm.get_cmap('Purples')(np.linspace(0.2, 0.8, len(jugadores))))

# Establecer las etiquetas de las marcas del eje x como nombres de jugadores
ax.set_xticks(x)
ax.set_xticklabels(jugadores, rotation=45)

# Establecer la etiqueta del eje y
ax.set_ylabel("Popularidad (en miles)")
# Establecer el título
ax.set_title("Ranking de Popularidad de los 10 Mejores Futbolistas")

# Anotar los valores en las barras
for barra, popularidad in zip(barras, popularidades):
    altura = barra.get_height()
    ax.annotate(f'{popularidad}K',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazamiento vertical del valor con respecto a la barra
                textcoords="offset points",
                ha='center', va='bottom')

# Ajustar el diseño para evitar que las etiquetas se corten
plt.tight_layout()
# Mostrar el gráfico
plt.show()