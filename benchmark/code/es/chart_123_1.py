import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2016-12", "2017-12", "2018-12", "2019-12", "2020-12", "2021-12", "2022-12", "2023-12"]
# Escala de usuarios de entrega de comida online (en diez miles de personas)
escala_usuarios = [20856, 34338, 40601, 39780, 41883, 54416, 52118, 54454]
# Tasa de penetración (porcentaje del total de usuarios de Internet)
tasa_penetracion = [28.5, 44.5, 49.0, 44.0, 42.3, 52.7, 48.8, 49.9]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Trazar el gráfico de barras de la escala de usuarios de entrega de comida online
ax1.bar(x, escala_usuarios, color='orange', label='Escala de usuarios de entrega de comida online (en diez miles de personas)')
ax1.set_ylabel('Escala de usuarios de entrega de comida online (en diez miles de personas)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='lower left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de penetración
ax2 = ax1.twinx()
ax2.plot(x, tasa_penetracion, marker='o', color='brown', label='Tasa de penetración (% del total de usuarios de Internet)')
ax2.set_ylabel('Tasa de penetración (%)')
ax2.legend(loc='center right')

# Agregar etiquetas para la escala de usuarios de entrega de comida online
for i, escala in enumerate(escala_usuarios):
    ax1.text(i, escala + 500, f'{escala}', ha='center', va='bottom')

# Agregar etiquetas para la tasa de penetración
for i, tasa in enumerate(tasa_penetracion):
    ax2.text(i, tasa + 1, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Escala de usuarios de entrega de comida online y tasa de penetración en China desde 2016 hasta 2023')

plt.tight_layout()
plt.show()