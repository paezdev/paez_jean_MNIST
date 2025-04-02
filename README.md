# Proyecto: Clasificación de Dígitos Manuscritos con MNIST

## Descripción

Este proyecto tiene como objetivo implementar y comparar tres enfoques diferentes para la clasificación de dígitos manuscritos utilizando el dataset MNIST. Los enfoques implementados son:

1. **Red Neuronal desde Cero:** Una implementación manual utilizando únicamente NumPy, para comprender los fundamentos de las redes neuronales.
2. **MLPClassifier con Scikit-learn:** Un modelo rápido y eficiente utilizando la biblioteca Scikit-learn.
3. **Red Neuronal con Keras:** Un modelo más avanzado y flexible utilizando la biblioteca Keras, con técnicas modernas como dropout y optimización avanzada.

El proyecto busca analizar las ventajas y desventajas de cada enfoque, evaluando su precisión, tiempo de desarrollo y facilidad de implementación.

---

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **`paez_jean_EA4.ipynb`:** Notebook de Jupyter con la implementación de los tres modelos, análisis de resultados y visualizaciones.
- **`README.md`:** Este archivo, que describe el proyecto y proporciona instrucciones para su uso.

---

## Requisitos

Para ejecutar el notebook, necesitas tener instaladas las siguientes bibliotecas de Python:

- `numpy`
- `matplotlib`
- `scikit-learn`
- `tensorflow` (opcional, para el modelo de Keras)

Puedes instalar estas bibliotecas utilizando `pip`:

```bash
pip install numpy matplotlib scikit-learn tensorflow
```

---

## Uso

1. Clona este repositorio en tu máquina local.
2. Abre el archivo `paez_jean_EA4.ipynb` con Jupyter Notebook o JupyterLab.
3. Ejecuta las celdas en orden para cargar los datos, entrenar los modelos y visualizar los resultados.

---

## Resultados

### Resumen de Resultados

| Modelo                  | Precisión en Entrenamiento | Precisión en Prueba |
|-------------------------|----------------------------|---------------------|
| Desde Cero (NumPy)      | 99.39%                    | 97.52%             |
| Scikit-learn (MLP)      | 98.47%                    | 96.49%             |
| Keras (Red Neuronal)    | 99.71%                    | 97.90%             |

### Interpretación de Resultados

1. **Red Neuronal desde Cero:**
   - Este modelo alcanzó una precisión del **97.52% en el conjunto de prueba**, demostrando que una implementación manual bien diseñada puede ser altamente efectiva.
   - Este enfoque es ideal para aprender los fundamentos de las redes neuronales, ya que permite un control total sobre cada paso del proceso.

2. **MLPClassifier con Scikit-learn:**
   - El modelo entrenado con Scikit-learn alcanzó una precisión del **96.49% en el conjunto de prueba**. Aunque es ligeramente inferior al modelo desde cero, su tiempo de desarrollo y entrenamiento fue significativamente menor.
   - Es una excelente opción para implementar modelos rápidamente, especialmente cuando no se necesita un control detallado sobre los cálculos internos.

3. **Red Neuronal con Keras:**
   - Este modelo fue el más preciso, alcanzando una precisión del **97.90% en el conjunto de prueba**. Su arquitectura más compleja y el uso de técnicas como dropout ayudaron a prevenir el sobreajuste.
   - Es ideal para proyectos más grandes o cuando se dispone de recursos computacionales adecuados.

---

## Visualización de Resultados

Se generaron visualizaciones para comparar las predicciones de los tres modelos con las etiquetas reales. En general, los tres modelos mostraron un rendimiento consistente, con errores en casos particularmente difíciles o ambiguos, como dígitos que son difíciles de distinguir incluso para un humano (por ejemplo, un "4" que parece un "9").

Además, se analizaron las gráficas de evolución de las pérdidas y la precisión del modelo de Keras:

- **Evolución de las Pérdidas:** La pérdida disminuyó rápidamente durante las primeras épocas, estabilizándose después de la décima época. Esto indica que el modelo alcanzó un punto de convergencia.
- **Evolución de la Precisión:** La precisión aumentó rápidamente durante las primeras épocas, alcanzando valores cercanos al 98%. La diferencia entre la precisión en entrenamiento y validación fue pequeña, lo que indica que el modelo generalizó bien.

---

## Conclusiones Generales

Este proyecto permitió explorar tres enfoques diferentes para resolver el problema de clasificación de dígitos manuscritos. Cada enfoque tiene sus ventajas y desventajas:

1. **Desde Cero:** Ideal para aprender los fundamentos de las redes neuronales y tener un control total sobre el proceso.
2. **Scikit-learn:** Excelente para prototipos rápidos y problemas estándar donde no se requiere personalización avanzada.
3. **Keras:** La mejor opción para proyectos complejos o de alto rendimiento, gracias a su flexibilidad y soporte para técnicas modernas.

---

## Recomendaciones

1. **Para aprender los fundamentos:** Implementar modelos desde cero para comprender cómo funcionan las redes neuronales en detalle.
2. **Para proyectos rápidos:** Usar Scikit-learn para implementar modelos funcionales con poco esfuerzo y en un tiempo reducido.
3. **Para proyectos complejos:** Usar Keras para construir modelos avanzados y aprovechar técnicas modernas como dropout y optimizadores avanzados.
4. **Optimización futura:**
   - Experimentar con arquitecturas más profundas o con más neuronas en las capas ocultas.
   - Probar diferentes tasas de aprendizaje y tamaños de batch.
   - Implementar técnicas de regularización adicionales, como L2 o batch normalization.
   - Usar aumento de datos (data augmentation) para enriquecer el conjunto de entrenamiento.

---

## Autor

Jean Paez

**Fecha:** 2 de abril de 2025