def proximidad(R):
    a = {}
    for x,y in R:
        a.setdefault(x, set()).add(y)
    return a

def crear_composicion(R1, R2):
    p1 = proximidad(R1)
    p2 = proximidad(R2)
    composite = set()
    for a, related in p1.items():
        for b in related:
            for c in p2.get(b, []):
                composite.add((a, c))
    return composite

R1={(1,1), (2,4), (2,3), (4,3), (3,4)}; R2={(1,0), (2,1), (3,3), (3,2), (4,1)}
print("Relaciones ingresadas:")
print("Relación 1: ",R1)
print("Relación 2: ",R2)
print("Composición creada:")
print(crear_composicion(R1, R2))