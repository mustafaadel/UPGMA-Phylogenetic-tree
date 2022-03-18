import sys
n = int(input("Enter the number of sequences:"))
Matrix = [[] for _ in range(n)]
for i in range(n):
    row = []
    for j in range(i):
        if i == 0:
            continue
        s = float(input(f"Enter the distance (Row {chr(ord('A')+i)}, Column {chr(ord('A')+j)}): "))
        row.append(s)
    Matrix[i] = row

def character_creater(n):
    global characters
    characters = []
    for i in range(ord("A"), ord("A") + n):
        characters.append((chr(i)))
    return characters

def concatenate_characters(characters,x,y):
    characters[x] = "("+ characters[x]+","+characters[y] + ")"
    del characters[y]
    print(characters)
def min_cell(matrix): # get the lowest cell in the matrix
    min = sys.maxsize
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min and matrix[i][j] != 0:
                min = matrix[i][j]
                x,y = i,j
    print("The minimum cell is:",min, "found at:",x,y )

    return x,y
def compare_index(x,y):
    if y < x:
        return y, x
    else:
        return x, y
def update_seqs(matrix, x, y):
    # Build the new row
    New_Row = []
    #print(x,y)
    for i in range(0, x):
        New_Row.append((matrix[x][i] + matrix[y][i]) / 2)
    matrix[x] = New_Row
    # Build the new column
    for i in range(x + 1, y):
        matrix[i][x] = (matrix[i][x] + matrix[y][i]) / 2

    # Get the rest of the values from row i
    for i in range(y + 1, len(matrix)):
        matrix[i][x] = (matrix[i][x] + matrix[i][y]) / 2
        # Delete the second index column
        del matrix[i][y]

    # Delete the row second index row
    del matrix[y]
    if len(matrix)>1:
        print(matrix)

def tree(matrix):
    print(matrix)
    # Stopping condition
    while len(matrix) > 1:
        x, y = min_cell(matrix)
        x, y = compare_index(x, y)
        concatenate_characters(characters, x, y)
        update_seqs(matrix, x, y)

character_creater(n)
tree(Matrix)