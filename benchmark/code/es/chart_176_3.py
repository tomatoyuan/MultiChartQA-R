import matplotlib.pyplot as plt

# Datos del gráfico circular y el gráfico de barras
etiquetas = ['18-24', '25-29', '30-34', '35-39', '40+']
tamaños_uv = [25, 25, 15, 20, 15]  # Proporción de edad
tamaños_crecimiento = [30, 15, 45, 60, 50]  # Tasa de crecimiento interanual (%)

# Crear la figura y los subgráficos
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico circular izquierdo: Proporción de edad
wedges, textos, autotextos = axs[0].pie(
    tamaños_uv,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=90
)
axs[0].axis('equal')
axs[0].set_title('Proporción de edad de usuarios que regalan')

# Configurar el estilo del texto dentro del gráfico circular
for texto in autotextos:
    texto.set_fontsize(10)

# Gráfico de barras derecho: Tasa de crecimiento interanual
barras = axs[1].bar(etiquetas, tamaños_crecimiento, color='lightcoral')
axs[1].set_title('Tasa de crecimiento interanual de usuarios que regalan')
axs[1].set_ylabel('Tasa de crecimiento interanual (%)')

# Agregar etiquetas de valor encima de las barras
for barra, crecimiento in zip(barras, tamaños_crecimiento):
    altura = barra.get_height()
    axs[1].text(
        barra.get_x() + barra.get_width() / 2,
        altura + 2,
        f"{crecimiento}%",
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.tight_layout()
plt.show()