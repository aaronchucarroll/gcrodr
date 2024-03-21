import numpy as np

# GCRO DR - GCRO with Defalted Restarting
# X = GCRODR(A, B, M, K) attempts to solve the system of linear equations A*X = B for X
# A must be an n x n coefficient matrix
# B must be a column vector of length n
# M is the maximum subspace dimension used by GCRODR
# K is the number of approximate eigenvectors kept from one cycle to the next
# OPTIONAL PARAMS:
# x0 specifies an initial guess. The default is an all zero vector

def gcrodr(A, b, m, k, x0):
    x = np.zeros(len(x0))  #initialize solution vector
    count = 1

    r = b - A.dot(x0)  #calculate initial preconditioned residual

    resvec = np.zeros(2) # calculate initial preconditioned residual norm
    resvec[0] = np.linalg.norm(r)
    print(f'||r|| = {resvec[0]}\t\tnmv = 0')

    bnorm = np.linalg.norm(b)
    U_persist = {}


