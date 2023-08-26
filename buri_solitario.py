from briscola_essentials import Carta, Mazzo, MazzoFinitoError, NOMI_DEI_SEMI, NOMI_DEI_VALORI
from copy import copy

class CartaBuri(Carta):
    def __eq__(self, other):
        return self.seme == other.seme or self.valore == other.valore

class MazzoBuri(Mazzo):
    def __init__(self):
        self.mazzo = []
        for seme in NOMI_DEI_SEMI:
            for valore in NOMI_DEI_VALORI:
                self.mazzo.append(CartaBuri(seme, valore))

class Mazzetto():
    def __init__(self, carta):
        self.carta_in_cima = carta
        self.eliminato_dal_gioco = False


class Tavolo:
    def __init__(self):
        self.mazzetti = []
        self.avvenuti_spostamenti_ultimo_controllo_ricorsivo = False
        self.indice_mazzetto_piu_profondo_sostituito = None #serve per evitare di controllare sempre tutti i mazzetti

    def __str__(self):
        carte = ""
        contatore = 0
        for mazzetto in self.mazzetti:
            if not mazzetto.eliminato_dal_gioco:
                carte += str(mazzetto.carta_in_cima) + "\t\t"

                contatore += 1
                if(contatore % 6 == 0):
                    carte += "\n"
        return carte

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

    def sovrapposizione_mazzetto(self, i_mazzetto_che_alzo, i_mazzetto_che_schiaccio):
        self.mazzetti[i_mazzetto_che_schiaccio] = copy(self.mazzetti[i_mazzetto_che_alzo])
        self.marka_mazzetto(i_mazzetto_che_alzo)

        self.avvenuti_spostamenti_ultimo_controllo_ricorsivo = True
        if(self.indice_mazzetto_piu_profondo_sostituito is None or i_mazzetto_che_schiaccio < self.indice_mazzetto_piu_profondo_sostituito):
            self.indice_mazzetto_piu_profondo_sostituito = i_mazzetto_che_schiaccio
        
        #print(str(self)) #debug
        #print()

    def pulizia_carte_markate(self):
        if (self.avvenuti_spostamenti_ultimo_controllo_ricorsivo and self.indice_mazzetto_piu_profondo_sostituito is not None): #ridondante
            for i in reversed(range(self.indice_mazzetto_piu_profondo_sostituito, len(self.mazzetti))):
                if self.mazzetti[i].eliminato_dal_gioco:
                    self.rimuovi_mazzetto(i)

    def setup_controllo_ricorsivo(self):
        self.avvenuti_spostamenti_ultimo_controllo_ricorsivo = False
        self.indice_mazzetto_piu_profondo_sostituito = None

    def controllo_ricorsivo(self, indice):
        numero_di_mazzetti_visibili = self.numero_di_mazzetti_visibili(indice)

        if(numero_di_mazzetti_visibili != 0 and indice > 0 and indice < len(self.mazzetti)):
            # Qui vado a fare i controlli sul mazzetto subito precedente
            if(self.mazzetti[indice].carta_in_cima == self.mazzetti[indice-1].carta_in_cima):
                self.sovrapposizione_mazzetto(i_mazzetto_che_alzo=indice, i_mazzetto_che_schiaccio=indice-1)
                return self.controllo_ricorsivo(indice-1)

            # Se non interagisco con il mazzetto subito precedente e ho possibilità di tentare con quello prima ancora, lo faccio
            elif(numero_di_mazzetti_visibili == 2):
                if(self.mazzetti[indice].carta_in_cima == self.mazzetti[indice-2].carta_in_cima):
                    self.sovrapposizione_mazzetto(i_mazzetto_che_alzo=indice, i_mazzetto_che_schiaccio=indice-2)
                    return self.controllo_ricorsivo(indice-2)
                


class Solitario:
    def __init__(self):
        self.mazzo = MazzoBuri()
        self.tavolo = Tavolo()

    def setup(self):
        self.mazzo.mescola()
        self.tavolo.mazzetti.clear()
        
    def gioca(self):
        self.setup()

        while True:
            try:
                self.tavolo.aggiungi_carta(self.mazzo.pesca())
                #print(str(self.tavolo)) #debug
                #print()


                while True: #l'alternativa al do while in python è un while True con un break ad una certa condizione
                    avvenuti_spostamenti_controlli_ricorsivi_multipli = False
                    for i in reversed(range(len(self.tavolo.mazzetti))):
                        self.tavolo.setup_controllo_ricorsivo()
                        self.tavolo.controllo_ricorsivo(i)
                        if self.tavolo.avvenuti_spostamenti_ultimo_controllo_ricorsivo:
                            avvenuti_spostamenti_controlli_ricorsivi_multipli = True
                        self.tavolo.pulizia_carte_markate()

                    if not avvenuti_spostamenti_controlli_ricorsivi_multipli:
                        break

        
            except MazzoFinitoError:
                if(len(self.tavolo.mazzetti) == 1):
                    #print("HAI VINTO!")
                    return True
                else:
                    #print("HAI PERSO, RITENTA!")
                    return False


if __name__ == "__main__":
    solitario = Solitario()
    solitario.gioca()
