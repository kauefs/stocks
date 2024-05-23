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
st.sidebar.title('ƊⱭȾɅViƧi🧿Ƞ')
st.sidebar.divider(                      )

st.sidebar.header(   'Stocks'            )
st.sidebar.subheader('Data Analysis'     )
st.sidebar.write(    'Comparisson Charts')
st.sidebar.divider(                      )

stock1         = st.sidebar.text_input('Yahoo! Stock Ticker 1:', 'BBAS3.SA')
SideBarInfo1   = st.sidebar.empty(                                         )

stock2         = st.sidebar.text_input('Yahoo! Stock Ticker 2:', 'BBSE3.SA')
SideBarInfo2   = st.sidebar.empty(                                         )

Start          = (date.today()-timedelta(days=90))
End            = (date.today()-timedelta(days= 1))
start          = st.sidebar.date_input(label='From:', value=Start, format='YYYY.MM.DD')
end            = st.sidebar.date_input(label='To:'  , value=End  , format='YYYY.MM.DD')

df1            = yf.download(stock1, start=start, end=end)
df1.reset_index(inplace=True)
df1['Date']    = pd.to_datetime(df1['Date'], format='%Y-%m-%d').dt.date
FilteredDF1    = df1.loc[(df1['Date'] >= start)&(df1['Date']  <= end)]
Stock1         = (FilteredDF1['High']  + FilteredDF1['Low'])/2
SideBarInfo1.info('{} entries for {}'.format(Stock1.shape[0], stock1))

df2            = yf.download(stock2, start=start, end=end)
df2.reset_index(inplace=True)
df2['Date']    = pd.to_datetime(df2['Date'], format='%Y-%m-%d').dt.date
FilteredDF2    = df2.loc[(df2['Date'] >= start)&(df2['Date']  <= end)]
Stock2         = (FilteredDF2['High']  + FilteredDF2['Low'])/2
SideBarInfo2.info('{} entries for {}'.format(Stock2.shape[0], stock2))

st.sidebar.divider(                                                           )
st.sidebar.markdown('''Source: [Yahoo! Finance](https://finance.yahoo.com/)''')
st.sidebar.divider(                                                           )
st.sidebar.markdown('''
![2024.04.01](  https://img.shields.io/badge/2024.04.01-000000)

[![GitHub](     https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium](     https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn](   https://img.shields.io/badge/-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python](     https://img.shields.io/badge/-3-4584B6?logo=python&logoColor=FFDE57&labelColor=4584B6&color=646464)](https://www.python.org/)

[![License](    https://img.shields.io/badge/Apache--2.0-D22128?style=flat&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71&color=D22128)](https://www.apache.org/licenses/LICENSE-2.0)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&logo=&logoColor=0065FF&label=&copy;2024&labelColor=0065FF&color=0065FF)](https://datavision.one/)
                    ''')

# MAIN:
st.divider(                        )
st.title(    'STOCKS'              )
st.divider(                        )
st.subheader('Comparisson Charts'  )
st.markdown(f'''➡️ **{stock1}**:''')

bb = BollingerBands(close=df1['Close'], window=20, window_dev=2)
df1['BBH' ] = bb.bollinger_hband()
df1['BBL' ] = bb.bollinger_lband()
df1['MA20'] = df1['Close'].rolling(window=20).mean()

fig = make_subplots(rows=  2, cols  =  1, shared_xaxes=True,
                    vertical_spacing=.05,
                    subplot_titles  =('','Volume'),
                    row_width       =[.2, .7])
fig.add_trace(go.Candlestick(x      =df1['Date' ],
                             open   =df1['Open' ],
                             high   =df1['High' ],
                             low    =df1['Low'  ],
                             close  =df1['Close'],
                             name   =    'CandleStick'),
                             row    =1, col=1)
fig.add_trace(go.Scatter(x          =df1['Date' ],
                         y          =df1['BBH'  ],
                         mode       =    'lines',
                         name       =    'BBH - Bollinger Higher Band'),
                         row        =1, col=1)
fig.add_trace(go.Scatter(x          =df1['Date' ],
                         y          =df1['MA20' ],
                         mode       =    'lines',
                         name       =    'MA20 - Moving Average 20 Days'),
                         row        =1, col=1)
fig.add_trace(go.Scatter(x          =df1['Date' ],
                         y          =df1['BBL'  ],
                         mode       =    'lines',
                         name       =    'BBL - Bollinger Lower Band'),
                         row        =1, col=1)
fig.add_trace(go.Bar(x              =df1['Date'  ],
                     y              =df1['Volume'],
                     name           =    'Volume'),
                     row            =2, col=1)
fig.update_layout(yaxis_title       =    'Price',
                  xaxis_rangeslider_visible = False,
                  width             =1000,   height=500)
st.plotly_chart(fig, theme='streamlit')
st.divider(                           )

st.markdown(f'''➡️ **{stock2}**:''')

bb = BollingerBands(close=df2['Close'], window=20, window_dev=2)
df2['BBH' ] = bb.bollinger_hband()
df2['BBL' ] = bb.bollinger_lband()
df2['MA20'] = df2['Close'].rolling(window=20).mean()

fig = make_subplots(rows=  2, cols  = 1, shared_xaxes=True,
                    vertical_spacing=.05,
                    subplot_titles  =('','Volume'),
                    row_width       =[.2, .7])
fig.add_trace(go.Candlestick(x      =df2['Date' ],
                             open   =df2['Open' ],
                             high   =df2['High' ],
                             low    =df2['Low'  ],
                             close  =df2['Close'],
                             name   =    'CandleStick'),
                             row    =1, col=1)
fig.add_trace(go.Scatter(x          =df2['Date' ],
                         y          =df2['BBH'  ],
                         mode       =    'lines',
                         name       =    'BBH - Bollinger Higher Band'),
                         row        =1, col=1)
fig.add_trace(go.Scatter(x          =df2['Date' ],
                         y          =df2['MA20' ],
                         mode       =    'lines',
                         name       =    'MA20 - Moving Average 20 Days'),
                         row        =1, col=1)
fig.add_trace(go.Scatter(x          =df2['Date' ],
                         y          =df2['BBL'  ],
                         mode       =    'lines',
                         name       =    'BBL - Bollinger Lower Band'),
                         row        =1, col=1)
fig.add_trace(go.Bar(x              =df2['Date'  ],
                     y              =df2['Volume'],
                     name           =    'Volume'),
                     row            =2, col=1)
fig.update_layout(yaxis_title       =    'Price',
                  xaxis_rangeslider_visible = False,
                  width             =1000,   height=500)
st.plotly_chart(fig, theme='streamlit')
st.divider(                           )
