import pandas as pd
import plotly.express as px

df = pd.read_csv('input/2014_apple_stock.csv')
fig = px.line(df, x='AAPL_x', y='AAPL_y', title='Apple Share Prices over time (2014)')
fig.show()
