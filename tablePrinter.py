tableData = [['apples', 'oranges', 'cherries', 'banana'], 
['Alice', 'Bob', 'Carol', 'David'], 
['dogs', 'cats', 'moose', 'goose']]

rowCount = len(tableData)
# print(rowCount) 3
columnCount = len(tableData[0])
# print(columnCount) 4


#figuring out the right width for each column
columnWidth = [0] * len(tableData)
# print(columnWidth)

#checking the longest item with looping in each row
for row in range(rowCount):
    for column in range(columnCount):
        if len(tableData[row][column]) > columnWidth[row]:
            columnWidth[row] = len(tableData[row][column])

print(columnWidth)


for column in range(columnCount):
    print()
    for row in range(rowCount):
        print(tableData[row][column].rjust(columnWidth[row]), end = ' ')