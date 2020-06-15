def es_transitiva(R):
    for a,b in R:
        for c,d in R:
            if b == c and ((a,d) not in R):
                    return "No es transitiva"
    return "Es transitiva"

print("Cadena ingresada: [(1,1), (1,2), (1,4), (2,1), (2,2), (3,3), (4,1), (4,4)]")
print(es_transitiva([(1,1), (1,2), (1,4), (2,1), (2,2), (3,3), (4,1), (4,4)]))
print("Cadena ingresada: [(1,1), (2,1), (3,1), (3,2), (4,1), (4,2), (4,3)]")
print(es_transitiva([(1,1), (2,1), (3,1), (3,2), (4,1), (4,2), (4,3)]))
print("Cadena ingresada: EXAMEN")
print(es_transitiva([(2,2), (2,3),(2,4), (3,2), (3,3), (3,4), (4,2), (4,3), (4,4)]))