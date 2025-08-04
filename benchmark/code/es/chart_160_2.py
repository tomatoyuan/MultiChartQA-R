import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# 数据
etiquetas = [
    "Pérdida de seguidores \n"
    "de más de 500.000",
    "Pérdida de seguidores \n"
    "entre 500.000 y 300.000",
    "Pérdida de seguidores \n"
    "entre 300.000 y 100.000",
    "Pérdida de seguidores \n"
    "entre 100.000 y 0",
    "Ganancia de seguidores \n"
    "entre 0 y 100.000",
    "Ganancia de seguidores \n"
    "entre 100.000 y 300.000",
    "Ganancia de seguidores \n"
    "entre 300.000 y 500.000",
    "Ganancia de seguidores \n"
    "de más de 500.000"
]
valores = [0.3, 0.4, 12.7, 38.3, 14.1, 14.1, 7.8, 12.2]
colores = ['#a0c8f0'] * 4 + ['#c09ee6'] * 4

fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.barh(range(len(etiquetas)), valores, color=colores)

# Agregar etiquetas de valores
for i, barra in enumerate(barras):
    ax.text(barra.get_width() + 0.5, barra.get_y() + barra.get_height() / 2,
            f"{valores[i]}%", va='center', fontsize=10)

# Agregar anotaciones de grupos
ax.text(40, 1.5, "Expertos en pérdida de seguidores\nRepresentan el 51.7%", fontsize=12, color='white', backgroundcolor='#619de2', ha='center', va='center')
ax.text(40, 6.5, "Expertos en ganancia de seguidores\nRepresentan el 48.3%", fontsize=12, color='white', backgroundcolor='#a460e8', ha='center', va='center')

# Agregar línea divisoria discontinua
ax.axhline(y=3.5, color='orange', linestyle='--', linewidth=2)
ax.text(35, 5, 'Cantidad promedio de ganancia\n'
               ' de seguidores 351.000', fontsize=13, weight='bold')

# Configuración de formato
ax.set_yticks(range(len(etiquetas)))
ax.set_yticklabels(etiquetas)
ax.invert_yaxis()
ax.set_xlim(0, 60)
ax.set_xlabel("Porcentaje (%)")
ax.set_title("Distribución de intervalos de ganancia y pérdida de seguidores")

plt.tight_layout()
plt.show()