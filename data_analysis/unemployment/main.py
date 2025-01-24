import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

unemployment_df = pd.read_csv(r'\python-applications\data_analysis\unemployment\unemployment_data\unemployment\output.csv')

Dataset = unemployment_df
X_Axis = 'Rate'
Y_Axis = 'Year'

def sns_plots_plots(X_Axis, Y_Axis, Dataset): 

    # scatter plot with plt 
    plt.scatter(Dataset[X_Axis], Dataset[Y_Axis])
    
    # Labels for scatter plot

    plt.title("Scatter Plot")
    
    # Setting the X and Y labels
    plt.xlabel(X_Axis)
    plt.ylabel(Y_Axis)

    plt.colorbar()

    # with sns plots
    sns.scatterplot(x=X_Axis, y=Y_Axis, data=Dataset)

    sns.lineplot(data=Dataset.drop([X_Axis], axis=1))

    sns.histplot(x=X_Axis, data=Dataset, kde=True, hue=Y_Axis)
        
    plt.show()