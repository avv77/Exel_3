import openpyxl

path = 'D:\\Работа\\Химия\\Хлорид железа\\Импорт_хлорид железа1.xlsx'
wb = openpyxl.load_workbook(path)
sheet = wb.active
quantity_row = sheet.max_row
quantity_column = sheet.max_column
for i in range(1, quantity_row + 1):
    for j in range(1, quantity_column + 1):
        a = sheet.cell(row=i, column=j)
        b = str(a.value)
        for k in b:
            if k == '`':
                c = b.replace('`', '')
                d = sheet.cell(row=i, column=j, value=c)
wb.save('D:\\Работа\\Химия\\Хлорид железа\\Импорт_хлорид железа1_1.xlsx')