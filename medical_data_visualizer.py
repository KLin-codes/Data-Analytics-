import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("/Users/k.lin/Documents/Documents - Kenny's MacBook Pro/Codes/csv/medical_examination.csv")

# 2
weight = df['weight']
height_squared = (df['height']/100) ** 2
df['overweight'] = (weight/height_squared) > 25
df['overweight'] = df['overweight'].astype(int)

# 3
df['cholesterol'] = df['cholesterol'] > 1
df['cholesterol'] = df['cholesterol'].astype(int)
df['gluc'] = df['gluc'] > 1
df['gluc'] = df['gluc'].astype(int)

# 4
def draw_cat_plot():
    # 5,6,7,8
    df_cat = pd.melt(
        df,
        id_vars = ['cardio'],
        value_vars= ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'],
        var_name= 'variable',
        value_name= 'value'
    )

    catplot = sns.catplot(
        data = df_cat,
        x = 'variable',
        hue = 'value',
        col = 'cardio',
        kind = 'count'
    )

    fig = catplot.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat[
        (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
        (df_heat['height'] <= df_heat['height'].quantile(0.095)) &
        (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
        (df_heat['weight'] <= df_heat['weight'].quantile(0.095))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype = bool))

    # 14
    fig, ax = plt.subplots(figsize=(12,10))

    # 15
    sns.heatmap(
        corr,
        mask = mask,
        annot = True,
        fmt = '.1f',
        ax = ax
    )

    fig = ax.get_figure()


    # 16
    fig.savefig('heatmap.png')
    return fig