import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# functions

df = pd.read_csv("python-applications\data_analysis\minimum_wage\minimum_wage_1968-2020\MinimumWageData.csv")

def states_to_columns(desired_data_points):
    act_min_wage = pd.DataFrame()

    for name, group in df.groupby("State"):
        if act_min_wage.empty:
            act_min_wage = group.set_index("Year")[[desired_data_points]].rename(columns={desired_data_points:name})
        else:
            act_min_wage = act_min_wage.join(group.set_index("Year")[[desired_data_points]].rename(columns={desired_data_points:name}))
    return act_min_wage.head()

def pandas_dataframes():
    n = 0 
    df.head(n) 
    df.tail(n) 
    df_COLUMN = df[df['COLUMN'] == 'ROW_VALUES']
    # averages example 
    oklahoma_df = df[df['State'] == 'Oklahoma']
    oklahoma_min_2020 = oklahoma_df['State.Minimum.Wage.2020.Dollars']
    oklahoma_min_2020.mean()
    df_NEW_INDEX = df.set_index('NEW_INDEX')
    df.cov().head()
    df.corr().head()


def missing_column(column):
    for problem in df[column].unique():
        if problem in df.columns:
            print("Missing something here....")

def plotting_mastermind(df): 
    
    labels = [c[:2] for c in df.columns]  # get abbv state names.
    fig = plt.figure(figsize=(12,12))  # figure so we can add axis
    ax = fig.add_subplot(111)  # define axis, so we can modify
    ax.matshow(df, cmap=plt.cm.RdYlGn)  # display the matrix
    ax.set_xticks(np.arange(len(labels)))  # show them all!
    ax.set_yticks(np.arange(len(labels)))  # show them all!
    ax.set_xticklabels(labels)  # set to be the abbv (vs useless #)
    ax.set_yticklabels(labels)  # set to be the abbv (vs useless #)

    plt.matshow(df)
    plt.show()

