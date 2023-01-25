import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns


def plotting_features(data, excluded_cols=None):
    """
    Return to distribution of numerical features and count of
    categorical features, specific features will ignore them,
    because they do not give us any meaning.
    -------
    """
    if excluded_cols is not None:
        cols = [col for col in data.columns if col not in excluded_cols]
    else:
        cols = data.columns

    nrows = int(np.ceil(len(cols) / 2))
    fig, ax = plt.subplots(
        nrows=nrows,
        ncols=2,
        figsize=(12, 8),
        constrained_layout=True)
    ax = ax.ravel()

    for i in range(len(cols)):
        if (data[cols[i]].dtypes == "object") or (len(data[cols[i]].unique().tolist()) < 10):

            sns.countplot(y=data[cols[i]], ax=ax[i])
            ax[i].set_title(f"{cols[i]} count")

        else:
            sns.histplot(x=data[cols[i]], ax=ax[i])
            ax[i].set_title(f"'{cols[i]}' distribution")


def plot_categorical_feature(data, var: str, normalize: bool = True):
    """"Plotting univatiate barplot """
    # assign your bars to a variable so their attributes can be accessed
    ax = data[[var]].value_counts(normalize=normalize).plot.bar(title=f"Distribution of '{var}' feature")

    # access the bar attributes to place the text in the appropriate location
    ax.bar_label(ax.containers[0], label_type="center")
    plt.show()


def plot_numerical_feature(data, var: str):
    """"Plotting a histogram and boxplot"""
    fig = px.histogram(data, x=var, marginal="box",  # or violin, rug
                       hover_data=data.columns,
                       title=f"Distribution of '{var}' feature",
                       width=800, height=400)
    fig.show()


def _plot_hist(data, bins, xlabel="x label", title='Distribution', **params):
    """
    Plot a histogram with nb_bins bins. Can add others params: color='blue', alpha=0.7, rwidth=0.85

    Parameters
    ----------
    data
    bins
    xlabel
    title
    params
    """

    plt.hist(data, bins=bins, **params)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.title(title)
    plt.show()


def plot_roc(roc_auc: float, roc_curve):
    fpr, tpr, threshold = roc_curve
    # Plotting the ROC
    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'r-', label='auc = %0.2f' % roc_auc)
    plt.plot([0, 1], [0, 1], 'k--', label='random')
    plt.plot([0, 0, 1, 1], [0, 1, 1, 1], 'g-', label='perfect')
    plt.legend(loc='lower right')
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
