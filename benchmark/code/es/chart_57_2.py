import matplotlib.pyplot as plt
import numpy as np

# Nombres de los canales
canales = [
    "SEO", "SEM", "Marketing por correo electrónico", "Anuncios en redes sociales",
    "Marketing de influencers", "Anuncios pagados", "Marketing afiliado"
]

# Convertir la velocidad de efectividad a niveles numéricos (1 = lento, 3 = rápido)
niveles_velocidad = [1, 3, 2, 3, 2, 3, 2]

# Convertir el costo a niveles numéricos (1 = bajo, 3 = alto)
niveles_costo = [1, 3, 1, 2.5, 2, 3, 2.5]

x = np.arange(len(canales))
ancho = 0.35  # Ancho de las barras

fig, ax = plt.subplots(figsize=(12, 6))

barras1 = ax.bar(x - ancho/2, niveles_velocidad, ancho, label='Velocidad de efectividad', color='#4CAF50')
barras2 = ax.bar(x + ancho/2, niveles_costo, ancho, label='Costo', color='#FF9800')

# Agregar etiquetas de texto
for barra in barras1:
    ax.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.05,
            f"{barra.get_height()}", ha='center', fontsize=9)
for barra in barras2:
    ax.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.05,
            f"{barra.get_height()}", ha='center', fontsize=9)

# Configuración de los ejes
ax.set_ylabel('Nivel (1 = Bajo o Lento, 3 = Alto o Rápido)', fontsize=12)
ax.set_title('Comparación de la velocidad de efectividad y el costo de cada canal de marketing', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(canales, rotation=30, ha='right')
ax.legend()

plt.tight_layout()
plt.show()