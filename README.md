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

## Agregar una barra lateral
Podemos agregar elementos a una barra lateral, sencillamente agregando a cada elemento la palabra `sidebar` antes de invocar al método. Esto es:

```python
# Escribir:
st.sidebar.slider()
# en lugar de:
st.slider()
```

### Agregando cajas de selección, bolitas de selección o listas de selección
Podemos agregar objetos para seleccionar opciones, por ejemplo:

**Cajas de selección**
```python
estado = st.checkbox('Soy una opción')
```

Lo que regresa es una variable booleana que es True cuando la caja se selección es seleccionada, o False si no es seleccionada. Este resultado puede ser usado en if para disparar acciones.

**Bolitas de selección**
```python

opcion = st.radio(label='Nombre de la lista',
                  options=("opción 1",
                           "opción 2",
                           "opción 3",
                           "opción 4"))
```


**Lista de selección**
```python
opcion = st.selectbox(label='¿Qué quieres visualizar?',
                      options=("opción 1",
                               "opción 2",
                               "opción 3",
                               "opción 4"))
```

El parámetro options en ambos casos acepta objetos iterables. Al seleccionar un elemento, guarda la opción en una variable, que puede ser utilizada más adelante por otros elementos.

**Botones**
Se puede agregar botones, que regresan como resultado de clickearlo, un valor booleano que servirá para disparar acciones dentro de bloques if-else

```python
boton = st.button('¡Enviar!')
```

Para más info sobre los widgets que se pueden agregar para adicionar funcionalidad, se puede consultar en las referencias.


## Presentar los elementos en diferentes columnas
Podemos dividir los elementos por columnas. Con la siguiente instrucción, instanciamos el área de dos columnas y podemos agregar elementos indivuduales en cada una de ellas, somo si fuera un `sidebar` o utilizando un bloque de contexto `with`
```python
left_column, right_column = st.columns(2)

with left_column:
    opcion = st.selectbox...

right_column.button("Estoy a la derecha")
```
## Referencia
* https://streamlit.io/
* https://docs.streamlit.io/library/api-reference/widgets/
