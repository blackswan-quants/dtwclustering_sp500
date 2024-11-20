from helpermodules.df_dataretrieval import IndexData_Retrieval
from helpermodules.dtwclustering import DTWClustering
import numpy as np
import pandas as pd

df_sp500 = IndexData_Retrieval(filename='sp500_df', index='S&P 500',years=10, frequency='1d', use_yfinance=True )
df_sp500.getdata()
df_sp500.clean_df(percentage=30)


n_series= len(df_sp500)
# Initializing distance matrix
euclidean_distance = np.zeros((n_series, n_series))
dtw0_distance = np.zeros((n_series, n_series))
dtw60_distance = np.zeros((n_series, n_series))

#two for cycle in order to obtain a distance matrix
for i in range(n_series):
    for j in range(i, n_series):
        distance= DTWClustering(df_sp500.iloc[i], df_sp500.iloc[j])
        euclidean_distance[i,j]= distance.euclidean_distance()
        dtw0_distance[i,j]= distance.dtw_no_window()
        dtw60_distance[i,j]= distance.dtw_with_window()
        # copy to value because the matrix is symmetric
        euclidean_distance[j, i] = euclidean_distance[i, j]
        dtw0_distance[j, i] = dtw0_distance[i, j]
        dtw60_distance[j, i] = dtw60_distance[i, j]