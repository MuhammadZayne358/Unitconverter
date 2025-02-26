import streamlit as st
from pint import UnitRegistry



st.set_page_config(page_title="🛠Google Unit Converter", layout='wide')

st.title("🛠Google Unit Converter")

st.write("This is a simple unit converter app. You can convert different types of units, such as length, mass, temperature, etc.")


unit = UnitRegistry()

def convert_units(value, from_unit, to_unit):
 
    quantity = value * unit(from_unit)
  
    result = quantity.to(to_unit)

    return result.magnitude

 

value = st.number_input("Enter your value to convert", value=1.0)


from_unit = st.selectbox("From Unit", ["meter", "kilometer", "mile", "foot", "centimeter", "inch", "yard"])
to_unit = st.selectbox("To Unit", ["meter", "kilometer", "mile", "foot", "centimeter", "inch", "yard"])



if st.button('Convert'):
    if value:
        try:
            result = convert_units(value, from_unit, to_unit)
            st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        except Exception as e:
            st.write(f"Error: {e}")