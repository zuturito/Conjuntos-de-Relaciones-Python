def es_antisimetrica(R):
    for a, b in R:
        if (a,b) in R and (b,a) in R and a != b:
            return "No es antisimétrica"
    return "Es antisimétrica"

print("Cadena ingresada: [(A,A), (A,C), (A,B), (C,C)]")
print(es_antisimetrica([("A","A"), ("A","C"), ("A","B"), ("C","C")]))
print("Cadena ingresada: [(A,A), (A,C), (C,A), (C,C)]")
print(es_antisimetrica([("A","A"), ("A","C"), ("C","A"), ("C","C")]))
print("Cadena ingresada: EXAMEN")
print(es_antisimetrica([(2,4), (3,4), (4,2), (4,3) ]))