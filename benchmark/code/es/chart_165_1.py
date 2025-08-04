import matplotlib.pyplot as plt
import numpy as np

# 数据
etiquetas = ['Tomb-Sweeping Festival 2023', 'Labor Day 2023', 'Dragon Boat Festival 2023', 'Mid-Autumn Festival & National Day 2023', 'New Year\'s Day 2024', 'Tomb-Sweeping Festival 2024']
porcentaje_personas = [68.0, 119.1, 112.8, 104.1, 109.4, 111.5]
porcentaje_ingresos = [39.2, 100.7, 94.9, 101.5, 105.6, 112.7]

x = np.arange(len(etiquetas))
ancho = 0.35

# 颜色设置（蓝绿色系）
colores_personas = '#0072B2'  # 蓝色
colores_ingresos = '#009E73'  # 绿色

fig, ax = plt.subplots(figsize=(10, 6))
barras1 = ax.bar(x - ancho/2, porcentaje_personas, ancho, label='Recuperación de viajeros al nivel del año 2019', color=colores_personas)
barras2 = ax.bar(x + ancho/2, porcentaje_ingresos, ancho, label='Recuperación de ingresos turísticos al nivel del año 2019', color=colores_ingresos)

# 添加文本标签
for barra in barras1:
    altura = barra.get_height()
    ax.annotate(f'{altura:.1f}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

for barra in barras2:
    altura = barra.get_height()
    ax.annotate(f'{altura:.1f}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# 细节设置
ax.set_ylabel('Recuperación al nivel del año 2019 (%)')
ax.set_title('Situación de recuperación de viajes turísticos')
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, rotation=30)
ax.legend()
ax.set_ylim(0, 140)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()