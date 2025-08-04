import matplotlib.pyplot as plt
import numpy as np

# Rangos de presupuesto de bodas
categorias = ["Por debajo de 50,000 yuan", "De 50,000 a 100,000 yuan", "De 100,000 a 200,000 yuan", "De 200,000 a 300,000 yuan", "De 300,000 a 400,000 yuan", "De 400,000 a 500,000 yuan", "Por encima de 500,000 yuan"]
# Proporciones correspondientes (%)
proporciones = [8.8, 30.4, 34.2, 18.2, 6.5, 1.2, 0.7]
# Número simulado de bolsas de dinero (aproximadamente correspondiente a la proporción, se puede ajustar para que la visual sea más cercana a la imagen original)
conteos_bolsas = [1, 6, 7, 4, 2, 1, 1]

x = np.arange(len(categorias))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de barras de "bolsas de dinero" (simular el efecto de apilamiento con múltiples pequeños rectángulos)
for i in range(len(categorias)):
    for j in range(conteos_bolsas[i]):
        rect = plt.Rectangle((x[i] - 0.2, j * 1), 0.4, 1, color='orange')
        ax.add_patch(rect)
        # Agregar la etiqueta de proporción cerca de la bolsa de dinero más alta (agregarla solo una vez)
        if j == conteos_bolsas[i] - 1:
            ax.text(x[i], (j + 1) * 1 + 0.2, f'{proporciones[i]}%', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Ilustración de apilamiento de bolsas de dinero')
ax.set_xlabel('Rango de presupuesto')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.set_ylim(0, max(conteos_bolsas) + 1)  # Reservar espacio para mostrar las etiquetas
ax.axis('off')  # Ocultar los ejes predeterminados para resaltar el estilo de las bolsas de dinero

ax.set_title('Encuesta sobre gastos/presupuestos de planificación de bodas en China')

plt.tight_layout()
plt.show()