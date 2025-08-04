import matplotlib.pyplot as plt
import numpy as np

# Izquierda: Datos sobre la necesidad de protección solar
etiquetas_izquierda = ["Creen que la protección solar es necesaria", "Creen que la protección solar no es necesaria"]
proporciones_izquierda = [92.5, 7.5]

# Derecha: Datos sobre los factores importantes de protección solar
etiquetas_derecha = ["Prevenir el bronceado solar", "Prevenir la quemadura solar", "Prevenir el envejecimiento fotoinducido", "Prevenir la pigmentación", "Prevenir el cáncer de piel"]
proporciones_derecha = [52.5, 83.2, 57.2, 57.3, 31.5]

fig, (ax_izquierda, ax_derecha) = plt.subplots(1, 2, figsize=(14, 6))

# Dibujar el gráfico de comparación de la izquierda
x_izquierda = np.arange(len(etiquetas_izquierda))
barras = ax_izquierda.bar(x_izquierda, proporciones_izquierda, color=['#FFA07A', '#FFD700'])
for i, prop in enumerate(proporciones_izquierda):
    ax_izquierda.text(i, prop + 1, f'{prop}%', ha='center', va='bottom')
ax_izquierda.set_ylabel('Proporción (%)')
ax_izquierda.set_xticks(x_izquierda)
ax_izquierda.set_xticklabels(etiquetas_izquierda)
ax_izquierda.set_title('Opiniones de los consumidores chinos sobre la protección solar')
ax_izquierda.yaxis.set_ticks([])
for espina in ['top', 'right', 'left']:
    ax_izquierda.spines[espina].set_visible(False)

# Dibujar el gráfico de radar de la derecha
num_vars = len(etiquetas_derecha)
angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
proporciones_derecha += proporciones_derecha[:1]
angulos += angulos[:1]
ax_derecha.fill(angulos, proporciones_derecha, color='#FFA07A', alpha=0.25)
ax_derecha.plot(angulos, proporciones_derecha, color='#FFA07A', linewidth=2)
for i, (angulo, prop) in enumerate(zip(angulos[:-1], proporciones_derecha[:-1])):
    ax_derecha.text(angulo, prop + 1, f'{prop}%', ha='center', va='bottom')
ax_derecha.set_yticklabels([])
ax_derecha.set_xticks(angulos[:-1])
ax_derecha.set_xticklabels(etiquetas_derecha, rotation=15, ha='right')
ax_derecha.set_title('Factores importantes de protección solar reconocidos por los consumidores chinos')

plt.tight_layout()
plt.show()