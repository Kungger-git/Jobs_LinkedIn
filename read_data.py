import pandas as pd
import os


def read():
    for root, dirs, files in os.walk(os.getcwd()):
        dirs = dirs
        for data in files:
            if data.endswith('.csv'):
                df = pd.read_csv(os.path.join(root, data))
                pd.set_option('display.max_rows', None)
                df.drop('Source', axis=1, inplace=True)
                print(df)


def read_scraped(folder_name, filename):
    for root, dirs, files in os.walk(f'{os.getcwd()}/{folder_name}'):
        dirs = dirs
        for data in files:
            if filename == data:
                df = pd.read_csv(os.path.join(root, data))
                pd.set_option('display.max_rows', None)
                df.drop('Source', axis=1, inplace=True)
                print(f'Data Frame:\n\n{df}')