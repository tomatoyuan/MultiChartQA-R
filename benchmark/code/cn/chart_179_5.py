labels_mkt = ['SEO营销', 'SEM营销', '社交营销\n（含账号自运营和广告投放）', '网红营销', '邮件营销', '其它方式']
values_mkt = [23.5, 45.6, 65.0, 47.5, 20.4, 5.3]
values_mkt += values_mkt[:1]
angles = np.linspace(0, 2 * np.pi, len(labels_mkt), endpoint=False).tolist()
angles += angles[:1]

fig2, ax2 = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
ax2.plot(angles, values_mkt, color='darkorange', linewidth=2)
ax2.fill(angles, values_mkt, color='darkorange', alpha=0.6)
ax2.set_thetagrids(np.degrees(angles[:-1]), labels_mkt, fontsize=10)
ax2.set_title("独立站主要营销推广方式选择", fontsize=14, fontweight='bold', pad=20)

for angle, value in zip(angles, values_mkt):
    ax2.text(angle, value + 2, f'{value:.1f}%', color='darkorange',ha='center', va='center', fontsize=10)

plt.figtext(0.5, 0.02, "来源：GoodsFox调研数据，统计时间2023年1月-12月", ha='center', fontsize=10)
plt.tight_layout()
plt.show()