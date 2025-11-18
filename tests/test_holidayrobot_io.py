import os
import pandas as pd
import unittest
from unittest.mock import patch
from config.holidayrobot_config import OUTPUT_PATH, OUTPUT_CSV, OUTPUT_PARQUET
from config.holidayrobot_config_class import HolidayRobotConfig
from HolidayRobot.HolidayRobot import HolidayRobot

class TestHolidayRobotFunctions(unittest.TestCase):

    def setUp(self):
        self.hr_config = HolidayRobotConfig()

        self.HoRo_utest = HolidayRobot(self.hr_config)
        self.HoRo_utest.data = pd.DataFrame({
                'Year': [2010, 2011, 2015, 2018, 2023, 2024, 2025],
                'Sex': ['Male', 'Male', 'Both', 'Female', 'Male', 'Female', 'Both'],
                'VALUE': [100, 200, 300, 400, 500, 600, 700],
                'Statistic Label': ['First Year', 'Third Year', 'First Year', 'No Year', 'Bla bla First Year', 'Bla bla Second Year', 'First Year']
            })
        
        # Ensure output directory exists for file tests
        os.makedirs(OUTPUT_PATH, exist_ok=True)
    
    def test_read_data(self):
        """test reading the source data into a DataFrame"""
        result = self.HoRo_utest.read_data().reset_index(drop=True)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertGreater(len(result), 1)
    
    def test_offload_to_file_csv(self):
        print(f"Attempting to write file to: {OUTPUT_PATH}/holidayrobot.csv") # Add this line
        self.HoRo_utest._offload_to_file('csv')
        self.assertTrue(os.path.isfile(f"{OUTPUT_PATH}/holidayrobot.csv"))

    def test_offload_to_file_parquet(self):
        self.HoRo_utest._offload_to_file('parquet')
        self.assertTrue(os.path.isfile(f"{OUTPUT_PATH}/holidayrobot.parquet"))

    @patch.object(HolidayRobot, '_offload_to_file')
    @patch('os.path.isdir')
    def test_output_data(self, mock_isdir, mock_offload):
        self.HoRo_utest.output_data()
        mock_isdir.return_value = True

        if OUTPUT_CSV:
                mock_offload.assert_any_call('csv')
        if OUTPUT_PARQUET:
            mock_offload.assert_any_call('parquet')

    def tearDown(self):
        pass
        
if __name__ == '__main__':
    unittest.main()        

    
