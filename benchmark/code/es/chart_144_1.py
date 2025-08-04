import matplotlib.pyplot as plt
import numpy as np

# --------------------- Datos para el gráfico del número de aspirantes al examen de admisión a la universidad y tasa de crecimiento ---------------------
años_gaokao = ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]
inscripciones_gaokao = [940, 940, 975, 1031, 1071, 1078, 1193]
crecimiento_gaokao = [np.nan, 0.0, 3.7, 5.7, 3.9, 0.7, 10.7]  # No hay tasa de crecimiento en 2016 (como año de inicio)

# --------------------- Datos para el gráfico de la escala de instituciones de educación superior y tasa de crecimiento ---------------------
años_escuela = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
escala_escuela = [2879, 2914, 2914, 2956, 3005, 3012, 3013, 3072]
crecimiento_escuela = [np.nan, 1.2, 0.0, 1.4, 1.7, 0.2, 0.0, 0.0]  # No hay tasa de crecimiento en 2016 (como año de inicio)

# Crear un lienzo con un diseño de 1x2
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# --------------------- Dibujar el gráfico del número de aspirantes al examen de admisión a la universidad y tasa de crecimiento (gráfico izquierdo) ---------------------
ax1.bar(años_gaokao, inscripciones_gaokao, color='orange', label='Número de aspirantes (en miles de personas)')
ax1.set_ylabel('Número de aspirantes (en miles de personas)')
ax1.set_xlabel('Año')
ax1.set_title('Número de aspirantes al examen de admisión a la universidad en China y tasa de crecimiento de 2016 - 2022')
ax1.legend(loc='center left')

# Dibujar el gráfico de línea de la tasa de crecimiento (eje doble)
ax1_2 = ax1.twinx()
ax1_2.plot(años_gaokao, crecimiento_gaokao, marker='o', color='gold', label='Tasa de crecimiento (%)', linewidth=2)
ax1_2.set_ylabel('Tasa de crecimiento (%)')
ax1_2.legend(loc='center right')

# Añadir etiquetas numéricas para el número de aspirantes al examen de admisión a la universidad
for i, num in enumerate(inscripciones_gaokao):
    ax1.text(i, num + 10, f'{num}', ha='center', va='bottom')

# Añadir etiquetas numéricas para la tasa de crecimiento del examen de admisión a la universidad (sin etiqueta para 2016, comenzando desde 2017)
for i, rate in enumerate(crecimiento_gaokao[1:], start=1):
    ax1_2.text(i, rate + 0.1, f'{rate}%', ha='center', va='bottom')

# --------------------- Dibujar el gráfico de la escala de instituciones de educación superior y tasa de crecimiento (gráfico derecho) ---------------------
ax2.bar(años_escuela, escala_escuela, color='orange', label='Escala de instituciones de educación superior (cantidad)')
ax2.set_ylabel('Escala de instituciones de educación superior (cantidad)')
ax2.set_xlabel('Año')
ax2.set_title('Escala de instituciones de educación superior en China y tasa de crecimiento de 2016 - 2023')
ax2.legend(loc='center left')

# Dibujar el gráfico de línea de la tasa de crecimiento (eje doble)
ax2_2 = ax2.twinx()
ax2_2.plot(años_escuela, crecimiento_escuela, marker='o', color='gold', label='Tasa de crecimiento (%)', linewidth=2)
ax2_2.set_ylabel('Tasa de crecimiento (%)')
ax2_2.legend(loc='center right')

# Añadir etiquetas numéricas para la escala de instituciones de educación superior
for i, num in enumerate(escala_escuela):
    ax2.text(i, num + 10, f'{num}', ha='center', va='bottom')

# Añadir etiquetas numéricas para la tasa de crecimiento de las instituciones de educación superior (sin etiqueta para 2016, comenzando desde 2017)
for i, rate in enumerate(crecimiento_escuela[1:], start=1):
    ax2_2.text(i, rate + 0.1, f'{rate}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()