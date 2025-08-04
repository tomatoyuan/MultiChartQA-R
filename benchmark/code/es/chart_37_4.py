import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# -------------------- Datos del gráfico circular para la proporción de género --------------------
gender_data = {
    "Género": ["Mujer", "Hombre"],
    "Proporción": [61, 39]
}
gender_df = pd.DataFrame(gender_data)

# -------------------- Datos del gráfico de barras para la distribución de edades --------------------
age_data = {
    "Grupo de edad": ["16 - 23 años", "24 - 30 años", "31 - 35 años", "36 - 40 años", "41 - 45 años", "46 - 50 años", "Más de 50 años"],
    "Proporción": [15, 22, 21, 14, 9, 8, 9]
}
age_df = pd.DataFrame(age_data)

# Crear un lienzo con 2 subgráficos (1 fila, 2 columnas)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))  # Aumentar el ancho del lienzo para dejar espacio para las etiquetas inclinadas

# -------------------- Dibujar un gráfico circular para la proporción de género --------------------
axes[0].pie(
    gender_df["Proporción"],
    labels=gender_df["Género"],
    autopct="%1.1f%%",  # Mostrar porcentaje, con 1 decimal
    colors=["#ff99cc", "#66b3ff"],  # Personalizar colores
    startangle=90  # Ángulo de inicio del gráfico circular
)
axes[0].set_title("Proporción de género de los clientes de ropa de\n otoño - invierno en el comercio electrónico de Douyin", fontsize=9, fontweight="bold")

# -------------------- Dibujar un gráfico de barras para la distribución de edades --------------------
bar_plot = sns.barplot(
    data=age_df,
    x="Grupo de edad",
    y="Proporción",
    color="#c9b69f",  # Personalizar el color del gráfico de barras
    ax=axes[1]
)
axes[1].set_title("Distribución de edades de los clientes de ropa de otoño - invierno en el comercio electrónico de Douyin", fontsize=9, fontweight="bold")
axes[1].set_xlabel("Grupo de edad")
axes[1].set_ylabel("Proporción")

# Configurar las etiquetas del eje x del gráfico de barras con inclinación
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=30, ha='right', fontsize=10)

# Agregar etiquetas numéricas al gráfico de barras
for p in bar_plot.patches:
    bar_plot.annotate(
        f'{p.get_height()}%',
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center',
        va='center',
        fontsize=10,
        color='black',
        xytext=(0, 5),
        textcoords='offset points',
    )

# Hacer que el diseño sea más compacto (evitar superposición de etiquetas, etc.)
plt.tight_layout()
# Mostrar el gráfico
plt.show()