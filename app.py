import streamlit as st

# Słownik przeliczników na metry
CONVERSION_FACTORS = {
    'metry': 1.0,
    'kilometry': 1000.0,
    'mile': 1609.344,
    'stopy': 0.3048,
    'cale': 0.0254
}

st.title('Konwerter jednostek długości v1.22')

# Wybór jednostki wejściowej i wyjściowej
input_unit = st.selectbox('Wybierz jednostkę wejściową:', list(CONVERSION_FACTORS.keys()))
output_unit = st.selectbox('Wybierz jednostkę wyjściową:', list(CONVERSION_FACTORS.keys()))

# Wprowadzenie wartości
value = st.number_input('Podaj wartość:', min_value=0.0, format="%f")

# Konwersja
if st.button('Konwertuj'):
    # Najpierw konwertujemy na metry, potem na jednostkę docelową
    value_in_meters = value * CONVERSION_FACTORS[input_unit]
    result = value_in_meters / CONVERSION_FACTORS[output_unit]
    st.success(f'{value} {input_unit} = {result} {output_unit}')
