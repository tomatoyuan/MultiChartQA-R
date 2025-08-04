import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Construir datos
data = {
    'Plataforma': ['Douyin', 'Kuaishou', 'Xiaohongshu', 'Bilibili', 'Weibo', 'Miaopai', 'Pipixia', 'Xigua Video', 'Cuenta de Video de WeChat'],
    'Puntuación 1': [2.1, 2.37, 3.22, 4.56, 2.08, 3.54, 3.03, 4.17, 3.03],
    'Puntuación 2': [5.01, 8.91, 7.07, 6.46, 8.33, 13.27, 14.39, 13.33, 7.74],
    'Puntuación 3': [13.67, 20.77, 11.58, 16.35, 26.39, 23.01, 22.73, 15.83, 19.19],
    'Puntuación 4': [40.09, 35.01, 40.83, 32.71, 29.17, 31.86, 33.33, 36.67, 36.36],
    'Puntuación 5': [38.50, 32.94, 37.30, 39.92, 34.03, 28.32, 26.52, 30.00, 33.68]
}

df = pd.DataFrame(data)
# Establecer la columna 'Plataforma' como índice para la posterior representación gráfica por plataforma
df.set_index('Plataforma', inplace=True)

# Definir colores correspondientes a los de la gráfica
colors = ['#FF5733', '#3498DB', '#2ECC71', '#9B59B6', '#E74C3C']
columns = df.columns

fig, ax = plt.subplots(figsize=(12, 6))  # Ajustar el ancho de la gráfica para adaptarse a la leyenda exterior
bottom = np.zeros(len(df))

for i, col in enumerate(columns):
    ax.bar(df.index, df[col], bottom=bottom, color=colors[i], label=col)
    bottom += df[col]
    # Anotar los valores
    for x, y in zip(df.index, bottom - df[col] / 2):
        ax.text(x, y, f'{df[col][x]}', ha='center', va='center')

ax.set_ylabel('Porcentaje (%)')
ax.set_title('Calificaciones de satisfacción general de los usuarios chinos para plataformas de vídeos cortos en 2025')

# Mover la leyenda a la parte exterior derecha de la gráfica
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()