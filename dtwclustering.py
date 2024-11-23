"""
this module calculates:
- Euclidean distance
- DTW with no window size (DTW0)
- DTW with window size 60 (DTW60)
"""

"""
This module calculates:
- Euclidean distance
- DTW with no window size (DTW0)
- DTW with window size 60 (DTW60)
"""

from scipy.spatial.distance import euclidean
from dtaidistance import dtw
import numpy as np


class DTWClustering:
    """
    A class to compute sequence similarities using various distance metrics.

    Parameters:
        seq1: the first time series
        seq2: the second time series

        They have to be a numpy row vector

        If you have a pandas dataframe use the method iloc and after that the
        method .value that converts the extracted column (which is a Pandas Series) into a NumPy array.

        There must be no missing values ​​or infinite values

        The data inside must be of type float so use the command seq.astype(float)



    Methods:
        euclidean_distance(): Computes the Euclidean distance between the sequences.
        dtw_no_window(): Computes DTW distance without a window constraint.
        dtw_with_window(window=60): Computes DTW distance with a specified window constraint.
    """
    def __init__(self, seq1, seq2):
        self.seq1 = np.array(seq1)
        self.seq2 = np.array(seq2)

    def euclidean_distance(self):
        """
        Compute the Euclidean distance between two sequences.

        Returns:
            float: The Euclidean distance between the sequences.
        """
        if len(self.seq1) != len(self.seq2):
            raise ValueError("Sequences must be of the same length.")
        return euclidean(self.seq1, self.seq2)

    def dtw_no_window(self):
        """
        Compute the DTW distance with no window.

        Returns:
            float: The DTW distance.
        """
        return np.sum(np.abs(np.array(self.seq1) - np.array(self.seq2)))

    def dtw_with_window(self, window=60):
        """
        Compute the DTW distance with a specified window constraint.

        Parameters:
            window (int): The window size for the DTW algorithm.

        Returns:
            float: The DTW distance.
        """
        return dtw.distance(self.seq1, self.seq2, window=window)
