import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['One - time success rate', 'Two - time success rate', 'Success rate after three or more attempts']
values = [8, 27, 65]

# Create a figure
fig, ax = plt.subplots(figsize=(10, 6))  # 调整图表宽度

# Draw a bar chart
ax.bar(labels, values, color=['lightblue', 'lightgreen', 'lightcoral'])

# 设置x轴标签旋转45度
plt.xticks(rotation=30, ha='right', fontsize=10)  # 倾斜30度并右对齐

# Add numerical labels
for i, v in enumerate(values):
    ax.text(i, v + 1, f'{v}%', ha='center')

# Set the title and axis labels (adjust as needed)
ax.set_ylabel('Percentage')
# Add a title
ax.set_title('Distribution of 12306 verification code entry success rates during the Spring Festival travel rush in 2016')

# Display the figure
plt.tight_layout()  # 调整布局
plt.show()