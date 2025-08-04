import matplotlib.pyplot as plt
import numpy as np

# AI数字人功能需求
functions = [
    "情感识别", "多轮对话", "代码能力", "跨语言交流（翻译等能力）", "文本改写", 
    "逻辑与推理", "身体动作识别", "文本分类", "自主学习与进化", "生成与创作", 
    "人脸识别", "人机互动", "自然语言理解", "多模态能力（文字、图片、语音、视频处理能力）"
]
# 对应占比（%）
proportions = [17.69, 17.95, 18.88, 19.02, 19.41, 
               19.68, 20.61, 21.41, 21.54, 22.34, 
               22.34, 24.87, 25.66, 32.98]

y = np.arange(len(functions))  # y轴坐标

fig, ax = plt.subplots(figsize=(12, 8))
# 绘制水平柱状图
bars = ax.barh(y, proportions, color='orange')

# 添加数值标注，在条形右侧
for i, proportion in enumerate(proportions):
    ax.text(proportion, i, f'{proportion}', va='center', ha='left', fontsize=9)

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(functions)
ax.set_xlabel('占比（%）')
ax.set_title('2025年中国企业对AI数字人的功能需求')

plt.tight_layout()
plt.show()