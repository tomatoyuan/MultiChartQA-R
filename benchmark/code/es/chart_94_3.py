import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Etiquetas simplificadas (para la leyenda)
etiquetas_cortas = [
    "Proceso lento", "Desajuste de dispositivos", 
    "Comunicación deficiente de requisitos", "Falta de servicio integral", 
    "Insatisfacción con el diseño", "Falta de servicio de instalación y depuración", 
    "Falta de supervisión", "Proveedores no profesionales"
]

# Datos originales
porcentajes = np.array([43.6, 33.1, 27.8, 27.1, 25.6, 19.5, 15.0, 6.8])
indices_cajas_punteadas = [0, 1]

# Ángulos de coordenadas polares
N = len(etiquetas_cortas)
angulos = np.linspace(0, 2 * np.pi, N, endpoint=False)

# Configuración del gradiente de color
norm = mcolors.Normalize(vmin=min(porcentajes), vmax=max(porcentajes))
cmap = cm.get_cmap("YlGnBu")
colores = [cmap(norm(p)) for p in porcentajes]

# Crear figura y subgráfico polar
fig, ax = plt.subplots(figsize=(8, 7), subplot_kw={'projection': 'polar'})

# Dibujar el gráfico de barras radial
barras = ax.bar(
    angulos,
    porcentajes,
    width=2 * np.pi / N * 0.9,
    color=colores,
    edgecolor='white',
    linewidth=1
)

# Resaltar los primeros dos elementos
for i in indices_cajas_punteadas:
    barras[i].set_edgecolor('deepskyblue')
    barras[i].set_linewidth(2.5)
    barras[i].set_alpha(1.0)

# Agregar etiquetas de datos
for angulo, barra, etiqueta, porcentaje in zip(angulos, barras, etiquetas_cortas, porcentajes):
    rotacion = np.rad2deg(angulo)
    alineacion = 'left' if np.pi/2 < angulo < 3*np.pi/2 else 'right'
    ax.text(
        angulo,
        barra.get_height() + 3,
        f"{porcentaje}%",
        ha='center',
        va='center',
        fontsize=9,
        color="#333"
    )

# Configurar la leyenda (cada color + categoría)
for i in range(N):
    ax.bar(0, 0, color=colores[i], label=etiquetas_cortas[i])

# Configurar las propiedades del gráfico radial
ax.set_ylim(0, 50)
ax.set_yticklabels([])
ax.set_xticks([])  # No mostrar las escalas de coordenadas polares
ax.spines['polar'].set_visible(False)

# Agregar leyenda
ax.legend(
    loc='center left',
    bbox_to_anchor=(1.1, 0.5),
    fontsize=10,
    title='Categorías de dificultades',
    frameon=True
)

# Agregar título
ax.set_title(
    "Dificultades encontradas por empresas de catering al abrir nuevas tiendas",
    fontsize=14,
    fontweight="bold",
    pad=30
)

plt.tight_layout()
plt.show()