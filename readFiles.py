import numpy as np
from confOps import C_matrix
from homOps import Z_matrix
from conversion import stdConversion

def stdReadMat(file):
    atoms = []

    with open(file, 'r') as f:
        lines = [l.strip() for l in f.readlines() if l.strip()]

    for line in lines:
        parts = line.split()
        n = len(parts)
        if n in [1, 3, 5, 7]:
            atoms.append(parts)
        else:
            print("Aviso: linha malformada:", parts)

    return atoms

def ReadCmats(file): 
    atoms = stdReadMat(file)
    theta, omega, dist = stdConversion(atoms)
    cmats = [] #o erro fica aqui, se você tem n atomos, 
    #voce gera n-1 zmats, o que é um problema, ja que ele calcula em pares
    cmats = [C_matrix(theta[i], omega[i], dist[i]) for i in range(len(dist))]
    return cmats


def ReadZmats(file):
    atoms = stdReadMat(file)
    theta, omega, dist = stdConversion(atoms)
    zmats = [np.eye(4)]
    for i in range(len(theta)):
        zmats.append(Z_matrix(theta[i], omega[i], dist[i]))
    return zmats
