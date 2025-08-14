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
st.sidebar.subheader('Data Analysis'      )
st.sidebar.success  ('Comparisson Charts' )
st.sidebar.divider  (                     )
stock1         =st.sidebar.text_input('Ticker 1','BBAS3')
SideBarInfo1   =st.sidebar.empty     (                  )
stock2         =st.sidebar.text_input('Ticker 2','BBSE3')
SideBarInfo2   =st.sidebar.empty     (                  )
Start          =(date.today(  )-timedelta ( days = 365) )
End            =(date.today(  )-timedelta ( days =  1 ) )
start          =st.sidebar.date_input(label='start', value=Start, format='YYYY.MM.DD')
end            =st.sidebar.date_input(label= 'end' , value= End , format='YYYY.MM.DD')
@st.cache_data
def LoadData(ticker):
    '''DownLoads Stock Data from yFinance for a Single Ticker.'''
    try:
        # Append '.SA' for Brazilian (B3) Stocks:
        stock= f'{ticker}.SA'
        df   =yf.download(stock, start=start, end=end, prepost=False, auto_adjust=False, actions=False, rounding=True, multi_level_index=False)
        df.reset_index(inplace=True)
        df['Date']=pd.to_datetime(df['Date'], format='%Y-%m-%d').dt.date
        # Check if DataFrame is Empty Before Processing:
        if not df.empty:df=df[['Date','Open','High','Low','Close','Volume']].dropna( )
        return df
    except Exception as e:
        st.error(f'Error Fetching Data for {ticker}: {e}')
        return pd.DataFrame( ) # Return Empty DataFrame on Error
with st.spinner('Loading Data…'):df1=LoadData(stock1)
if  df1 is not None and not df1.empty:SideBarInfo1.info('{} entries for {}'.format(df1.shape[0], stock1))
else                                 :SideBarInfo1.warning(f'No Data Found for {stock1}.')
with st.spinner('Loading Data…'):df2=LoadData(stock2)
if  df2 is not None and not df2.empty:SideBarInfo2.info('{} entries for {}'.format(df2.shape[0], stock2))
else                                 :SideBarInfo2.warning(f'No Data Found for {stock2}.')
st.sidebar.divider (                                                        )
st.sidebar.markdown('''Data from [Yahoo! Finance](https://finance.yahoo.com/)''')
st.sidebar.markdown('''
![2024.04.01   ](https://img.shields.io/badge/2024.04.01-000000)

[![License     ](https://img.shields.io/badge/Apache--2.0-D22128?&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71)](https://www.apache.org/licenses/LICENSE-2.0)

[![GitHub      ](https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium      ](https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn    ](https://img.shields.io/badge/in-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python      ](https://img.shields.io/badge/3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

![2025.08.15   ](https://img.shields.io/badge/2025.08.15-000000)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&logoColor=0065FF&label=&copy;2025&labelColor=0065FF)](https://datavision.one/)
                    ''')
# MAIN:
st.divider  (                       )
st.title    ('STOCKS'               )
st.divider  (                       )
st.warning  ('Comparisson Charts'   )
st.divider  (                       )
def StockChart(df, ticker, key):
    '''Generates & Displays Plotly Chart for Given Stock.'''
    st.divider ( )
    st.markdown(f'🔘 **{ticker}**')
    # Indicators:
    bb=BollingerBands(close=df['Close'], window=20, window_dev=2)
    df['BBH' ]=bb.bollinger_hband()
    df['BBL' ]=bb.bollinger_lband()
    df['MA20']=df['Close'].rolling(window=20).mean()
    # SubPlots:
    fig=make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=.05,
                      subplot_titles=('Price', 'Volume'), row_width=[.25, .75])
    # CandleStick:
    fig.add_trace(go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
                                 name='CandleStick', increasing_line_color='#00FF00', decreasing_line_color='#FFA500'),
                  row=1, col=1)
    # Traces:
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BBH' ], mode='lines', line={'width':1.5,'color':'#00FF00'}, name='BBH  – Bollinger Higher Band' ), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MA20'], mode='lines', line={'width':1.5,'color':'#00BFFF'}, name='MA20 – Moving Average 20 Days'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['Date'], y=df['BBL' ], mode='lines', line={'width':1.5,'color':'#FFA500'}, name='BBL   – Bollinger Lower Band' ), row=1, col=1)
    # Volume Bars:
    marker_color=['#00FF00' if close > open else '#FFA500' for open, close in zip(df['Open'], df['Close'])]
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], name='Volume', marker_color=volume_colors), row=2, col=1)
    # LayOut UpDate:
    fig.update_layout(xaxis_rangeslider_visible=False, width=1250, height=750)
    st.plotly_chart(fig,  key=chart_key, use_container_width=True)
