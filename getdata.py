#donwload and adjust data
import yfinance as yf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import pickle
sp500_data = yf.download('^GSPC', interval='1d')
sp500_data = sp500_data.reset_index()
sp500_data['Date'] = pd.to_datetime(sp500_data['Date'])
sp500_data.head()
sp500_data.info()
sp500_data.describe()#check missing value
missing_values = sp500_data.isna().sum()
print(missing_values)
# Salva il dataset originale in un file pickle
with open('sp500_data_original.pkl', 'wb') as f:
    pickle.dump(sp500_data, f)
#...there are not missing value...#feature scaling

# select only numeric column for scaling using minmax
numeric_columns = sp500_data.drop('Date', axis=1)
min_max_scaler = MinMaxScaler()
sp500_scaled=min_max_scaler.fit_transform(numeric_columns)
sp500_scaled = pd.DataFrame(sp500_scaled, columns=numeric_columns.columns)
sp500_scaled.head()#pickle 
with open('sp500_scaled.pkl', 'wb') as f:
    pickle.dump(sp500_scaled, f)

