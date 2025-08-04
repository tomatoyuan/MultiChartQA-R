import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Imágenes', 'Vídeos', 'Carrusel', 'Reels']
conteos = [17, 11, 36, 644]
colores = ['#3C9B8E', '#7E55C2', '#F3B63A', '#DA3B9C']

# Calcular porcentajes y etiquetas de leyenda
total = sum(conteos)
porcentajes = [c / total for c in conteos]
etiquetas_leyenda = [f"{etq} {c} ({p:.1%})" for etq, c, p in zip(etiquetas, conteos, porcentajes)]

# Crear figura
fig, ax = plt.subplots(figsize=(10, 6))

# Gráfico circular tipo donut
segmentos, _ = ax.pie(
    conteos,
    colors=colores,
    startangle=90,
    wedgeprops=dict(width=1)
)

# Anotaciones externas con líneas
for i, segmento in enumerate(segmentos):
    angulo = (segmento.theta2 + segmento.theta1) / 2
    angulo_rad = np.deg2rad(angulo)
    x = np.cos(angulo_rad)
    y = np.sin(angulo_rad)

    # Posición del texto externo
    x_text = 1.2 * x
    y_text = 1.5 * y
    alineacion = 'left' if x >= 0 else 'right'

    ax.annotate(
        f"{conteos[i]} ({porcentajes[i]:.1%})",
        xy=(0.5 * x, 0.7 * y),       # Punto de flecha
        xytext=(x_text, y_text),     # Texto
        ha=alineacion, va='center',
        fontsize=10, color='black',
        rotation=-30,
        arrowprops=dict(arrowstyle='-', color='gray', lw=1)
    )

# Leyenda a la derecha
ax.legend(
    segmentos,
    etiquetas_leyenda,
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    fontsize=12
)

# Texto descriptivo
descripcion = (
    "A través de los datos del backend de OneSight Marketing Cloud,\n"
    "descubrimos que en el perfil global de Instagram de Insta360,\n"
    "en las publicaciones de 2023, los Reels representan\n"
    "más del 90%."
)
plt.text(-1.8, 0.2, descripcion, fontsize=13, va='top')

# Formato final
ax.set_aspect('equal')
plt.tight_layout()
plt.show()