# 图表2：2022年独立站销售额同比增长
labels_2 = ["100%以上", "80%至100%", "50%至80%", "20%至50%", "0%至20%", "负增长"]
values_2 = [2.3, 3.5, 8.0, 14.6, 40.5, 35.1]

fig2, ax2 = plt.subplots(figsize=(8, 5))
bars2 = ax2.bar(labels_2, values_2, color='coral')
ax2.set_title("B2C 独立站运营状况调查\n- 2022年独立站销售额同比增长 -", fontsize=14)
ax2.set_ylabel("占比（%）")
ax2.set_ylim(0, 50)
for bar in bars2:
    height = bar.get_height()
    ax2.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center')

fig2.text(0.5, -0.05, "来源：GoodsFox 调研数据，统计时间2023年1月-12月", ha='center', fontsize=10)
fig2.tight_layout()

plt.show()