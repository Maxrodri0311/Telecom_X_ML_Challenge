import pandas as pd
import json
import os

print("Iniciando puente de datos de Parte 1 a Parte 2...")

# 1. Carga del raw JSON anidado
ruta_archivo = os.path.join('Telecom X', 'Datos', 'TelecomX_Data.json')
with open(ruta_archivo, 'r') as file:
    data = json.load(file)

df_telecom = pd.json_normalize(data)

# 2. Ejecucion exacta de la Limpieza exitosa de la Parte 1
df_clean = df_telecom.copy()
df_clean.columns = [col.split('.')[-1] if '.' in col else col for col in df_clean.columns]

df_clean['Total'] = df_clean['Total'].replace(' ', pd.NA)
df_clean['Total'] = pd.to_numeric(df_clean['Total'], errors='coerce').fillna(0)

cols_texto = df_clean.select_dtypes(include=['object']).columns
for col in cols_texto:
    if col != 'customerID': 
        df_clean[col] = df_clean[col].str.lower().str.strip()

mapeo_binario = {'yes': 1, 'no': 0}
col_binarias = ['Churn', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']

for col in col_binarias:
    if col in df_clean.columns:
        df_clean[col] = df_clean[col].map(mapeo_binario).fillna(df_clean[col])

df_clean['Cuentas_Diarias'] = round(df_clean['Monthly'] / 30.4, 2)

# 3. Exportacion para la Parte 2
ruta_salida = os.path.join('Telecom X', 'Datos', 'TelecomX_dataset_limpio.csv')
df_clean.to_csv(ruta_salida, index=False)

print(f"Dataset exportado exitosamente con {len(df_clean)} filas y {len(df_clean.columns)} columnas.")
print(f"Ruta: {ruta_salida}")
