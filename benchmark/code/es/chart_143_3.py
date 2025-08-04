import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Preparación de datos
data = {
    "Tipo de marca": ["Marcas tradicionales nacionales", "Nuevas marcas nacionales", "Marcas internacionales conocidas", "Marcas nicho extranjeras"],
    "Disminución": [24.0, 21.0, 30.3, 31.4],
    "Sin cambio significativo": [49.1, 52.1, 48.6, 54.7],
    "Aumento": [26.9, 26.9, 21.1, 13.9]
}
df = pd.DataFrame(data).set_index("Tipo de marca")

# Crear un mapa de calor (con anotaciones numéricas)
plt.figure(figsize=(8, 6))
sns.heatmap(df, annot=True, fmt=".1f", cmap="Oranges", 
            cbar=False, annot_kws={"size": 10, "color": "black"})

# Ajustar las etiquetas de los ejes y el título
plt.yticks(rotation=0)  # Mostrar las etiquetas del eje y horizontalmente
plt.xlabel("Cambio en la frecuencia de compra")
plt.ylabel("Tipo de marca")
plt.title("Encuesta sobre los cambios en la frecuencia de compra de marcas de cosméticos en China en 2023", y=1.03, fontsize=12, fontweight="bold")
# Agregar subtítulo en inglés
plt.suptitle("Encuesta sobre los cambios en la frecuencia de compra de marcas de cosméticos en China en 2023", 
             y=0.93, fontsize=10, color="gray")

# Simular las cajas discontinuas en la figura original (marcadas manualmente, se pueden calcular coordenadas precisas adicionalmente)
# Marcar Marcas tradicionales nacionales y Nuevas marcas nacionales en la columna "Aumento"
for i in [0, 1]:
    plt.plot([2.2, 2.2], [i + 0.5, i + 1.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([1.8, 2.6], [i + 0.5, i + 0.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([1.8, 2.6], [i + 1.5, i + 1.5], linestyle="--", color="orange", linewidth=2)
# Marcar Marcas internacionales conocidas y Marcas nicho extranjeras en la columna "Disminución"
for i in [2, 3]:
    plt.plot([0.2, 0.2], [i + 0.5, i + 1.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([-0.2, 0.8], [i + 0.5, i + 0.5], linestyle="--", color="orange", linewidth=2)
    plt.plot([-0.2, 0.8], [i + 1.5, i + 1.5], linestyle="--", color="orange", linewidth=2)

plt.tight_layout()
plt.show()