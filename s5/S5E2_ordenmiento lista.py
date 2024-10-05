lista=input("ingresa una lista de palabras separadas por espacios:")
def ordenar(lista):
    lista1=[str(x) for x in lista.split()]
    ord=lista1.sort()
    return lista1
print(ordenar(lista))