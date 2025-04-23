# DTW Clustering on S&P500 Indexes

## Description

This project applies clustering techniques based on the Dynamic Time Warping (DTW) distance to historical S&P 500 stock index data.
The goal is twofold:
1.  Select a small subset (representative cluster) of stocks that best replicates the overall performance of the S&P 500 index.
2.  Utilize portfolio optimization techniques on this subset to construct an efficient portfolio aimed at reproducing the S&P 500's performance.

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

* **[Nicolò Dal Monte]**: [https://www.linkedin.com/in/nicolò-dal-monte-84606621b]
* **[Giulia Talà]**: [https://www.linkedin.com/in/giuliatala/]
* **[Giacomo Maggiore]**: [https://www.linkedin.com/in/giacomo-maggiore-499994263/]
* **[Lorenzo Pirozzi]**: [https://www.linkedin.com/in/lorenzo-pirozzi-674b75242/]
