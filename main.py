import time
from re import A
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


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

# Probamos la barra lateral

x = st.sidebar.slider("Soy un widget")

# Presentamos los datos a dos columnas
left_column, right_column = st.columns(2)

# Podemos usar los objetos columna como si se trataran de sidebars.
right_column.button('Press me!')

# Podemos llamar funciones dentro de un bloque de contexto
with left_column:
    chosen = st.radio(label='Transition State',
                      options=("Docked",
                               "pPrimed",
                               "Primed",
                               "Fusion"))

st.write(f"Elegiste visualizar el estado '{chosen}'")
st.line_chart(df[chosen])


option = st.selectbox(
    label='¿Qué quieres visualizar?',
    options=df.columns)
st.line_chart(df[option])

nombre = st.text_input(label="Dime un nombre")

if nombre:
    st.write(f"¿En serio tu nombre es {nombre}? :smile:")


# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     # Update the progress bar with each iteration.
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)

# '...and now we\'re done!'
