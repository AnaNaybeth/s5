def numnat(n):
    if n==0:
        return 0
    elif n > 0:
        return n+numnat(n-1)
n=int(input("ingrese un numero natural:"))
print(numnat(n))

#import circulo

def main():
    rad=int(input("ingresa el radio:"))
    try:
        print(calcular_area_circulo(rad))
if _name_ == "_main_":
    main()
