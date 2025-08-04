import matplotlib.pyplot as plt

# Configurar los datos de la categoría principal
main_labels = ['Otros envases', 'Envases sostenibles']
main_sizes = [75, 25]
main_colors = ['#E0E0E0', '#8BC34A']

# Configurar los datos de las subcategorías internas de los envases sostenibles
inner_labels = ['Envases de reutilización', 'Otros envases sostenibles', 'Otros envases (sin细分)']
inner_sizes = [10, 15, 75]
inner_colors = ['#AED581', '#A1887F', '#FFFFFF00']  # El tercer elemento es transparente (para que "Otros envases" no se muestre nuevamente)

# Crear la gráfica
fig, ax = plt.subplots(figsize=(8, 6))

# Círculo exterior (categoría principal)
wedges1, _ = ax.pie(
    main_sizes,
    radius=1,
    labels=[f'{v}%' for v in main_sizes],
    colors=main_colors,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Círculo interior (subcategorías de envases sostenibles)
wedges2, _ = ax.pie(
    inner_sizes,
    radius=1 - 0.3,
    labels=['10%', '15%', ''],
    colors=inner_colors,
    startangle=0,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Agregar el título
plt.title('Estructura de productos de la industria global de envases en 2020', fontsize=16, color='green', weight='bold')

# Leyenda
custom_legend = [
    plt.Line2D([0], [0], marker='o', color='w', label='Otros envases', markerfacecolor='#E0E0E0', markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='Envases sostenibles', markerfacecolor='#8BC34A', markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='Envases de reutilización', markerfacecolor='#AED581', markersize=12),
    plt.Line2D([0], [0], marker='o', color='w', label='Otros envases sostenibles', markerfacecolor='#A1887F', markersize=12)
]
plt.legend(handles=custom_legend, loc='lower center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=10, frameon=False)

plt.tight_layout()
plt.show()