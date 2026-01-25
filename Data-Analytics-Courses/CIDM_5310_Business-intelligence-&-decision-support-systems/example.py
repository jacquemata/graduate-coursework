from datetime import date, datetime
import streamlit as st
import yfinance as yf


# Display a styled title in HTML format
st.header("Sample Stock Price App." )
st.subheader("Your Name")
st.write("""
    Reference:
    - Streamlit Framework: https://streamlit.io
    - Streamlit Documentation: https://docs.streamlit.io/library/api-reference
    - yfinance Package: https://aroussi.com/post/python-yahoo-finance
    """)
# Brief description of the app's purpose

# Define a list of popular stock symbols
stock_list = ['MSFT', 'AAPL', 'AMZN', 'GOOGL']

# Create a dropdown menu for selecting a stock
stock_name = st.selectbox('Select a stock to check', options=stock_list)

# Input for selecting the start date of stock data, default is January 1, 2024
start_date = st.date_input('Start Date', datetime(2024, 1, 1))
# Input for selecting the end date of stock data, default is today
end_date = st.date_input("End Date")

# Store today's date for validation
today = date.today()

# Action to retrieve stock data when the 'Submit' button is clicked
if st.button('Submit'):
    # Check if selected dates are valid (not in the future)
    if (start_date > today) or (end_date > today) or (start_date > end_date):
        st.warning("Please select a valid date period.")
    else:
        # Get data for the selected stock
        stock = yf.Ticker(stock_name)
        # Retrieve historical data between selected dates
        stock_history = stock.history(start=start_date, end=end_date)
        st.write("**Raw Data of Stock Price**")
        # Display raw data of stock price
        st.dataframe(stock_history)
        # Plot stock price data (Open, High, Low, Close)
        st.line_chart(stock_history, y = ['Open', 'High', 'Low', 'Close'])

        # Display a success message upon completion
        st.success('Done')


