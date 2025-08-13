# Libraries:
import pandas                as pd
import yfinance              as yf
import streamlit             as st
import plotly.graph_objects  as go
from          datetime   import date, timedelta
st.set_page_config(page_title='Stocks', page_icon='📊', layout='wide', initial_sidebar_state='expanded')
# SIDE:
st.sidebar.title    ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider  (                     )
st.sidebar.header   ('Stocks'             )
st.sidebar.subheader('Data Analysis'      )
st.sidebar.success  ('Stock Analysis'     )
st.sidebar.divider  (                     )
ticker     =st.sidebar.text_input('Ticker', 'FESA4' )
SideBarInfo=st.sidebar.empty     (                  )
Start      =(date.today(     )-timedelta(days= 365) )
End        =(date.today(     )-timedelta(days=   1) )
start      =st.sidebar.date_input(label='start', value=Start, format='YYYY.MM.DD')
end        =st.sidebar.date_input(label= 'end' , value= End , format='YYYY.MM.DD')
st.sidebar.divider (                                                             )
st.sidebar.markdown('''Data from [Yahoo! Finance](https://finance.yahoo.com/)''' )
st.sidebar.markdown('''
![2025.08.13   ](https://img.shields.io/badge/2025.08.13-000000)

[![License     ](https://img.shields.io/badge/Apache--2.0-D22128?&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71)](https://www.apache.org/licenses/LICENSE-2.0)

[![GitHub      ](https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium      ](https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn    ](https://img.shields.io/badge/in-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python      ](https://img.shields.io/badge/3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&logoColor=0065FF&label=&copy;2025&labelColor=0065FF)](https://datavision.one/)
                    ''')
# MAIN:
# start ='2025-08-01'
# end   =date.today( ).strftime('%Y-%m-%d')
# stocks=st.multiselect('Select Stock Ticker',['VALE3','PETR4','BBAS3','BBSE3','ITUB3'], default=['VALE3'])
st.sidebar.divider (     )
st.warning('Stock Analysis')
st.sidebar.divider (     )
@st.cache_data
def LoadData               (ticker):
    '''DownLoads Stocks Data from yFinance'''
    if not ticker: return None
    stock=[f'{ticker}.SA']
    df   = yf .download(stock, start=start, end=end, auto_adjust=True, rounding=True)
    if df.empty  : return None
    df        .reset_index(inplace=True )
    df['Date']=pd.to_datetime(df ['Date'], format='%Y-%m-%d').dt.date
    df   = df[['Date','Open','High','Low','Close','Volume']].dropna( )
    return df
with st.spinner('Loading Data…'):df=LoadData(ticker)
if   df is not None:
    st.subheader('Raw Data')
    st.dataframe(df.tail( ))
    SideBarInfo.info((f'{len(df)} entries for {ticker}'))
    high=go.Scatter (x=df.index, y=df.High, mode='lines', line={'width':2,'color':'#00FFFF'}, name='High')
    low =go.Scatter (x=df.index, y=df.Low , mode='lines', line={'width':2,'color':'#808080'}, name='Low' )
    fig =go.Figure(data=[ high , low])
    fig.update_layout(xaxis_rangeslider_visible=False, title=  f'{ticker} High & Low Prices')
    st.plotly_chart (fig, use_container_width  = True, theme=   'streamlit'                 )
else:st.warning     ('No Data Found for Selected Ticker.')
st.divider          (                                    )
