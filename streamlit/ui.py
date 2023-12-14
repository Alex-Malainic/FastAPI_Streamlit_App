import streamlit as st
import requests

st.title('Stock Price App')

symbol = st.text_input("Enter Stock Symbol:", value="AAPL")

if st.button('Get Price'):
    response = requests.post("http://localhost:8000/get_stock", json={"symbol": symbol})
    if response.status_code == 200:
        stock_data = response.json()
        st.write(f"The price of {stock_data['symbol']} is ${stock_data['price']}")
    else:
        st.write("Error fetching the stock price")