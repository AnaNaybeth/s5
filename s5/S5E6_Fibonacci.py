def fibonacci(n):
    num=[0,1]
    def recursivo(n):
        if n<len(num):
            return num[n]
        else:
            num2=recursivo(n-1)+recursivo(n-2)
            num.append(num2)
            return num2
    return recursivo(n),num

n=int(input("Ingresa un  numero:"))
print(fibonacci(n)) 
    