import matplotlib.pyplot as plt
import numpy as np

# Datos
plataformas = ["Aplicaciones para madres e infantes \n(por ejemplo, Mama.cn Pregnancy, Babytree Pregnancy, Mama Community)",
               "Aplicaciones de gestión de salud femenina (por ejemplo, Meiyou)",
               "Plataformas de comunidades de contenido (por ejemplo, Xiaohongshu)",
               "Plataformas sociales (por ejemplo, grupos de WeChat)",
               "Plataformas de vídeos cortos (por ejemplo, Douyin)"]
porcentajes = [61.5, 16.6, 12.0, 5.0, 4.9]

x = np.arange(len(plataformas))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras horizontales
barras = ax.barh(x, porcentajes, color='orange', label='Proporción de contacto (%)')
ax.set_xlabel('Proporción de contacto (%)')
ax.set_ylabel('Tipos de plataformas')
ax.set_yticks(x)
ax.set_yticklabels(plataformas)
ax.invert_yaxis()  # Hacer que la primera plataforma aparezca en la parte superior
ax.set_title('Distribución de las plataformas más frecuentemente accedidas por la población en edad de embarazo en China para productos pre - embarazo en 2023')

# Añadir etiquetas numéricas
for barra in barras:
    longitud = barra.get_width()
    ax.text(longitud + 1, barra.get_y() + barra.get_height() / 2,
            f'{longitud}%', ha='left', va='center')

plt.tight_layout()
plt.show()