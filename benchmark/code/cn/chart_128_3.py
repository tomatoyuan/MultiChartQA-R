import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# 非 VR 游戏/应用数量
non_vr = [3935, 5844, 8028, 7522, 8924, 10827, 11620, 13765]
# VR 游戏/应用数量
vr = [735, 1105, 872, 612, 822, 562, 945, 689]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 7))

# 绘制非 VR 部分（橙色）
ax.bar(x, non_vr, color='orange', label='非VR游戏/应用')
# 绘制 VR 部分（黄色，堆叠在非 VR 上方）
ax.bar(x, vr, bottom=non_vr, color='gold', label='VR游戏/应用')

# 添加非 VR 数量标注
for i, nv in enumerate(non_vr):
    ax.text(i, nv / 2, f'{nv}', ha='center', va='center', color='white')

# 添加 VR 数量标注
for i, v in enumerate(vr):
    ax.text(i, non_vr[i] + v / 2, f'{v}', ha='center', va='center', color='black')

ax.set_ylabel('数量（个）')
ax.set_xlabel('年份')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('2016-2023年Steam平台逐年新增游戏/应用数量')

plt.tight_layout()
plt.show()