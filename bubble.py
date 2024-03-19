import os
import numpy as np
from scipy.io import loadmat
from scipy.sparse.linalg import gcrotmk
from scipy.sparse import csc_matrix, eye

# Adding paths and setting up parameters
n = 7700
x0 = np.zeros(n)
tol = 1e-6
max_it = n // 4
#restart = 1000
recy_dim = 500
recycle = True
solver = 'gcrotmk'
iter_store = np.zeros(215)

mat_folder = 'N7700Mats'  # Folder containing the .mat files
output_file = 'iteration_counts.txt'  # Output file to write iteration counts


with open(output_file, 'w') as f:
    for i in range(1, 216):  # Adjusted range to match MATLAB indexing
        file_name = os.path.join(mat_folder, f'Step{i}.mat')  # Construct file path
        data = loadmat(file_name)
        A = csc_matrix(data['A'])
        b = data['b'].ravel()

        if recycle:
            if i == 1:
                x, iter_count = gcrotmk(A, b, x0=x0, tol=tol, maxiter=max_it)
                Unew = eye(n)
                x0 = x
            else:
                x, iter_count = gcrotmk(A, b, x0=x0, tol=tol, maxiter=max_it, V=Unew)
                Unew = eye(n)
                x0 = x
        else:
            x, iter_count = gcrotmk(A, b, x0=x0, tol=tol, maxiter=max_it)
            x0 = x

        iter_store[i-1] = iter_count
        f.write(f'Step {i}: {iter_count} iterations\n')

