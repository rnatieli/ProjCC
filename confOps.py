import math as mt
import numpy as np

def C_matrix(theta, omega, d):
    A = np.array([
        [-np.cos(theta), -np.sin(theta), 0],
        [ np.sin(theta)*np.cos(omega), -np.cos(theta)*np.cos(omega), -np.sin(omega)],
        [ np.sin(theta)*np.sin(omega), -np.cos(theta)*np.sin(omega),  np.cos(omega)]
    ])
    
    b = np.array([[-d*np.cos(theta)],
                  [ d*np.sin(theta)*np.cos(omega)],
                  [ d*np.sin(theta)*np.sin(omega)]])
   
    normb2 = float(np.sum(b**2))
    
   
    U = np.block([
        [A, b, np.zeros((3,1))],
        [np.zeros((1,3)), np.array([[1,0]])],
        [b.T @ A, np.array([[normb2/2, 1]])]
    ])
    return U

def ConformalDistance(i, j, cmats):
    e0 = np.array([[0],[0],[0],[1],[0]])
    e_inf = np.array([[0],[0],[0],[0],[1]])

    if i >= len(cmats):
        print("length err")
        return 0

    Bcum = [np.eye(5)]
    #Bcum = []
    for Bi in cmats:
        Bcum.append(Bcum[-1] @ Bi)

    if j >= len(Bcum):
        j = len(Bcum) - 1
    # transformação entre os pontos i e j
    
    Bij = np.linalg.inv(Bcum[i]) @ Bcum[j]
    val = 2 * (e_inf.T @ Bij @ e0)
    return np.sqrt(abs(float(val)))

#def C_matrix(theta, omega, d):
#    A = np.array([
#        [-np.cos(theta), -np.sin(theta), 0, -d*np.cos(theta), 0],
#        [np.sin(theta)*np.cos(omega), -np.cos(theta)*np.cos(omega), -np.sin(omega), d*np.sin(theta)*np.cos(omega), 0],
#        [np.sin(theta)*np.sin(omega), -np.cos(omega)*np.sin(omega), np.cos(omega), d*np.sin(theta)*np.sin(omega), 0],
#        [0, 0, 0, 1, 0],
#        [d, 0, 0, (d*d)/2, 1]
#    ])
#    return A
#
#def ConformalDistance(i, j, cmats):
#    e0 = np.array([[0],[0],[0],[-1/2],[1/2]])
#    e_inf = np.array([[0],[0],[0],[1],[1]])
#
#    Bij = cmats[i+1]
#    
#    for n in range(i+2, j+1):
#        Bij = Bij @ cmats[n]
#    
#
#    value2 = 2*e_inf.T@Bij@e0
#    #print(value2)
#    #print(np.sqrt(abs(value2)))
#    return float(np.sqrt(abs(value2)))