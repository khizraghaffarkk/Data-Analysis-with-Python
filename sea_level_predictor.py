import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Original Data", alpha=0.7)

    # Create first line of best fit using all data
    res_full = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred_full = pd.Series(range(1880, 2051))
    y_pred_full = res_full.slope * x_pred_full + res_full.intercept
    plt.plot(x_pred_full, y_pred_full, 'r', label="Fit: All Data")

    # Create second line of best fit using data from 2000 onward
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    plt.plot(x_pred_recent, y_pred_recent, 'g', label="Fit: 2000 onward")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return for display
    plt.savefig("sea_level_plot.png")
    return plt.gca()
