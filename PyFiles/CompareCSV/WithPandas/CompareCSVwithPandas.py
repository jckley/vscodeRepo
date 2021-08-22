# https://realpython.com/pandas-merge-join-and-concat/
# https://www.youtube.com/watch?v=6FXQJ-aK5MU

#  USING PANDAS.MERGE

import pandas as pd
import pprint
from tabulate import tabulate
left_CSV = input("Left CSV name ? (without extension) = ")
right_CSV = input("Right CSV name ? (without extension)= ")
output_CSV = input("Output CSV name ? (without extension)= ")


csv_FilesPath = '/Users/juancarloskleylein/Downloads/CompareCSV/'
data1 = csv_FilesPath + left_CSV + '.csv'
data2 = csv_FilesPath + right_CSV + '.csv'

df_Left = pd.read_csv(data1, low_memory=False)
df_Right = pd.read_csv(data2, low_memory=False)


# result1 = df_Left.merge(df_Right, indicator=True,
#                        how='outer')

# result2 = df_Left.merge(df_Right, indicator=True,
#                        how='outer').loc[lambda v: v['_merge'] != 'both']

# PYTHON LOC
# EJEMPLO =   loc[lambda x : x['_merge']=='left_only']
# loc accepts (among other things) a one-argument callable that is called on each row.
# The callable is expected to return something that can be used as an index (in this case, a boolean).
# Effectively, this syntax means "for each row x in the merged dataframes, call the lambda on the row and select it if
# x['_merge'] == 'left_only'.
# es decir lambda x: devuelve x == true o x == false depende de si el contenido del campo '_merge' para esa fila es == 'left_only' o no
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
# since no "on= Key_field"  is defined, then columns from the two DataFrames that share names will be used as join keys.
# result3 = df_Left.merge(df_Right, indicator=True,how='outer').loc[lambda v: v['_merge'] == 'both']


#result3 = df_Left.merge(df_Right, indicator=True, how='inner', on=['Email']).loc[lambda v: v['_merge'] == 'both']

result3 = df_Left.merge(df_Right, indicator=True, how='inner',
                        left_on='Email Address', right_on='Email').loc[lambda v: v['_merge'] == 'both']
# result4 = df_Left.merge(df_Right, indicator=True, how='outer',
#                      left_on='Email Address', right_on='Email').loc[lambda v: v['_merge'] == 'both']

indexLeft, indexRight = df_Left.index, df_Right.index
number_of_rowsLeft = len(indexLeft)
print(f" CANTIDAD REGISTROS LEFT_DF = {number_of_rowsLeft}")
number_of_rowsRight = len(indexRight)
print(f" CANTIDAD REGISTROS RIGHT_DF = {number_of_rowsRight}")

""" print("----------------------------------------------------------")
index1 = result1.index
number_of_rows1 = len(index1)
print(f" CANTIDAD REGISTROS = {number_of_rows1}")
print(f"************OUTER JOIN ALL - LEFT+RIGHT+IN = ********** \n {result1}")

print("----------------------------------------------------------")
index2 = result2.index
number_of_rows2 = len(index2)
print(f" CANTIDAD REGISTROS = {number_of_rows2}")
print(f"************OUTER JOIN - LEFT+RIGHT = ********** \n {result2}") """

print("----------------------------------------------------------")
index3 = result3.index
number_of_rows3 = len(index3)
# display.max_rows and display.max_columns  ---> Sets the display of rows and columns of a dafaframe
pd.set_option("max_columns", 10)

print(f" CANTIDAD REGISTROS = {number_of_rows3}")
# print(f"************OUTER JOIN - ONLY INNER MATCHED = ********** \n {result3}")
print(f"************OUTER JOIN - ONLY INNER MATCHED = ********** \n")
print(tabulate(result3, headers="keys"))
result3.to_csv(output_CSV,
               index=False, encoding='utf-8-sig')


# print(f"************OUTER JOIN - LEFT+RIGHT = ********** \n {result4}")
