import openpyxl  #to handle xls/xlsx files

#read in data
wb = openpyxl.load_workbook('test.xlsx',
	read_only=True)

#get the names of 'sheets'
print(wb.get_sheet_names())
#get the first sheet
sheet = wb['Sheet1']
#print contents of cell B2 on sheet1
print(sheet['B2'].value)
r = 0            #keep track of rows
#go through all rows
for c in sheet.rows:
	print(r)      #print the row number
	#print cells in each row
	for i in range(len(c)):
		print('\t',c[i].value)
	r += 1

