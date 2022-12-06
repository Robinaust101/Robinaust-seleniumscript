from openpyxl import load_workbook

wb = load_workbook('For_read.xlsx')
sheet = wb.active

# Cell Header
print('First cell Name:', sheet['A1'].value)
print('Second cell Name:', sheet['B1'].value)

# Read all data in  single cell
columns = sheet['A']
for data in columns:
    print(data.value)


#wb.save('For_read.xlsx')