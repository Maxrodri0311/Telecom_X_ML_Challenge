# 🤖 Telecom X - Parte 2: Predicción de Cancelación (Churn) con Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" />
</p>

Este es el repositorio correspondiente a la **Parte 2 del Challenge de Data Science LATAM** de Alura. Evolucionando desde el rol de Analista de Datos hasta Científico de Datos Junior, este proyecto aplica técnicas formales de Machine Learning para predecir qué clientes abandonarán a la compañía de telecomunicaciones "Telecom X".

---

## 🎯 Propósito del Proyecto

Construir y evaluar un pipeline predictivo robusto. No solo buscamos adivinar la fuga, sino **identificar las causas matemáticas** (Feature Importance) que empujan a los clientes a irse, entregando a la junta directiva estrategias accionables de retención.

---

## 🧠 Arquitectura del Pipeline de Machine Learning

### 1. Preprocesamiento Avanzado

- **One-Hot Encoding (`get_dummies`)**: Transformación de variables categóricas complejas (tipos de contrato, métodos de pago) en matrices binarias comprensibles para los algoritmos.
- **Purga de Fallos Transaccionales**: Detección y eliminación de `NaN` residuales inyectados en la variable objetivo (`Churn`) para el cumplimiento estricto de los requisitos de Scikit-Learn.
- **Estandarización Z-Score (`StandardScaler`)**: Penalización de varianzas altas y compresión de escalas dispares (como la diferencia de magnitud entre Gastos Mensuales y Antigüedad) para optimizar modelos basados en distancia y gradiente.

### 2. Tratamiento de Desbalanceo (SMOTE)

La naturaleza del Churn implica que la gran mayoría de clientes *no abandona* (aprox. 73% vs 27%). Para evitar un modelo sesgado ("vago") que maximice el acierto prediciendo siempre la clase mayoritaria, se inyectaron datos sintéticos con **SMOTE** únicamente en la partición de entrenamiento, equilibrando las clases a 50/50.

### 3. Competencia Algorítmica (Modelado)

Se entrenaron dos arquitecturas supervisadas radicalmente diferentes:

1. **Regresión Logística**: Modelo lineal paramétrico, matemáticamente transparente mediante coeficientes interpretables.
2. **Random Forest Classifier**: Ensamble no paramétrico basado en múltiples árboles de decisión robustos frente a la escala y datos complejos.

---

## 📊 Medición y Resultados

Ambos modelos fueron auditados bajo datos de Prueba (`test_size=0.3`) rigurosamente estratificados.

- **Ganador Analítico:** La **Regresión Logística**.
- **Justificación de Negocio:** Aunque Random Forest es poderoso, la Regresión Logística identificó a un **mayor número de deserciones reales** tras la aplicación de SMOTE. En escenarios de fuga (Churn), atrapar al cliente *antes* de que se vaya, aunque signifique enviar algunas promociones innecesarias a clientes fieles (Falsos Positivos), es infinitamente más rentable que ignorar a los que se van a ir indudablemente (Falsos Negativos). La Regresión Logística demostró superioridad de `Recall` sobre la clase crítica (1).

---

## 💡 Conclusión Estratégica (Feature Importance / Coeficientes)

La extracción matemática del algoritmo nos reveló una radiografía exacta del comportamiento del consumidor, dándonos el plan de acción:

### 🚨 Factores Críticos de Fuga (Culpables)

1. **Contratos Month-to-Month**: La estacionalidad mensual da demasiada ventana a la cancelación por mero impulso o inconformismo pasajero.
2. **Internet de Fibra Óptica**: Presumiblemente por costos ocultos, insatisfacción en velocidades percibidas o fuertes contra-ofertas de la competencia.
3. **Pagos Electrónicos (Electronic Check)**: Facturaciones en frío sin débito en cuenta causan mayor fricción, obligando al cliente a revisar el servicio mensualmente.

### 🛡️ Factores Vitales de Retención (Salvadores)

1. **Mayor Antigüedad (`tenure`)**: A mayor paso de los meses de fricción general o periodo de prueba, se afianzan a la compañía y el peligro de fuga se desploma a niveles negativos.
2. **Contratos a Largo Plazo (Two-Year)**: Retienen estructuralmente al cliente.
3. **Subscripciones Secundarias Integradas**: Adquisición de servicios combinados.

### 📢 Estrategia Propuesta

**Telecom X** debe priorizar agresivamente campañas para *migrar usuarios de contratos mensuales a anuales*, implementando promociones en los planes de fibra óptica a cambio de lealtad multianual, y ofrecer incentivos a quienes automaticen su pago con tarjeta de crédito/débito en lugar de usar cheques electrónicos.

---
*Desarrollado estratégicamente para la predicción de negocio en Machine Learning por Maxi.*
