from RREF import *
from MatrixMulti import *

# Function to compute the null space of a matrix
def nullSpace(M):
    # Perform row reduction on M1
    M1 = rref(M)
    
    # Initialize variables for tracking pivots and free variables
    null = []
    types = []
    ind = []
    numFree = 0
    
    # Iterate through columns of M1 to identify pivots and free variables
    for i in range(len(M1[0])):
        curr = findPiviot(M1,i)
        if not curr:
            numFree += 1
            ind.append(i)
        types.append(curr)
    
    # If there are no free variables, the null space is just the zero vector
    if numFree == 0:
        return [0]
    
    # Create identity matrix with size equal to number of free variables
    ident = makeIdent(numFree)
    
    # Compute the null space by constructing vectors that satisfy Ax = 0
    for i in range(numFree):
        null.append([])
        count = 0 
        for j in range(len(M1[0])):
            if (not types[j]):
                null[i].append(ident[i][count])
                count += 1
            else:
                null[i].append(-1 * M1[j][ind[i]])
    
    # Transpose the null space to return a list of column vectors
    return transpose(null)

# Function to transpose a matrix
def transpose(matrix):
    ret =[]
    for i in range(len(matrix[0])):
        ret.append([])
        for j in range(len(matrix)):
            ret[i].append(matrix[j][i])
    return ret

# Function to create an identity matrix of size n x n
def makeIdent(n):
    ret = []
    for i in range(n):
        ret.append([])
        for j in range(n):
            if i == j:
                ret[i].append(1)
            else:
                ret[i].append(0)
    return ret

# Function to identify pivots in a matrix
def findPiviot(Matrix, col):
    count = 0
    for row in Matrix:
        if row[col] != 0 and row[col] != 1:
            return False
        if row[col] != 0:
            count += 1
        if count > 1:
            return False
    return True

if __name__ == "__main__":
    # Test matrix
    M1 = generate_random_matrix(random.randint(1, 30),random.randint(1, 30))
    # Compute null space of M1
    M2 = nullSpace(M1)
    M1 = rref(M1)
    # Print original matrix M1
    for row in M1:
        for elem in row:
            if elem == 0:
                elem = 0
            print(elem, end=' ')
        print()
    
    # Print null space of M1
    print("Null Space")
    if(len(M2)==1):
        print(M2)
    else:
        for row in M2:
            for elem in row:
                if elem == 0:
                    elem = 0
                print(elem, end=' ')
            print()
    
    # Check if the null space calculation is correct
    if(len(M2)==1):
        print('Just an identity matrix')
    else:
        M3 = matrixMulti(M1, M2)
        print("Is it correct")
        for row in M3:
            for elem in row:
                print(elem, end=' ')
            print()
