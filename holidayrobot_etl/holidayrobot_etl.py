
#all functions to work on the data will be here
import pandas as pd
from support.performance import timer


class HoRo_etl:

    def __init__(self):
        pass


    @timer
    def _fitler_first_year(self):
        return self.data[self.data['Statistic Label'].str.contains('First Year')]

    @timer
    def _get_year_groups(self):
        """create new field with years grouped by 5"""
        self.data['year_group'] = (self.data['Year'] // 5 * 5)
        self.data = self.data[['year_group', 'Sex', 'VALUE']].groupby(['year_group', 'Sex']).sum().reset_index()
        return self.data

    @timer
    def _rename_header(self):
        self.data.columns = self.data.columns.str.lower()
        return self.data
    
    
    @timer
    def perform_etl(self) -> pd.DataFrame:
        """perform all etl actions on data"""
        self._fitler_first_year()
        self._get_year_groups()
        self._rename_header()