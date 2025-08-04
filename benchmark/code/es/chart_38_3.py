import matplotlib.pyplot as plt
import numpy as np

# Tipos de lentes de contacto desechables
categorias = ['Lentes de contacto diarios desechables', 'Lentes de contacto mensuales desechables', 'Lentes de contacto bi - semanales desechables', 'Lentes de contacto trimestrales desechables', 'Lentes de contacto semestrales desechables', 'Lentes de contacto anuales desechables']
# Proporción de lentes de contacto transparentes (datos simulados, generalmente cercanos a la proporción del ejemplo)
transparentes = [25, 20, 15, 10, 5, 2]
# Proporción de lentes de contacto coloreados (datos simulados, la suma es aproximadamente la proporción correspondiente en el ejemplo, como la suma de los diarios desechables es aproximadamente 41%)
coloridos = [16, 19, 12, 10, 10, 2]

x = np.arange(len(categorias))  # Posiciones en el eje x
ancho = 0.35  # Ancho de cada barra en el grupo

fig, ax = plt.subplots()
# Dibujar barras para lentes de contacto transparentes
rects1 = ax.bar(x - ancho/2, transparentes, ancho, label='Lentes de contacto transparentes', color='#5799C6')
# Dibujar barras para lentes de contacto coloreados
rects2 = ax.bar(x + ancho/2, coloridos, ancho, label='Lentes de contacto coloreados', color='#F28A2B')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=30, ha='right')
# Establecer la etiqueta del eje y
ax.set_ylabel('Proporción (%)')
# Establecer el título
ax.set_title('Los consumidores eligen alternativamente lentes de contacto diarios y mensuales desechables en el uso diario\nTipos de desechables más utilizados en el último año')
ax.legend()

# Anotar los valores encima de cada barra
def autolabel(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate('{}%'.format(altura),
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 3),  # Desplazamiento vertical de la anotación numérica en relación a la barra
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()