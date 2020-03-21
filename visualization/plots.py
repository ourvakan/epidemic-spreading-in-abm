# SEE EXAMPLES HERE
# https://github.com/bokeh/bokeh/tree/master/examples/app
# ANIMATED
# https://towardsdatascience.com/how-to-create-animated-graphs-in-python-bb619cc2dec1

import pandas as pd
from pathlib import Path

import bokeh
from bokeh.palettes import brewer
from bokeh.plotting import figure, output_file, show
from bokeh.io import export_png
import matplotlib.pyplot as plt


history_plot_path = Path(__file__).parent.parent / 'data' / 'plots'
area_plot_path = Path(__file__).parent.parent / 'data' / 'area_plot'


def plot_history(path):

    df = pd.read_csv(path)

    fix, ax = plt.subplots(figsize=(14, 9))
    ax.plot(df.step, df.infected)
    ax.plot(df.step, df.recovered)
    ax.plot(df.step, df.dead)
    ax.plot(df.step, df.susceptible + df.immune)

    ax.legend(['Infected', 'Recovered', 'Dead', 'Healthy'])
    plt.savefig(history_plot_path / f'{path.split("/")[-1][:-4]}.png', dpi=300)


def area_plot(path):

    df = pd.read_csv(path)
    n = df.loc[0, 'susceptible'] + df.loc[0, 'immune'] + df.loc[0, 'infected']

    p = figure(x_range=(0, len(df) - 1), y_range=(0, n), plot_width=800, plot_height=800)
    p.grid.minor_grid_line_color = '#eeeeee'

    names = ['infected', 'dead', 'recovered', 'susceptible', 'immune']
    p.varea_stack(stackers=names, x='step', color=brewer['Spectral'][len(names)], legend_label=names, source=df)

    # reverse the legend entries to match the stacked order
    p.legend.items.reverse()

    export_png(p, filename=area_plot_path / f"area_stack_{path.split('/')[-1][:-4]}.png")
    show(p)


def slider():
    """https://github.com/bokeh/bokeh/b1lob/master/examples/app/sliders.py"""
    pass


if __name__ == '__main__':

    pth = '../data/simulations/03-20-2020__02-05-29.csv'
    area_plot(pth)

