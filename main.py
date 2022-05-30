import streamlit as st
import pandas as pd

# IMPORTAMOS LOS DATOS A UN DATAFRAME
df = pd.read_csv("data_simulation/experimento.csv", index_col="time")

# MOSTRAMOS EN EL DASHBOARD UNA MUESTRA DE LOS DATOS
st.write("""
## Modelo Cinético de la Liberación de Neurotransmisor

**Presentamos los resultados de la simulación estocástica del modelo cinético.**
"""
)

st.write(df.head())

# DESPLEGAMOS LOS GRÁFICOS QUE DESEAMOS MOSTRAR A PARTIR DE UN DATAFRAME
st.write("""
**Evolución temporal de la cantidad de vesiculas en cada estado.**
""")

st.line_chart(df[["Docked", "pPrimed", "Primed", "Fusion"]])

st.write("""
**La dinámica de la liberación de las vesiculas.**

""")

st.line_chart(df["Transition 5"])



