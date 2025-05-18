
import streamlit as st
import pandas as pd

# Cargar el dataset
@st.cache_data
def cargar_datos():
    df = pd.read_excel("dataset_meteostat_madrid_castellano.xlsx")
    df['fecha'] = pd.to_datetime(df['fecha'])
    return df

df = cargar_datos()

# Configurar título
st.title("📰 Generador de Titulares Meteorológicos")
st.markdown("Consulta un titular informativo para una fecha concreta en Madrid, basado en datos reales.")

# Selector de fecha
fecha = st.date_input("Selecciona una fecha", min_value=df['fecha'].min(), max_value=df['fecha'].max())

# Selector de parámetro
parametro = st.selectbox("Selecciona un parámetro", [
    "temperatura máxima",
    "temperatura mínima",
    "precipitación",
    "racha de viento"
])

# Buscar fila
row = df[df['fecha'] == fecha]

# Generar titular
if not row.empty:
    row = row.iloc[0]
    if parametro == "temperatura máxima" and row['temperatura_maxima'] >= 30:
        st.success(f"Madrid supera los {row['temperatura_maxima']}°C el {fecha.strftime('%-d de %B')}")
    elif parametro == "temperatura mínima" and row['temperatura_minima'] <= 3:
        st.success(f"Se esperan noches frías en Madrid con {row['temperatura_minima']}°C el {fecha.strftime('%-d de %B')}")
    elif parametro == "precipitación" and row['precipitacion'] > 0:
        st.success(f"Ha llovido {row['precipitacion']} mm en Madrid el {fecha.strftime('%-d de %B')}")
    elif parametro == "racha de viento" and row['racha_viento'] >= 50:
        st.success(f"Riesgo de vientos fuertes en Madrid el {fecha.strftime('%-d de %B')} con ráfagas de {row['racha_viento']} km/h")
    else:
        st.info("No se han registrado fenómenos destacados ese día para el parámetro seleccionado.")
else:
    st.warning("Fecha no disponible en el dataset.")
