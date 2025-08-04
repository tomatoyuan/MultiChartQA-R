import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# Configurar soporte para fuentes chinas
fuentes_chinas = [
    "SimHei", "Heiti TC", "WenQuanYi Micro Hei",
    "Microsoft YaHei", "Arial Unicode MS"
]
fuentes_disponibles = {f.name for f in fm.fontManager.ttflist}
for fuente in fuentes_chinas:
    if fuente in fuentes_disponibles:
        plt.rcParams["font.family"] = fuente
        break
plt.rcParams['axes.unicode_minus'] = False

# Datos
años = ['2019', '2020', '2021', '2022', '2023']
T1 = [12, 11, 11, 10, 10]
T2 = [47, 47, 46, 45, 43]
T3 = [41, 43, 44, 45, 48]
totales = [6243, 4114, 7044, 5476, 6221]

ancho_barra = 0.5
fig1, ax1 = plt.subplots(figsize=(10, 6))

# Calcular la base
base_T1 = np.array(T3)
base_T2 = base_T1 + np.array(T2)

# Dibujar el gráfico de barras
p1 = ax1.bar(años, T3, label='T3+', color='#FDB462')
p2 = ax1.bar(años, T2, bottom=base_T1, label='T2', color='#80B1D3')
p3 = ax1.bar(años, T1, bottom=base_T2, label='T1', color='#FB8072')

# Agregar la anotación del total en la parte superior
for i, total in enumerate(totales):
    ax1.text(i, 103, str(total), ha='center', va='bottom', fontsize=10, fontweight='bold')

# Agregar la anotación de la proporción de cada segmento
for i in range(len(años)):
    # T3+
    ax1.text(i, T3[i] / 2, f"{T3[i]}%", ha='center', va='center', fontsize=10, color='black')
    # T2
    ax1.text(i, base_T1[i] + T2[i] / 2, f"{T2[i]}%", ha='center', va='center', fontsize=10, color='black')
    # T1
    ax1.text(i, base_T2[i] + T1[i] / 2, f"{T1[i]}%", ha='center', va='center', fontsize=10, color='black')

# Configurar el título y los ejes
ax1.set_title('Distribución de nuevas tiendas abiertas entre 2019 y 2023', fontsize=14)
ax1.set_ylabel('Proporción (%)')
ax1.set_ylim(0, 115)
ax1.legend()

plt.tight_layout()
plt.show()