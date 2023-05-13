import pandas as pd
import glob
import openpyxl

filepaths = glob.glob("*.xlsx")
print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)