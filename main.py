import streamlit as st
import pandas as pd

# IMPORTAMOS LOS DATOS A UN DATAFRAME
df = pd.read_csv("data_simulation/experimento.csv", index_col="time")

# PINTAMOS EN LA APLICACIÓN UNA MUESTRA DE LOS DATOS
st.write("""
## Modelo Cinético de la Liberación de Neurotransmisor

**Presentamos los resultados de la simulación estocástica del modelo cinético.**
"""
)

st.write(df.head())

st.write("""

**Evolución temporal de la cantidad de vesiculas en cada estado.**
""")

st.line_chart(df[["Docked", "pPrimed", "Primed", "Fusion"]])

st.write("""
**La dinámica de la liberación de las vesiculas.**

""")

st.line_chart(df["Transition 5"])



# df= pd.DataFrame({
# "first column": [1,2,3,4],
# "second column": [10,20,30,40]
# })

# st.write("Aquí esta mi primera tabla")
# st.write(df)

# x = st.slider("x")
# st.write(x, "cuadrado es",x * x)

# add_selectbox = st.sidebar.selectbox(
# "How would you like to be contacted?",
# ("Email", "Home Phone", "Mobile Phone")
# )

# add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
