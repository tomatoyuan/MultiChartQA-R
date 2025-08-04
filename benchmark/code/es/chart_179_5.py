import numpy as np
import matplotlib.pyplot as plt

# Traducción de las etiquetas
labels_mkt = ['Marketing SEO', 'Marketing SEM', 'Marketing social\n(Incluye gestión propia de cuentas y publicidad paga)', 'Marketing de \ninfluencers', 'Marketing por \ncorreo electrónico', 'Otros métodos']
values_mkt = [23.5, 45.6, 65.0, 47.5, 20.4, 5.3]
values_mkt += values_mkt[:1]
angles = np.linspace(0, 2 * np.pi, len(labels_mkt), endpoint=False).tolist()
angles += angles[:1]

fig2, ax2 = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
ax2.plot(angles, values_mkt, color='darkorange', linewidth=2)
ax2.fill(angles, values_mkt, color='darkorange', alpha=0.6)
ax2.set_thetagrids(np.degrees(angles[:-1]), labels_mkt, fontsize=10)
# Título traducido
ax2.set_title("Opciones de promoción de marketing principales para tiendas independientes", fontsize=14, fontweight='bold', pad=20)

for angle, value in zip(angles, values_mkt):
    ax2.text(angle, value + 2, f'{value:.1f}%', color='darkred', ha='center', va='center', fontsize=12)

# Texto de origen traducido
plt.figtext(0.5, 0.02, "Fuente: Datos de investigación de GoodsFox, período de estadísticas de enero a diciembre de 2023", ha='center', fontsize=10)
plt.tight_layout()
plt.show()