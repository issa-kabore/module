import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def one_hot_encoder(df: pd.DataFrame, column_list: list):
    """Takes in a dataframe and a list of columns
    for pre-processing via one hot encoding returns
    a dataframe of one hot encoded values"""
    df_encoded = pd.get_dummies(df, columns=column_list)
    return df_encoded


def scale_data(df, column_list, scaler=MinMaxScaler()):
    """Takes in a dataframe and a list of column names to transform
     returns a dataframe of scaled values"""
    df_to_scale = df[column_list]
    x = df_to_scale.values
    x_scaled = scaler.fit_transform(x)
    df_to_scale = pd.DataFrame(x_scaled, columns=df_to_scale.columns)
    return df_to_scale
