# 图表 1.1-3：比例 de soluciones para la mejora de los poros dilatados (comparación de dos gráficos circulares)

etiquetas = ["Cuidado de la piel", "Métodos", "Estilo de vida", "Medicina estética", "Suplementos orales"]
tamaños_2023 = [69.36, 17.76, 7.52, 4.70, 0.66]
tamaños_2024 = [71.33, 12.58, 6.45, 9.07, 0.57]
colores = ['#224b4a', '#628a89', '#a9c0bf', '#cededc', '#e7f0ef']

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico circular 1 - 2022/08-2023/07
cuñas1, textos1, autotextos1 = axs[0].pie(
    tamaños_2023, labels=etiquetas, autopct='%1.2f%%', startangle=140, colors=colores,
    textprops={'fontsize': 9}
)
axs[0].set_title("2022/08–2023/07")

# Gráfico circular 2 - 2023/08-2024/07
cuñas2, textos2, autotextos2 = axs[1].pie(
    tamaños_2024, labels=etiquetas, autopct='%1.2f%%', startangle=140, colors=colores,
    textprops={'fontsize': 9}
)
axs[1].set_title("2023/08–2024/07")

fig.suptitle("Figura 1.1-3 Proporción de soluciones para la \n"
             "mejora de los poros dilatados (Fuente de datos: Feigua)", fontsize=13)
plt.tight_layout()
plt.show()