import os 
import openpyxl

main_dir = os.path.dirname(__file__)
path = os.path.join(main_dir, 'censuspopdata.xlsx')

wb = openpyxl.load_workbook(path)

sheet = wb['Population by Census Tract']

elements = {}
# for row in range(sheet.max_row + 1):
#     state = sheet['B' + str(row)].value
#     country = sheet['C'+ str(row)].value
#     pop = sheet['D'+ str(row)].value
    
  