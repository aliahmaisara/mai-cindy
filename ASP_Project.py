import numpy as np
import  pandas as pd
import matplotlib as plt
import openpyxl as pyx


dataframe = pd.read_excel(r'Project_File.xlsx')

#rename the column
dataframe = dataframe.rename(columns= {'   ':'date'})
print(dataframe)