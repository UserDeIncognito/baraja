palos = ['o','c','e','b']
numeros = [ 'A','2','3','4','5','6','7','S','C','R']

def creaBaraja():
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)
    return baraja


def intercambio(primerV,segundoB):
    aux = primerV
    primerV = segundoB
    segundoB = aux

def barajar(lista_de_naipes):
    for i in range (len(lista_de_naipes)):
            nueva_pos = random.randrange(len(lista_de_naipes))
            """
            Intercambio de cartas,tecnica vaso vacio
            """
            aux= lista_de_naipes[nueva_pos]
            lista_de_naipes[nueva_pos] = lista_de_naipes[i]
            lista_de_naipes [i] = aux
    return lista_de_naipes

print (creaBaraja())
