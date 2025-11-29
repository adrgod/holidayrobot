
import pandas as pd

from config.holidayrobot_config import *
from holidayrobot_io.holidayrobot_io import HoRo_io
from holidayrobot_etl.holidayrobot_etl import HoRo_etl

class HolidayRobot:
    """Main HolidayRobot object using composition: holds IO and ETL components."""

    def __init__(self, config):
        """initialize HolidayRobot with composed IO and ETL components"""
        self.config = config
        self.io = HoRo_io(config)
        self.etl = HoRo_etl()
        self.data = pd.DataFrame()

    def read_data(self) -> pd.DataFrame:
        """Read data via the IO component and keep it on the robot."""
        self.io.read_data()
        self.data = self.io.data
        return self.data

    def perform_etl(self) -> pd.DataFrame:
        """Run ETL on the robot's data using the ETL component."""
        # give the ETL component the current data, run transformations, and store result
        self.etl.data = self.data
        self.data = self.etl.perform_etl()
        return self.data

    def output_data(self) -> None:
        """Write out the robot's data using the IO component."""
        self.io.data = self.data
        self.io.output_data()


