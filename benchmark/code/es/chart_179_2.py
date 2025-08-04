import matplotlib.pyplot as plt

# 图表1：调查独立站运营时间
# Gráfico 1: Encuesta sobre el tiempo de operación de las tiendas independientes
labels_1 = ["Menos de 1 año", "De 1 a 3 años", "De 3 a 5 años", "De 5 a 10 años", "Más de 10 años"]
values_1 = [26.6, 45.3, 22.3, 4.2, 1.6]

fig1, ax1 = plt.subplots(figsize=(8, 5))
bars1 = ax1.bar(labels_1, values_1, color='coral')
ax1.set_title("Encuesta sobre el estado de operación de las tiendas independientes B2C\n- Encuesta sobre el tiempo de operación de las tiendas independientes -", fontsize=14)
ax1.set_ylabel("Porcentaje (%)")
ax1.set_ylim(0, 50)
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center')

fig1.text(0.5, -0.05, "Fuente: Datos de la encuesta de GoodsFox, período de estadísticas de enero a diciembre de 2023", ha='center', fontsize=10)
fig1.tight_layout()

plt.show()