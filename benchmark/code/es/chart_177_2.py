import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# 数据
categorias = [
    "Capacidad de aprendizaje\n y hábitos de estudio",
    "Desarrollo intelectual y\n capacitación científica",
    "Tutorías académicas y \nconocimientos curriculares",
    "Cultivo de intereses",
    "Habilidades de vida y\n hábitos de comportamiento",
    "Salud mental",
    "Capacidad de competición\n y rendimiento", "Condición física"
]
valores = [68, 57, 54, 50, 40, 35, 26, 20]

# Configuración del gradiente de color
norm = mcolors.Normalize(vmin=min(valores), vmax=max(valores))
cmap = cm.Reds

# Creación del gráfico
fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(categorias, valores, color=cmap(norm(valores)))

# Etiquetado de los valores
for barra in barras:
    valor_y = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2.0, valor_y + 1, f'{valor_y}%', ha='center', va='bottom', fontsize=10)

# Mejora visual del gráfico
ax.set_ylabel('Proporción de atención (%)')
ax.set_title('Aspectos que los padres prestan atención y valoran en la educación familiar')
ax.set_ylim(0, 80)
plt.xticks(rotation=30, ha='right')
plt.tight_layout()

plt.show()