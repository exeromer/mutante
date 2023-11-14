

def isMutant(dna):
    count = 0
    n = len(dna)

    for i in range(n):
        for j in range(n):
            if j + 3 < n and dna[i][j] == dna[i][j +1] == dna[i][j + 2] == dna[i][j + 3]:
                count += 1
            if i + 3 < n and dna[i][j] == dna[i+1][j] == dna[i+2][j] == dna[i+3][j]:
                count +=1   
            if i + 3 < n and j + 3 < n and dna[i][j] == dna[i+1][j+1] == dna[i+2][j+2] == dna[i+3][j+3]:
                count += 1
            if i + 3 < n and j - 3 >= 0 and dna[i][j] == dna[i+1][j-1] == dna[i+2][j-2] == dna[i+3][j-3]:
                count +=1
    return count > 1            

dna = []
print("--- LE PEDIREMOS ACONTINUACION QUE INGRESE LAS 6 FILAS ---")

while len(dna) <6:
    s = input(f"Ingrese la cadena {len(dna)+1} de adn: ")
    if s.isalpha() and len(s) == 6 and set(s.lower()) <= set(['a', 'c', 't', 'g']):
        dna.append(s)
    else:
        print("El string no es válido. Intente nuevamente.")
        print("RECUERDE QUE EL STRING DEBE CONTENER SOLAMENTE LAS LETRAS A,C,G,T Y DEBE CONTENER SOLO 6 LETRAS")

if isMutant(dna):
    print("El humano es mutante")
else:
    print("El humano no es mutante")
