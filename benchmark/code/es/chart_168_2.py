import matplotlib.pyplot as plt

# 数据
etiquetas = ['Muy informado', 'Bastante informado', 'Información media', 'Sin información']
tamaños = [35, 50, 10, 5]
colores = ['#955c23', '#d8b77f', '#f3e7d3', '#f5f3ef']

# 绘图
fig, ax = plt.subplots(figsize=(10, 10))
sectores, textos = ax.pie(
    tamaños, labels=etiquetas, startangle=90, counterclock=False,
    wedgeprops=dict(width=0.4, edgecolor='w'), colors=colores
)

# 添加标题
plt.title('Conocimiento de los consumidores sobre la pasta de madera virgen', fontsize=14)

# 添加文字说明
plt.text(-1.9, -1.0, '50%', fontsize=24, color='#d8b77f', weight='bold')
plt.text(-2.1, -1.3, 'de los consumidores están bastante informados sobre \n'
                     'el concepto de pasta de madera virgen,  saben sus \n'
                     'características y tienen la intención de comprarla', color='#d8b77f',  fontsize=12)

plt.text(1.1, -0.2, '35%', fontsize=24, color='#955c23', weight='bold')
plt.text(1.0, -0.9, 'de los consumidores conocen muy \n'
                    'bien el concepto de pasta de madera virgen, \n'
                    ' y dicen que priorizarán los pañuelos de \n'
                    'este tipo de materia prima al hacer una compra',  color='#955c23', fontsize=12)

# 添加数据来源
plt.text(-2.2, -1.8,
         'Fuente de datos: Encuesta de tendencias del papel higiénico para el \n'
         'hogar de los consumidores chinos realizada por CBNData en marzo de 2024\n'
         'Explicación de los datos: ¿Cuál de las siguientes opciones se acerca más a su conocimiento \n'
         'sobre la pasta de madera virgen (pasta de madera hecha de madera natural'
         'sin adición de otras fibras)? N = 1000',
         fontsize=8, color='gray')

plt.tight_layout()
plt.show()