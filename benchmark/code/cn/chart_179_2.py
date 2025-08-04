import matplotlib.pyplot as plt

# 图表1：独立站运营时间调查
labels_1 = ["少于1年", "1年~3年", "3年~5年", "5年~10年", "10年以上"]
values_1 = [26.6, 45.3, 22.3, 4.2, 1.6]

fig1, ax1 = plt.subplots(figsize=(8, 5))
bars1 = ax1.bar(labels_1, values_1, color='coral')
ax1.set_title("B2C 独立站运营状况调查\n- 独立站运营时间调查 -", fontsize=14)
ax1.set_ylabel("占比（%）")
ax1.set_ylim(0, 50)
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center')

fig1.text(0.5, -0.05, "来源：GoodsFox 调研数据，统计时间2023年1月-12月", ha='center', fontsize=10)
fig1.tight_layout()


plt.show()