import matplotlib.pyplot as plt
import numpy as np

# Etiquetas para los costos
labels_cost = ['Costo de creación \nde sitio web', 'Desarrollo de producto', 'Costo de tráfico', 'Almacenamiento\n y logística', 'Costo de mano de obra', 'Otros costos']
# Valores de los costos
values_cost = [6.1, 25.5, 32.6, 13.0, 18.5, 4.3]
values_cost += values_cost[:1]
# Ángulos para el gráfico polar
angles = np.linspace(0, 2 * np.pi, len(labels_cost), endpoint=False).tolist()
angles += angles[:1]

# Crear la figura y el eje polar
fig1, ax1 = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
# Dibujar la línea del gráfico
ax1.plot(angles, values_cost, color='darkorange', linewidth=2)
# Rellenar el área debajo de la línea
ax1.fill(angles, values_cost, color='darkorange', alpha=0.6)
# Establecer las etiquetas en los ángulos
ax1.set_thetagrids(np.degrees(angles[:-1]), labels_cost, fontsize=10)
# Establecer el título del gráfico
ax1.set_title("Gastos principales de la tienda independiente", fontsize=14, fontweight='bold', pad=20)

# Añadir los valores en cada punto del gráfico
for angle, value in zip(angles, values_cost):
    ax1.text(angle, value + 2, f'{value:.1f}%', color='darkred', ha='center', va='center', fontsize=12)

# Añadir la fuente de los datos
plt.figtext(0.5, 0.02, "Fuente: Datos de investigación de GoodsFox, período de estadísticas de enero a diciembre de 2023", ha='center', fontsize=10)
# Ajustar el diseño
plt.tight_layout()
# Mostrar el gráfico
plt.show()