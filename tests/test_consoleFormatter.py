#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Jordi Corbilla
# Created Date: 2023
# version ='0.8.0'
# ---------------------------------------------------------------------------

from tablepy_lib.consoleFormatter import ConsoleFormatter
import pandas as pd
import unittest

class MyFormatterTests(unittest.TestCase):
    def test_dict_toMarkdown(self):
        data = {
            "Name": ["John", "Emily", "Tom", "JC"],
            "Age": [28, 32, 25, 2],
            "Country": ["USA", "Canada", "UK", "DE"],
            "Data": ["USA", "Canada", "UK", "3434243"]
        }
        
        expected_result = []
        expected_result.append("| Name    | Age   | Country   | Data      |")
        expected_result.append("| ------- | ----- | --------- | --------- |")
        expected_result.append("| John    | 28    | USA       | USA       |")
        expected_result.append("| Emily   | 32    | Canada    | Canada    |")
        expected_result.append("| Tom     | 25    | UK        | UK        |")
        expected_result.append("| JC      | 2     | DE        | 3434243   |")
        
        table = ConsoleFormatter(data).to_table()
        
        self.assertTrue(expected_result[0] in table)
        self.assertTrue(expected_result[1] in table)
        self.assertTrue(expected_result[2] in table)
        self.assertTrue(expected_result[3] in table)
        self.assertTrue(expected_result[4] in table)
        self.assertTrue(expected_result[5] in table)
        
    def test_pandas_toMarkdown(self):
        data = {
            "Name": ["John", "Emily", "Tom", "JC"],
            "Age": [28, 32, 25, 2],
            "Country": ["USA", "Canada", "UK", "DE"],
            "Data": ["USA", "Canada", "UK", "3434243"]
        }
        
        expected_result = []
        expected_result.append("| Name    | Age   | Country   | Data      |")
        expected_result.append("| ------- | ----- | --------- | --------- |")
        expected_result.append("| John    | 28    | USA       | USA       |")
        expected_result.append("| Emily   | 32    | Canada    | Canada    |")
        expected_result.append("| Tom     | 25    | UK        | UK        |")
        expected_result.append("| JC      | 2     | DE        | 3434243   |")
        
        df = pd.DataFrame(data)
        table = ConsoleFormatter(df).to_table()
        
        self.assertTrue(expected_result[0] in table)
        self.assertTrue(expected_result[1] in table)
        self.assertTrue(expected_result[2] in table)
        self.assertTrue(expected_result[3] in table)
        self.assertTrue(expected_result[4] in table)
        self.assertTrue(expected_result[5] in table)        
        
        
    def test_toSql(self):
        data = {
            "Name": ["John", "Emily", "Tom", "JC"],
            "Age": [-28, 3002.6, 25, 2],
            "Country": ["USA", "Canada", "UK", "DE"],
            "Data": ["USA", "Canada", "UK", "3434243"]
        }
        
        expected_result = []
        expected_result.append("INSERT INTO dd (Name, Age, Country, Data) VALUES ('John', -28, 'USA', 'USA');")
        expected_result.append("INSERT INTO dd (Name, Age, Country, Data) VALUES ('Emily', 3002.6, 'Canada', 'Canada');")
        expected_result.append("INSERT INTO dd (Name, Age, Country, Data) VALUES ('Tom', 25, 'UK', 'UK');")
        expected_result.append("INSERT INTO dd (Name, Age, Country, Data) VALUES ('JC', 2, 'DE', 3434243);")
        
        table = ConsoleFormatter(data).to_sql('dd')
        
        self.assertTrue(expected_result[0] in table)
        self.assertTrue(expected_result[1] in table)
        self.assertTrue(expected_result[2] in table)
        self.assertTrue(expected_result[3] in table)        
        

if __name__ == '__main__':
    unittest.main()
    


