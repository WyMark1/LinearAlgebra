from RREF import *
from MatrixMulti import *
from NullSpace import *
from numpy.polynomial import polynomial as P

# Function to find eigenvalues of a square matrix
def findEigenValue(M1):
    # Check if the input matrix is square
    if len(M1[0])!=len(M1):
        print("Not Valid")
        return False
    
    # Initialize variables for iteration
    curVec = []
    curMatrix = []
    # Create initial vector of column indices
    for i in range(len(M1[0])):
        curVec.append([])
        curVec[i].append(i+1)
    # Initialize variables to check for free columns
    hasFreeColumn = False
    curMatrix = curVec.copy()
    # Iterate until a free column is found
    while not hasFreeColumn:
        # Compute the next vector by multiplying M1 with the previous vector
        curVec = matrixMulti(M1,curVec)
        # Add the new vector to the current matrix
        addVectorToMatrix(curMatrix,curVec)
        # Compute the RREF of the current matrix to check for free columns
        M = rref(curMatrix)
        if hasFree(M):
            hasFreeColumn = True
    # Compute the null space of the current matrix to obtain eigenvectors
    curMatrix = nullSpace(curMatrix)
    # Compute the polynomial coefficients to obtain eigenvalues
    ret = []
    for i in range(len(curMatrix)-1,0,-1):
        ret.append(curMatrix[i][0])
    return P.polyroots(ret)

# Function to check if a matrix has a free column
def hasFree(M1):
    for i in range(len(M1[0])):
        if not findPiviot(M1,i):
            return True
    return False

# Function to combine two vectors into a matrix
def vectorsToMatrix(V1,V2):
    ret =[]
    for i in range(len(V1)):
        ret.append([])
        ret[i].append(V1[i][0])
        ret[i].append(V2[i][0])
    return ret

# Function to add a vector to a matrix
def addVectorToMatrix(M1,V1):
    for i in range(len(V1)):
        M1[i].append(V1[i][0])

# Function to generate a random square matrix
def generate_random_SQmatrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(0, 100))
        matrix.append(row)
    return matrix

if __name__ == "__main__":
    # Generate a random square matrix and find its eigenvalues
    M1 = generate_random_SQmatrix(random.randint(2, 30))
    print(findEigenValue(M1))
