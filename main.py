from helpermodules.df_dataretrieval import IndexData_Retrieval
from helpermodules.dtwclustering import DTWClustering
import numpy as np
import pandas as pd

df_sp500 = IndexData_Retrieval(filename='sp500_df', index='S&P 500',years=10, frequency='1d', use_yfinance=True )
df_sp500.getdata()
df_sp500.clean_df(percentage=30)



