import matplotlib.pyplot as plt

# 数据
etiquetas = ['Costo de compra de\n materias primas', 'Costo de mano de obra', 'Tres gastos', 'Costo de alquiler y servicios', 'Costo de energía', 'Impuestos']
tamaños = [42.7, 21.9, 20.1, 8.8, 3.6, 2.9]
colores = ['#E73331', '#233B7B', '#999999', '#F5B92E', '#4BA2C8', '#892D2D']
# explode = [0.05 if i == 0 else 0 for i in range(len(etiquetas))]  # Resaltar "Costo de compra de materias primas"

# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(aspect="equal"))
wedges, textos, autotextos = ax.pie(
    tamaños, labels=etiquetas, colors=colores, autopct='%.1f%%',
    startangle=90, wedgeprops=dict(width=1.0), textprops=dict(color="black", fontsize=12)
)

# Establecer la fuente de las etiquetas en blanco y centrarlas
for autotexto in autotextos:
    autotexto.set_color('white')
    autotexto.set_fontsize(12)
    autotexto.set_fontweight('bold')

ax.set_title("Proporción de diversos costos de empresas\n"
             " de muestra de la industria alimentaria en China en 2023", fontsize=16)
plt.tight_layout()
plt.show()