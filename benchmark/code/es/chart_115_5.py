import matplotlib.pyplot as plt
import numpy as np

# Tipos de demanda de servicios digitales de reclutamiento
necesidades = ["Eficiente selección de currículums", "Agregación y recopilación de talento", "Simplificar el proceso de almacenamiento de currículums",
               "Eficiente gestión de puestos", "Modelado preciso de puestos", "Análisis preciso de currículums", "Entrevistador virtual de IA"]
# Proporciones correspondientes (%)
proporciones = [35.47, 33.76, 33.55, 33.12, 32.69, 31.84, 29.70]

x = np.arange(len(necesidades))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas, centradas por encima de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(necesidades, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Demanda de servicios digitales de reclutamiento entre empresas chinas en 2025')

plt.tight_layout()
plt.show()