import matplotlib.pyplot as plt

# Datos
años = [2023, 2024, 2029]
tamaño_del_mercado = [9000, 9500, 15000]  # Los datos de 2023 y 2024 son aproximados, el valor de 2029E es un ejemplo y se puede reemplazar con datos precisos reales
# Si se tienen datos precisos del tamaño del mercado en 2023 y 2024, simplemente se reemplacen los valores correspondientes en la lista

# Crear el gráfico
fig, ax = plt.subplots()

# Usar índices como posiciones en el eje x para que las barras se distribuyan uniformemente
pos_x = range(len(años))
barras = ax.bar(pos_x, tamaño_del_mercado, color='pink')  # Guardar los objetos de las barras en una variable

# Agregar título y etiquetas
ax.set_title('Tamaño del mercado de ropa funcional en China')
ax.set_ylabel('(miles de millones de yuanes)')
ax.text(0.5, 1.05, 'Tasa de crecimiento compuesto anual = 9.8%\n*Entre 2024 y 2029', ha='center', va='bottom', transform=ax.transAxes)

# Establecer etiquetas del eje x (usar puntos suspensivos para representar los años intermedios y agregar la marca E al año 2029)
ax.set_xticks(pos_x)
ax.set_xticklabels(['2023', '2024', '... 2029E'])

# Establecer las divisiones del eje y, ajustarlas según el rango de los datos
ax.set_ylim([0, 16000])  # Ampliar ligeramente el límite superior para evitar que las anotaciones de los valores se salgan del gráfico
ax.set_yticks(range(0, 16001, 5000))  

# Agregar anotaciones de datos encima de cada barra
for barra in barras:
    altura = barra.get_height()  # Obtener la altura de la barra (es decir, el valor)
    # Agregar texto en la posición central por encima de la barra
    ax.text(barra.get_x() + barra.get_width()/2., altura + 200,  # 200 es la distancia desde la barra
            f'{altura}',  # Mostrar el valor
            ha='center', va='bottom')  # Centrado horizontalmente, abajo verticalmente

# Mostrar el gráfico
plt.show()