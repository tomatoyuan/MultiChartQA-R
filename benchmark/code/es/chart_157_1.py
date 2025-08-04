import matplotlib.pyplot as plt
import numpy as np

# Etiquetas y colores de cada nivel (apilados de abajo hacia arriba)
categorias = ['No desea pagar un plus adicional', 'Está dispuesto a pagar un plus de menos del 5%', 'Está dispuesto a pagar un plus del 5% - 10%', 'Está dispuesto a pagar un plus del 10% - 20%', 'Está dispuesto a pagar un plus superior al 20%']
colores = ['#FF5C40', '#FF7B5C', '#FF9C80', '#FFBFA6', '#FFE3DC']

# Datos ordenados en orden de apilamiento
total_consumo_verde = [34, 34, 22, 9, 1]
alimentos_bebidas = [30, 36, 22, 10, 2]

# Transponer los datos para la gráfica de barras apiladas
datos = np.array([total_consumo_verde, alimentos_bebidas])
datos_acumulados = datos.cumsum(axis=1)

x = np.arange(datos.shape[0])
ancho = 0.5

# Crear la figura
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar la gráfica de barras apiladas (de abajo hacia arriba)
for i in range(len(categorias)):
    bases = datos_acumulados[:, i - 1] if i > 0 else np.zeros_like(x)
    valores = datos[:, i]
    barras = ax.bar(x, valores, ancho, bottom=bases, label=categorias[i], color=colores[i])

    # Agregar etiquetas de texto
    for j in range(len(x)):
        if valores[j] > 3:  # Evitar superposición de valores pequeños
            ax.text(x[j], bases[j] + valores[j]/2, f'{valores[j]}%', ha='center', va='center', fontsize=10, color='white')

# Configurar el título y los ejes
ax.set_xticks(x)
ax.set_xticklabels(['Visión general del deseo de consumo verde', 'Alimentos y bebidas'], fontsize=12)
ax.set_ylabel('Porcentaje (%)', fontsize=12)
ax.set_ylim(0, 105)
ax.set_title('Los consumidores chinos tienen cierta disposición a pagar un plus por consumo verde', fontsize=16, weight='bold')

# Leyenda (en el mismo orden que la apilación en la gráfica)
ax.legend(loc="center", title='Porcentaje dispuesto a pagar de plus', fontsize=8, title_fontsize=10)

plt.tight_layout()
plt.show()