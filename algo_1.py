
testRessources(processus p, machine m)
pour chaque ressource r
si capa_res[m][r] < r(p,r)
return false
fin si
fin pour
return true
    
