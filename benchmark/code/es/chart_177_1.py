import matplotlib.pyplot as plt
import numpy as np

# 数据
etiquetas = ['Antes de la política\n "Dobles Reducciones"', 'Después de la política\n "Dobles Reducciones"']
tutoria = [56, 18]     # Proporción de padres que inscriben a sus hijos en clases particulares
educacion_familiar = [68, 77]     # Proporción del tiempo dedicado a la educación familiar

x = np.arange(len(etiquetas))
ancho = 0.35

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Gráfico 1: Proporción de clases particulares
ax1.bar(x, tutoria, color='orange')
ax1.set_title('Proporción de padres que inscriben a sus\n'
              ' hijos en clases particulares antes y después\n '
              'de la política "Dobles Reducciones"')
ax1.set_xticks(x)
ax1.set_xticklabels(etiquetas, rotation=20)
ax1.set_ylim(0, 100)
for i, v in enumerate(tutoria):
    ax1.text(i, v + 2, f'{v}%', ha='center', fontsize=10)

# Gráfico 2: Proporción del tiempo de educación familiar
ax2.bar(x, educacion_familiar, color='red')
ax2.set_title('Cambio en la proporción del tiempo \n'
              'dedicado a la educación familiar antes y \n'
              'después de la política "Dobles Reducciones"')
ax2.set_xticks(x)
ax2.set_xticklabels(etiquetas, rotation=20)
ax2.set_ylim(0, 100)
for i, v in enumerate(educacion_familiar):
    ax2.text(i, v + 2, f'{v}%', ha='center', fontsize=10)

plt.suptitle('Fuente de datos: Ministerio de Educación '
             'de la República Popular China, \n"Investigación sobre el impacto de la política "Dobles Reducciones" en la educación familiar"', fontsize=10, y=0)
plt.tight_layout()
plt.show()