# Gráfico 2: Crecimiento año sobre año de las ventas de las tiendas independientes en 2022
labels_2 = ["Más del 100%", "Entre el 80% y el 100%", "Entre el 50% y el 80%", "Entre el 20% y el 50%", "Entre el 0% y el 20%", "Crecimiento negativo"]
values_2 = [2.3, 3.5, 8.0, 14.6, 40.5, 35.1]

fig2, ax2 = plt.subplots(figsize=(8, 5))
bars2 = ax2.bar(labels_2, values_2, color='coral')
ax2.set_title("Encuesta sobre el estado de operación de las tiendas independientes B2C\n- Crecimiento año sobre año de las ventas de las tiendas independientes en 2022 -", fontsize=14)
ax2.set_ylabel("Porcentaje (%)")
ax2.set_ylim(0, 50)
for bar in bars2:
    height = bar.get_height()
    ax2.annotate(f'{height:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center')

fig2.text(0.5, -0.15, "Fuente: Datos de la encuesta de GoodsFox, período de estadísticas de enero a diciembre de 2023", ha='center', fontsize=10)
fig2.tight_layout()
plt.xticks(rotation=30)

plt.show()