import matplotlib.pyplot as plt
import numpy as np

# Izquierda: Datos sobre las formas en que los inversores chinos obtienen información de inversión y financiera
left_labels = [
    "Profesionales de inversión profesionales, como \ngestores de riqueza de bancos/instituciones de valores", 
    "Relaciones sociales, como familiares y amigos", 
    "Aplicaciones de inversión", 
    "Medios propios, redes sociales, etc.", 
    "Documentos oficiales, anuncios, datos, etc.", 
    "Otros (sitios web financieros, \naplicaciones de noticias, bases de datos, etc.)"
]
left_proportions = [56.01, 38.37, 36.24, 34.11, 33.91, 0.97]

# Derecha: Datos sobre los tipos de aplicaciones de inversión utilizadas por los inversores chinos
right_labels = [
    "Plataformas de pago tercerizadas, como Alipay y WeChat", 
    "Aplicaciones propias de las compañías de valores", 
    "Plataformas financieras de Internet tercerizadas, como Flush"
]
right_proportions = [75.94, 68.45, 51.34]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Dibujar un gráfico de barras horizontales de las formas de obtener información en la izquierda
y1 = np.arange(len(left_labels))
ax1.barh(y1, left_proportions, color='orange')
ax1.set_yticks(y1)
ax1.set_yticklabels(left_labels)
ax1.set_xlabel('Proporción (%)')
ax1.set_title('Formas en que los inversores chinos obtienen información de inversión y financiera')
# Agregar anotaciones numéricas en la izquierda
for i, proportion in enumerate(left_proportions):
    ax1.text(proportion + 1, i, f'{proportion}%', va='center')

# Dibujar un gráfico de barras horizontales de los tipos de aplicaciones utilizadas en la derecha
y2 = np.arange(len(right_labels))
ax2.barh(y2, right_proportions, color='orange')
ax2.set_yticks(y2)
ax2.set_yticklabels(right_labels)
ax2.set_xlabel('Proporción (%)')
ax2.set_title('Tipos de aplicaciones de inversión utilizadas por los inversores chinos')
# Agregar anotaciones numéricas en la derecha
for i, proportion in enumerate(right_proportions):
    ax2.text(proportion + 1, i, f'{proportion}%', va='center')

plt.tight_layout()
plt.show()