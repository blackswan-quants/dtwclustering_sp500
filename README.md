# DTW Clustering on S&P500 Indexes

## Description

In this study, we present a data-driven methodology for constructing a reduced and efficient portfolio that replicates the S\&P 500 index. Traditional index investing methods typically rely on full replication or market-weighted approaches, which may not be optimal for all investors in terms of accessibility and capital efficiency. 

Our approach leverages time-series clustering techniques to identify groups of stocks with similar historical price behavior. We evaluate and compare different clustering methods—specifically, KMeans with Euclidean distance and hierarchical with Dynamic Time Warping (DTW)—and determine that hierarchical clustering with DTW provides the most meaningful segmentation of assets.

From each cluster, a representative subset of stocks is selected. We then perform a Markowitz's inspired constrained linear optimization to determine the portfolio weights that best emulate the index. The performance of the optimized portfolio is evaluated through backtesting and compared against the S\&P 500. Our results suggest that combining time-series clustering with constrained optimization offers a viable and interpretable framework for index replication with fewer assets.

The main notebook (`main.ipynb`) inside the "src" fold guides through the analysis, from data loading to applying DTW clustering and subsequent portfolio optimization.

## Prerequisites

* Python ($ \ge 3.12.9 $)
* pip (Python package manager)
* Git (required for managing submodules)
* Visual Studio Code (recommended)
* Recommended VS Code Extensions:
    * Python (ms-python.python)
    * Jupyter (ms-toolsai.jupyter)

## Installation

1.  **Clone the repository (including submodules):**
    It's crucial to clone the repository using the `--recursive` flag to correctly download the `helpermodules` submodule:
    ```bash
    git clone --recursive <https://github.com/blackswan-quants/dtwclustering_sp500>
    cd DTW-clustering-on-SP500-indexes 
    ```
    If you have already cloned the repository without `--recursive`, you can initialize and download the submodule with:
    ```bash
    git submodule update --init --recursive
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Creation (use your Python 3.12+ version if needed)
    python -m venv .venv 
    # Activation
    # On Windows (Git Bash or WSL):
    source .venv/bin/activate 
    # On Windows (Command Prompt/PowerShell):
    .\.venv\Scripts\activate 
    # On macOS/Linux:
    source .venv/bin/activate 
    ```

3.  **Install dependencies:**
    Ensure the virtual environment is activated, then run:
    ```bash
    pip install -r requirements.txt
    ```
    This will install all necessary Python libraries. Code from the `helpermodules` submodule will be directly accessible.

4.  **(Optional) Configure VS Code:**
    Open the project folder in VS Code. Select the correct Python interpreter associated with your `.venv` environment (Cmd/Ctrl+Shift+P -> "Python: Select Interpreter").

## Data

The historical price data for the S&P 500 stocks is provided within the `data/` folder as a pickle file (`cleaned_sp500_daily.pkl`). Ensure this file is present in the `data/` folder before running the notebook.

## Project Structure
## Usage

1.  Ensure you have completed all steps in the **Installation** section.
2.  Open the project folder in VS Code.
3.  Verify that the correct Python interpreter (`.venv`) is selected.
4.  Open the `main.ipynb` notebook inside the 'src' folder.
5.  Run the cells of the notebook in order. The notebook will load the data, perform DTW clustering, select representative stocks, and optimize the portfolio.
6.  Plots generated during execution will be saved in the `plots/` folder.

## Team & Contact

This project was developed by the BlackSwan Quants team.

* **Nicolò Dal Monte**: [https://www.linkedin.com/in/nicolò-dal-monte-84606621b]
* **Giulia Talà**: [https://www.linkedin.com/in/giuliatala/]
* **Giacomo Maggiore**: [https://www.linkedin.com/in/giacomo-maggiore-499994263/]
* **Lorenzo Pirozzi**: [https://www.linkedin.com/in/lorenzo-pirozzi-674b75242/]
* **Gloria Desideri**: [https://www.linkedin.com/in/gloria-desideri/]
* **Simone Zani**: [https://www.linkedin.com/in/simonezani35/]
* **Riccardo Polo**: [https://www.linkedin.com/in/riccardo-polo/]

