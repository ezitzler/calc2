import pandas as pd
"""csv Class"""

class csv_output:
    """csv_output"""

    @staticmethod
    def write_test():
        """ write_test"""
        cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
        cities.to_csv('cities.csv')
        return True

