import matplotlib.pyplot as plt
import numpy as np

# Nombres de las empresas
empresas = ["Samsung", "Tencent", "Baidu", "Sony", "OPPO", "Ping An Group", "SenseTime", "Canon", "Huawei", "Microsoft"]
# Número de patentes (unidades)
conteo_patentes = [4094, 4085, 3094, 2637, 2301, 2260, 2194, 2163, 2126, 2108]

x = np.arange(len(empresas))

fig, ax = plt.subplots(figsize=(12, 7))
# Dibujar un gráfico de barras
barras = ax.bar(x, conteo_patentes, color='orange', label='Número de patentes (unidades)')

# Agregar etiquetas numéricas sobre las barras
for i, conteo in enumerate(conteo_patentes):
    ax.text(i, conteo + 50, f'{conteo}', ha='center', va='bottom')

ax.set_ylabel('Número de patentes (unidades)')
ax.set_xlabel('Nombres de las empresas')
ax.set_xticks(x)
ax.set_xticklabels(empresas, rotation=45)  # Rotar las etiquetas del eje x para evitar superposiciones
ax.legend()
ax.set_title('Conteo de patentes de invención de VR/AR globales (10 empresas principales)')

plt.tight_layout()
plt.show()