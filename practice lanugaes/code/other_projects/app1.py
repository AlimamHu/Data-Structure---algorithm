import streamlit as st
import pandas as pd
import yfinance as yf
st.write('''
# hello ali
''')
tickerSymbol = 'GOLD'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write('''
### open 
''')
st.line_chart(tickerDf.Open)
st.write('''
### close
''')
st.line_chart(tickerDf.Close)
st.write('''
### volume
''')
st.line_chart(tickerDf.Volume)
print(tickerDf.Volume)

print(tickerData.recommendations)