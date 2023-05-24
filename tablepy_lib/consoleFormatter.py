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
        rows = [list(map(str, self.data[key])) for key in col_names]
        formatted_data = [col_names] + rows

        # Column width calculation
        col_widths = [0 for col in formatted_data[0]]

        # header size calculation
        for i in range(len(col_names)):
            size = len(col_names[i]) + 2
            if size > col_widths[i]:
                col_widths[i] = size

        items = len(rows[0]) - 1
        #print(items)

        # Data size calculation
        for i in range(items):
            for j in range(len(rows)):
                # print(formatted_data[j][i+1])
                size = len(formatted_data[j][i+1]) + 2
                if (size > col_widths[i]):
                    col_widths[i] = size

        # Add extra width for table borders and separators
        # print(formatted_data[0])

        table_formatted = "\n"

        header = "| "
        for i in range(len(formatted_data[0])):
            size = col_widths[i] - len(formatted_data[0][i])
            filler = " " * size
            header += formatted_data[0][i] + filler + " | "

        table_formatted += header + "\n"

        line = "| "
        for i in range(len(formatted_data[0])):
            size = col_widths[i]
            filler = "-" * size
            line += filler + " | "

        table_formatted += line + "\n"

        items = len(rows[0])

        print(col_widths)

        ta = ""
        for i in range(items):
            
            data = "| "
            for j in range(len(rows)):
                print(formatted_data[j][i+1])
                size = col_widths[j] - len(formatted_data[j][i+1])
                filler = " " * size
                data += formatted_data[j][i+1] + filler + " | "
            ta += data + "\n"
            
        table_formatted += ta  + "\n"
        return table_formatted

    
    
data = {
    "Name": ["John", "Emily", "Tom"],
    "Age": [28, 32, 25],
    "Country": ["USA", "Canada", "UK"],
    "Data": ["USA", "Canada", "UK"]
}

formatter = ConsoleFormatter(data)
table = formatter.to_table()
print(table)    

data_frame = pd.DataFrame(data)

formatter = ConsoleFormatter(data_frame)
table = formatter.to_table()
print(table)



# col_names = list(data.keys())
# # print(col_names)
# rows = [list(map(str, data[key])) for key in col_names]
# # print(rows)
# formatted_data = [col_names] + rows
# # print(formatted_data)
# col_widths = [max(len(str(item))+2 for item in col) for col in formatted_data]
# # print(col_widths)


# # Column width calculation
# col_widths = [0 for col in formatted_data[0]]
# # print(col_widths)

# # header size calculation
# for i in range(len(formatted_data[0])):
#     size = len(formatted_data[0][i]) + 2
#     if size > col_widths[i]:
#         col_widths[i] = size
# # print(col_widths)


# items = len(formatted_data[0])

# # Data size calculation
# for i in range(items):
#     for j in range(len(rows)):
#         size = len(formatted_data[i+1][j]) + 2
#         # print(formatted_data[i+1][j]) 
#         # print(size) 
#         if (size > col_widths[i]):
#             col_widths[i] = size
# # print(col_widths)

# # Add extra width for table borders and separators
# # print(formatted_data[0])

# table_formatted = "\n"

# header = "| "
# for i in range(len(formatted_data[0])):
#     size = col_widths[i] - len(formatted_data[0][i])
#     filler = " " * size
#     header += formatted_data[0][i] + filler + " | "

# table_formatted += header + "\n"
# #print(header)

# line = "| "
# for i in range(len(formatted_data[0])):
#     size = col_widths[i]
#     filler = "-" * size
#     line += filler + " | "

# table_formatted += line + "\n"
# #print(line)

# items = len(formatted_data[0])

# # header = "| "
# # for item in formatted_data[0]:
# #     header += item + " | "
    


# ta = ""
# for j in range(len(rows)):
#     data = "| "
#     for i in range(items):
#         size = col_widths[i] - len(formatted_data[i+1][j])
#         filler = " " * size
#         data += formatted_data[i+1][j] + filler + " | "
#         #print(formatted_data[i+1][j])
#     ta += data + "\n"
    
# table_formatted += ta  + "\n"

# print(table_formatted)


# # for i in range(items):
# #     data = "| "
# #     for j in range(len(rows)):
# #         size = col_widths[i] - len(formatted_data[i+1][j])
# #         filler = " " * size
# #         data += formatted_data[i+1][j] + filler + " | "
# #         #print(formatted_data[i+1][j])
# #     ta += data + "\n"
    
# # print(ta)

# # n = 1
# # for a in formatted_data:
# #     if n == 1:
# #         print(a)
# #     else:
# #         items = len(formatted_data[n+1])
        
    


# col_widths = [width + 3 for width in col_widths]

# formatted_rows = [" | ".join(item.ljust(width) for item, width in zip(row, col_widths)) for row in formatted_data]

# separator = "-+-".join("-" * width for width in col_widths)
# header = formatted_rows[0]
# table = "\n".join([header, separator] + formatted_rows[1:])

# table_with_borders = f"| {table} |"
# table_width = len(table_with_borders.split('\n')[0])

# border_line = "-" * table_width

# formatted_table = f"{border_line}\n{table_with_borders}\n{border_line}"

#print(formatted_table) 

# formatter = ConsoleFormatter(data_dict)
# table = formatter.to_table()
# print(table)    

# data_frame = pd.DataFrame(data_dict)

# formatter = ConsoleFormatter(data_frame)
# table = formatter.to_table()
# print(table)
# print(data_frame)