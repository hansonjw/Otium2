
import pandas as pd


def write_dataframe_to_file(df, strgLoc, fileName):
    csv = df.to_csv(strgLoc+fileName, mode='a')

def read_csv_to_dataframe(strgLoc, fileName):
    df = pd.read_csv(strgLoc+fileName)
    return df