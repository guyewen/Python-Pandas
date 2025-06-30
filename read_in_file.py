import pandas as pd

# set max number of rows displayed
# pd.set_option('display.max.rows', None) # display all rows
# pd.options.display.max_rows = None # or like this

# force to show 100 rows
# pd.set_option('display.max_rows', 100)
# pd.set_option('display.min_rows', 100)

# set max number of columns
pd.set_option('display.max.columns', 20)

# import csv
# if your csv does not have header, then you can read like this: pd.read_csv(
# r"C:\PythonProject\PandasProject\Data\countries of the world.csv", header=None, names=['Country', 'Region'])
data_csv = pd.read_csv(r"C:\PythonProject\PandasProject\Data\countries of the world.csv")
# print(data_csv)
# data_csv.info()
# print(data_csv.shape)  # gives total number of rows and columns
# print(data_csv.head(10))  # gives first 10 rows
# print(data_csv.tail(10))  # gives last 10 rows

# import Excel file for a specified sheet
data_excel_sheet = pd.read_excel(r"C:\PythonProject\PandasProject\Data\world_population_excel_workbook.xlsx",
                                 sheet_name='Sheet1')
print(data_excel_sheet)
# print(data_excel_sheet['Rank'])  # gives a specific column
print(data_excel_sheet.loc[229])  # gives a specific row

# import text, in this txt, two rows are separated by a tab
data_txt = pd.read_table(r"C:\PythonProject\PandasProject\Data\countries of the world.txt")
# print(data_txt)
# can also read like below, to specify the separator
# pd.read_csv(r"C:\PythonProject\PandasProject\Data\countries of the world.txt", sep='\t')


# read json file
data_json = pd.read_json(r"C:\PythonProject\PandasProject\Data\json_sample.json")
# print(data_json)
