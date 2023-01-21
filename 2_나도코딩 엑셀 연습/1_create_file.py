from openpyxl import load_workbook
wb = load_workbook("연습파일.xlsx")
ws = wb.active


for row in tuple(ws.rows):
    print(row[1].value)
        
        













wb.save("연습파일.xlsx")