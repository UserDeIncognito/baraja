import baraja

palos = ["corazaones" "picas" "diamantes" , "treboles"] 
numeros = ["A", "1","2","3","4","5","6","7","8","9","10","J","Q","K"]

ordenada = baraja.creaBaraja(palos, numeros)
print("Esta es la primera baraja: ", ordenada)

otraBaraja = baraja.creaBaraja(palos, numeros)
print("esta es la segunda baraja nada mas crearla:", otraBaraja)
baraja.baraja(otraBaraja)
print("y ahora la he barajado:", otraBaraja)
print("Para que fernando se lo crea, la baraja primera:", ordenado)