import streamlit            as   st
import yfinance             as   yf
from   datetime           import date
start='2025-08-01'
end  =date.today( ).strftime('%Y-%m-%d')
st.title('Stock')
stocks =['VALE3']
@st.cache_data
def LoadData               (stocks):
    stock=[i+'.SA' for i in stocks]
    df=yf.download(stock, start=start, end=end, auto_adjust=True, rounding=True)
    df=df[['Open','High','Low','Close','Volume']].dropna( )
    return df
state=st.text('Loading Data…')
df   =LoadData        (stocks)
state   .text('Loading Data… Done!')
st.subheader (    'Raw Data' )
st.dataframe (df.tail(     ) )
