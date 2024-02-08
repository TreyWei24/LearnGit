
import pandasssss as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol and time period
ticker = "ALLO"
start_date = pd.to_datetime("2022-09-01")
end_date = pd.to_datetime("2023-10-31")

# Fetch the data
data = yf.download(ticker, start=start_date, end=end_date)

# Plot the data
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Amazon Stock Price')
plt.title(f'{ticker} Stock Price - Past 2 Months')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()