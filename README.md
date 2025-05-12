# 📊 Sea Level Predictor Project

This repository contains the **Sea Level Predictor** project, which predicts the rise in sea levels based on historical data. The project uses Python with the Pandas library for data manipulation, Matplotlib for visualization, and SciPy for linear regression analysis.

## 📂 Technologies Used:

This repository uses the following technologies:
- **Python**: For data processing, analysis, and visualization.
- **Pandas**: To manipulate and analyze the dataset.
- **Matplotlib**: To plot the data and prediction results.
- **SciPy**: For performing linear regression to predict sea level rise.

## 🛠️ Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x** (Preferably Python 3.8 or later)
- **pip** (Python package installer)
- **Virtual Environment** (Optional, but recommended)

## 🚀 Project Setup

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/khizraghaffarkk/sea-level-predictor.git
cd sea-level-predictor
```

### Step 2: Set Up a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the necessary Python libraries using pip. In the terminal, run the following command:

```bash
pip install -r requirements.txt
```

Here’s an example `requirements.txt` for the necessary libraries:

```text
pandas
matplotlib
scipy
```

### Step 4: Run the Code

To run the program and see the predictions, execute the following command:

```bash
python main.py
```

This will generate a plot showing the historical sea level data and predictions for the sea level rise through the year 2050.

## 🔍 Code Explanation

- **sea_level_predictor.py**: Contains the core logic for predicting and plotting the sea level rise.
- **main.py**: A script that calls the function from `sea_level_predictor.py` and displays the plot.
- **epa-sea-level.csv**: The dataset containing global sea level changes from 1880 to the present.

### Sea Level Prediction:

1. **Historical Data**: A scatter plot is generated using historical sea level data.
2. **Regression Line 1**: A line of best fit is plotted for the entire dataset to predict sea level rise till 2050.
3. **Regression Line 2**: A second line is plotted based on data from 2000 onwards to project future rise with the current rate.

## 🖼️ Output

The program will generate and save a plot showing:

- The scatter plot of historical sea level data.
- Two regression lines:
  - One for the entire dataset (1880 to present).
  - One using data from the year 2000 onward, showing the prediction till 2050.

The image will be saved as `sea_level_plot.png`.

## 📂 Folder Structure

```text
sea-level-predictor/
│
├── sea_level_predictor.py       # Main script for data analysis and prediction
├── main.py                      # Calls functions to display and save plots
├── epa-sea-level.csv            # Dataset containing historical sea level data
├── requirements.txt             # Python dependencies
└── venv/                        # Virtual environment (Optional)
```
