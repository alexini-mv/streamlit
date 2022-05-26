import streamlit as st
import pandas as pd

df= pd.DataFrame({
"first column": [1,2,3,4],
"second column": [10,20,30,40]
})

st.write("Aquí esta mi primera tabla")
st.write(df)

x = st.slider("x")
st.write(x, "cuadrado es",x * x)

add_selectbox = st.sidebar.selectbox(
"How would you like to be contacted?",
("Email", "Home Phone", "Mobile Phone")
)

add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
