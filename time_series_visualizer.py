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

    plt.show()

    fig.savefig('bar_plot.png')
    return fig
# %%
