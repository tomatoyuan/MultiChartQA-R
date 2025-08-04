import matplotlib.pyplot as plt
import numpy as np

# Campos de aplicación de 5G
campos = ["Terminales Inteligentes 5G", "Medios de Comunicación 5G", "Conducción Autónoma", "Hogar Inteligente", "Telemedicina", "Educación", "Realidad Virtual"]
# Proporciones correspondientes (%)
proporciones = [44.00, 37.71, 37.71, 37.49, 36.80, 31.31, 27.09]

x = np.arange(len(campos))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(8, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(campos, rotation=30)
ax.set_ylabel('Proporción (%)')
ax.set_title('Campos de Aplicaciones 5G Esperados por los Usuarios Chinos en 2025')

plt.tight_layout()
plt.show()