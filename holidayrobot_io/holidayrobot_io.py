"""class for Holiday Robot IO module, including all methods to inut or output data"""
import logging
import os
import pandas as pd

from support.performance import timer

class HoRo_io:
    """class for the input/output methods of HolidayRobot"""

    def __init__(self, config):
        """initialize HolidayRobotIO"""
        # keep a reference to configuration and ensure data exists
        self.config = config
        self.data = pd.DataFrame()

    @timer
    def read_data(self) -> pd.DataFrame:
        """method to read data from source defined in the configuration"""
        try:
            path = getattr(self.config, 'path', None)
            if not path:
                logging.info("No input PATH provided in config.")
                return self.data
            self.data = pd.read_csv(path)
        except (FileNotFoundError, PermissionError, OSError):
            logging.info("Error reading the source file.")
        return self.data

    def _offload_to_file(self, fformat):
        """method to write a file, independent of format. only considering csv and parquet."""
        try:
            # Ensure output directory exists
            output_path = getattr(self.config, 'output_path', './')
            os.makedirs(output_path, exist_ok=True)

            if fformat == 'csv':
                self.data.to_csv(f"{output_path}/holidayrobot.csv", index=False)
                logging.info("Successfully written data into %s file.", fformat)
            elif fformat == 'parquet':
                self.data.to_parquet(f"{output_path}/holidayrobot.parquet", index=False)
                logging.info("Successfully written data into %s file.", fformat)
        except (FileNotFoundError, PermissionError, OSError):
            logging.info("Error writing the %s file.", fformat)

    @timer
    def output_data(self) -> None:
        """method to write the data to the specified output"""    
        output_path = getattr(self.config, 'output_path', './')
        output_csv = getattr(self.config, 'output_csv', True)
        output_parquet = getattr(self.config, 'output_parquet', True)
        force_create = getattr(self.config, 'force_create_output', False)

        if os.path.isdir(output_path):
            if output_csv:
                self._offload_to_file('csv')
            if output_parquet:
                self._offload_to_file('parquet')
            logging.info("Finished writing data.")
        elif force_create:
            os.makedirs(output_path, exist_ok=True)
            self.output_data()
        else:
            logging.info("Output folder doesn't exist and config won't let me create it.")
  