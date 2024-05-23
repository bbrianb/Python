def det(matrix):
    if (len(matrix)) == 1:
        return matrix[0]
    else:
        print(f'{matrix=}')
        determinant = 0
        k = 1
        i = 1
        while k <= len(matrix[0]):
            # print(f'{((-1)**(i+x)) = }')
            # print(f'{matrix[i-1][x-1] = }')
            # print(f'{minor(matrix, i, x) = }\n')
            # print(f'{det(minor(matrix, i, x)) = }\n')
            determinant += ((-1)**(i+k)) * \
                           matrix[i-1][k-1] * det(minor(matrix, i, k))
            k += 1
        return determinant


def minor(matrix_in, i_in, j_in):
    matrix = []
    for i in matrix_in:
        matrix.append(i.copy())
    i = i_in - 1
    j = j_in - 1
    matrix.pop(i)
    for row in matrix:
        row.pop(j)
    if len(matrix) == 1:
        matrix = matrix[0]
    return matrix


augmented_matrix = [
    [3, 2, 1, 5],
    [4, -5, 0, 28],
    [2, 0, -3, -17]
]

D = []
for r in augmented_matrix:
    D.append(r[:-1])

Dx = []
Dy = []
Dz = []
for q, r in enumerate(D):
    Dx.append(r[:])
    Dy.append(r[:])
    Dz.append(r[:])
    Dx[-1][0] = augmented_matrix[q][-1]
    Dy[-1][1] = augmented_matrix[q][-1]
    Dz[-1][2] = augmented_matrix[q][-1]

D = det(D)
Dx = det(Dx)
Dy = det(Dy)
Dz = det(Dz)
x = Dx/D
y = Dy/D
z = Dz/D
print(f'{D=}')
print(f'{x=}, {y=}, {z=}')

B = [[1, 2, -1, -2],
     [3, -4, -3, 0],
     [1, 0, 0, 1],
     [-2, 5, 0, 4]
     ]
print(f'{det(B)=}')
print('area =', 0.5*abs(det(B)))
