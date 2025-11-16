
import pandas as pd
import logging

from config.holidayrobot_config import *

class HoRo_io:

    def __init__(self, config):
        """initialize HolidayRobotIO"""
        pass

    def read_data(self) -> pd.DataFrame:
        """method to read data from source defined in the configuration"""
        try:
                self.data = pd.read_csv(path)
        except (FileNotFoundError, PermissionError, OSError):
                logging.info("Error reading the source file.")
        return self.data

    def output_data(self) -> None:
        """method to write the data to the specified output"""
        if output_csv:
            try:
                self.data.to_csv(f"{output_path}/holidayrobot.csv", index=False)
            except (FileNotFoundError, PermissionError, OSError):
                logging.info("Error writing the csv file.")
        if output_parquet:
            try:
                self.data.to_parquet(f"./{output_path}/holidayrobot.parquet", index=False)
            except (FileNotFoundError, PermissionError, OSError):
                logging.info("Error writing the parquet file.")
        logging.info("successfuly written all output.")            