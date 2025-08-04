import matplotlib.pyplot as plt
import numpy as np

# Nombres de las plataformas
plataformas = ["Tienda en línea de Douyin", "Taobao", "Pinduoduo", "Tienda en línea de Kuaishou", "JD.com", "Xiaohongshu", 
               "Compra grupal en la comunidad", "MissFresh", "Tmall", "Vip.com", "Suning.com", "Cuenta de video de WeChat"]
# Proporciones correspondientes (%)
proporciones = [29.79, 25.00, 24.73, 24.20, 24.20, 23.14, 23.14, 23.14, 23.14, 20.74, 20.74, 19.95]

x = np.arange(len(plataformas))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 7))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(plataformas, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Plataformas comúnmente utilizadas por los operadores de comercio electrónico rural en China en 2025 para vender productos')

plt.tight_layout()
plt.show()