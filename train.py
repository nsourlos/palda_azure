from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

path="https://raw.githubusercontent.com/nsourlos/palda_azure/main/palda.csv"

def clean_data(data):
    y_df = data.iloc[:,-2]
    x_df = data.iloc[: , :-1] #was -1



    return x_df, y_df

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    # TODO: Create TabularDataset using TabularDatasetFactory
    # Data is located at:
    # "https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv"

    url="https://raw.githubusercontent.com/nsourlos/palda_azure/main/palda.csv"
    # ds = TabularDatasetFactory(url)
    # ds=from_delimited_files(url, validate=True, include_path=False, infer_column_types=True, set_column_types=None, separator=',', header=True, partition_format=None, support_multi_line=False, empty_as_string=False, encoding='utf8')
    ds=TabularDatasetFactory.from_delimited_files(path=url)#datastore_path)
    
    df=ds.to_pandas_dataframe()

    ### YOUR CODE HERE ###
    
    x, y = clean_data(df)

    # TODO: Split data into train and test sets.

    ### YOUR CODE HERE ###a
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

    os.makedirs('./outputs', exist_ok=True)
    joblib.dump(model, "./outputs/model.joblib")

if __name__ == '__main__':
    main()