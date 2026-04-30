"""
Tests para el modelo Football Valuator MLOps
Ejecutar con: pytest tests/test_modelo.py -v
"""

import os
import pandas as pd
import joblib
import numpy as np


# ============================================================
# RUTAS
# ============================================================
DATASET_PATH = 'data/processed/dataset_modelo.csv'
MODELO_PATH = 'models/modelo_final.pkl'
FEATURES_PATH = 'models/features.pkl'


# ============================================================
# TEST 1: El dataset existe y se carga
# ============================================================
def test_dataset_existe():
    """Verifica que el dataset procesado se puede cargar"""
    assert os.path.exists(DATASET_PATH), f"No se encuentra {DATASET_PATH}"
    
    dataset = pd.read_csv(DATASET_PATH)
    assert len(dataset) > 0, "El dataset está vacío"
    assert len(dataset) > 100_000, "El dataset tiene menos filas de las esperadas"


# ============================================================
# TEST 2: Las columnas críticas existen y no tienen nulos
# ============================================================
def test_dataset_columnas_criticas():
    """Verifica que las columnas más importantes están presentes y completas"""
    dataset = pd.read_csv(DATASET_PATH)
    
    columnas_criticas = [
        'valor_ajustado_2025',
        'edad',
        'position',
        'tier_liga',
        'minutos_ventana'
    ]
    
    for col in columnas_criticas:
        assert col in dataset.columns, f"Falta la columna crítica: {col}"
        assert dataset[col].notna().all(), f"La columna {col} tiene valores nulos"


# ============================================================
# TEST 3: El modelo se carga correctamente
# ============================================================
def test_modelo_se_carga():
    """Verifica que el modelo entrenado se puede cargar"""
    assert os.path.exists(MODELO_PATH), f"No se encuentra {MODELO_PATH}"
    assert os.path.exists(FEATURES_PATH), f"No se encuentra {FEATURES_PATH}"
    
    modelo = joblib.load(MODELO_PATH)
    features = joblib.load(FEATURES_PATH)
    
    # Verificar que tiene método predict
    assert hasattr(modelo, 'predict'), "El modelo no tiene método predict"
    assert len(features) > 0, "La lista de features está vacía"


# ============================================================
# TEST 4: El modelo predice valores positivos y razonables
# ============================================================
def test_modelo_predice_valores_razonables():
    """Verifica que el modelo predice valores positivos y dentro de rangos esperados"""
    modelo = joblib.load(MODELO_PATH)
    features = joblib.load(FEATURES_PATH)
    
    # Crear un jugador "promedio" de prueba
    jugador_prueba = pd.DataFrame(0, index=[0], columns=features)
    jugador_prueba['edad'] = 25
    jugador_prueba['edad_cuadrado'] = 625
    jugador_prueba['height_in_cm'] = 180
    jugador_prueba['minutos_ventana'] = 1500
    jugador_prueba['partidos_ventana'] = 20
    jugador_prueba['goles_ventana'] = 5
    jugador_prueba['ratio_minutos'] = 0.85
    jugador_prueba['tier_liga'] = 1
    
    # Predecir (recordamos: el modelo predice en escala log)
    pred_log = modelo.predict(jugador_prueba)[0]
    pred_eur = np.expm1(pred_log)
    
    # Verificaciones razonables
    assert pred_eur > 0, "La predicción es negativa"
    assert pred_eur < 500_000_000, "La predicción es absurdamente alta"
    assert pred_eur > 10_000, "La predicción es absurdamente baja"