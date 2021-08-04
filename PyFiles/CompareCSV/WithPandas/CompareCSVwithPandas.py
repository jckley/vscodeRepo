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

print(f"************OUTER JOIN ALL - LEFT+RIGHT+IN = ********** \n {result1}")
print("----------------------------------------------------------")
print(f"************OUTER JOIN - LEFT+RIGHT = ********** \n {result2}")
print("----------------------------------------------------------")
print(f"************OUTER JOIN - ONLY INNER MATCHED = ********** \n {result3}")
