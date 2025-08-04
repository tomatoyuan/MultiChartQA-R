import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ["La transformación digital del marketing es muy importante",
             "En la era digital, las operaciones y los datos son igualmente importantes",
             "En la era digital, la marca sigue siendo muy importante",
             "En la era digital, construir una plataforma de marketing es muy importante"]
muy_de_acuerdo = np.array([64, 68, 78, 53])  # Porcentaje de fuertemente de acuerdo
de_acuerdo = np.array([33, 29, 19, 40])  # Porcentaje de de acuerdo
en_desacuerdo = np.array([2, 2, 2, 5])  # Porcentaje de en desacuerdo
fuertemente_en_desacuerdo = np.array([1, 1, 1, 2])  # Porcentaje de fuertemente en desacuerdo

# Esquema de colores (utilizando una paleta de colores más moderna)
colores = ['#E63946', '#F1FAEE', '#A8DADC', '#1D3557']  # Gradiente de rojo a azul oscuro

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño de la figura

# Dibujar un gráfico de barras apiladas horizontales
parte_inferior = np.zeros(len(etiquetas))
for i, (datos, etiqueta, color) in enumerate(zip(
    [fuertemente_en_desacuerdo, en_desacuerdo, de_acuerdo, muy_de_acuerdo],
    ['Fuertemente en desacuerdo', 'En desacuerdo', 'De acuerdo', 'Fuertemente de acuerdo'],
    colores
)):
    barras = ax.barh(etiquetas, datos, left=parte_inferior, color=color, label=etiqueta,
                     alpha=0.9, edgecolor='w', linewidth=0.5)

    # Etiquetar el porcentaje en cada barra
    for barra, valor in zip(barras, datos):
        if valor > 2:  # Solo mostrar texto en barras lo suficientemente anchas
            ax.text(
                barra.get_x() + barra.get_width() / 2,
                barra.get_y() + barra.get_height() / 2,
                f"{valor}%",
                ha='center',
                va='center',
                color='black' if i < 2 else 'white',  # Ajustar el color del texto según el color de fondo
                fontweight='bold',
                fontsize=10
            )

    parte_inferior += datos

# Establecer el título
ax.set_title('Resultados de la encuesta de opiniones de los anunciantes sobre marketing digital en 2021', fontsize=16, fontweight='bold', pad=20)

# Establecer las etiquetas
ax.set_xlabel('Porcentaje (%)', fontsize=12, labelpad=10)
# ax.set_ylabel('Opiniones', fontsize=12, labelpad=10)  # Eliminar la etiqueta del eje y

# Establecer las líneas de la cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Establecer el rango del eje x
ax.set_xlim(0, 100)

# Embelezar la leyenda - Colocarla debajo del título
fig.legend(loc='upper center', bbox_to_anchor=(0.6, 0.95), ncol=4, frameon=False, fontsize=10)

# Ajustar los bordes
for espina in ax.spines.values():
    espina.set_visible(False)

# Ajustar el diseño para dejar espacio para la leyenda
plt.subplots_adjust(top=0.85)  # Reducir el margen superior
plt.tight_layout()

# Mostrar el gráfico
plt.show()