def es_reflexiva(R):
	R = list(R)
	A = set(a for a, _ in R)
	resultado = set((a, b) for a, b in R if a == b)
	return ("Es reflexiva", resultado) if len(A) == len(resultado) else ("No es reflexiva", set())

#Reflexiva
#[(1,1),(2,2),(3,3),(4,4)] 
#No Reflexiva
#[(1,2), (2,1), (1,3), (1,4), (2,3), (2,4), (3,4)]
print("Cadena ingresada: [(1,1),(2,2),(2,1),(3,3)]")
print(es_reflexiva([(1, 1), (2, 2), (2, 1), (3,3)]))
print("Cadena ingresada: [(1,2), (2,1), (1,3), (1,4), (2,3), (2,4), (3,4)]")
print(es_reflexiva([(1,2), (2,1), (1,3), (1,4), (2,3), (2,4), (3,4)]))
print("EXAMEN")
print(es_reflexiva([(1,1), (1,3), (2,1), (2,2), (3,1), (3,3), (4,2), (4,3), (4,4) ]))

