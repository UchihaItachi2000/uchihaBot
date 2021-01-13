xlpath="C:\\Users\\mphpamatrasu2000\\Desktop\\uchihaBot\\test.xlsx"
import openpyxl
wb=openpyxl.load_workbook(xlpath)
print(wb.get_sheet_names())
sh=wb['Sheet1']
sh.cell(row=1,column=1).value="125"
wb.save(xlpath)
