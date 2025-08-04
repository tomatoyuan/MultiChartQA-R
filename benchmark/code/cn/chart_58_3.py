import matplotlib.pyplot as plt
import numpy as np

# 数据
weeks = ["4月第1周", "4月第2周", "4月第3周", "4月第4周", "4月第5周"]
data_2024 = [3500.2, 3726.2, 3616.5, 3628.3, 3598.8]  # 模拟数据，可替换为实际值
data_2025 = [4039.3, 4230.8, 4409.0, 4232.3, 3966.2]  # 模拟数据，可替换为实际值

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制折线
ax.plot(weeks, data_2025, color="#a5d65d", marker="o", label="2025年", linewidth=2)
ax.plot(weeks, data_2024, color="#4bb7e6", marker="o", label="2024年", linewidth=2)

# 添加数据标注
for x, y in zip(weeks, data_2025):
    ax.text(x, y + 20, f'{y}', ha='center', va='bottom', fontsize=9)
for x, y in zip(weeks, data_2024):
    ax.text(x, y + 20, f'{y}', ha='center', va='bottom', fontsize=9)

# 美化设置
ax.set_title("UserTracker-2024&2025年清明节至五一节期间，文艺演出APP趋势对比\n单位：周活跃用户设备数（万台）", fontsize=12, fontweight='bold')
ax.legend()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()