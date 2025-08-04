import matplotlib.pyplot as plt

# 数据
paises = ["Estados Unidos", "Japón", "Europa"]
porcentajes = [48, 45, 7]
colores = ["pink", "lightgreen", "lightblue"]

# 创建饼图
plt.pie(
    porcentajes,
    labels=paises,
    colors=colores,
    autopct="%1.1f%%",  # 显示百分比
    startangle=90,  # 起始角度
    textprops={"fontsize": 12}
)

# 添加标题
plt.title("¿Dónde ir a tratarse fuera del país?", fontsize=16, fontweight="bold")

# 调整布局（避免标签挤压）
plt.tight_layout()

# 显示图表
plt.show()