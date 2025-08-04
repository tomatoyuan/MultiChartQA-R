import matplotlib.pyplot as plt
import numpy as np

# Canales de información
canales = ["Plataformas de contenido de nuevos medios (por ejemplo, WeChat, cuentas oficiales, etc.)", "Plataformas comerciales electrónicas integrales (por ejemplo, Taobao, JD.com, etc.)", "Plataformas de intercambio de contenido (por ejemplo, Xiaohongshu, Weibo, etc.)", 
            "Plataformas de intercambio de videos (por ejemplo, Bilibili, etc.)", "Plataformas de transmisión en vivo de vídeos cortos", "Tiendas físicas de la marca", "Sitios web oficiales de la marca", "Anuncios en exteriores (anuncios en paredes y edificios, etc.)", 
            "Recomendaciones de familiares y amigos", "Anuncios en el metro o en ascensores"]
# Proporciones correspondientes (%)
proporciones = [36.43, 34.27, 32.36, 30.70, 27.90, 26.75, 25.86, 24.20, 21.40, 20.25]

y = np.arange(len(canales))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Añadir anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(canales)
ax.set_xlabel('Proporción (%)')
ax.set_title('Canales de información para que los consumidores chinos conozcan productos inteligentes en 2025')

plt.tight_layout()
plt.show()