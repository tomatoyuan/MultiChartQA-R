import matplotlib.pyplot as plt
import numpy as np

# Años y rangos de fechas
años = ["Abr - Sep 2019", "Abr - Sep 2020", "Abr - Sep 2021", "Abr - Sep 2022", "Abr - Sep 2023"]
# Proporciones de cada categoría (%), en el orden de [Joyería de incrustación/platino/joyería de oro K, Joyería y productos de oro, Relojes]
proporciones_categoría = np.array([
    [29.1, 64.5, 6.4],
    [30.1, 60.9, 9.0],
    [22.6, 70.7, 6.7],
    [19.1, 75.6, 5.3],
    [14.7, 80.1, 5.2]
])

x = np.arange(len(años))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras apiladas
base = np.zeros(len(años))
for i in range(proporciones_categoría.shape[1]):
    ax.bar(x, proporciones_categoría[:, i], bottom=base, width=0.6, label=['Joyería de incrustación/platino/joyería de oro K', 'Joyería y productos de oro', 'Relojes'][i])
    # Agregar etiquetas numéricas
    for j in range(len(años)):
        ax.text(j, base[j] + proporciones_categoría[j, i] / 2, f'{proporciones_categoría[j, i]}%', ha='center', va='center')
    base += proporciones_categoría[:, i]

ax.set_ylabel('Proporción (%)')
ax.set_xlabel('Fecha')
ax.set_xticks(x)
ax.set_xticklabels(años)
ax.legend()
ax.set_title('Proporción de ingresos brutos de las categorías de productos de Chow Tai Fook en los informes semestrales de 2019 a 2023')

plt.tight_layout()
plt.show()