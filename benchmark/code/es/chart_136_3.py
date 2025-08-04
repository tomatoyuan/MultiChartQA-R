import matplotlib.pyplot as plt

# Datos de amuletos
etiquetas_amuletos = ["Por encima de 700 yuan", "Entre 500 - 700 yuan", "Entre 350 - 500 yuan", "Por debajo de 350 yuan"]
tamaños_amuletos = [12.0, 23.0, 41.0, 24.0]
colores_amuletos = ["#E4725F", "#F6C85F", "#94B49F", "#92574C"]

# Datos de pulseras
etiquetas_pulseras = ["Por encima de 1000 yuan", "Entre 600 - 1000 yuan", "Por debajo de 600 yuan"]
tamaños_pulseras = [14.0, 46.0, 40.0]
colores_pulseras = ["#E4725F", "#F6C85F", "#94B49F"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Dibujar el gráfico circular de amuletos
segmentos1, textos1, textos_auto1 = ax1.pie(tamaños_amuletos, colors=colores_amuletos, autopct='%1.1f%%', startangle=90,
                                           wedgeprops=dict(width=0.4))
ax1.set_title('Distribución de precios de amuletos Pandora en China')
# Ajustar la leyenda y colocarla a la derecha del gráfico circular
ax1.legend(segmentos1, etiquetas_amuletos, title="Rango de precios", loc="center left", bbox_to_anchor=(1, 0.5))
# Hacer que el color del texto de las anotaciones sea más claro (diferenciar entre segmentos oscuros/claros)
for texto_auto in textos_auto1:
    texto_auto.set_color('blue' if texto_auto.get_position()[1] > 0.5 else 'black')

# Dibujar el gráfico circular de pulseras
segmentos2, textos2, textos_auto2 = ax2.pie(tamaños_pulseras, colors=colores_pulseras, autopct='%1.1f%%', startangle=90,
                                           wedgeprops=dict(width=0.4))
ax2.set_title('Distribución de precios de pulseras Pandora en China')
ax2.legend(segmentos2, etiquetas_pulseras, title="Rango de precios", loc="center left", bbox_to_anchor=(1, 0.5))
for texto_auto in textos_auto2:
    texto_auto.set_color('blue' if texto_auto.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()