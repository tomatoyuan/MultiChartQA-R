import matplotlib.pyplot as plt
import numpy as np

# Canales
canales = ['Redes sociales', 'Influencers', 'Aplicaciones de mensajería', 'Vídeo en directo', 'Vídeo/chat en tiempo real', 'Asistentes de voz', 'Chat']
# Datos de la etapa de descubrimiento
descubrimiento = [50, 22, 14, 11, 8, 0, 0]
# Datos de la etapa de compra
compra = [59, 0, 36, 21, 20, 24, 20]

# Posiciones en el eje x
x = np.arange(len(canales))
ancho_barra = 0.35

# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(10, 5))
barras1 = ax.bar(x - ancho_barra/2, descubrimiento, width=ancho_barra, label='Descubrimiento', color='#009800')
barras2 = ax.bar(x + ancho_barra/2, compra, width=ancho_barra, label='Compra', color='#005B4C')

# Agregar etiquetas de valores
for barra in barras1:
    altura = barra.get_height()
    if altura > 0:
        ax.text(barra.get_x() + barra.get_width()/2, altura + 1, f'{int(altura)}%', ha='center', va='bottom', fontsize=10)

for barra in barras2:
    altura = barra.get_height()
    if altura > 0:
        ax.text(barra.get_x() + barra.get_width()/2, altura + 1, f'{int(altura)}%', ha='center', va='bottom', fontsize=10)

# Otras configuraciones
ax.set_xticks(x)
ax.set_xticklabels(canales, rotation=20)
ax.set_ylabel('Proporción (%)')
ax.set_title('Compradores globales que utilizan canales específicos para descubrir y comprar productos')
ax.legend()
plt.tight_layout()
plt.show()