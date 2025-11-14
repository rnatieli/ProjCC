import numpy as np

#==============================================
#Eu nao sei se fazer desse jeito e ideal, provavelmente isso que esta fazendo o codigo rodar bem rapido, ja que 
#voce manda do conforme pro cartesiano uma vez e depois só faz por cartesiano, eu estava tentando implementar fazendo
#um produto de vetores que nem a definição mas não consegui e decidi focar nas cmats
#==============================================

def Z_matrix(theta, omega, d):
    A = np.array([
        [-np.cos(theta), -np.sin(theta), 0, -d*np.cos(theta)],
        [np.sin(theta)*np.cos(omega), -np.cos(theta)*np.cos(omega), -np.sin(omega), d*np.sin(theta)*np.cos(omega)],
        [np.sin(theta)*np.sin(omega), -np.cos(theta)*np.sin(omega), np.cos(omega), d*np.sin(theta)*np.sin(omega)],
        [0, 0, 0, 1]
    ])
    return A

def Positions(theta, beta, d):
    n = len(d)
   
    e4 = np.array([0, 0, 0, 1])
    
    positions = [np.zeros(3)]

    Id = np.eye(4)
    
    for i in range(n):
        Bi = Z_matrix(theta[i], beta[i], d[i])
        Id = Id @ Bi
        xi = Id @ e4
        positions.append(xi[:3])  
    return np.array(positions)

def HomogeneousDistance(i, j, positions):
    return np.linalg.norm(positions[j]-positions[i])
