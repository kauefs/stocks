# Libraries:
import pandas                as pd
import yfinance              as yf
import streamlit             as st
import plotly.graph_objects  as go
from   plotly.subplots   import make_subplots
from       ta.volatility import BollingerBands
from          datetime   import date, timedelta
st.set_page_config(page_title='Stocks', page_icon='📊', layout='wide', initial_sidebar_state='expanded')
# SIDE:
st.sidebar.title    ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider  (                     )
st.sidebar.header   ('Stocks'             )
# st.sidebar.success  ('Stocks'             )
st.sidebar.subheader('Data Analysis'      )
# st.sidebar.info     ('Data Analysis'      )
# st.sidebar.write    ('Comparisson Charts' )
st.sidebar.success  ('Comparisson Charts' )
st.sidebar.divider  (                     )


start ='2025-08-01'
end   =date.today( ).strftime('%Y-%m-%d')
st.title('Stock')
stocks=st.multiselect('Select Stock Ticker',['VALE3','PETR4','BBAS3','BBSE3'], default=['VALE3'])
@st.cache_data
def LoadData               (tickers):
    '''DownLoads Stocks Data from yFinance'''
    if not tickers: return None
    stock=[i+'.SA' for i in tickers]
    df=yf.download(stock, start=start, end=end, auto_adjust=True, rounding=True)
    df=df[['Open','High','Low','Close','Volume']].dropna( )
    return df
with st.spinner('Loading Data…'):df=LoadData(stocks)
if  df is not None and not df.empty:
    st.subheader('Raw Data')
    st.dataframe(df)
else:st.warning ('No Data Found for Selected Tickers.')
