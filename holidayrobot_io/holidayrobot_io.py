
import pandas as pd

from config import holidayrobot_config as conf

def read_data():
    df = pd.read_csv(conf._path)
    return df

def get_year_groups(df):
    df['year_group'] = (df['Year'] // 5 * 5)
    df = df[['year_group', 'Sex', 'VALUE']].groupby(['year_group', 'Sex']).sum().reset_index()
    return df

def output_data(df):
    df.to_csv(f"{conf._output_path}/holidayrobot.csv", index=False)
    df.to_parquet(f"./{conf._output_path}/holidayrobot.parquet", index=False)