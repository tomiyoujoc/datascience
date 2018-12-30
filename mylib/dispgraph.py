# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_axc_distribution(data, x, hue, ax=None):
    hue_unique_data = data[hue].unique()
    for h in hue_unique_data:
        data.loc[data[hue] == h, x].plot(kind="hist", alpha=.5, ax=ax)
    if ax is None:
        plt.xlabel(x)
        plt.ylabel("count")
        leg = plt.legend(hue_unique_data)
        leg.set_title(hue)
    else:
        ax.set_xlabel(x)
        ax.set_ylabel("count")
        leg = ax.legend(hue_unique_data)
        leg.set_title(hue)

def plot_axa_distribution(data, x, y, ax=None):
    sns.regplot(x=x, y=y, data=data, ax=ax)

def plot_cxa_distribution(data, x, y, ax=None):
    sns.boxplot(x=x, y=y, data=data, ax=ax)

def plot_cxc_distribution(data, x, hue, ax=None):
    sns.countplot(x=x, hue=hue, data=data, ax=ax)

def is_analog_data(data):
    if data.dtype == np.float:
        return True
    elif data.dtype == np.int64:
        if len(data.unique()) > 100:
            return True
        else:
            return False
    else:
        return False

def plot_distribution(data, x, y=None, ax=None):
    if y is None:
        #1変数
        if is_analog_data(data[x]):
            sns.distplot(data[x].dropna(), kde=None, ax=ax)
            if ax is None:
                plt.xlabel(x)
                plt.ylabel("count")
            else:
                ax.set_xlabel(x)
                ax.set_ylabel("count")
        else:
            sns.countplot(x=x, data=data, ax=ax)
    else:
        #2変数
        if is_analog_data(data[x]):
            if is_analog_data(data[y]):
                plot_axa_distribution(data, x, y, ax)
            else:
                plot_axc_distribution(data, x, y, ax)
        else:
            if is_analog_data(data[y]):
                plot_cxa_distribution(data, x, y, ax)
            else:
                plot_cxc_distribution(data, x, y, ax)

def plot_all_distribution(data, y=None):
    NCOLS = 3
    columns = data.columns.tolist()
    nrows = len(columns) // NCOLS + 1
    if len(columns) % NCOLS == 0:
        nrows -= 1
    fig, axes = plt.subplots(figsize=(4*NCOLS, 3*nrows), ncols=NCOLS, nrows=nrows)
    axes = axes.flatten()
    for i, x in enumerate(columns):
        plot_distribution(data, x, y, axes[i])
    plt.tight_layout()