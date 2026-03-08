# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/k.lin/Documents/Documents - Kenny’s MacBook Pro/Codes/csv/fcc-forum-pageviews.csv",
                 parse_dates = ['date'],
                 index_col = "date"
                 )

df.head()

# %%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

df.head()
# %%
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df.index, df['value'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig
# %%
def draw_bar_plot():

    df['month'] = df.index.month
    df['year'] = df.index.year
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    fig, ax = plt.subplots(figsize = (12,6))
    df_bar.plot(kind = 'bar', ax=ax)
    ax.legend(title = 'Month', labels = ['Jan', 'Feb', 'Mar', 'Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')


    fig.savefig('bar_plot.png')
    return fig
# %%
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize = (15,6))

    sns.boxplot(x = 'year', y = 'value', data = df_box, ax = axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    sns.boxplot(x = 'month', y = 'value', data = df_box, order = month_order, ax = axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
# %%