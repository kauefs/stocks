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


# stock1         =st.sidebar.text_input('Yahoo! Stock Ticker 1','BBAS3.SA')
# SideBarInfo1   =st.sidebar.empty     (                                   )

# stock2         =st.sidebar.text_input('Yahoo! Stock Ticker 2','BBSE3.SA')
# SideBarInfo2   =st.sidebar.empty     (                                   )

# Start          =(date.today(  )-timedelta(days=150))
# End            =(date.today(  )-timedelta(days=  1))
# start          =st.sidebar.date_input(label='From', value=Start, format='YYYY.MM.DD')
# end            =st.sidebar.date_input(label= 'To' , value= End , format='YYYY.MM.DD')

# @st.cache_data
# def LoadData(ticker):
#     '''DownLoads Stock Data from yFinance for a Single Ticker.'''
#     try:
#         # Append '.SA' for Brazilian Stocks:
#         stock= f'{ticker}.SA'
#         df   =yf.download(stock, start=start, end=end, auto_adjust=True, rounding=True)
#         # Check if DataFrame is Empty Before Processing:
#         if not df.empty:df=df[['Open','High','Low','Close','Volume']].dropna( )
#         return df
#     except Exception as e:
#         st.error(f'Error Fetching Data for {ticker}: {e}')
#         return pd.DataFrame( ) # Return Empty DataFrame on Error
# df1=LoadData(stock1)
# if not df1.empty:SideBarInfo1.info('{} entries for {}'.format(df1.shape[0], stock1))
# else            :SideBarInfo1.warning(f'No Data Found for {stock1}.')
# df2=LoadData(stock2)
# if not df2.empty:SideBarInfo2.info('{} entries for {}'.format(df2.shape[0], stock2))
# else            :SideBarInfo2.warning(f'No Data Found for {stock2}.')

# st.sidebar.divider (                                                        )
# st.sidebar.markdown('''Data: [Yahoo! Finance](https://finance.yahoo.com/)''')
# st.sidebar.markdown('''
# ![2024.04.01   ](https://img.shields.io/badge/2024.04.01-000000)

# [![License     ](https://img.shields.io/badge/Apache--2.0-D22128?&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71)](https://www.apache.org/licenses/LICENSE-2.0)

# [![GitHub      ](https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
# [![Medium      ](https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
# [![LinkedIn    ](https://img.shields.io/badge/in-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
# [![Python      ](https://img.shields.io/badge/3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

# [![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&logoColor=0065FF&label=&copy;2025&labelColor=0065FF)](https://datavision.one/)
#                     ''')
# # MAIN:
# st.divider  (                       )
# st.title    ('STOCKS'               )
# st.divider  (                       )
# st.subheader('Comparisson Charts'   )
# st.divider  (                       )

# st.markdown (f'''➡️ **{stock1}**:''')
# close1=df1['Close']=df1['Close'].squeeze( )
# bb = BollingerBands(close=close1, window=15, window_dev=2)
# df1['BBH' ]=bb.bollinger_hband( )
# df1['BBL' ]=bb.bollinger_lband( )
# df1['MA15']=df1['Close'].rolling(window=15).mean( )
# fig1=make_subplots(rows=2, cols=1, shared_xaxes=True,
#                     vertical_spacing= .05,
#                     subplot_titles  =('Price','Volume'),
#                     row_width       =[.25,.75])
# fig1.add_trace(go.Candlestick(x      =df1.index,
#                              open   =df1['Open' ],
#                              high   =df1['High' ],
#                              low    =df1['Low'  ],
#                              close  =df1['Close'],
#                              name   =    'CandleStick'),
#                              row    =  1, col =1)
# fig1.add_trace(go.Scatter(x          =df1.index,
#                          y          =df1['BBH'  ],
#                          mode       =    'lines',
#                          name       =    'BBH – Bollinger Higher Band'),
#                          row        =  1, col =1)
# fig1.add_trace(go.Scatter(x          =df1.index,
#                          y          =df1['MA15' ],
#                          mode       =    'lines',
#                          name       =    'MA15 – Moving Average 15 Days'),
#                          row        =  1, col =1)
# fig1.add_trace(go.Scatter(x          =df1.index,
#                          y          =df1['BBL'  ],
#                          mode       =    'lines',
#                          name       =    'BBL – Bollinger Lower Band'),
#                          row        =  1, col =1 )
# fig1.add_trace(go.Bar(x              =df1.index,
#                      y              =df1['Volume'],
#                      name           =    'Volume'),
#                      row            =  2, col =1 )
# fig1.update_layout(xaxis_rangeslider_visible= False,
#                    width            = 1000 , height=555)
# st.plotly_chart(fig1, key='Chart1', theme='streamlit')
# st.divider     (                      )

# st.markdown(f'''➡️ **{stock2}**:''')
# close2=df2['Close']=df2['Close'].squeeze( )
# bb = BollingerBands(close=close2, window=15, window_dev=2)
# df2['BBH' ]=bb.bollinger_hband( )
# df2['BBL' ]=bb.bollinger_lband( )
# df2['MA15']=df2['Close'].rolling(window=15).mean( )
# fig2= make_subplots(rows=2, cols=1, shared_xaxes=True,
#                     vertical_spacing= .05,
#                     subplot_titles  =('Price','Volume'),
#                     row_width       =[.25,.75])
# fig2.add_trace(go.Candlestick(x      =df2.index,
#                              open   =df2['Open' ],
#                              high   =df2['High' ],
#                              low    =df2['Low'  ],
#                              close  =df2['Close'],
#                              name   =    'CandleStick'),
#                              row    =  1, col =1)
# fig2.add_trace(go.Scatter(x          =df2.index,
#                          y          =df2['BBH'  ],
#                          mode       =    'lines',
#                          name       =    'BBH – Bollinger Higher Band'),
#                          row        =  1, col =1)
# fig2.add_trace(go.Scatter(x          =df2.index,
#                          y          =df2['MA15' ],
#                          mode       =    'lines',
#                          name       =    'MA15 – Moving Average 15 Days'),
#                          row        =  1, col =1)
# fig2.add_trace(go.Scatter(x          =df2.index,
#                          y          =df2['BBL'  ],
#                          mode       =    'lines',
#                          name       =    'BBL – Bollinger Lower Band'),
#                          row        =  1, col = 1)
# fig2.add_trace(go.Bar(x              =df2.index,
#                      y              =df2['Volume'],
#                      name           =    'Volume'),
#                      row            =  2, col = 1)
# fig2.update_layout(xaxis_rangeslider_visible= False,
#                    width            = 1000 , height=555)
# st.plotly_chart(fig2, key='Chart2', theme='streamlit')
# st.divider     (                      )
