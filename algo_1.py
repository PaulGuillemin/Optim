from data1 import * 
nbRessources = 2


def testRessources(p, m):
    for i in range(nbRessources):
        if machines[m][i] > processus[p][i+1]:
            return False
    return True



    
