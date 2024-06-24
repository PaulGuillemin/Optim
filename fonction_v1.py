from data1 import * 
nbRessources = 2
nbMachines = 4
nbServices = 79
machineneutre = 0



def testRessources(p, m):
    for i in range(nbRessources):
        if machines[m][i] > processus[p][i+1]:
            return False
    return True

def updateRessources(p, m):
    for i in range(nbRessources):
        machines[m][i] = machines[m][i] - processus[p][i+1]

def testAll(p):
    useMach = [[False for i in range(nbServices)] for j in range(nbMachines)]
    for m in range(nbMachines):
        service = processus[p][0]
        if useMach[m][service] == False:
            if testRessources(p,m)== True:
                useMach[m][service] = True 
                return m
    return machineneutre

def testNewLoc(p):
    useLoc = [[False for i in range(nbServices)] for j in range(nbMachines)]
    service = processus[p][0]
    for m in range(nbMachines):
        loc = machines[m]
        if not useLoc[loc][service]:
            if testRessources(p, m):
                useLoc[loc][service] = True
                return m
    return machineneutre







            


    






    
