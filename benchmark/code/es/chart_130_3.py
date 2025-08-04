import matplotlib.pyplot as plt
import numpy as np

# Tipos de problemas de calidad del sueño
etiquetas = ["Sueño ligero", "Dificultad para conciliar el sueño", "Despertarse fácilmente", "Somnolencia", "Sentirse cansado después de despertar", 
             "Dolor muscular y molestias en las articulaciones", "Trastorno respiratorio del sueño", "Trastorno de terror nocturno", 
             "Tiempo de sueño demasiado corto", "Sueños frecuentes", "Hablar en el sueño", "Trastorno de caminar sonámbulo", "Otros"]
# Proporción de cada problema (%)
proporciones = [32.1, 28.0, 27.7, 26.5, 26.5, 
                24.5, 23.9, 21.9, 21.7, 20.6, 
                13.1, 10.3, 4.2]

x = np.arange(len(etiquetas))

fig, ax = plt.subplots(figsize=(14, 8))

# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas encima de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f"{proporcion}%", ha="center", va="bottom")

# Configurar los ejes
ax.set_ylabel("Proporción (%)")
ax.set_xlabel("Tipos de problemas de calidad del sueño")
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, rotation=45, ha='right')  # Rotar las etiquetas para evitar solapamiento

ax.set_title("Problemas de calidad del sueño experimentados por los residentes chinos")

plt.tight_layout()
plt.show()