import matplotlib.pyplot as plt
import numpy as np

# Datos
efectos = ["Hidratante", "Antioxidante", "Calmativo", "Despigmentante", "Iluminador", "Aislante"]
porcentajes = [57.8, 52.3, 47.1, 38.1, 31.2, 31.2]

x = np.arange(len(efectos))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, porcentajes, color='orange')

# Agregar anotaciones numéricas
for i, porcentaje in enumerate(porcentajes):
    ax.text(i, porcentaje + 1, f'{porcentaje}%', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Porcentaje (%)')
ax.set_xlabel('Tipo de Eficacia')
ax.set_xticks(x)
ax.set_xticklabels(efectos)
ax.set_title('Eficacia Preferida de Cosméticos Antisolares entre Consumidores Chinos')

plt.tight_layout()
plt.show()