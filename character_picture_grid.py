# Character Grid Printing using Python

grid = [['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]


for i in range(len(grid[0])): # grid[0]= 8 integers taken as in range
    print()
    for j in range(len(grid)):
        print(grid[j][i], end = '')

for i in range(len(grid[0])): # range(5) will increase every time with 1
    print() # will create a new line every time after each iteration
    for j in range(len(grid)): # range(8) will increase every time with 1
        print((j,i), end = '') #first iteration will be like (j = 0, i = 0)


# for i in range(3):
#     print("First for Loop.")
#     for j in range(5):
#         print("Second Loop.")

# for i in range(5): # In the loop under loop construction the first loop starts but then the inner loop takes control and then the first loop will only iterate when the inner loop finish its iteration and it will till for the inner loop to end his iteration. This is the best which can easily prove the statement.
#     print() # it is to make new line for every iteration so that we can get the desired output in the desired format
#     for j in range(8):
#         print((j,i ), end = '')