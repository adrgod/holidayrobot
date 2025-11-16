import logging
import pandas as pd

from HolidayRobot.HolidayRobot import HolidayRobot
from config.holidayrobot_config_class import HolidayRobotConfig

from support import *


def main():
    # initializing logging config
    FORMAT = '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
    logging.basicConfig(format=FORMAT, filename='holidayrobot-executions.log', level=logging.INFO)

    logging.info("Process started.")
    HRConfig = HolidayRobotConfig()
    if HRConfig.output_csv:
        logging.info("Data will be written as a csv file.")
    if HRConfig.output_parquet:
        logging.info("Data will be written as a parquet file.")

    
    HoRo = HolidayRobot(HRConfig)
    HoRo.read_data()

    HoRo.perform_etl() #all etl steps in one call

    HoRo.output_data()

if __name__ == '__main__':
    main()
