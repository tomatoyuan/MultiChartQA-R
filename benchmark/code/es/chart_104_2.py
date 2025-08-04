import matplotlib.pyplot as plt
import numpy as np

# Nombres de los cursos
cursos = ["Instrumentos de teclado (Piano, Órgano, Acordeón, Teclado electrónico, etc.)", 
          "Instrumentos de cuerda (Violín, Guitarra, Erhu, Guzheng, Pipa, etc.)", 
          "Instrumentos de viento madera (Flauta, Suona, Oboe, Saxofón, etc.)", 
          "Instrumentos de percusión (Xilófono, Tambor de tensión, Bombo, Chapines, Yangqin, etc.)", 
          "Instrumentos de viento metal (Trompeta, Corneta, Trombón, Trompa francesa, Tuba, etc.)", 
          "Música vocal"]
# Proporciones correspondientes
proporciones = [40.08, 35.22, 31.31, 29.82, 27.94, 17.95]

y = np.arange(len(cursos))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(cursos)
ax.set_xlabel('Proporción (%)')
ax.set_title('Principales cursos inscritos por usuarios chinos en 2025')

plt.show()