
import pandas as pd

from config.holidayrobot_config import *
from holidayrobot_io.holidayrobot_io import HoRo_io
from holidayrobot_etl.holidayrobot_etl import HoRo_etl

class HolidayRobot(HoRo_io, HoRo_etl):

    def __init__(self, config):
        """initialize HolidayRobot"""
        self.HoRoIO = HoRo_io(config)
        self.config = config
        self.data = pd.DataFrame()  #creating here just for visibility, as etl functions create the 'data' variable

    def read_data(self):
        return super().read_data()
    
    def output_data(self):
        return super().output_data()
    
    def perform_etl(self):
        return super().perform_etl()


