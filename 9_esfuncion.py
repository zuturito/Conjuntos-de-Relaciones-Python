from tabulate import tabulate #pip install tabulate

def es_funcion(R):
	R = list(R)
	A = set(a for a, _ in R)
	resultado = set(ab for ab in R if ab[0] == ab[0])
	return ("Es función", resultado) if len(A) == len(resultado) else ("No es función")

print("Suponga que se tiene el siguiente Dominio/Rango")
print(tabulate([[1,'A'],[2,'B'],[3,'C'],[4,'D'],['','E']], headers=['Dominio', 'Rango'], tablefmt='orgtbl'))
print("Una relación se define como función, cuando los valores de X tienen exactamente un valor asignado en Y")
print("Cadena ingresada: [(1,'A'),(2,'C'),(3,'C'),(4,'D')]")
print(es_funcion([(1,'A'),(2,'C'),(3,'C'),(4,'D')]))
print("Cadena ingresada: [(1,'A'),(1,'C'),(3,'C'),(4,'D')]")
print(es_funcion([(1,'A'),(1,'C'),(3,'C'),(4,'D')]))