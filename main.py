import barajaC

palos = ["Oros", "Copas", "Espadas" , "Bastos"] 
numeros = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

miBaraja = barajaC.Mibaraja(palos, numeros)

print(miBaraja.mazacote)

print(miBaraja.repartir(3,5))

miBaraja.barajar()

print(miBaraja.mazacote)