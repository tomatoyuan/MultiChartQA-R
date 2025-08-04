import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Datos de la distribución de género
etiquetas_genero = ["Hombre", "Mujer"]
tamaños_genero = [32.2, 67.8]
colores_genero = ["#6495ED", "#FFA07A"]

# Datos de la distribución de edad
categorias_edad = ["15 - 25 años", "26 - 29 años", "31 - 40 años", "41 - 50 años", "51 - 55 años", "56 - 60 años", "Otros"]
proporciones_edad = [13.8, 34.1, 31.5, 13.1, 5.4, 1.7, 0.4]
colores_edad = ["#FFD700", "#FF7F50", "#FF7F50", "#FFD700", "#FFD700", "#FFD700", "#D3D3D3"]

# Datos del estado civil
etiquetas_estado_civil = ["Soltero", "Casado sin hijos", "Casado con hijos"]
tamaños_estado_civil = [18.1, 14.4, 67.5]
colores_estado_civil = ["#FFD700", "#32CD32", "#FF7F50"]

# Crear un lienzo con 3 subgráficos
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# Izquierda: Distribución de género
x_hombre, y_hombre = 0.2, 0.5
ancho_hombre, alto_hombre = 0.2, 0.4
ax1.add_patch(plt.Rectangle((x_hombre, y_hombre - alto_hombre / 2), ancho_hombre, alto_hombre, color=colores_genero[0]))
ax1.add_patch(plt.Circle((x_hombre + ancho_hombre / 2, y_hombre + 0.1), 0.05, color=colores_genero[0]))
ax1.text(x_hombre + ancho_hombre / 2, y_hombre - 0.3, f'{etiquetas_genero[0]}, {tamaños_genero[0]}%', ha='center', va='top')

x_mujer, y_mujer = 0.6, 0.5
ancho_mujer, alto_mujer = 0.2, 0.4
ax1.add_patch(plt.Rectangle((x_mujer, y_mujer - alto_mujer / 2), ancho_mujer, alto_mujer, color=colores_genero[1]))
ax1.add_patch(plt.Circle((x_mujer + ancho_mujer / 2, y_mujer + 0.1), 0.05, color=colores_genero[1]))
ax1.text(x_mujer + ancho_mujer / 2, y_mujer - 0.3, f'{etiquetas_genero[1]}, {tamaños_genero[1]}%', ha='center', va='top')

ax1.axis('off')
ax1.set_title('Distribución de género de los consumidores chinos en 2024')

# Centro: Gráfico de barras de la distribución de edad（横坐标倾斜）
ax2.bar(categorias_edad, proporciones_edad, color=colores_edad)
ax2.set_ylabel('Proporción (%)')
ax2.set_title('Distribución de edad de los consumidores chinos en 2024')
# 添加数值标注
for i, prop in enumerate(proporciones_edad):
    ax2.text(i, prop + 1, f'{prop}%', ha='center', va='bottom', fontsize=9)
# 正确设置横坐标标签（修复警告）
ax2.set_xticks(range(len(categorias_edad)))  # 设置刻度位置
ax2.set_xticklabels(categorias_edad, rotation=45, ha='right', fontsize=9)  # 设置刻度标签

# Derecha: Gráfico circular del estado civil（修复解包错误）
wedges, texts, autotexts = ax3.pie(tamaños_estado_civil, colors=colores_estado_civil, startangle=90, autopct='%1.1f%%')
ax3.legend(wedges, etiquetas_estado_civil, loc='lower left', fontsize=9)
for text in autotexts:
    text.set_color('white')
ax3.set_title('Estado civil de los consumidores chinos en 2024')

plt.tight_layout()
plt.show()