def inversa_relacion(R):
    return [(y, x) for x, y in R]

print("Cadena ingresada: [(1,1), (1,2), (2,3), (4,2)]")
print(inversa_relacion([(1,1), (1,2), (2,3), (4,2)]))