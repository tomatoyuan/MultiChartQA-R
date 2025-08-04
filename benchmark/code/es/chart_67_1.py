import matplotlib.pyplot as plt
import numpy as np

# Datos simulados (consistentes con la tendencia del gráfico original y aproximados en valores)
ciudades = [
    "Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Tianjin", 
    "Shenyang", "Dalian", "Nanjing", "Hangzhou", "Qingdao", 
    "Wuhan", "Chongqing", "Chengdu", "Xi'an"
]
stock = np.array([849, 833.3, 561.7, 637.8, 238.5, 121.2, 98.1, 237.8, 230.7, 160.1, 257.2, 182.9, 270.4, 280.8])  # Stock
absorcion_neta = np.array([34.1, 53.1, 42.6, 64.1, 12.9, 3.5, 2.4, 22.2, 6.4, 9.7, 17.1, 11.3, 19.7, 12.6])  # Absorción neta
tasa_vacante = np.array([10, 10, 8, 19, 29, 33, 32, 22, 16, 24, 35, 28, 13, 22])  # Tasa de vacante

# Inicializar el lienzo (ancho y alto coinciden con el gráfico original)
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()  # Ejes duales

# Dibujar gráficos de barras (stock + absorción neta)
x = np.arange(len(ciudades))
ancho = 0.6
# Gráfico de barras de stock
rects_stock = ax1.bar(x, stock, ancho, label="Stock de distritos comerciales centrales en 2021 (10,000 metros cuadrados)", color="#8BC34A")
# Gráfico de barras de absorción neta (apilado en la parte inferior del stock, use un tamaño más pequeño para simular la "barra azul")
rects_absorcion = ax1.bar(x, absorcion_neta, ancho, bottom=0, label="Absorción neta de distritos comerciales centrales en 2021 (10,000 metros cuadrados)", color="#42A5F5")

# Dibujar un gráfico de línea (tasa de vacante)
line_vacancy, = ax2.plot(x, tasa_vacante, marker="o", color="#7CB342", label="Tasa de vacante de distritos comerciales centrales en 2021 (%)", linewidth=2)

# Agregar etiquetas de datos (stock, absorción neta, tasa de vacante)
for rect in rects_stock:
    altura = rect.get_height()
    ax1.annotate(f'{altura}', 
                 xy=(rect.get_x() + rect.get_width()/2, altura),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9)
for rect in rects_absorcion:
    altura = rect.get_height()
    ax1.annotate(f'{altura}', 
                 xy=(rect.get_x() + rect.get_width()/2, altura/2 + 5),  # Etiqueta en el centro de la barra azul
                 xytext=(0, 0),
                 textcoords="offset points",
                 ha='center', va='center', fontsize=9, color='white')
for i, tasa in enumerate(tasa_vacante):
    ax2.annotate(f'{tasa}%', 
                 xy=(x[i], tasa),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9, color="black")

# Configuración de ejes y leyendas
ax1.set_xticks(x)
ax1.set_xticklabels(ciudades, fontsize=10, rotation=45)
ax1.set_ylabel("Stock/Absorción neta (10,000 metros cuadrados)", fontsize=11, color="#8BC34A")
ax2.set_ylabel("Tasa de vacante (%)", fontsize=11, color="#7CB342")

# 组合图例并调整位置
handles, labels = ax1.get_legend_handles_labels()
handles.append(line_vacancy)
labels.append(line_vacancy.get_label())

# 将图例放置在标题下方，纵向排列
fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 0.95), ncol=1, fontsize=9)

# Título y mejora visual
plt.title("Escala del mercado de edificios de oficinas de clase A y tasa de vacante en distritos comerciales centrales de principales ciudades de primer y segundo nivel en China en 2021", fontsize=14, pad=40)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
plt.tight_layout()
plt.subplots_adjust(top=0.85)  # 为标题和图例腾出空间

# Mostrar el gráfico
plt.show()