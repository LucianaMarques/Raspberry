class Leitura:
    
    contagem = 0
    
    def __init__(self, ID, timestamp):
        Leitura.contagem += 1
        
        self.ID = ID
        self.timestamp = timestamp

    def adicionarDistancia(self, ID, valor):
        self.distancia = Distancia(ID, valor)

class Distancia:

    contagem = 0

    def __init__(self, ID, valor):
        Distancia.contagem += 1

        self.ID = ID
        self.valor = valor
        
