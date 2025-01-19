# some cool functions 
import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csvdf = pd.read_cs(r"data_analysis\avacado_data\avacado_dataset\avocado.csv")


def pandas_dataframes():
    n = 0 
    df.head(n) 
    df.tail(n) 
    df_COLUMN = df[df['COLUMN'] == 'ROW_VALUES']
    df_NEW_INDEX = df.set_index('NEW_INDEX')

def multiple_categorical_graph(category_index)
    for region in df['region'].unique()[:16]:
        print(region)
        region_df = df.copy()[df['region']==region]
        region_df.set_index('Date', inplace=True)
        region_df.sort_index(inplace=True)
        region_df[f"{region}_price25ma"] = region_df["AveragePrice"].rolling(25).mean()

        if graph_df.empty:
            graph_df = region_df[[f"{region}_price25ma"]]  # note the double square brackets!
        else:
            graph_df = graph_df.join(region_df[f"{region}_price25ma"])
    graph_df.plot(figsize=(8,5), legend=False)