#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Jordi Corbilla
# Created Date: 2023
# version ='0.5.0'
# ---------------------------------------------------------------------------

from tablepy_lib import consoleFormatter
import pandas as pd

class MyFormatterTests:
    def test_toSql(self):
        data = {
            "Name": ["John", "Emily", "Tom", "JC"],
            "Age": [28, 32, 25, 2],
            "Country": ["USA", "Canada", "UK", "DE"],
            "Data": ["USA", "Canada", "UK", "3434243"]
        }
        
        formatter = consoleFormatter(data)
        table = formatter.to_table()
        print(table)
        assert table == ""
        


data = {
    "Name": ["John", "Emily", "Tom", "JC"],
    "Age": [-28, 3002.6, 25, 2],
    "Country": ["USA", "Canada", "UK", "DE"],
    "Data": ["USA", "Canada", "UK", "3434243"]
}

formatter = consoleFormatter(data)
table = formatter.to_table()
print(table)    

data_frame = pd.DataFrame(data)

table = consoleFormatter(data_frame).to_table()
print(table)

table = consoleFormatter(data_frame).to_sql('dd')
print(table)