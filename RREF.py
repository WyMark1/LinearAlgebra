import copy
import random

# Function to perform row reduction to echelon form
def rref(M):
    # Calculate number of pivots
    M1 = copy.deepcopy(M)
    if len(M1[0]) < len(M1):
        numPiv = len(M1[0])
    else:
        numPiv = len(M1[0]) - abs(len(M1) - len(M1[0]))
    # Initialize row counter
    row = 0
    # Loop over columns
    for i in range(len(M1[0])):
        # Check if all pivots have been found
        if row == numPiv:
            break
        # Initialize loop variables
        done = False
        count = 0
        # Find pivot or swap rows if necessary
        while not done and i + count < len(M1):
            if M1[row][i] == 1:
                done = True
            elif M1[row + count][i] == 1:
                temp = M1[row + count][i]
                M1[row + count][i] = M1[row][i]
                M1[row][i] = temp
                done = True
            count += 1
        # If pivot is 0, swap with nonzero row if possible
        if M1[row][i] == 0:
            rowval = findNonZero(M1, i, row)
            if rowval is not None:
                temp = M1[row][i]
                M1[row][i] = M1[rowval][i]
                M1[rowval][i] = temp
            else:
                continue
        # Divide row by pivot
        if M1[row][i] != 1:
            M1[row] = VectorMulti(M1[row], 1/M1[row][i])
        # Make the column i all zeros except the pivot
        for j in range(len(M1)):
            if row == j:
                k = 0
            else:
                VectorAdd(VectorMulti(M1[row], -1 * M1[j][i]), M1[j])
        # Increment row counter
        row += 1
    return M1

# Function to find the first nonzero entry in a column
def findNonZero(matrix, colval, startval):
    for i in range(startval, len(matrix)):
        if matrix[i][colval] != 0:
            return i
    return None

# Function to multiply a vector by a scalar
def VectorMulti(vec, fac):
    # Make a deep copy of the input vector to avoid modifying it
    ret = copy.deepcopy(vec)
    # Multiply each entry by the scalar
    for i in range(len(vec)):
        ret[i] = vec[i] * fac   
        ret[i]=round(ret[i],5)
    return ret

# Function to add two vectors
def VectorAdd(V1, V2):
    # Add each entry of the first vector to the corresponding entry of the second vector
    for i in range(len(V1)):
        V2[i] += V1[i]
        V2[i]=round(V2[i],5)

def generate_random_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(random.randint(0, 100))
        matrix.append(row)
    return matrix

# Main program
if __name__ == "__main__":
    # Test matrix

    M = generate_random_matrix(random.randint(1, 30),random.randint(1, 30))
    # Perform row reduction
    for row in M:
        print(row)
    M1 = rref(M)
    # Print result
    for row in M1:
        for elem in row:
            #elem = round(elem,5)
            if elem == 0:
                elem =0
            print(elem,end=' ')
        print()




