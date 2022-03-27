import os
import openpyxl

main_dir = os.path.dirname(__file__)
path = os.path.join(main_dir, 'doc_excel.xlsx')

wb = openpyxl.load_workbook(path)

# print(wb.active)
sheet1 = wb['Sheet1']

print(sheet1['C3'].value)
