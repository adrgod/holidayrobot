import argparse
import logging
from HolidayRobot.HolidayRobot import HolidayRobot
from config.holidayrobot_config_class import HolidayRobotConfig


def main():
    """nitializing logging config"""
    
    #command line enable performance print out
    parser = argparse.ArgumentParser(description='interact with variables through command line.')
    parser.add_argument('--perf', type=str, default='True', help='Print out methods performance.')

    # Parse the arguments
    args = parser.parse_args()
    

    #logging message format
    FORMAT = '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
    logging.basicConfig(format=FORMAT, filename='holidayrobot-executions.log', level=logging.INFO)

    logging.info("Process started.")
    HRConfig = HolidayRobotConfig()

    HRConfig.print_performance = str(args.perf).lower() in ("true", "1", "yes", "y")

    #assign args values to variables
    HRConfig.print_performance = args.perf
    logging.info("performance print out flag is: %s", HRConfig.print_performance)

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
