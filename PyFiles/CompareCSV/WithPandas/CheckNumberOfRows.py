import pandas as pd

input_CSV = input("Input CSV name ? (without extension) = ")

csv_FilesPath = "/Users/juancarloskleylein/Downloads/"
data1 = csv_FilesPath + input_CSV + ".csv"


df_data1 = pd.read_csv(data1, low_memory=False)

index_data1 = df_data1.index
number_of_rowsLeft = len(index_data1)
print(
    "----------------------------------RESULT-----------------------------------------------"
)
print(f" CANTIDAD REGISTROS del archivo --> {input_CSV}.csv = {number_of_rowsLeft}")
print(
    "----------------------------------END-----------------------------------------------"
)

