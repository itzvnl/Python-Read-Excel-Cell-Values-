import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Data Sheet1')
print sheet['A1']

print sheet['A1'].value

c = sheet['B1']
print c.value

print 'Row' + str(c.row) + ', column ' + c.column + 'is' + c.value

print 'Cell' + c.coordinate + 'is'+ c.value

print sheet['C1'].value
