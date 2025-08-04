# 图表3：不良反应的应对措施（高亮特定扇区的环形图）
# Gráfico 3: Medidas de respuesta a reacciones adversas (diagrama circular anular con sector específico resaltado)

# 数据
# Datos
labels = [
    'Descansar y beber más agua', 'Mejorar la dieta', 'Tomar medicamentos por cuenta propia',
    'Tomar probióticos para regularizar', 'No tomar medidas', 'Acudir inmediatamente a un hospital oficial', 'Pedir consejo a familiares y amigos'
]
sizes = [18.5, 17.4, 20.3, 15.0, 2.9, 12.4, 13.5]
highlight_index = 3  # 高亮“服用益生菌调理”
# Resaltar "Tomar probióticos para regularizar"

# 定义颜色和突出项
# Definir colores y elementos resaltados
colors = ['#555', '#666', '#777', '#0056d6', '#999', '#bbb', '#99c']
explode = [0.01 if i == highlight_index else 0 for i in range(len(labels))]

# 绘图
# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    sizes, labels=None, autopct='%1.1f%%', startangle=90,
    counterclock=False, colors=colors,
    explode=explode, wedgeprops=dict(width=0.3, edgecolor='white'),
    textprops={'fontsize': 10}
)

# 设置图例
# Configurar la leyenda
ax.legend(wedges, labels, title="Formas de respuesta", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10)

# 中心文本
# Texto en el centro
ax.text(0, 0, 'Medidas de respuesta ante\nreacciones adversas', ha='center', va='center', fontsize=12, fontweight='bold')

# 标题
# Título
ax.set_title("Medidas de respuesta ante reacciones adversas (porcentaje de usuarios)", fontsize=14)
plt.tight_layout()
plt.show()