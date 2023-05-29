# tablepy Lib

This is a versatile and user-friendly Python table library that can quickly render any Dictionary{key, []} or DataFrame into a visually appealing markdown or sql insert

## Usage - Markdown

```python
data = {
    "Name": ["John", "Emily", "Tom", "JC"],
    "Age": [-28, 3002.6, 25, 2],
    "Country": ["USA", "Canada", "UK", "DE"],
    "Data": ["USA", "Canada", "UK", "3434243"]
}

formatter = consoleFormatter(data)
table = formatter.to_table()
print(table)    
```

Sample output:

```
| Name    | Age      | Country   | Data      | 
| ------- | -------- | --------- | --------- | 
| John    | -28.0    | USA       | USA       | 
| Emily   | 3002.6   | Canada    | Canada    | 
| Tom     | 25.0     | UK        | UK        | 
| JC      | 2.0      | DE        | 3434243   | 
```

| Name    | Age      | Country   | Data      | 
| ------- | -------- | --------- | --------- | 
| John    | -28.0    | USA       | USA       | 
| Emily   | 3002.6   | Canada    | Canada    | 
| Tom     | 25.0     | UK        | UK        | 
| JC      | 2.0      | DE        | 3434243   | 

## Usage - SQL Insert

```python
data = {
    "Name": ["John", "Emily", "Tom", "JC"],
    "Age": [-28, 3002.6, 25, 2],
    "Country": ["USA", "Canada", "UK", "DE"],
    "Data": ["USA", "Canada", "UK", "3434243"]
}

data_frame = pd.DataFrame(data)
table = sql_insert(data_frame, 'dd')
print(table)

```

Sample output:

```
INSERT INTO dd (Name, Age, Country, Data) VALUES ('John', -28.0, 'USA', 'USA');
INSERT INTO dd (Name, Age, Country, Data) VALUES ('Emily', 3002.6, 'Canada', 'Canada');
INSERT INTO dd (Name, Age, Country, Data) VALUES ('Tom', 25.0, 'UK', 'UK');
INSERT INTO dd (Name, Age, Country, Data) VALUES ('JC', 2.0, 'DE', 3434243);
```
