import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Platos precocinados\n compuestos/Condimentos para recetas', 'Condimentos básicos', 'Condimentos compuestos no precocinados', 'Condimentos regionales/especialidades']
datos_internos = [38, 35, 27, 0]  # 2023 Q1
datos_externos = [38, 33, 29, 0]  # 2024 Q1

colores = ['#1f4e79', '#2ca197', '#f6a965', '#d1d1e0']

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')

# Círculo interno: 2023 Q1
segmentos_internos, _ = ax.pie(
    datos_internos,
    radius=0.7,
    colors=colores,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Círculo externo: 2024 Q1
segmentos_externos, _ = ax.pie(
    datos_externos,
    radius=1.0,
    colors=colores,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Agregar etiquetas de porcentaje
def agregar_etiquetas(segmentos, datos, radio):
    angulo = 90
    total = sum(datos)
    for i, (segmento, valor) in enumerate(zip(segmentos, datos)):
        if valor == 0:
            continue
        theta = (angulo - valor / total * 360 / 2) * np.pi / 180
        x = radio * np.cos(theta)
        y = radio * np.sin(theta)
        ax.text(x, y, f'{valor}%', ha='center', va='center', fontsize=10)
        angulo -= valor / total * 360

agregar_etiquetas(segmentos_internos, datos_internos, radio=0.55)
agregar_etiquetas(segmentos_externos, datos_externos, radio=1.15)

# Agregar leyenda
plt.legend(segmentos_externos, etiquetas, title="Categorías", loc="center left", bbox_to_anchor=(1, 0.5))

# Agregar título
plt.title('Tendencia de ventas de categorías de condimentos en el primer trimestre de 2024\nCírculo interno: 2023 Q1 | Círculo externo: 2024 Q1')

# Agregar explicación de la fuente de datos
plt.figtext(
    -0.1, 0.1,
    "Fuente de datos: Magic Mirror Insight, 'Tendencia de desarrollo de la industria de condimentos en China en 2024'\n"
    "Explicación de datos: El mercado de condimentos se refiere a los productos de la categoría 'Aceites y\n"
    "condimentos/Comida rápida/Productos secos/Repostería > Condimentos/Mermeladas/Salsas/Alimentos secos' \n"
    "en las plataformas de Tmall Taobao, JD.com y Douyin.",
    ha='left', fontsize=9
)

plt.tight_layout()
plt.show()