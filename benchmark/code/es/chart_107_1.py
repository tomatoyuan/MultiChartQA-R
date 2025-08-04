import matplotlib.pyplot as plt
import numpy as np

# Nombres de las operadoras
operadoras = ["China Mobile", "China Unicom", "China Telecom", "China Broadcasting Network"]
# Proporciones correspondientes (%)
proporciones = [59.10, 38.65, 35.33, 16.27]

x = np.arange(len(operadoras))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(8, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(operadoras)
ax.set_ylabel('Proporción (%)')
ax.set_title('Operadoras de comunicaciones más utilizadas por los usuarios chinos en 2025')

plt.tight_layout()
plt.show()