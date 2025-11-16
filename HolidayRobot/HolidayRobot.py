
import pandas as pd

from config.holidayrobot_config import *
from holidayrobot_io.holidayrobot_io import *
from holidayrobot_etl.holidayrobot_etl import *

class HolidayRobot(HoRo_io, HoRo_etl):

    def __init__(self, config):
        """initialize HolidayRobot"""
        self.data = pd.DataFrame({})
        self.config = config

    def read_data(self):
        return super().read_data()
    
    def output_data(self):
        return super().output_data()
    
    def perform_etl(self):
        return super().perform_etl()


