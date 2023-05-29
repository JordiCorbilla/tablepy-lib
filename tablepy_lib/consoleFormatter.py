#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Jordi Corbilla
# Created Date: 2023
# version ='1.0'
# ---------------------------------------------------------------------------

import pandas as pd

class ConsoleFormatter:
    def __init__(self, data):
        if isinstance(data, dict):
            if not data:
                raise ValueError("Invalid input data type. Supported types are dictionary and pandas DataFrame.")
            self.data = data
        elif isinstance(data, pd.DataFrame):
            self.data = data.to_dict('list')
            if data.empty:
                raise ValueError("Invalid input data type. Supported types are dictionary and pandas DataFrame.")
        else:
            raise ValueError("Invalid input data type. Supported types are dictionary and pandas DataFrame.")

    def to_table(self):
        col_names = list(self.data.keys())
        row_data = [list(map(str, self.data[key])) for key in col_names]
        formatted_data = row_data

        # Column width calculation
        col_widths = [0 for col in col_names]

        # header size calculation
        for i in range(len(col_names)):
            size = len(col_names[i]) + 2
            if size > col_widths[i]:
                col_widths[i] = size

        rows = len(row_data[0])
        columns = len(col_names)

        for row in range(rows):
            for column in range(columns):
                size = len(formatted_data[column][row]) + 2
                if (size > col_widths[column]):
                    col_widths[column] = size
        
        # Add extra width for table borders and separators

        table_formatted = "\n"

        header = "| "
        for i in range(len(col_names)):
            size = col_widths[i] - len(col_names[i])
            filler = " " * size
            header += col_names[i] + filler + " | "

        table_formatted += header + "\n"

        line = "| "
        for i in range(len(col_names)):
            size = col_widths[i]
            filler = "-" * size
            line += filler + " | "

        table_formatted += line + "\n"

        ta = ""
        
        for row in range(rows):
            data = "| "
            for column in range(columns):
                size = col_widths[column] - len(formatted_data[column][row])
                filler = " " * size
                data += formatted_data[column][row] + filler + " | " 
            ta += data + "\n"
            
        table_formatted += ta  + "\n"
        return table_formatted
    
    def to_sql(self, table_name):
        col_names = list(self.data.keys())
        row_data = [list(map(str, self.data[key])) for key in col_names]
        formatted_data = row_data
    
        rows = len(row_data[0])
        columns = len(col_names)
    
        insert = f"INSERT INTO {table_name} ("
        insert += ', '.join(map(str, self.to_sql_column(col_names)))
        insert += ") VALUES ("
        
        data = ""
        
        for row in range(rows):
            data += insert
            for column in range(columns):
                data += self.to_sql_field(formatted_data[column][row]) + ", " 
            data += ");\n"
            data = data.replace(', )', ')')
            
        return data 

    def to_sql_column(self, fields):
        col_names = list(fields)
        for i in range(len(fields)):
            if col_names[i].find(' ') > 0:
                col_names[i] = f"[{col_names[i]}]"
        return col_names
    
    def to_sql_field(self, data):
        formatted_value = ""
        
        # test for numeric
        try:
            value = int(data)
            formatted_value = str(value)
            return formatted_value
        except:
            pass
        
        try:
            value = float(data)
            formatted_value = str(value)
            if ',' in formatted_value:
                formatted_value = formatted_value.replace(',', '')
            return formatted_value
        except:
            pass
        
        formatted_value = "'" + data.replace("'", "''") + "'"
        return formatted_value

    
def markdown(data):
    return ConsoleFormatter(data).to_table()

def sql_insert(data):
    return ConsoleFormatter(data).to_sql()