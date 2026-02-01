
import openpyxl

def excelreader(path, sheet_name):
    wb = openpyxl.load_workbook(path)
    sheet=wb[sheet_name]
    data=[]
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data
