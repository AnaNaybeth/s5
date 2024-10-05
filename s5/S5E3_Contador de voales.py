def contarvocales():
    voc="aeiou"
    cad=input("ingrese una cadena de texto:")
    numvoc={vocal: 0 for vocal in voc}
    cadmin=cad.lower()
    for let in cadmin:
        if let in voc:
           numvoc[let]+=1
    tupla=sorted(numvoc.items())
    print("Numeros de vocales")
    for vocal,cantidad in tupla:
        print(f"{vocal}:{cantidad}")
contarvocales()
