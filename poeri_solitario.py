from game_essentials import Carta, Mazzo

class PoeriSolitario:
    def __init__(self):
        self.mazzo = Mazzo()

    def setup(self):
        
        self.mazzo.mescola()
