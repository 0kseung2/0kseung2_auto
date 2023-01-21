from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) #8번째 줄이 비워짐
# ws.insert_rows(8, 5) #8번째 줄에 5줄이 추가됨

# ws.insert_cols(2) #B번쩨 열이 비워짐
ws.insert_cols(2, 3)#B번째 열로부터 3칸 추가




wb.save("sample_insert_cols.xlsx")