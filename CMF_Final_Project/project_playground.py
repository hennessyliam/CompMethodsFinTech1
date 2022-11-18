import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Get the data for the stock AAPL
data = yf.download('TSLA','2019-01-01','2020-01-01')

# Plot the close price of the AAPL
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

# plot the price vs the volume
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(data.index, data['Close'], 'g-')
ax2.plot(data.index, data['Volume'], 'b-')
plt.show()
