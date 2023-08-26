from briscola_essentials import Carta, Mazzo, MazzoFinitoError, NOMI_DEI_SEMI, NOMI_DEI_VALORI
from copy import copy

class CartaBuri(Carta):
    def __eq__(self, other):
        return self.seme == other.seme or self.valore == other.valore

class MazzoBuri(Mazzo):
    def __init__(self):
        self.indice_carta_da_pescare = 0
        self.carte = []
        for seme in NOMI_DEI_SEMI:
            for valore in NOMI_DEI_VALORI:
                self.carte.append(CartaBuri(seme, valore))

class Mazzetto():
    def __init__(self, carta):
        self.carte = [carta]
        self.eliminato_dal_gioco = False

    def __eq__(self, other):
        return self.carte[-1] == other.carte[-1]

    def __str__(self):
        return str(self.carte[-1])

    def aggiungi_carta(self, carta):
        self.carte.append(carta)

    def accogli_sopra(self, mazzetto):
        self.carte.extend(mazzetto.carte)


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
                carte += str(mazzetto) + "\t\t"

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
        self.mazzetti[i_mazzetto_che_schiaccio].accogli_sopra(self.mazzetti[i_mazzetto_che_alzo])
        self.marka_mazzetto(i_mazzetto_che_alzo)

        self.avvenuti_spostamenti_ultimo_controllo_ricorsivo = True
        if(self.indice_mazzetto_piu_profondo_sostituito is None or i_mazzetto_che_schiaccio < self.indice_mazzetto_piu_profondo_sostituito):
            self.indice_mazzetto_piu_profondo_sostituito = i_mazzetto_che_schiaccio
        
        #print(str(self)) #debug
        #print()

    def pulizia_mazzetti_markati(self):
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
            if(self.mazzetti[indice] == self.mazzetti[indice-1]):
                self.sovrapposizione_mazzetto(i_mazzetto_che_alzo=indice, i_mazzetto_che_schiaccio=indice-1)
                return self.controllo_ricorsivo(indice-1)

            # Se non interagisco con il mazzetto subito precedente e ho possibilità di tentare con quello prima ancora, lo faccio
            elif(numero_di_mazzetti_visibili == 2):
                if(self.mazzetti[indice] == self.mazzetti[indice-2]):
                    self.sovrapposizione_mazzetto(i_mazzetto_che_alzo=indice, i_mazzetto_che_schiaccio=indice-2)
                    return self.controllo_ricorsivo(indice-2)
                
    def raggruppa_mazzetti_da_destra_a_sinistra_in_nuovo_deck(self):
        for i in range(1, len(self.mazzetti)):
            self.sovrapposizione_mazzetto(i_mazzetto_che_schiaccio=0, i_mazzetto_che_alzo=i)

        return copy(self.mazzetti[0].carte)

    def raggruppa_mazzetti_da_sinistra_a_destra_in_nuovo_deck(self):
        for i in reversed(range(0, len(self.mazzetti)-1)):
            self.sovrapposizione_mazzetto(i_mazzetto_che_schiaccio=len(self.mazzetti)-1, i_mazzetto_che_alzo=i)

        return copy(self.mazzetti[len(self.mazzetti)-1].carte)
            


class Solitario:
    def __init__(self):
        self.mazzo = MazzoBuri()
        self.mazzo.mescola()
        self.tavolo = Tavolo()

    def setup_post_game_da_destra_a_sinistra(self):
        self.mazzo.carte = self.tavolo.raggruppa_mazzetti_da_destra_a_sinistra_in_nuovo_deck()
        self.mazzo.indice_carta_da_pescare = 0
        self.tavolo.mazzetti.clear()

    def setup_post_game_da_sinistra_a_destra(self):
        self.mazzo.carte = self.tavolo.raggruppa_mazzetti_da_sinistra_a_destra_in_nuovo_deck()
        self.mazzo.indice_carta_da_pescare = 0
        self.tavolo.mazzetti.clear()

    def gioca(self):
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
                        self.tavolo.pulizia_mazzetti_markati()

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
    print("----------------------------------------")
    #solitario.setup_post_game_da_destra_a_sinistra()
    solitario.setup_post_game_da_sinistra_a_destra()
    print("il mazzo ha " + str(len(solitario.mazzo.carte)) + " carte")
    print("mazzo: ")
    print(str(solitario.mazzo))
    print("----------------------------------------")
    solitario.gioca()
