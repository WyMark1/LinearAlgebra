import copy

def matrixMulti(M1, M2):
    # Check if matrix multiplication is valid
    if len(M1[0]) != len(M2):
        print("Not Valid Matrix")
    # Initialize result matrix with zeros
    ret = []
    for i in range(len(M1)):
        ret.append([])
        for j in range(len(M2[0])):
            ret[i].append(0)
    # Perform matrix multiplication
    for i in range(len(M2[0])):
        temp = 0
        # Create a deep copy of M1 to avoid changing it
        M3 = copy.deepcopy(M1)
        for j in range(len(M1[0])):
            for k in range(len(M1)):
                # Multiply corresponding elements of M1 and M2
                M3[k][j] *= M2[j][i]
        for arr in range(len(M3)):
            # Add the elements in the resulting row to get the value in the result matrix
            ret[arr][i] = arrayAdd(M3[arr])
    return ret

def arrayAdd(ar):
    # Helper function to add up the elements in an array
    ret = 0
    for i in ar:
        ret += i
    return ret

if __name__ == "__main__":
    # Test matrices
    M1 = [[1,2,3],[4,5,6]]
    M2 = [[1],[2],[3]]
    # Perform matrix multiplication and print result
    print(matrixMulti(M1,M2))
