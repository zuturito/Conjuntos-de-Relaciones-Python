def particion_equivalente(I, R):
    clases = []
    particiones = {}
    for o in I:
        found = False
        for c in clases:
            if R(next(iter(c)), o):  #es equivalente(?)
                c.add(o)
                particiones[o] = c
                found = True
                break
        if not found:  #Es equivalente en otra clase
            clases.append(set([o]))
            particiones[o] = clases[-1]
    return clases, particiones

def probar_particion(clases, particiones, R): #generar clases de equivalencia de R
    for o, c in particiones.items():
        for _c in clases:
            assert (o in _c) ^ (not _c is c)
    for c1 in clases:
        for o1 in c1:
            for c2 in clases:
                for o2 in c2:
                    assert (c1 is c2) ^ (not R(o1, o2))

def evaluar_equivalencia(): #evalua equivalencia de la relación por medio de lambda y el rango
    R = lambda x, y: (x - y) % 4 == 0
    clases, particiones = particion_equivalente(
        range(-3,5,7),
        R
    )
    probar_particion(clases, particiones, R)
    print("Relación ingresada: [(-3,5,7)]")
    print("Clases de equivalencia")
    for c in clases: print(c)
    print("Particion de equivalencia")
    for o, c in particiones.items(): print(o, ':', c)


if __name__ == '__main__':
    evaluar_equivalencia()