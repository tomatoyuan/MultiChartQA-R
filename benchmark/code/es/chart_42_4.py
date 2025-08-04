import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ['', '']
valores = [8, 9.84]  # Datos exactos: 8 * (1+0.18) = 9.44, ajustados a 9.84 de acuerdo con la apariencia visual del gráfico
x = np.arange(len(categorias))

# Crear una figura
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
ancho_barra = 0.6
rects1 = ax.bar(x[0], valores[0], width=ancho_barra, color='#6aa84f', label='Ventas Previas', 
                edgecolor='black', linewidth=0.8)
rects2 = ax.bar(x[1], valores[1], width=ancho_barra, color='#3d85c6', label='Ventas de Enero 2025', 
                edgecolor='black', linewidth=0.8)

# Agregar etiquetas de datos
def agregar_etiquetas(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate(f'{altura}',
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=12)

agregar_etiquetas(rects1)
agregar_etiquetas(rects2)

# Agregar una anotación de flecha horizontal (apuntando a la derecha)
inicio_flecha = (x[0] + ancho_barra/2, valores[0] + 0.3)  # Punto de inicio de la flecha: lado derecho de la primera barra
fin_flecha = (x[1] - ancho_barra/4, valores[0] + 0.3)  # Punto final de la flecha: lado izquierdo de la segunda barra
ax.annotate('Incremento del 18%',
            xy=fin_flecha,
            xytext=inicio_flecha,
            arrowprops=dict(arrowstyle='->, head_width=0.4, head_length=0.8', 
                           color='black', lw=1.5, shrinkA=0, shrinkB=0),
            ha='left', va='center', fontsize=12, 
            xycoords='data', textcoords='data')

# Establecer el estilo del gráfico
ax.set_ylim([0, 12])
ax.set_ylabel('Miles de millones', fontsize=14)
ax.set_title('Crecimiento de las ventas de la industria de alimentos saludables en enero de 2025', fontsize=16, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(categorias, fontsize=12)
ax.legend(fontsize=12, loc='upper left')

# Agregar líneas de cuadrícula
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ajustar el borde
for spine in ax.spines.values():
    spine.set_color('gray')

# Mejorar el estilo general
plt.tight_layout()

# Mostrar el gráfico
plt.show()