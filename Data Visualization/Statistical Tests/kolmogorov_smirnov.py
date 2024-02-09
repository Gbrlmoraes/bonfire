import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kstest

# Creating a function to check whether a variable follows a normal distribution or not
def check_normal_distribuition(variable : str, data : pd.DataFrame, significance : float = 0.05):

    # Kolmogorov-Smirnov
    kstest_statistic, kstest_p_value = kstest(data[variable], 'norm', N = data[variable].shape[0])

    if kstest_p_value > significance:
        title = f'The variable {variable} follow a normal distribuition, \nconsidering a Shapiro-Wick significance of {significance * 100}% and a p-value of {kstest_p_value:.2e}'
    else:
        title = f'The variable {variable} does not follow a normal distribuition, \nconsidering a Shapiro-Wick significance of {significance * 100}% and a p-value of {kstest_p_value:.2e}'

    fig, axes = plt.subplots(2)
    fig.set_figheight(8),
    fig.set_figwidth(8)

    # Histogram
    sns.histplot(
        x = variable,
        data = data,
        kde = True,
        ax = axes[0]
    )
    axes[0].set_title(title, fontsize = 12)

    # QQPlot
    probplot(
        x = data[variable],
        plot = axes[1]
    )
    axes[1].set_title('')

    plt.show()