"""class for the holiday robot ETL module"""
import pandas as pd
from support.performance import timer


class HoRo_etl:
    """class definition for HolidayRobot ETL"""

    def __init__(self):
        self.data = pd.DataFrame()


    @timer
    def _filter_first_year(self):
        return self.data[self.data['Statistic Label'].str.contains('First Year')]

    @timer
    def _get_year_groups(self):
        """create new field with years grouped by 5"""
        self.data['year_group'] = self.data['Year'] // 5 * 5
        self.data = self.data[['year_group', 'Sex', 'VALUE']].groupby(['year_group', 'Sex']).sum().reset_index()
        return self.data

    @timer
    def _rename_header(self):
        """method to lower case the df header"""
        self.data.columns = self.data.columns.str.lower()
        return self.data

    @timer
    def perform_etl(self) -> pd.DataFrame:
        """perform all etl actions on data"""
        # make sure each step updates and returns the DataFrame
        self.data = self._filter_first_year()
        self.data = self._get_year_groups()
        self.data = self._rename_header()
        return self.data