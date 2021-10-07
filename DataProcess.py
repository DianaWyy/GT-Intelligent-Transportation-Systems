import xlsxwriter

#open data text file
inputFile = open("1805.stp.txt", "r")

#create a new excel workbook
workbook = xlsxwriter.Workbook('Script.xlsx')

#add a new worksheet to the workbook
worksheet = workbook.add_worksheet()

row = 0
col = 0
name = ''

#read lines in the input file and put them into cells in the excel file
for line in inputFile:
    line.strip()
    lst = line.split()
    for data in lst:
        if(row != 0 and col == 2 and data[-1] not in '0123456789'):
                col -= 1
                name += data + ' '
        elif(row != 0 and col == 2):
                worksheet.write(row, col, name)
                col += 1
                name = ''
                worksheet.write(row, col, data)
        else:
                worksheet.write(row, col, data)
        col += 1
    row += 1
    col = 0

#close files
inputFile.close()
workbook.close()
