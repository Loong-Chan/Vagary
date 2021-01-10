import time
import openpyxl

import pandas as pd
import os
import sys


def transToTxt(ExcelName, SheetName):
    '''
    在excel所在的同一级目录下创建一个转换之后的txt文件
    '''
    path = os.getcwd() + "\\" + ExcelName
    sheet = pd.read_excel(path, sheet_name=SheetName, header=None)
    sheet.to_csv('file2.txt', header=None, sep=',', index=False)


'''
t1 = time.time()
df = pd.read_excel('./QuickExcelRW/TestSet.xlsx',
                   sheet_name='Sheet1', header=None)
df.to_csv('file2.txt', header=None, sep=',', index=False)
f = open("file2.txt")
f.close()
t2 = time.time()


t3 = time.time()
wb = openpyxl.load_workbook("./QuickExcelRW/TestSet.xlsx")
wb.close()
t4 = time.time()


print(t2 - t1)
print(t4 - t3)
'''



print(sys.argv[0])
