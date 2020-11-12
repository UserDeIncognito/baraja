import Baraja

class Mibaraja():

    def __init__(self,palos,numeros):
        self.palos = palos
        self.numeros = numeros
        self.mazacote = Baraja.creaBaraja(palos, numeros)

    def barajar(self):
        Baraja.barajar(self.mazacote)

    def repartir(self, num_jugadores, num_cartas):
        jugadores = []
        for i in range (num_jugadores):
            jugadores.append([])

        for carta in range(num_cartas):
            for jugador in range(num_jugadores):
                jugadores[jugador].append(self.mazacote.pop(0))
        return jugadores