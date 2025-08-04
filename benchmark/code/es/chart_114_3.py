import matplotlib.pyplot as plt

# Razones para la revisión médica
razones = ["Revisión médica regular personal", "Revisión obligatoria (por ejemplo, revisión pre - matrimonio, revisión pre - empleo)",
           "De repente, se desea conocer el estado de salud propio", "Se necesita realizar una revisión debido a una enfermedad"]
# Proporciones correspondientes (%)
proporciones = [50.82, 44.83, 44.46, 31.22]
# Colores correspondientes (coherentes con el naranja en el gráfico)
colores = ['#FF7F27', '#1E90FF', '#4B53FF', '#32CD32'] * len(razones)

fig, ax = plt.subplots(figsize=(8, 8))
# Dibujar un gráfico de donut, establecer el ancho para dejar el centro hueco, y wedgeprops controla el estilo del donut
wedges, texts, autotexts = ax.pie(proporciones, labels=razones, colors=colores, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Ajustar la posición del texto de la anotación para que esté en el área adecuada del donut (adaptado para este diseño de donut)
for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_verticalalignment('center')

ax.set_title('Razones por las que los consumidores de exámenes médicos chinos se someten a revisiones médicas en 2025')

plt.show()