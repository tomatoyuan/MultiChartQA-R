import matplotlib.pyplot as plt
import numpy as np

# Tipos de empresas
categorias = ["Empresas estatales", "Organismos gubernamentales", "Empresas privadas", "Empresas de inversión extranjera", "Instituciones públicas"]
# Proporciones de cada año de graduación (Clase de 2021, Clase de 2022, Clase de 2023)
porcentajes_2021 = [42.5, 11.4, 19.0, 11.2, 13.2]
porcentajes_2022 = [44.4, 9.4, 17.4, 11.9, 14.7]
porcentajes_2023 = [46.7, 12.5, 12.6, 14.6, 12.3]

x = np.arange(len(categorias))
ancho = 0.25

fig, ax = plt.subplots(figsize=(12, 8))

# Dibujar gráficos de barras para la Clase de 2021 (naranja), Clase de 2022 (amarillo) y Clase de 2023 (verde)
bar_2021 = ax.bar(x - ancho, porcentajes_2021, ancho, color='coral', label='Clase de 2021')
bar_2022 = ax.bar(x, porcentajes_2022, ancho, color='gold', label='Clase de 2022')
bar_2023 = ax.bar(x + ancho, porcentajes_2023, ancho, color='green', label='Clase de 2023')

# Agregar etiquetas de valor
for barras in [bar_2021, bar_2022, bar_2023]:
    for barra in barras:
        altura = barra.get_height()
        ax.text(barra.get_x() + barra.get_width() / 2, altura + 1, f'{altura}%', ha='center', va='bottom')

ax.set_ylabel('Proporción (%)')
ax.set_xlabel('Tipos de empresas')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()
ax.set_title('Tipos de empresas de empleo deseados por los recién graduados chinos de 2021 a 2023')

plt.tight_layout()
plt.show()