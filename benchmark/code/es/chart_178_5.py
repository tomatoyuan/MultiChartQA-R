import matplotlib.pyplot as plt

# Configurar los datos
etiquetas = ['Actualización del consumo, \n'
             'más dispuestos a gastar mucho\n'
             ' en regalos de Año Nuevo',
             'Consumo estable, no se saldrán de\n'
             ' su nivel de consumo habitual',
             'Degradación del consumo, \n'
             'los regalos son un gasto no esencial,\n'
             ' se ahorrará lo más posible']
tamaños = [42, 49, 8]
colores = ['#a32020', '#f25e41', '#ffa768']

# Dibujar el gráfico circular anular
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos, textos_automaticos = ax.pie(
    tamaños, labels=etiquetas, autopct='%1.0f%%', startangle=90, colors=colores,
    wedgeprops={'width': 0.4}, textprops={'fontsize': 10}
)

# Agregar texto en el centro
plt.text(0, 0, "Actitud de consumo\npara regalos de Año Nuevo", ha='center', va='center', fontsize=14, fontweight='bold')

# Agregar fuente de datos y explicación
plt.figtext(0.5, 0.01,
            "Fuente de datos: Encuesta de CBNData en enero de 2024  \n"
            "Explicación de datos: En comparación con su consumo habitual, "
            "¿Cuál de las siguientes opciones \nse ajusta mejor a su cambio de consumo al adquirir regalos de Año Nuevo? N = 1500",
            wrap=True, horizontalalignment='center', fontsize=9)

# Establecer el título
plt.title("Distribución de la actitud de consumo de la gente \n"
          "hacia los regalos de Año Nuevo en comparación con el consumo diario", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()