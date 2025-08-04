import matplotlib.pyplot as plt
import numpy as np

# Canales de adquisición de información
canales = ["Plataformas de comunidades de contenido (por ejemplo, Xiaohongshu)", "Plataformas de comercio electrónico (por ejemplo, Taobao, JD.com)",
           "Plataformas de redes sociales (por ejemplo, WeChat)", "Plataformas verticales de maternas e infantiles (por ejemplo, Mama.cn)",
           "Plataformas de vídeos cortos (por ejemplo, Douyin)", "Plataformas de compartición de vídeos (por ejemplo, Bilibili)"]
# Razones para cada elección (orden de la leyenda)
razones = ["Alta profesionalidad (expertos/Preguntas y respuestas)", "Información confiable de maternas e infantiles",
           "Frecuente interacción de usuarios", "Seguir recomendaciones de las personas de alrededor", "Hábito personal",
           "Preferencia por la conveniencia"]
# Colores correspondientes
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', '#1E90FF']
# Datos de proporción para cada razón bajo cada canal (en el orden de canales y razones)
datos = np.array([
    [7.74, 14.26, 15.48, 12.83, 8.15, 4.07],
    [5.91, 17.52, 11.41, 13.65, 7.74, 4.68],
    [8.35, 12.83, 13.65, 9.98, 7.94, 2.24],
    [11.20, 14.87, 14.26, 10.59, 9.16, 3.46],
    [5.30, 11.00, 13.65, 9.57, 9.98, 4.48],
    [6.52, 13.24, 12.63, 12.42, 8.96, 3.87]
])

x = np.arange(len(canales))  # Eje x corresponde a diferentes canales
ancho_barra = 0.8  # Ancho de la barra

fig, ax = plt.subplots(figsize=(14, 8))
base = np.zeros(len(canales))

for i, razon in enumerate(razones):
    # Recorrer cada razón y dibujar un gráfico de barras apiladas
    ax.bar(canales, datos[:, i], width=ancho_barra, bottom=base, color=colores[i], label=razon)
    # Agregar anotaciones numéricas
    for j in range(len(canales)):
        ax.text(j, base[j] + datos[j, i] / 2, f'{datos[j, i]:.2f}', ha='center', va='center', fontsize=8)
    base += datos[:, i]

ax.set_ylabel('Proporción (%)')
ax.set_title('Razones por las cuales los consumidores chinos de maternas e infantiles eligen canales de adquisición de información en 2025')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Colocar la leyenda a la derecha
plt.xticks(x, canales, rotation=15, ha='right')
plt.tight_layout()
plt.show()