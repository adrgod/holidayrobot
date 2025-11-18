"""class for Holiday Robot IO module, including all methods to inut or output data"""
import logging
import os
import pandas as pd

from support.performance import timer

from config.holidayrobot_config import PATH, OUTPUT_PATH, FORCE_CREATE_OUTPUT, OUTPUT_CSV, OUTPUT_PARQUET

class HoRo_io:
    """class for the input/output methods of HolidayRobot"""

    def __init__(self, config):
        """initialize HolidayRobotIO"""
        pass

    @timer
    def read_data(self) -> pd.DataFrame:
        """method to read data from source defined in the configuration"""
        try:
            self.data = pd.read_csv(PATH)
        except (FileNotFoundError, PermissionError, OSError):
            logging.info("Error reading the source file.")
        return self.data

    def _offload_to_file(self, fformat):
        """method to write a file, independent of format. only considering csv and parquet."""
        try:
            # Ensure output directory exists
            os.makedirs(OUTPUT_PATH, exist_ok=True)
            
            if fformat == 'csv':
                self.data.to_csv(f"{OUTPUT_PATH}/holidayrobot.csv", index=False)
                logging.info("Successfuly written data into %s file.", fformat)
            elif fformat == 'parquet':
                self.data.to_parquet(f"{OUTPUT_PATH}/holidayrobot.parquet", index=False)
                logging.info("Successfuly written data into %s file.", fformat)
        except (FileNotFoundError, PermissionError, OSError):
            logging.info("Error writing the %s file.", fformat)

    @timer
    def output_data(self) -> None:
        """method to write the data to the specified output"""    
        if os.path.isdir(OUTPUT_PATH):
            if OUTPUT_CSV:
                self._offload_to_file('csv')
            if OUTPUT_PARQUET:
                self._offload_to_file('parquet')
            logging.info("Finished writing data.")
        elif FORCE_CREATE_OUTPUT:
            os.makedirs(OUTPUT_PATH)
            self.output_data()
        else:
            logging.info("Output folder doesn't exist and config won't let me create it.")
  