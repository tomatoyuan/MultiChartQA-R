import matplotlib.pyplot as plt

# Años
años = list(range(2015, 2027))

# Tasa de crecimiento del comercio minorista global (línea negra)
crecimiento_minorista = [6.2, 6.0, 6.5, 4.5, 5.3, -2.6, 5.0, 6.9, 3.9, 4.3, 3.7, 3.4]

# Tasa de crecimiento del comercio minorista electrónico global (línea naranja)
crecimiento_comercio_electronico = [23.0, 26.8, 28.4, 22.0, 20.9, 26.7, 16.8, 7.1, 8.9, 9.4, 8.8, 8.1]

# Dibujar el gráfico
plt.figure(figsize=(12, 6))
plt.plot(años, crecimiento_minorista, marker='o', color='black', label='Crecimiento del comercio minorista global')
plt.plot(años, crecimiento_comercio_electronico, marker='o', color='orange', label='Crecimiento del comercio minorista electrónico global')

# Etiquetar los datos de cada punto
for i, (r, e) in enumerate(zip(crecimiento_minorista, crecimiento_comercio_electronico)):
    plt.text(años[i], r + 0.5, f'{r}%', ha='center', va='bottom', fontsize=9, color='black')
    plt.text(años[i], e + 0.5, f'{e}%', ha='center', va='bottom', fontsize=9, color='orange')

plt.title("Cambio en las tasas de crecimiento del comercio minorista global y del comercio minorista electrónico global", fontsize=14)
plt.xlabel("Año")
plt.ylabel("Tasa de crecimiento (%)")
plt.xticks(años)
plt.ylim(-5, 32)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()