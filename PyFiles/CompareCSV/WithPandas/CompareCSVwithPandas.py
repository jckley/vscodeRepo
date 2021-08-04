import pandas as pd

csv_FilesPath = '/Users/juancarloskleylein/Downloads/AWS_CSV/'
data1 = csv_FilesPath + 'Data1.csv'
data2 = csv_FilesPath + 'Data2.csv'

df_Left = pd.read_csv(data1)
df_Right = pd.read_csv(data2)


result1 = df_Left.merge(df_Right, indicator=True,
                        how='outer')
result2 = df_Left.merge(df_Right, indicator=True,
                        how='outer').loc[lambda v: v['_merge'] != 'both']

result3 = df_Left.merge(df_Right, indicator=True,
                        how='outer').loc[lambda v: v['_merge'] == 'both']

indexLeft, indexRight = df_Left.index, df_Right.index
number_of_rowsLeft = len(indexLeft)
print(f" CANTIDAD REGISTROS LEFT_DF = {number_of_rowsLeft}")
number_of_rowsRight = len(indexRight)
print(f" CANTIDAD REGISTROS RIGHT_DF = {number_of_rowsRight}")

print("----------------------------------------------------------")
index1 = result1.index
number_of_rows1 = len(index1)
print(f" CANTIDAD REGISTROS = {number_of_rows1}")
print(f"************OUTER JOIN ALL - LEFT+RIGHT+IN = ********** \n {result1}")

print("----------------------------------------------------------")
index2 = result2.index
number_of_rows2 = len(index2)
print(f" CANTIDAD REGISTROS = {number_of_rows2}")
print(f"************OUTER JOIN - LEFT+RIGHT = ********** \n {result2}")
print("----------------------------------------------------------")
index3 = result3.index
number_of_rows3 = len(index3)
print(f" CANTIDAD REGISTROS = {number_of_rows3}")
print(f"************OUTER JOIN - ONLY INNER MATCHED = ********** \n {result3}")
