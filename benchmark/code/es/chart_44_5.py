import matplotlib.pyplot as plt
import numpy as np

# Datos del gráfico
estados = ["Sedentario, sentado casi todo el día con poco movimiento", 
           "Levantarse y caminar solo cuando se sienta incómodo por estar sentado demasiado tiempo", 
           "Instalar un soporte para el ordenador en el puesto de trabajo y trabajar a menudo de pie", 
           "Exigirse regularmente levantarse y moverse a intervalos, como cada hora", 
           "Moverse con frecuencia debido a los requisitos del trabajo y no tener el problema de estar sentado durante largos períodos"]
porcentaje = [34, 44, 8, 13, 2]
tgi = [138, 108, 73, 59, 65]

# Crear un lienzo y dos ejes Y
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Establecer las posiciones de las barras
x = np.arange(len(estados))
ancho = 0.35

# Dibujar las barras
barras1 = ax1.bar(x - ancho/2, porcentaje, ancho, label='Porcentaje', color='#5DA5DA')
barras2 = ax2.bar(x + ancho/2, tgi, ancho, label='TGI', color='#FAA43A')

# Establecer las etiquetas de los ejes y el título
ax1.set_xlabel('Estado diario en la oficina', fontsize=12)
ax1.set_ylabel('Porcentaje (%)', fontsize=12, color='#5DA5DA')
ax2.set_ylabel('TGI', fontsize=12, color='#FAA43A')
plt.title('Distribución del estado diario en la oficina y TGI entre los trabajadores con horas extras intensivas', fontsize=16, pad=80)

# Establecer las marcas y etiquetas del eje x
ax1.set_xticks(x)
ax1.set_xticklabels(estados, rotation=45, ha='right', fontsize=10)

# Añadir una leyenda
lineas1, etiquetas1 = ax1.get_legend_handles_labels()
lineas2, etiquetas2 = ax2.get_legend_handles_labels()
ax2.legend(lineas1 + lineas2, etiquetas1 + etiquetas2, loc='upper right')

# Añadir etiquetas de datos
def agregar_etiquetas(barras, ax, es_porcentaje=True):
    for barra in barras:
        altura = barra.get_height()
        if es_porcentaje:
            ax.annotate(f'{altura}%',
                        xy=(barra.get_x() + barra.get_width() / 2, altura),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
        else:
            ax.annotate(f'{altura}',
                        xy=(barra.get_x() + barra.get_width() / 2, altura),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

agregar_etiquetas(barras1, ax1)
agregar_etiquetas(barras2, ax2, False)

# Establecer las líneas de cuadrícula
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()