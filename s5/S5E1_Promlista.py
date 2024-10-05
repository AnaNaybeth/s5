lista=input("ingresa una lista de numeros separdas por (-) :")
def promedio(lista):
    lista1=[int(x) for x in lista.split("-")]
    s=sum(lista1)
    n=len(lista1)
    prom=s/n
    return prom

print(promedio(lista))



