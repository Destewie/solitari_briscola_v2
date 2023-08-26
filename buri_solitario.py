from briscola_essentials import Carta, Mazzo, MazzoFinitoError

class CartaBuri(Carta):
    def __eq__(self, other):
        return self.seme == other.seme or self.valore == other.valore

if __name__ == "__main__":

