# Gráfico 4 (Reoptimizado): Agregar etiquetas en chino y valores porcentuales junto a cada sector circular para mejorar la legibilidad

etiquetas = [
    "Madres sofisticadas", "Jóvenes de los pueblos", "Clase media senior", "Jóvenes profesionales urbanos",
    "Adultos mayores de los pueblos", "Gen Z", "Adultos mayores urbanos", "Trabajadores calificados urbanos", "Trabajadores calificados senior"
]
tamaños = [22, 20, 19, 16, 9, 8, 3, 2, 1]
colores = plt.cm.PuRd(np.linspace(0.2, 0.9, len(etiquetas)))

fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=140,
    colors=colores,
    wedgeprops=dict(width=0.4),
    textprops=dict(color="black", fontsize=9)
)

# Mejorar el título
ax.set_title("Distribución de preferencias de población para pantalones de tiburón (en orden descendente de proporción)", fontsize=13)

plt.tight_layout()
plt.show()