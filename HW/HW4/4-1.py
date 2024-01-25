import numpy as np

def read_matrices(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().split())
        matrices = []
        for _ in range(n):
            matrix = [list(map(int, file.readline().split())) for _ in range(m)]
            matrices.append(np.array(matrix))
    return matrices

def find_and_invert(matrices):
    max_det = float('-inf')
    selected_matrices = None
 
    for i in range(len(matrices)):
        for j in range(i+1, len(matrices)):
            product = np.dot(matrices[i], matrices[j])
            det = np.linalg.det(product)
            if det > max_det:
                max_det = det
                selected_matrices = (matrices[i], matrices[j])
    
    result_matrix = np.dot(selected_matrices[1], selected_matrices[0])  
    inverted_matrix = np.linalg.inv(result_matrix)
    
    return inverted_matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{x:.3f}" for x in row))

def solve_problem(input_file):
    matrices = read_matrices(input_file)
    result = find_and_invert(matrices)
    print_matrix(result)

solve_problem('input.txt')