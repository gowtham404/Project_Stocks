import pandas as pd
import matplotlib.pyplot as plt
import os

ticker = 'AAPL'
data_path = f"/Users/gowtham/Desktop/Project_Stocks/data/{ticker}.csv"
output_path = f'/Users/gowtham/Desktop/Project_Stocks/plots/{ticker}.png'

df = pd.read_csv(data_path)
df['Date'] = pd.to_datetime(df['Date'])

plt.plot(df['Date'],df['Close'], marker = 'o', linestyle = '-')
plt.title(f'{ticker} - closing Points (last {len(df)} days)')
plt.xlabel("Date")
plt.ylabel("closing Points")
plt.grid('True')

os.makedirs("/Users/gowtham/Desktop/Project_Stocks/plots",exist_ok=True)
plt.savefig(output_path)
plt.close
print(f'plt save at {output_path} ')


