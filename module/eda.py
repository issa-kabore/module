from . import LOGGER
from termcolor import colored as cl  # text customization
import pandas as pd
from pandas_profiling import ProfileReport


def data_info(dataframe: pd.DataFrame):
    LOGGER.info("Getting dataframe information")
    print(cl('------------------------------------------------------------------------', attrs=['bold']))
    print(cl('COLUMNS INFORMATION', attrs=['bold'], color='green'))
    print(cl('The dataset has {} cases and {} features'.format(*dataframe.shape), attrs=['bold']))
    print(dataframe.info(verbose=True, show_counts=False))
    print(cl('------------------------------------------------------------------------', attrs=['bold']))
    print(cl('NULL VALUES', attrs=['bold'], color='green'))
    print(null_column_report_df(dataframe))
    print(cl('------------------------------------------------------------------------', attrs=['bold']))
    print(cl('SUMMARY OF STATISTICS', attrs=['bold'], color='green'))
    print(dataframe.describe())
    print(cl('------------------------------------------------------------------------', attrs=['bold']))


def data_report(df, report_title="your_report.html", html_save: bool = True):
    """Generate a profile report from a Dataset stored as a pandas `DataFrame`.
        - Used as is, it will output its content as an HTML report in a Jupyter notebook.
        - Use on jupyter lab/notebook"""
    LOGGER.info("Generating Pandas Profiling Report")
    profile = ProfileReport(df.reset_index(drop=True), explorative=True, title=report_title)
    profile.config.interactions.targets = df.columns.tolist()
    if html_save:
        profile.to_file(report_title)
        LOGGER.debug(f"Report saved in '{report_title}'")
    return profile


def replace_df_values(df, values):
    """ Call pd.DataFrame.replace() on a dataframe and return resulting dataframe.
    Values should be in format of nested dictionaries,
    E.g., {‘a’: {‘b’: nan}}, are read as follows:
        Look in column ‘a’ for the value ‘b’ and replace it with nan
    """
    df_copy = df.copy()
    return df_copy.replace(values)


def null_column_report_df(df):
    """
    Searches a dataframe for null columns and returns a dataframe of the format
    Column | Total Nulls | Percent Nulls
    """
    num_null_columns = df.shape[1] - df.dropna(axis=1).shape[1]
    print(cl('Number of columns with null values:\n{}\n'.format(num_null_columns), attrs=['bold']))
    null_columns = df.columns[df.isnull().any()].tolist()
    null_info_records = []
    for col in null_columns:
        total_null_records = df[col].isnull().sum()
        percent_null_records = round(total_null_records / df.shape[0], 2)
        null_info_records.append({
            'Column': col,
            'Total_Null_Records': total_null_records,
            'Percent_Null_Records': percent_null_records
        })
    return pd.DataFrame(null_info_records)
