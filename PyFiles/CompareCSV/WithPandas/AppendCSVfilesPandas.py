# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 06:56:16 2019
@author: Chris
"""
# credited:
# https://stackoverflow.com/questions/9234560/find-all-csv-files-in-a-directory-using-python/12280052

import os
import glob
import pandas as pd

# set working directory
os.chdir("/Users/juancarloskleylein/Downloads/CombineCSVs/")

# find all csv files in the folder
# use glob pattern matching -> extension = 'csv'
# save result in list -> all_filenames
# assumes all csvs have the same columns and header names
extension = "csv"
all_filenames = [i for i in glob.glob("*.{}".format(extension))]
# print(all_filenames)
x = 0
for i in all_filenames:
    print(f"CSV ({x}) = {i}")
    x += 1
# Specify the fields to be read
# col_list = ["Id", "First Name", "Email"]
col_list = pd.read_csv(
    all_filenames[0], nrows=1
).columns  # reads the headers of the first CSV
# print(col_list)
x = 0
for i in col_list:
    print(f"FIELD ({x}) = {i}")
    x += 1
# combine all files in the list - specified fields must be in each csv
combined_csv = pd.concat([pd.read_csv(f, usecols=col_list) for f in all_filenames])
# export to csv
combined_csv.to_csv("OUTPUT_Combined_csv.csv", index=False, encoding="utf-8-sig")
