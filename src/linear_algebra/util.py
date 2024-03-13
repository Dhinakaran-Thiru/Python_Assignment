import numpy as np


def find_the_determinant_value(N, matrix_value):
    matrix_value = np.array(matrix_value)


    determinant_value = np.linalg.det(matrix_value) #it will calculate the determinant

    # it should round off the values thats why i used round
    return round(determinant_value, 2)
