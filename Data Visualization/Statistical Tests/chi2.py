import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

def check_qualitative_variable(variable : str, data : pd.DataFrame, significance : float = 0.05, primary_variable : str = 'Churn'):
    df_cross = pd.crosstab(data[primary_variable], data[variable])

    p_value = chi2_contingency(df_cross)[1]

    if p_value < significance:
        title = f'There is a significant association between customer {variable} and {primary_variable}, \nconsidering a chi2 significance of {significance * 100}% and a p-value of {p_value:.2e}'
    else:
        title = f'There is no significant association or dependence between customer {variable} and {primary_variable}, \nconsidering a chi2 significance of {significance * 100}% and a p-value of {p_value:.2e}'

    plt.figure(figsize = (8, 7))
    ax = sns.countplot(
        x = variable,
        data = data,
        hue = primary_variable
    )
    for p in ax.patches:
        ax.annotate(
            f'{p.get_height()}', 
            (p.get_x() + p.get_width() / 2, p.get_height()),
            ha='center', va='bottom', fontsize=12, color='black'
        )

    plt.suptitle(f'Amount of {primary_variable} per {variable}', fontsize = 16)
    plt.title(title, fontsize = 12, y = 1)
    plt.show()