import matplotlib.pyplot as plt

# 数据
etiquetas = ['Todos los días', '4 - 6 días a la semana', '1 - 3 días a la semana', 'Menos de 1 día a la semana', 'Sin patrón regular']
tamaños = [18, 36, 39, 6, 2]
colores = ['#ff6384', '#ff8fa3', '#ff2d55', '#ffb6c1', '#ffe5eb']  # Serie de tonos rojos para distinguir diferentes frecuencias

# 构建标签内容
etiquetas_con_porcentaje = [f'{etiqueta}\n {tamaño}%' for etiqueta, tamaño in zip(etiquetas, tamaños)]

# 创建图表
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos = ax.pie(tamaños,
                           labels=etiquetas_con_porcentaje,
                           colors=colores,
                           startangle=90,
                           labeldistance=1.1,
                           textprops={'fontsize': 10},
                           wedgeprops=dict(width=0.6))

# 添加标题
plt.title('Distribución de la frecuencia de visualización de miniseries cortas', fontsize=14, fontweight='bold', pad=20)

# 确保图为圆形
ax.axis('equal')

# 添加数据来源说明
fig.text(0.01, 0.01,
         'Fuente de datos: Encuesta cuantitativa en línea de usuarios de miniseries cortas de Millward Brown, enero de 2024, N = 1,000\n'
         'B1. ¿Con qué frecuencia suele ver miniseries cortas? [Respuesta única]\n',
         fontsize=9, ha='left')

plt.tight_layout(rect=[0, 0.1, 1, 1])
plt.show()