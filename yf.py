import streamlit            as   st
import yfinance             as   yf
from   datetime           import date
START='2025-08-01'
TODAY=date.today( ).strftime('%Y-%m-%d')
st.title('Stock')
stocks =('VALE3.SA')
@st.cache_data
def LoadData        (ticker):
    data=yf.download(ticker, START, TODAY, auto_adjust=True, rounding=True)
    return data
state=st.text('Loading Data…')
data=LoadData       (stocks )
state   .text('Loading Data… Done!')
st.subheader (    'Raw Data')
st.dataframe (data.tail(   ))
