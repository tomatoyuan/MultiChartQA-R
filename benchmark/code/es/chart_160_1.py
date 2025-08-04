# 重新设置中文字体与绘图配置
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Datos
años = ['2020', '2021', '2022', '2023']
creadores = [900, 1100, 1310, 1420]
tasas_de_crecimiento = ['+22%', '+18%', '+8%']

# Graficación
plt.figure(figsize=(10, 6))
plt.plot(años, creadores, marker='o', color='#6A78FF', linewidth=3)

# Etiquetar los valores de los puntos (negrita, azul)
for i, valor in enumerate(creadores):
    plt.text(i, valor + 30, f"{valor}", ha='center', fontsize=14, color='#1F3BB3', fontweight='bold')

# Etiquetar las tasas de crecimiento (fuente más grande, cursiva, púrpura)
for i in range(1, len(creadores)):
    mid_x = (i - 1 + i) / 2
    mid_y = (creadores[i - 1] + creadores[i]) / 2 + 20
    plt.text(mid_x, mid_y, tasas_de_crecimiento[i - 1], ha='center', fontsize=16, color='#B03ACC', fontstyle='italic')

# Configuración del gráfico
plt.title("Número total de creadores con más de diez mil seguidores en las \n"
          "principales plataformas de redes sociales (en miles)", fontsize=16, fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()