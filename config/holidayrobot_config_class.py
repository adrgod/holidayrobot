
#config file to have all in one place for variables and params

from config.holidayrobot_config import *

class HolidayRobotConfig:

    def __init__(self):
        self.path = path
        self.output_path = output_path
        self.output_csv = output_csv
        self.output_parquet = output_parquet
        self.print_performance = print_performance

