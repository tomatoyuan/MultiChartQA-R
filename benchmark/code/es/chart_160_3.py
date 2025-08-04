import matplotlib.pyplot as plt

# 数据
# Categorías
categorias = ["Registros de vida", "Apariencia física", "Gastronomía", "Humor y diversión", "Juegos", "Música", "Cine y televisión", "Maquillaje", "Moda", "Emociones"]
# Valores
valores = [100, 90, 70, 80, 80, 70, 65, 60, 60, 50]  # Valores de ejemplo

# Índices a resaltar
indices_resaltados = [0, 7, 8]  # Resaltar "Registros de vida", "Maquillaje", "Moda"

# Graficar
fig, ax = plt.subplots(figsize=(10, 4))
# Crear barras
barras = ax.bar(categorias, valores, color="#4da6ff")

# Marcar las categorías importantes con un marco discontinuo
for idx in indices_resaltados:
    barra = barras[idx]
    altura = barra.get_height()
    ax.add_patch(plt.Rectangle(
        (barra.get_x() - 0.1, 0), barra.get_width() + 0.2, altura + 5,
        fill=False, edgecolor="#b084e9", linewidth=2, linestyle='--'
    ))

# Agregar etiquetas de valor
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, altura + 2, f"{altura}",
            ha='center', va='bottom', fontsize=10)

# Mejorar la apariencia del gráfico
ax.set_title("Distribución de la proporción de las 10 categorías de contenido de los influencers de nivel intermedio de TikTok", fontsize=12)
ax.set_ylabel("Cantidad (indicativa)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()