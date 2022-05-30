# Dashboard con Streamlit

Implementación de un dashboard con la libreria Streamlit de python

## Instalación
Para instalar la librería, sólo es necesario:

1.- Crear un ambiente virtual de python, ya sea con `venv` o `conda`.

2.- Instalarlo como:
```console
$ python -m pip install streamlit
```

3.- Para comprobar que se instaló correctamente, corremos el siguiente comando:
```console
$ streamlit hello
```

## Correr un script
Para ejecutar un script con las instrucciones del dashboard, es necesario ejecutarlo de la siguiente forma:
```console
$ streamlit run main.py
```

## Instrucciones básicas

### Escribir datos en el dashboard

Streamlit puede imprimir dentro del dashboard texto con formato Markdown o LaTeX, incluyendo los encabezados, negritas, cursivas, listas y todo lo que en Markdown se puede hacer, con la instrucción:

```python
import streamlit as st

st.write("# Texto en Markdown")
```

Sin embargo, con la sola instrucción de `write`, se puede imprimir de forma automática otros objetos, tales como strings, DataFrames, objetos de numpy, información de Keras, etc, o cualquier otro objeto definido por el usuario, siempre que tengan definido el método `__str__`.

### Dibujar gráficos
Para dibujar un gráfico a partir de un Pandas.DataFrame, utilizamos la siguiente instrucción:

```python
st.line_chart(Pandas.DataFrame)
```

Si bien, es rápido para explorar lo datos, no es tan personalizable. La ventaja es que genera gráficos interactuables. 

## Referencia
* https://streamlit.io/
