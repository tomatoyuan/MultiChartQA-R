import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Establece el estilo y la paleta de colores
plt.style.use("ggplot")
sns.set_palette("Set2")

# Datos
categorias = ["Ingresos del proveedor de PaaS", "Costo de recursos", "Costo de I+D", "Beneficio bruto"]
datos = [100, 33, 37, 30]
colores = sns.color_palette("flare", len(datos))  # Esquema de colores de gradiente brillante

# Gráfico polar (una variante del gráfico de radar) - solo una dimensión, también se puede simular con un gráfico circular
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

# Ángulos polares
angulos = np.linspace(0, 2 * np.pi, len(datos), endpoint=False).tolist()
# Cierra la forma
datos += datos[:1]
angulos += angulos[:1]

# Graficando
ax.fill(angulos, datos, color=colores[0], alpha=0.25)
ax.plot(angulos, datos, color=colores[0], linewidth=2, linestyle="-", marker='o')

# Agrega etiquetas de datos
for angulo, valor, etiqueta in zip(angulos[:-1], datos[:-1], categorias):
    ax.text(
        angulo,
        valor - 5,  # Desplaza hacia afuera un poco para evitar superposición con el gráfico, ajustable
        f"{valor}%",
        ha='center',
        va='top',
        fontsize=10,
        color='black',
        fontweight='bold'
    )

# Establece etiquetas de categorías
categorias += categorias[:1]
ax.set_xticks(angulos)
ax.set_xticklabels(categorias, fontsize=11)

# Establece el título
plt.title("Distribución de rentabilidad del proveedor de RTC PaaS (Vista polar)", fontsize=14, fontweight="bold", pad=20)

# Configura el rango del eje
ax.set_rlabel_position(30)
ax.set_yticks([25, 50, 75, 100])
ax.set_yticklabels(["25%", "50%", "75%", "100%"], fontsize=10)
ax.grid(color="gray", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()