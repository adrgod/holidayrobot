import unittest
from unittest.mock import patch
import pandas as pd
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
    
    def test_filter_first_year(self):
        """test filtering data to keep only data related to first year"""
        expected_df = pd.DataFrame({
                'Year': [2010, 2015, 2023, 2025],
                'Sex': ['Male', 'Both', 'Male', 'Both'],
                'VALUE': [100, 300, 500, 700],
                'Statistic Label': ['First Year', 'First Year','Bla bla First Year', 'First Year']
            })
        result = self.HoRo_utest._fitler_first_year().reset_index(drop=True)
        self.assertIsInstance(result, pd.DataFrame)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_get_year_groups(self):
        """test if data is grouped in 5 years time"""
        expected_df = pd.DataFrame({
                'year_group': [2010, 2015, 2015, 2020, 2020, 2025],
                'Sex': ['Male', 'Both', 'Female', 'Female', 'Male', 'Both'],
                'VALUE': [300, 300, 400, 600, 500, 700]
            })
        result = self.HoRo_utest._get_year_groups().reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_rename_header(self):
        """test if header gets lower-cased"""
        expected_df = pd.DataFrame({
                'year': [2010, 2011, 2015, 2018, 2023, 2024, 2025],
                'sex': ['Male', 'Male', 'Both', 'Female', 'Male', 'Female', 'Both'],
                'value': [100, 200, 300, 400, 500, 600, 700],
                'statistic label': ['First Year', 'Third Year', 'First Year', 'No Year', 'Bla bla First Year', 'Bla bla Second Year', 'First Year']
            })
        result = self.HoRo_utest._rename_header().reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected_df)

    @patch.object(HolidayRobot, '_fitler_first_year')
    @patch.object(HolidayRobot, '_get_year_groups')
    @patch.object(HolidayRobot, '_rename_header')
    def test_perform_etl(self, mock_rename, mock_years, mock_filter):
        """test if all etl functions get called"""
        mock_filter.return_value = self.HoRo_utest.data
        mock_years.return_value = self.HoRo_utest.data
        mock_rename.return_value = self.HoRo_utest.data
        
        self.HoRo_utest.perform_etl()

        mock_filter.assert_called_once()
        mock_years.assert_called_once()
        mock_rename.assert_called_once()

    def tearDown(self):
        del self.HoRo_utest
        
if __name__ == '__main__':
    unittest.main()        

    
