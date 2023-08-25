from game_essentials import Carta, Mazzo, MazzoFinitoError

class PoeriSolitario:
    def __init__(self):
        self.mazzo = Mazzo()

    def setup(self):
        self.mazzo.mescola()

    def gioca(self):
        self.setup()
        contatore = 0

        while True:
            try:
                contatore = (contatore % 3) + 1  # 1, 2, 3, 1, 2, 3, ...
                carta = self.mazzo.pesca()
                if(contatore == carta.valore):
                    return False
            except MazzoFinitoError:
                return True
