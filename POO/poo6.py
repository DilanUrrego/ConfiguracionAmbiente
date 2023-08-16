class Carta:

    CORAZON = "Corazon"
    DIAMANTE = "Diamante"
    TREBOL = "Trebol"
    PICA = "Pica"
    
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

carta1 = Carta("8", Carta.DIAMANTE)
print(carta1.valor, carta1.pinta)

carta2 = Carta("A", Carta.CORAZON)
print(carta2.valor, carta2.pinta)
