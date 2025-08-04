import matplotlib.pyplot as plt
import numpy as np

# Datos de socios oficiales
socios = {
    "Shell": 0.2,
    "Tag Heuer": 0.4
}

# Calcular el monto total
total = sum(socios.values())

# Crear una figura
plt.figure(figsize=(10, 6))

# Gráfico de barras horizontales de socios oficiales
nombres_socios = list(socios.keys())
valores_socios = list(socios.values())

# Trazar el gráfico de barras horizontales
posicion_y = np.arange(len(nombres_socios))
barras = plt.barh(posicion_y, valores_socios, align='center', color='#4e79a7', height=0.6)
plt.yticks(posicion_y, nombres_socios, fontsize=12)
plt.xlabel('Monto (100 millones de yuanes)', fontsize=12)
plt.title('Distribución de Socios y Proveedores Oficiales', fontsize=14)
plt.xlim(0, max(valores_socios) * 1.3)  # Ajustar el rango del eje x para dejar espacio para las etiquetas

# Agregar etiquetas de valor en las barras
for i, v in enumerate(valores_socios):
    plt.text(v + 0.01, i, f'{v:.2f} 100 millones de yuanes', va='center', fontsize=11)
    plt.text(v + 0.01, i - 0.3, f'({v/total*100:.1f}%)', va='center', fontsize=9, color='gray')

# Agregar información del total
plt.axvline(x=total, color='r', linestyle='--', alpha=0.5)
plt.text(total + 0.01, len(nombres_socios), f'Total: {total:.2f} 100 millones de yuanes', va='center', fontsize=11, color='red')

plt.tight_layout()
plt.show()