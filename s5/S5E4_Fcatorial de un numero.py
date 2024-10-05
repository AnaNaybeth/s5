
def facnum(n):
    if n==1:
        return 1
    elif n > 1:
        return n*facnum(n-1)
n=int(input("ingrese un numero entero positivo:"))
    
print(facnum(n))

