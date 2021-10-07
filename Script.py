# import xlsxwriter

# inputFile = open("1805.stp.txt", "r")
# dataList = []
# for line in inputFile:
#     line.strip()
#     Lst = line.split()
#     for data in Lst:
#         dataList.append(data)
# inputFile.close()
# workbook = xlsxwriter.Workbook('Script.xlsx')
# worksheet = workbook.add_worksheet()
# row = 0
# col = 0
# for each in dataList:
#     if row == 0 and col == 140:
#         worksheet.write(row, col, null)
#         row += 1
#         col = 0
#         continue
#     if row > 0 and (col == 3 or col == 4) and not(each[-1] in '012345678'):
#         col = 2
#         worksheet.write(row, col, each)
#         col += 1
#         continue
#     worksheet.write(row, col, each)
#     col += 1
#     if col > 0 and col % 140 == 0:
#         row += 1
#         col = 0
# workbook.close()

import xlsxwriter

inputFile = open("1805.stp.txt", "r")
dataList = []
workbook = xlsxwriter.Workbook('Script.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0
for line in inputFile:
    line.strip()
    Lst = line.split()
    for i in range(len(Lst)):
        if(row > 0 and col == 3 and Lst[i][-1] not in '0123456789'):
            col = 2
            Lst[i] = Lst[i-1] + Lst[i]
            worksheet.write(row, col, Lst[i])
            col += 1
        else:
            worksheet.write(row, col, Lst[i])
        col += 1
    row += 1
    col = 0
inputFile.close()
workbook.close()