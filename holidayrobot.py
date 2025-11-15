

import pandas as pd

from holidayrobot_io import holidayrobot_io as hr_io
from holidayrobot_etl import holidayrobot_etl as hr_etl
from support import *


def main():
    df = hr_io.read_data()
    df = hr_etl.fitler_first_year(df)
    df = hr_io.get_year_groups(df)
    df = hr_etl.rename_header(df)
    hr_io.output_data(df)


if __name__ == '__main__':
    main()
