from briscola_essentials import Mazzo, MazzoFinitoError

class Solitario:
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
                #print(self.mazzo)
                return True
