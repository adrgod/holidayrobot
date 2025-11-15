import pandas as pd
import unittest
from unittest.mock import patch
import holidayrobot
from holidayrobot_etl import holidayrobot_etl
from holidayrobot_io import holidayrobot_io

from config import holidayrobot_config as conf

class TestHolidayRobotFunctions(unittest.TestCase):

    def setUp(self):
        """create sample data to test"""
        self.example_df = pd.DataFrame({
            'Year': [2023,2024,2025],
            'Sex': ['Male', 'Female', 'Both'],
            'VALUE': [100, 200, 300],
            'Statistic Label': ['Bla bla First Year', 'Bla bla Second Year', 'First Year']
        })

    @patch('holidayrobot_io.holidayrobot_io.pd.read_csv')
    def test_read_data(self, mock_path):
        """test reading the data from the file"""
        mock_path.return_value = self.example_df
        result = holidayrobot_io.read_data()
        self.assertIsInstance(result, pd.DataFrame)
        mock_path.assert_called_once()

    def test_filter_first_year(self):
        """test if the data is filtered for only first year"""
        df = self.example_df.copy()
        result = holidayrobot_etl.fitler_first_year(df)
        self.assertEqual(len(df), 3)
        self.assertTrue(all(result['Statistic Label'].str.contains('First Year')))

    @patch('holidayrobot_io.holidayrobot_io.pd.DataFrame.to_parquet')
    @patch('holidayrobot_io.holidayrobot_io.pd.DataFrame.to_csv')
    def test_output_data(self, mock_to_csv, mock_to_parquet):
        """test if the data gets out properly"""
        df = self.example_df.copy()
        holidayrobot_io.output_data(df)
        mock_to_csv.assert_called_once_with(f"{conf._output_path}/holidayrobot.csv", index=False)
        mock_to_parquet.assert_called_once_with(f"./{conf._output_path}/holidayrobot.parquet", index=False)

    def test_rename_header(self):
        """test renaming headers"""
        df_test = self.example_df.copy()
        result = holidayrobot_etl.rename_header(df_test)
        self.assertTrue(all(col.islower() for col in result.columns))

    def test_get_year_group(self):
        """test getting the data to work with"""
        df_test = self.example_df.copy()
        result = holidayrobot_io.get_year_groups(df_test)
        self.assertIn('year_group', result.columns)
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()        

    
