"""config file to have all in one place for variables and params"""

from config.holidayrobot_config import (PATH, OUTPUT_PATH, OUTPUT_CSV, OUTPUT_PARQUET, PRINT_PERFORMANCE, FORCE_CREATE_OUTPUT)

class HolidayRobotConfig:
    """class to keep all configurations and parameters"""

    def __init__(self):
        self.path = PATH
        self.output_path = OUTPUT_PATH
        self.output_csv = OUTPUT_CSV
        self.output_parquet = OUTPUT_PARQUET
        self.print_performance = PRINT_PERFORMANCE
        self.force_create_output = FORCE_CREATE_OUTPUT
