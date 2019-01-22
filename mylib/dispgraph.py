# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

def __plot_large_data(data, x, ax=None):
    if ax is None:
        ax = plt.subplot(111)
    ax.text(0.25, 0.4, "{}\nunique values".format(len(data[x].unique())), fontsize=18)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(x)

def __plot_axc_distribution(data, x, hue, ax=None):
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

def __plot_axa_distribution(data, x, y, ax=None):
    sns.regplot(x=x, y=y, data=data, ax=ax)

def __plot_cxa_distribution(data, x, y, ax=None):
    if len(data[x].unique()) <= 20:
        sns.boxplot(x=x, y=y, data=data, ax=ax)
    else:
        __plot_large_data(data, x, ax)

def __plot_cxc_distribution(data, x, hue, ax=None):
    if len(data[x].unique()) <= 20:
        sns.countplot(x=x, hue=hue, data=data, ax=ax)
    else:
        __plot_large_data(data, x, ax)

def __is_analog_data(data):
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
        if __is_analog_data(data[x]):
            sns.distplot(data[x].dropna(), kde=None, ax=ax)
            if ax is None:
                plt.xlabel(x)
                plt.ylabel("count")
            else:
                ax.set_xlabel(x)
                ax.set_ylabel("count")
        else:
            if len(data[x].unique()) <= 20:
                sns.countplot(x=x, data=data, ax=ax)
            else:
                __plot_large_data(data, x, ax)
    else:
        #2変数
        if __is_analog_data(data[x]):
            if __is_analog_data(data[y]):
                __plot_axa_distribution(data, x, y, ax)
            else:
                __plot_axc_distribution(data, x, y, ax)
        else:
            if __is_analog_data(data[y]):
                __plot_cxa_distribution(data, x, y, ax)
            else:
                __plot_cxc_distribution(data, x, y, ax)
    if ax is not None:
        ax.set_xticks(rotation=80)
    else:
        plt.xticks(rotation=80)

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
    
def plot_scatter_regression(data, x, y, my_regfunc=None):
    if my_regfunc is None:
        ax = sns.regplot(x=data[x], y=data[y], fit_reg=True)
    else:
        ax = sns.regplot(x=data[x], y=data[y], fit_reg=False)
        disp_X = np.linspace(np.min(data[x])-0.1, np.max(data[x])+0.1, 100)
        ax.plot(disp_X, my_regfunc(disp_X))

def plot_feature_magnitude(data):
    plt.plot(data.min(axis=0).values, 'o', label="min")
    plt.plot(data.max(axis=0).values, '^', label="max")
    plt.legend(loc=1)
    plt.xlabel("Feature index")
    plt.ylabel("Feature magnitude")

def plot_gridCV_score(grid, params, value):
    index = params[0]
    column = params[1]
    result = pd.DataFrame(grid.cv_results_)
    df = result[[index, column, value]]
    temp = df.groupby([index, column])[value].max().unstack()
    sns.heatmap(temp, annot=True, fmt='.3f')
    
    print("Best cross-validation accuracy:{:.3f}".format(grid.best_score_))
    print("Best parameters:{}".format(grid.best_params_))

def plot_confusion_matrix(y_true, y_pred):
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import classification_report
    from sklearn.metrics import accuracy_score
    labels = sorted(list(set(y_true)))
    cmx_data = confusion_matrix(y_true, y_pred, labels=labels)
    cmx_rate = cmx_data/np.vstack(cmx_data.sum(axis=1))

    df_cmx_date = pd.DataFrame(cmx_data, index=labels, columns=labels)
    df_cmx_rate = pd.DataFrame(cmx_rate, index=labels, columns=labels)
    
    fig, axes = plt.subplots(figsize = (8,4), ncols=2, nrows=1)
    sns.heatmap(df_cmx_date, annot=True, fmt='.3f', ax=axes[0])
    sns.heatmap(df_cmx_rate, annot=True, fmt='.3f', ax=axes[1])
    axes[0].set_ylabel("True label")
    axes[0].set_xlabel("Predicted label")
    plt.tight_layout()
    
    #レポート
    print(classification_report(y_true, y_pred))
    print("Accuracy score:{:.2f}".format(accuracy_score(y_true, y_pred)))

def plot_precision_recall_curve(y_true, y_before_pred):
    from sklearn.metrics import precision_recall_curve
    from sklearn.metrics import average_precision_score
    precision, recall, thresholds = precision_recall_curve(y_true, y_before_pred)
    close_zero = np.argmin(np.abs(thresholds))
    plt.plot(precision[close_zero], recall[close_zero], 'o', markersize=10,
            label="threshold zero", fillstyle="none", c="k", mew=2)
    plt.plot(precision, recall, label="precision recall curve")
    plt.xlabel("Precision")
    plt.ylabel("Recall")
    plt.legend()
    
    #平均適合率
    print("Average preciion:{:.2f}".format(average_precision_score(y_true, y_before_pred)))

def plot_roc_curve(y_true, y_before_pred):
    from sklearn.metrics import roc_curve
    from sklearn.metrics import roc_auc_score
    fpr, tpr, thresholds = roc_curve(y_true, y_before_pred)
    close_zero = np.argmin(np.abs(thresholds))
    plt.plot(fpr[close_zero], tpr[close_zero], 'o', markersize=10,
            label="threshold zero", fillstyle="none", c="k", mew=2)
    plt.plot(fpr, tpr, label="roc curve")
    plt.xlabel("FPR")
    plt.ylabel("TPR")
    plt.legend()
    
    #AUC
    print("AUC:{:.2f}".format(roc_auc_score(y_true, y_before_pred)))
    
def plot_qqplot(data, x):
#    stats.probplot(data[x], dist="norm", plot=plt)
    sm.qqplot(data[x], line="q")

def plot_arrays_line(array_likes, columns=None, remove_legend=False):
    temp = pd.DataFrame(array_likes)
    if columns is not None:
        temp.columns = columns
    ax = temp.T.plot()
    if remove_legend:
        ax.remove_legend()
    del temp