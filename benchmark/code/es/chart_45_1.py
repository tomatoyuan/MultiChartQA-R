import matplotlib.pyplot as plt

# Datos
años = [2023, 2024, 2029]
tamaño_del_mercado = [3500, 3700, 3850]  # Los datos de 2023 y 2024 son aproximados, el valor de 2029E es un ejemplo y se puede reemplazar con datos precisos reales

# Crear el gráfico
fig, ax = plt.subplots()

# Usar índices como posiciones en el eje x para que las barras estén uniformemente distribuidas
x_pos = range(len(años))
barras = ax.bar(x_pos, tamaño_del_mercado, color='pink')

# Agregar título y etiquetas
ax.set_title('Tamaño del mercado global de ropa funcional')
ax.set_ylabel('(miles de millones de dólares)')
ax.text(0.5, 1.05, 'Tasa de crecimiento compuesto anual = 6.1%\n*De 2024 a 2029', ha='center', va='bottom', transform=ax.transAxes)

# Configurar las etiquetas del eje x (usar puntos suspensivos para representar los años intermedios y agregar la marca E al año 2029)
ax.set_xticks(x_pos)
ax.set_xticklabels(['2023', '2024', '... 2029E'])

# Agregar anotaciones de valores encima de cada barra
for i, (x, valor) in enumerate(zip(x_pos, tamaño_del_mercado)):
    ax.text(x, valor + 5, f'{valor}', ha='center', va='bottom')

# Configurar las divisiones del eje y
ax.set_ylim([3300, 3900])
ax.set_yticks(range(3300, 3901, 100))

# Mostrar el gráfico
plt.show()