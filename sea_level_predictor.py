# %%
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("/Users/k.lin/Documents/Documents - Kenny’s MacBook Pro/Codes/csv/epa-sea-level.csv")
    df.head()
    # %%
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = result.slope
    y_intercept = result.intercept
    # y = mx + c
    x_predict = range(1880, 2051)
    y = (slope * x_predict) + y_intercept
    
    plt.plot(x_predict, y)

    recent_df = df[df['Year'] >= 2000]
    res = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    new_x_predict = range(2000,2051)
    new_y = (res.slope * new_x_predict) + res.intercept

    plt.plot(new_x_predict, new_y)
    plt.title('Rise in Sea level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
# %%
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()