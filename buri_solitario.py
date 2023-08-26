from briscola_essentials import Carta, Mazzo, MazzoFinitoError

class CartaBuri(Carta):
    def __eq__(self, other):
        return self.seme == other.seme or self.valore == other.valore

class Mazzetto():
    def __init__(self, carta):
        self.carta_in_cima = carta
        self.eliminato_dal_gioco = False


class Tavolo:
    def __init__(self):
        self.mazzetti = []
        self.avvenuti_spostamenti = False
        self.indice_mazzetto_piu_profondo_sostituito = None #serve per evitare di controllare sempre tutti i mazzetti

    def __str__(self):
        for i, carta in enumerate(self.mazzetti):
            if (i % 6 == 0):
                print()
            print(carta.carta_in_cima, end="\t")

    def aggiungi_carta(self, carta):
        self.mazzetti.append(Mazzetto(carta))

    def numero_di_mazzetti_visibili(self, indice):
        if(indice == 0):
            return 0
        elif (indice == 1):
            return 1
        else:
            return 2

    def marka_mazzetto(self, indice):
        self.mazzetti[indice].eliminato_dal_gioco = True

    def rimuovi_mazzetto(self, indice):
        return self.mazzetti.pop(indice)

    def sovrapposizione_mazzetto(self, i_vecchio_mazzetto, i_nuovo_mazzetto):
        self.mazzetti[i_nuovo_mazzetto] = self.mazzetti[i_vecchio_mazzetto]
        self.marka_mazzetto(i_vecchio_mazzetto)

        self.avvenuti_spostamenti = True
        if(self.indice_mazzetto_piu_profondo_sostituito is None or i_nuovo_mazzetto < self.indice_mazzetto_piu_profondo_sostituito):
            self.indice_ultimo_mazzetto_sostituito = i_nuovo_mazzetto

    def pulizia_tavolo(self):
        if (self.avvenuti_spostamenti and self.indice_ultimo_mazzetto_sostituito is not None): #ridondante
            for i in reversed(range(self.indice_mazzetto_piu_profondo_sostituito+1, len(self.mazzetti))):
                if self.mazzetti[i].eliminato_dal_gioco:
                    self.rimuovi_mazzetto(i)

            self.avvenuti_spostamenti = False
            self.indice_ultimo_mazzetto_sostituito = None

    def controllo_ricorsivo(self, indice):



class Solitario:
    def __init__(self):
        self.mazzo = Mazzo()
        self.tavolo = Tavolo()

    def setup(self):
        self.mazzo.mescola()
        
    def gioca(self):
        while True:
            try:
                self.tavolo.aggiungi_carta(self.mazzo.pesca())
        
            except MazzoFinitoError:
                break


#if __name__ == "__main__":

