import matplotlib.pyplot as plt
import numpy as np

# Datos simulados (coherentes con la tendencia del gráfico original)
años = ["2017", "2018", "2019", "2020", "2021", "2022e", "2023e", "2024e"]
tamaño_del_mercado = np.array([2, 4, 8, 15, 16, 18, 22, 30])  # Tamaño del mercado (en miles de millones de yuanes)
tasa_de_crecimiento = np.array([136.6, 101.1, 89.4, 10.3, 12.0, 23.7, 33.4])  # Tasa de crecimiento (%)

# Inicializar un lienzo de doble eje
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Dibujar un gráfico de barras (tamaño del mercado)
x = np.arange(len(años))
ancho_de_barra = 0.6
rects = ax1.bar(x, tamaño_del_mercado, width=ancho_de_barra, label="Tamaño del Mercado PaaS de Audio y Video en Tiempo Real (RTC) de China (en miles de millones de yuanes)", color="#A4C639")

# Dibujar un gráfico de línea (tasa de crecimiento)
line, = ax2.plot(x[1:], tasa_de_crecimiento, marker="o", color="#42A5F5", label="Tasa de Crecimiento del Tamaño del Mercado PaaS de Audio y Video en Tiempo Real (RTC) de China", linewidth=2)

# Agregar anotaciones del tamaño del mercado (encima del gráfico de barras)
for rect in rects:
    altura = rect.get_height()
    ax1.annotate(f'{altura}', 
                 xy=(rect.get_x() + rect.get_width()/2, altura),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9)

# Agregar anotaciones de la tasa de crecimiento (encima de los puntos del gráfico de línea)
for i, tasa in enumerate(tasa_de_crecimiento):
    ax2.annotate(f'{tasa}%', 
                 xy=(x[i+1], tasa),  # x comienza en 2018 (índice 1)
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9, color="#42A5F5")

# Agregar anotaciones de CAGR
ax1.annotate(
    "CAGR=77.6%", 
    xy=(0.2, 0.8), xycoords="axes fraction",
    xytext=(0.2, 0.9), textcoords="axes fraction",
    arrowprops=dict(facecolor='gray', width=1, headwidth=6),
    fontsize=10, ha='center'
)
ax1.annotate(
    "CAGR=28.4%", 
    xy=(0.7, 0.8), xycoords="axes fraction",
    xytext=(0.7, 0.9), textcoords="axes fraction",
    arrowprops=dict(facecolor='gray', width=1, headwidth=6),
    fontsize=10, ha='center'
)

# Configuración de ejes y leyenda
ax1.set_xticks(x)
ax1.set_xticklabels(años, fontsize=10)
ax1.set_ylabel("Tamaño del Mercado (en miles de millones de yuanes)", fontsize=11, color="#A4C639")
ax2.set_ylabel("Tasa de Crecimiento (%)", fontsize=11, color="#42A5F5")

# 组合图例并设置为纵向排列（ncol=1）
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
# 调整图例位置，避免与标题或图表重叠
ax1.legend(handles, labels, loc="upper left", bbox_to_anchor=(0, 1.09), ncol=1, fontsize=9)

# Título y mejora visual
plt.title("Tamaño y Pronóstico del Mercado PaaS de Audio y Video en Tiempo Real (RTC) de China de 2017 a 2024", fontsize=14, pad=30)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
# 调整布局，为纵向图例留出空间
plt.subplots_adjust(left=0.15)  # 增加左侧边距，避免图例文本被截断
plt.tight_layout()

# Mostrar el gráfico
plt.show()