import matplotlib.pyplot as plt
import numpy as np

# Datos
canales = ["Motores de búsqueda en línea", "Redes sociales", "Canales oficiales de plataformas de comercio electrónico", "Medios de noticias tradicionales", "Informes e investigaciones de la industria", "Familiares y amigos", "Otros"]
porcentajes = [63.0, 59.2, 55.3, 35.2, 11.4, 6.3, 0.2]

x = np.arange(len(canales))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, porcentajes, color='orange')

# Agregar anotaciones numéricas
for i, porcentaje in enumerate(porcentajes):
    ax.text(i, porcentaje + 1, f'{porcentaje}%', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Porcentaje (%)')
ax.set_xlabel('Fuentes de información')
ax.set_xticks(x)
ax.set_xticklabels(canales, rotation=15, ha='right')
ax.set_title('Principales formas en las que los consumidores chinos se informan sobre el comercio electrónico impulsado por IA en 2024')

plt.tight_layout()
plt.show()