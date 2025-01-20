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
    df_NEW_INDEX = df.set_index('NEW_INDEX')
    df.cov().head()
    df.corr().head()