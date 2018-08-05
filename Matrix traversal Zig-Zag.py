ROW = 5
COL = 4
 
def diagonalOrder(matrix) :
    li=[]
    lilarge=[]
    for line in range(1, (ROW + COL)) :
        li=[]
        start_col = max(0, line - ROW)       
        count = min(line, (COL - start_col), ROW)
        for j in range(0, count) :
            li.append(matrix[min(ROW, line) - j - 1]
                        [start_col + j])
 
        if(line%2==0):
           li.reverse()
        for kl in li:
            lilarge.append(kl)
         
    print(lilarge)
    
    
def printMatrix(matrix) :
    for i in range(0, ROW) :
        for j in range(0, COL) :
            print(matrix[i][j], end = "\t")
             
        print()
    

    
# Driver COde
M = [ [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20] ]
print("Given matrix is ")
printMatrix(M)
 
print ("\nDiagonal printing of matrix is ")
diagonalOrder(M)
 
