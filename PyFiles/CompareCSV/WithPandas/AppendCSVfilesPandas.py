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
os.chdir("/Users/juancarloskleylein/Downloads/Pulso2021/T1yT2Enviados/")

# find all csv files in the folder
# use glob pattern matching -> extension = 'csv'
# save result in list -> all_filenames
extension = "csv"
all_filenames = [i for i in glob.glob("*.{}".format(extension))]
print(all_filenames)
# Specify the fields to be read
col_list = ["Id", "First Name", "Email"]
# combine all files in the list - specified fields must be in each csv
combined_csv = pd.concat([pd.read_csv(f, usecols=col_list) for f in all_filenames])
# export to csv
combined_csv.to_csv("T1yT2_combined_csv.csv", index=False, encoding="utf-8-sig")
