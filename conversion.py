import numpy as np

def stdConversion(atoms):
   
    d, theta, omega = [], [], []

    #Converter os angulos para rad
    for entry in atoms[1:]:
        
        # distance
        if len(entry) >= 3:
            d.append(float(entry[2]))
        else:
            d.append(0.0)

        # bonda angle
        if len(entry) >= 5:
            theta.append(np.deg2rad(float(entry[4])))
        else:
            theta.append(np.deg2rad(90.0))

        # torsion angle
        if len(entry) >= 7:
            omega.append(np.deg2rad(float(entry[6])))  
        else:
            omega.append(0.0)
    return np.array(theta), np.array(omega), np.array(d)