from readFiles import ReadCmats, stdReadMat
from confOps import ConformalDistance
from homOps import HomogeneousDistance, Positions
from conversion import stdConversion
from itertools import combinations
from os import walk
import time

inpFol = r"input-mats"

def calcCDists(cmats):
    CrunTimeList = []
    t0 = time.time()
    numOps = 0
    for comb in combinations(range(len(cmats)+1), 2):
        print(comb)
        print(ConformalDistance(comb[0],comb[1],cmats))
        numOps += 1
    runTime = time.time()-t0
    print("==========END==========")
    print("Run time is", runTime, "second(s)")
    print("Number of operations: ", numOps)
    CrunTimeList.append(runTime)
 

def calcZDists(positions):
    ZrunTimeList = []
    t0 = time.time()
    numOps = 0
    for comb in combinations(range(len(positions)), 2):
        print(comb)
        print(HomogeneousDistance(comb[0],comb[1],positions))
        numOps += 1
    runTime = time.time()-t0
    print("==========END==========")
    print("Run time is", runTime, "second(s)")
    print("Number of operations: ", numOps)
    ZrunTimeList.append(runTime)

def distsLoop(inpFol):
    files = []
    for (dirpath, dirnames, filenames) in walk(inpFol):
        files.extend(filenames)
        break
    return files


def getCMolecules(inpFol):
    files = distsLoop(inpFol)
    allMolecs = []
    for file in files:
        allMolecs.append(ReadCmats(inpFol+"/"+file))
    return allMolecs

def Zconvert(inpFol):
    theta, omega, d = stdConversion(inpFol)
    positions = Positions(theta, omega, d)
    return positions

def getZMolecules(inpFol):
    files = distsLoop(inpFol)
    allMolecs = []
    for file in files:
        allMolecs.append(Zconvert(stdReadMat(inpFol+"/"+file)))

    return allMolecs

def allCDists(): #rotina para calcular distancias em Cmats
    allMolecs = getCMolecules(inpFol)
    init_time = time.time()
    for molec in allMolecs:
        calcCDists(molec)
    totRunTime = time.time() - init_time
    print(f"Total run time is {totRunTime} seconds")
    return totRunTime

def allZDists(): #rotina para calcular distancias em Zmats
    allMolecs = getZMolecules(inpFol)
    init_time = time.time()
    for molec in allMolecs:
        calcZDists(molec)
    totRunTime = time.time() - init_time
    print(f"Total run time is {totRunTime} seconds")
    return totRunTime


allCDists()
allZDists() #ao que tudo indica isso é o método mais rápido, mas como estamos convertendo as zmat em cartesianas (essencialmente) pode ser por conta disso
#calcular a inversa de uma matriz é beeem caro como voce sabe, e como fazemos isso em confOps ConformalDistances pode ser a causa do peso
print("=======================END=OF=CODE=======================")
print("Time to run all operations in Z-matrices is {zTime} seconds")
print("Time to run all operations in C-matrices is {cTime} seconds")
