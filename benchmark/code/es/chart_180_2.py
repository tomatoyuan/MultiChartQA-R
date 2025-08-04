import matplotlib.pyplot as plt
import numpy as np

# 数据
años = ['2022H1', '2023H1']
registro_total = [883, 670]
registro_nuevo = [134, 358]
registro_otros = [registro_total[i] - registro_nuevo[i] for i in range(2)]
registro_total_dossier = [1481, 1937]

x = np.arange(len(años))  # Posición en el eje x
ancho = 0.35

fig, ax = plt.subplots(figsize=(8, 6))

# Parte de registro: Gráfico de barras apiladas
bar_otros = ax.bar(x - ancho/2, registro_otros, ancho, label='Otros expedientes', color='lightgray')
bar_nuevo = ax.bar(x - ancho/2, registro_nuevo, ancho, bottom=registro_otros, label='Expedientes de nuevos productos', color='blue')

# Etiquetar los valores totales de registro (en la parte superior)
for i in range(len(años)):
    ax.text(x[i] - ancho/2, registro_total[i] + 30, str(registro_total[i]),
            ha='center', va='bottom', fontsize=10)

# ✅ Etiquetar los valores de los expedientes de nuevos productos (en el centro de la pila)
for i in range(len(años)):
    ax.text(x[i] - ancho/2, registro_otros[i] + registro_nuevo[i] / 2,
            str(registro_nuevo[i]), ha='center', va='center', fontsize=9, color='white')

# Parte de inscripción: Gráfico de barras independientes
bar_registro_dossier = ax.bar(x + ancho/2, registro_total_dossier, ancho, label='Inscripción', color='skyblue')

# Etiquetar los valores de inscripción
for i in range(len(años)):
    ax.text(x[i] + ancho/2, registro_total_dossier[i] + 30, str(registro_total_dossier[i]),
            ha='center', va='bottom', fontsize=10)

# Configurar las etiquetas del eje y el título
ax.set_xticks(x)
ax.set_xticklabels(años)
ax.set_ylabel('Número de expedientes', fontsize=12)
ax.set_title('2022H1 vs. 2023H1 Situación de registro e inscripción de suplementos dietéticos en China', fontsize=14, fontweight='bold')
ax.legend(loc='upper left')

# Explicación de la fuente de datos
plt.figtext(0.5, 0.01, 'Nota: Los datos de inscripción no incluyen productos de inscripción de importación\nFuente de datos: Administración General de Mercado de China',
            wrap=True, horizontalalignment='center', fontsize=9)
plt.ylim(0, 2250)
plt.tight_layout()
plt.show()