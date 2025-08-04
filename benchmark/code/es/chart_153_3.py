# 图表 1.2-10：毛孔粗大带来的其他皮肤问题

labels = [
    "Piel grasa", "Muchos granos negros \ny puntos cerrados", "Tez opaca",
    "Rugosidad", "Granos", "Enrojecimiento"
]
values = [77.33, 74.33, 61.33, 55.33, 45.00, 34.33]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(labels[::-1], values[::-1], color=['#245b5b'] * 3 + ['#b4d4d4'] * 3)

# Agregar etiquetas de porcentaje
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{width:.2f}%', va='center', fontsize=10)

ax.set_xlabel('Proporción (%)')
ax.set_title("Figura 1.2-10 Otros problemas de la piel causados por poros dilatados")
fig.text(0.9, 0.02, "N = 300", ha='right', fontsize=10)
plt.xlim(0, 90)
plt.tight_layout()
plt.show()