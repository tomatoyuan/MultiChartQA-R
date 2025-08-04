import matplotlib.pyplot as plt
import numpy as np

# Comprendiendo los canales
canales = ["Periódicos/libros", "Informado por familiares/amigos", "Medios de comunicación al aire libre (publicidad en el metro, televisión en autobuses, anuncios en aeropuertos, etc.)",
            "Exposiciones/conferencias tecnológicas (exposiciones de telecomunicaciones, foros tecnológicos, etc.)",
            "Plataformas de compartición de contenido (Xiaohongshu, Weibo, etc.)",
            "Informes/análisis de investigación de la industria (informes de investigación y análisis de mercado de empresas tecnológicas, etc.)",
            "Plataformas de vídeos cortos (Douyin, Kuaishou, etc.)",
            "Programas de televisión/radio (noticias, canales tecnológicos, etc.)",
            "Notificaciones push de aplicaciones móviles (tiendas de aplicaciones, aplicaciones de noticias, etc.)",
            "Plataformas de redes sociales (WeChat, QQ, etc.)",
            "Actividades de promoción de operadores de telecomunicaciones (sucursales, actividades de promoción online y offline, etc.)"]
# Proporciones correspondientes (%)
proporciones = [12.67, 18.39, 23.13, 23.24, 23.79, 26.32, 27.64, 27.75, 28.52, 29.07, 34.69]

y = np.arange(len(canales))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(12, 8))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Añadir etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(canales)
ax.set_xlabel('Proporción (%)')
ax.set_title('Canales para que los usuarios chinos conozcan la 5G en 2025')

plt.tight_layout()
plt.show()