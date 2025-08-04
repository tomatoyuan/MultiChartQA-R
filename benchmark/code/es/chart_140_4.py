import matplotlib.pyplot as plt

# Datos
etiquetas = ["Vehículos Eléctricos de Batería (Motores a Bordo)", "Vehículos Eléctricos Híbridos (Nueva Energía Híbrida Gasolina - Eléctrica)", "Vehículos Eléctricos de Pila de Combustible de Hidrógeno", 
             "Vehículos de Pila de Combustible (Generación de Energía a través de Reacciones Químicas)", "Vehículos de Gas (Gas Natural)", "Vehículos de Combustible Alternativo (por ejemplo, Etanol)"]
tamaños = [61.3, 22.0, 8.4, 4.7, 2.9, 0.7]
colores = ["#FAD6A5", "#F9CB9C", "#F7B787", "#F4A460", "#E9967A", "#CD5C5C"]

fig, ax = plt.subplots(figsize=(10, 7))

# Dibujar un gráfico circular
porciones, textos, textos_automaticos = ax.pie(tamaños, colors=colores, autopct='%1.1f%%', startangle=90)

ax.set_title('Tipos de Vehículos de Nueva Energía Considerados Más \nPrometedores para el Desarrollo por los Consumidores Chinos en 2023')
ax.legend(porciones, etiquetas, title="Tipos de Vehículos", loc="center left", bbox_to_anchor=(1, 0.5))

# Ajustar el color del texto de la anotación para garantizar que sea claramente visible en las porciones claras/oscuras
for texto_automatico in textos_automaticos:
    texto_automatico.set_color('white' if texto_automatico.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()