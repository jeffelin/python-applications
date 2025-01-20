import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# functions


def states_to_columns(desired_data_points):
    act_min_wage = pd.DataFrame()

    for name, group in df.groupby("State"):
        if act_min_wage.empty:
            act_min_wage = group.set_index("Year")[[desired_data_points]].rename(columns={desired_data_points:name})
        else:
            act_min_wage = act_min_wage.join(group.set_index("Year")[[desired_data_points]].rename(columns={desired_data_points:name}))
    return act_min_wage.head()