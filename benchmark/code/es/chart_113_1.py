import matplotlib.pyplot as plt
import numpy as np

# Tipos de información de interés
tipos_de_informacion = ["Conocimientos de crianza científica", "Conocimientos de salud prenatal", "Recomendación de productos/alimentos maternos y infantiles", "Guía científica de embarazo", 
                        "Guía de rehabilitación postparto", "Cursos de educación temprana", "Ropa de moda para bebés y niños pequeños", "Guía de vestimenta durante el embarazo"]
# Proporciones correspondientes (%)
proporciones = [34.62, 33.60, 33.20, 32.59, 32.59, 32.59, 31.16, 28.31]

x = np.arange(len(tipos_de_informacion))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, girar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(tipos_de_informacion, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Principales informaciónes de interés para los consumidores maternos e infantiles chinos durante el embarazo y la crianza en 2025')

plt.tight_layout()
plt.show()