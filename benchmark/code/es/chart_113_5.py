import matplotlib.pyplot as plt
import numpy as np

# Tipos de contenido de interés
contenidos = ["Consejos de dieta nutritiva y saludable", "Compartir conocimientos y experiencias maternas e infantiles", "Consultas médicas en línea", "Asesoramiento psicológico prenatal y gestión emocional", 
              "Preguntas y respuestas de conocimiento de expertos", "Interacción y actividades entre padres e hijos", "Registros de todo el proceso de embarazo y crianza", "Compras de productos en el centro comercial"]
# Proporciones correspondientes (%)
proporciones = [33.40, 32.59, 30.75, 29.94, 29.33, 28.31, 28.11, 27.29]

x = np.arange(len(contenidos))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(contenidos, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Contenido que preocupa a los consumidores maternos e infantiles chinos al usar aplicaciones verticales para madres e hijos en 2025')

plt.tight_layout()
plt.show()