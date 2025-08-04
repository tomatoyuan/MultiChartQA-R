import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Categorías de grupos
grupos = ["Crecimiento interanual del volumen de transacciones", "Crecimiento interanual del precio unitario"]
# Categorías de datos (correspondientes a la leyenda)
categorias = ["Belleza y Cuidado del Cabello (Tmall Global)", "Belleza y Cuidado del Cabello (Tmall + Taobao)"]
# Datos simulados (se pueden ajustar)
datos = [[35, 25],  # Crecimiento interanual del volumen de transacciones: Tmall Global, Tmall + Taobao
         [18, 10]]  # Crecimiento interanual del precio unitario: Tmall Global, Tmall + Taobao

# Texto de anotación
texto_anotacion = "Tmall Global tiene ventajas evidentes en el crecimiento interanual del volumen de transacciones y en el crecimiento interanual del precio unitario"
# Parámetros de la flecha
propiedades_flecha = dict(arrowstyle="->", color="green", connectionstyle="arc3,rad=0.2")

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar gráficos de barras agrupados
x = np.arange(len(grupos))
ancho_barra = 0.35
for i in range(len(categorias)):
    desplazamiento = ancho_barra * i
    ax.bar(x + desplazamiento, datos[i], width=ancho_barra, 
           color="#C63974" if i == 0 else "#87CEEB",
           label=categorias[i])

# Agregar anotaciones de datos
for i in range(len(grupos)):
    for j in range(len(categorias)):
        altura = datos[j][i]
        ax.annotate(f'{altura}%',
                    xy=(x[i] + ancho_barra * j, altura),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x + ancho_barra / len(categorias))
ax.set_xticklabels(grupos)
# Establecer las marcas del eje y
ax.set_ylim(0, 40)
# Establecer el título
ax.set_title("Crecimiento del mercado de Belleza y Cuidado del Cabello en China: \nComparación de los datos del último mes entre marzo de 2021 y marzo de 2022", 
             fontsize=14, fontweight="bold", y=1.1)

# Leyenda personalizada (para evitar el problema del orden de la leyenda generada automáticamente)
elementos_leyenda = [Patch(facecolor="#C63974", label=categorias[0]),
                     Patch(facecolor="#87CEEB", label=categorias[1])]
ax.legend(handles=elementos_leyenda, loc="upper right")

# Embellir: Ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

# plt.tight_layout()
plt.show()