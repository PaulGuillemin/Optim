from data1 import *
import numpy as np

nbRessources = 2
nbMachines = 4
nbServices = 79
machineneutre = 0

services_ = np.copy(services)

nb_loc = np.array(np.zeros(len(services)))

for s in range(len(services)):
    nb_loc[s] = 0

for p in range(len(processus)):
    services_[p]