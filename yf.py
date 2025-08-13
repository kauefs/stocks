import streamlit            as   st
import yfinance             as   yf
from   datetime           import date
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
