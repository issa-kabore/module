# This is a sample Python script.
from module import LOGGER
from module.eda import *
import module.preprocessing as pr

import pandas as pd
pd.set_option("display.max.columns", None)
# pd.set_option("display.precision", 2)


# --------------------------------------
path_data = "data/"
filename = "bike-rentals.csv"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    LOGGER.info('Importing data')
    df = pd.read_csv(path_data + filename)
    # print(df.head())

    columns = get_columns(df)
    print(columns)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
