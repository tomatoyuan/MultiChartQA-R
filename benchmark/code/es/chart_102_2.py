import matplotlib.pyplot as plt
import numpy as np

# Nombres de las plataformas de videos cortos
plataformas = ["Douyin", "Kuaishou", "Xiaohongshu", "Cuenta de Video de WeChat", "Bilibili", "Video Xigua", "Weibo", "Pipixia", "Miaopai"]
# Porcentajes de uso de usuarios (%) de cada plataforma
porcentajes = [46.80, 35.93, 33.16, 31.66, 28.04, 25.59, 15.35, 14.07, 12.05]

x = np.arange(len(plataformas))  # Se utiliza para establecer la posición del eje x del gráfico de barras

fig, ax = plt.subplots()
barras = ax.bar(x, porcentajes, color='orange')

# Etiquetar el valor en cada barra
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2., altura,
            f'{altura}',
            ha='center', va='bottom')

# Establecer las etiquetas de las marcas del eje x como nombres de plataformas con espaciado uniforme
plt.xticks(x, plataformas, rotation=45, ha='right')  # Usar plt.xticks para asegurar la distribución uniforme
# Establecer el título del gráfico y las etiquetas de los ejes
ax.set_title('Plataformas de videos cortos utilizadas por usuarios chinos en 2025')
ax.set_ylabel('Porcentaje (%)')

plt.tight_layout()  # Asegurar un diseño compacto y evitar que las etiquetas se recorten
plt.show()