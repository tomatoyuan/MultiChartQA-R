import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Construir datos
datos = {
    "categoria": ["Mujer", "Hombre", "Menos de 19 años", "20 - 29 años", "30 - 39 años", "40 - 49 años", "Más de 50 años"],
    "porcentaje": [33, 67, 11, 26, 29, 23, 11]
}
df = pd.DataFrame(datos)

# Clasificar datos en grupos de género y edad
datos_genero = df.iloc[:2]
datos_edad = df.iloc[2:]

# Crear un lienzo con dos subgráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
fig.patch.set_facecolor('#f8f9fa')  # Establecer el color de fondo del lienzo

# Embelezar el gráfico de barras - Distribución de género
sns.barplot(x="categoria", y="porcentaje", data=datos_genero, palette=["#ff6b6b", "#48dbfb"], ax=ax1)
ax1.set_title("Distribución de género de los seguidores del Campeonato Europeo de Fútbol UEFA", fontsize=15, pad=12)
ax1.set_xlabel("Género", fontsize=12)
ax1.set_ylabel("Porcentaje (%)", fontsize=12)
ax1.set_ylim(0, 100)  # Establecer el rango del eje y
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # Optimizar las líneas de la cuadrícula

# Añadir etiquetas numéricas para la distribución de género
for p in ax1.patches:
    altura = p.get_height()
    ax1.text(p.get_x() + p.get_width() / 2., altura + 1.5,
             f'{altura:.1f}%', ha="center", fontsize=11)

# Embelezar el gráfico circular - Distribución de edad
wedges, texts, autotexts = ax2.pie(
    datos_edad["porcentaje"],
    labels=datos_edad["categoria"],
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("pastel"),
    wedgeprops={'edgecolor': 'w', 'linewidth': 1},
    textprops={'fontsize': 10}
)
ax2.set_title("Distribución de edad de los seguidores\n del Campeonato Europeo de Fútbol UEFA", fontsize=15, pad=12)
ax2.axis('equal')  # Asegurar que el gráfico circular sea un círculo perfecto

# Ajustar el diseño
plt.tight_layout(pad=3)  # Aumentar el espacio entre los subgráficos
plt.suptitle("Estadísticas básicas de datos de la atención al Campeonato Europeo de Fútbol UEFA", fontsize=18, y=1.02, fontweight='bold')

# Mostrar el gráfico
plt.show()