import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.font_manager as fm

# Datos
fechas = ["19 de julio", "20 de julio"]
busquedas = [234381, 534381]
incremento = 41  # Tasa de crecimiento

# Crear un gradiente de color personalizado
colores = [(0.9, 0.95, 1), (0.1, 0.3, 0.6)]  # De azul claro a azul oscuro
cmap_personalizado = LinearSegmentedColormap.from_list("azul_personalizado", colores, N = 100)

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 8), facecolor="#f8fafc")
ax.set_facecolor("#f8fafc")

# Dibujar la cuadrícula de fondo
for y in np.linspace(0, max(busquedas), 6):
    ax.axhline(y, color='lightblue', alpha=0.15, linewidth=1)

# Dibujar un gráfico de barras (con efecto tridimensional)
pos_x = np.arange(len(fechas))
ancho_barra = 0.6

for i, (fecha, busqueda) in enumerate(zip(fechas, busquedas)):
    # Gráfico de barras principal (relleno de gradiente)
    rect = Rectangle((i - ancho_barra/2, 0), ancho_barra, busqueda, 
                    facecolor='none', edgecolor='none')
    ax.add_patch(rect)
    
    img = np.ones((100, 1)) * np.linspace(0.3, 1, 100).reshape(-1, 1)
    ax.imshow(img, aspect='auto', extent=[i - ancho_barra/2, i + ancho_barra/2, 0, busqueda],
              cmap=cmap_personalizado, alpha=0.9, clip_path=rect)
    
    # Resaltado superior
    resaltado_superior = Rectangle((i - ancho_barra/2, busqueda - 10000), ancho_barra, 10000, 
                             facecolor='white', alpha=0.3)
    ax.add_patch(resaltado_superior)
    
    # Etiqueta numérica (con efecto de sombra)
    etiqueta_fondo = Rectangle((i - 0.25, busqueda + 15000), 0.5, 30000, 
                        facecolor='navy', alpha=0.8, zorder=3)
    ax.add_patch(etiqueta_fondo)
    
    ax.text(i, busqueda + 30000, f'{busqueda:,}', 
            ha='center', va='center', color='white', fontsize=18, 
            fontweight='bold', zorder=4)

# Agregar indicación de tasa de crecimiento (usando flechas y signos de porcentaje)
class FlechaPersonalizada(FancyArrowPatch):
    def __init__(self, posA, posB, **kwargs):
        super().__init__(posA, posB, arrowstyle='-|>', 
                         mutation_scale=20, **kwargs)

flecha = FlechaPersonalizada((1.1, busquedas[0]), (1.1, busquedas[1]*0.85), 
                   color='navy', alpha=0.8, linewidth=2)
ax.add_patch(flecha)

# Marcador de porcentaje de tasa de crecimiento
fondo_crecimiento = Rectangle((1.1 - 0.15, busquedas[1]*0.85), 0.3, 30000, 
                     facecolor='navy', alpha=0.9, zorder=3)
ax.add_patch(fondo_crecimiento)

ax.text(1.1, busquedas[1]*0.85 + 15000, f'{incremento}%', 
        ha='center', va='center', color='white', fontsize=20, 
        fontweight='bold', zorder=4)

# Establecer el título (con líneas decorativas)
titulo = ax.set_title('Veces de búsqueda de comida para llevar en días lluviosos', 
                     fontdict={'fontsize':26, 'fontweight':'bold', 'color':'navy'},
                     pad=40, loc='center')

# Línea decorativa debajo del título
inicio_linea = 0.35
fin_linea = 0.65
ax.plot([inicio_linea, fin_linea], [0.94, 0.94], transform=ax.transAxes, 
        color='navy', alpha=0.3, linewidth=2)

# Ocultar los ejes
ax.set_xticks(pos_x)
ax.set_xticklabels(fechas, color='navy', fontsize=18, fontweight='bold')
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Establecer el rango del eje y
ax.set_ylim(0, max(busquedas) * 1.3)

# Agregar una barra decorativa inferior
barra_inferior = Rectangle((-0.5, -30000), 2.5, 30000, 
                      facecolor='navy', alpha=0.1)
ax.add_patch(barra_inferior)

# Optimizar el diseño
plt.tight_layout()
plt.subplots_adjust(top=0.85)  # Hacer espacio para el título
plt.show()