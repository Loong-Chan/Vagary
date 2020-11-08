import time
import openpyxl
import sklearn


t1 = time.time()
df = pd.read_excel('奶嘴训练集.txt', sheetname='Sheet1', header=None)
df.to_csv('file2.txt', header=None, sep=',', index=False)
f = open("file2.txt")
f.close()
t2 = time.time()


t3 = time.time()
wb = openpyxl.load_workbook("奶嘴训练集.xlsx")
wb.close()
t4 = time.time()


print(t2 - t1)
print(t4 - t3)