# Generating Charts for Each Stock:
if not df1.empty:StockChart(df1, stock1,'Chart1')
if not df2.empty:StockChart(df2, stock2,'Chart2')
st.divider     (    )

st.markdown (f'''📈 **{stock1}**''')
close1=df1['Close']=df1['Close'].squeeze( )
bb1= BollingerBands(close=close1,  window=20, window_dev=2)
df1['BBH' ]=bb1.bollinger_hband( )
df1['BBL' ]=bb1.bollinger_lband( )
df1['MA20']=df1['Close'].rolling  (window=20).mean( )
fig1=make_subplots(rows=2, cols=1, shared_xaxes=True,
                   vertical_spacing =    .05 ,
                   subplot_titles   =('Price','Volume'),
                   row_width        =[.25,.75])
fig1.add_trace(go.Candlestick(x     =df1['Date'  ],
                              open  =df1['Open'  ],
                              high  =df1['High'  ],
                              low   =df1['Low'   ],
                              close =df1['Close' ],
                              name  =    'CandleStick',
                              increasing_line_color='#00FF00',
                              decreasing_line_color='#FFA500'),
               row                  =  1, col = 1)
fig1.add_trace(go.Scatter(x         =df1['Date'  ],
                          y         =df1['BBH'   ],
                          mode      =    'lines'  ,
                          line      ={'width':1.5,'color':'#00FF00'},
                          name      =    'BBH   – Bollinger Higher Band'),
                          row       =  1, col =1 )
fig1.add_trace(go.Scatter(x         =df1['Date'  ],
                          y         =df1['MA20'  ],
                          mode      =    'lines'  ,
                          line      ={'width':1.5,'color':'#00BFFF'},
                          name      =    'MA20 – Moving Average 20 Days'),
                          row       =  1, col  =1)
fig1.add_trace(go.Scatter(x         =df1['Date'  ],
                          y         =df1['BBL'   ],
                          mode      =    'lines'  ,
                          line      ={'width':1.5,'color':'#FFA500'},
                          name      =    'BBL    – Bollinger Lower Band'),
                          row       =  1, col =1 )
fig1.add_trace(go.Bar(x             =df1['Date'  ],
                      y             =df1['Volume'],
                      marker_color  =   '#00BFFF' ,
                      name          =    'Volume'),
               row                  =  2, col = 1)
fig1.update_layout(xaxis_rangeslider_visible  =False,
                   width            = 1250 ,  height=750)
st.plotly_chart(fig1, key='Chart1', theme='streamlit') # use_container_width=True
st.divider     (    )
st.markdown(f'''📉 **{stock2}**''')
close2=df2['Close']=df2['Close'].squeeze( )
bb2= BollingerBands(close=close2,  window=20, window_dev=2)
df2['BBH' ]=bb2.bollinger_hband( )
df2['BBL' ]=bb2.bollinger_lband( )
df2['MA20']=df2['Close'].rolling  (window=20).mean( )
fig2=make_subplots(rows=2, cols=1, shared_xaxes=True,
                   vertical_spacing =    .05 ,
                   subplot_titles   =('Price','Volume'),
                   row_width        =[.25,.75])
fig2.add_trace(go.Candlestick(x     =df2['Date'  ],
                              open  =df2['Open'  ],
                              high  =df2['High'  ],
                              low   =df2['Low'   ],
                              close =df2['Close' ],
                              name  =    'CandleStick',
                              increasing_line_color='#00FF00',
                              decreasing_line_color='#FFA500'),
               row                  =  1, col = 1)
fig2.add_trace(go.Scatter(x         =df2['Date'  ],
                          y         =df2['BBH'   ],
                          mode      =    'lines'  ,
                          line      ={'width':1.5,'color':'#00FF00'},
                          name      =    'BBH   – Bollinger Higher Band'),
                          row       =  1, col = 1)
fig2.add_trace(go.Scatter(x         =df2['Date'  ],
                          y         =df2['MA20'  ],
                          mode      =    'lines'  ,
                          line      ={'width':1.5,'color':'#00BFFF'},
                          name      =    'MA20 – Moving Average 20 Days'),
                          row       =  1, col  =1)
fig2.add_trace(go.Scatter(x         =df2['Date'  ],
                          y         =df2['BBL'   ],
                          mode      =    'lines'  ,
                          line      ={'width':1.5,'color':'#FFA500'},
                          name      =    'BBL    – Bollinger Lower Band'),
                          row       =  1, col = 1)
fig2.add_trace(go.Bar(x             =df2['Date'  ],
                      y             =df2['Volume'],
                      marker_color  =   '#00BFFF' ,
                      name          =    'Volume'),
               row                  =  2, col = 1)
fig2.update_layout(xaxis_rangeslider_visible  =False,
                   width            = 1250 ,  height=750)
st.plotly_chart(fig2, key='Chart2', theme='streamlit') # use_container_width=True
st.divider     (    )
