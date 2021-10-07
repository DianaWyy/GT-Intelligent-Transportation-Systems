import xlsxwriter

inputFile = open("1805.stp.txt", "r")
workbook = xlsxwriter.Workbook('Script.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
name = ''
for line in inputFile:
    line.strip()
    Lst = line.split()
    for data in Lst:
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
inputFile.close()
workbook.close()
