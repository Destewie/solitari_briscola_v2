from briscola_essentials import Carta, Mazzo, MazzoFinitoError, NOMI_DEI_SEMI, NOMI_DEI_VALORI
import logging

# modifica ad hoc per questo caso
class CartaRe(Carta):
    def __init__(self, seme, valore):
        super().__init__(seme, valore)
        self.coperta = True

# modifica ad hoc per questo caso
class MazzoRe(Mazzo):
    def __init__(self):
        super().__init__()
        self.carte = []
        for seme in NOMI_DEI_SEMI:
            for valore in NOMI_DEI_VALORI:
                self.carte.append(CartaRe(seme, valore))

class Solitario: 
    def __init__(self):
        self.mazzo = MazzoRe()

        self.NUM_RIGHE = 4
        self.NUM_COLONNE = 10
        self.tavola = [[0 for i in range(self.NUM_COLONNE)] for j in range(self.NUM_RIGHE)]

    def setup(self):
        self.mazzo.mescola()

        #resetto i posti dei re
        for i in range(self.NUM_RIGHE):
            self.tavola[i][self.NUM_COLONNE-1] = None

        #riempio la tavola tranne i posti dei re
        for i in range(self.NUM_RIGHE):
            for j in range(self.NUM_COLONNE-1):
                self.tavola[i][j] = self.mazzo.pesca()

    def stampa_tavola(self):
        #stampo il tavolo rappresentando le carte coperte con un asterisco
        #rappresento le carte scoperte con una coppia di interi, il primo per il seme e il secondo per il valore
        for i in range(self.NUM_RIGHE):
            for j in range(self.NUM_COLONNE):
                if self.tavola[i][j] == None or isinstance(self.tavola[i][j], int):
                    print("  -  ", end=" ")
                elif self.tavola[i][j].coperta:
                    print("  *  ", end=" ")
                else:
                    print(f"({self.tavola[i][j].seme},{self.tavola[i][j].valore})", end=" ")
            print()



    def gioca(self):
        self.setup()
        carta_in_mano = None

        try:
            while(True): 
                if carta_in_mano == None or isinstance(carta_in_mano, int):
                    carta_in_mano = self.mazzo.pesca()
                    #print("Hai pescato: ", end=" ")
                carta_in_mano.coperta = False

                #print(f"{carta_in_mano}: {carta_in_mano.seme}, {carta_in_mano.valore}")

                carta_dal_tavolo = self.tavola[carta_in_mano.seme-1][carta_in_mano.valore-1]
                self.tavola[carta_in_mano.seme-1][carta_in_mano.valore-1] = carta_in_mano #metto la carta sul tavolo

                #self.stampa_tavola()
                #print()

                carta_in_mano = carta_dal_tavolo #prendo la carta dal tavolo

        except MazzoFinitoError:
            for i in range(self.NUM_RIGHE):
                for j in range(self.NUM_COLONNE):
                    if self.tavola[i][j].seme-1 != i or self.tavola[i][j].valore-1 != j or self.tavola[i][j] == None:
                        return False
            return True


if __name__ == "__main__":
    solitario = Solitario()
    solitario.setup()

    if solitario.gioca():
        print("HAI VINTO!")
    else:
        print("SE GIRO TUTTE LE CARTE:")
        for i in range(solitario.NUM_RIGHE):
            for j in range(solitario.NUM_COLONNE):
                if solitario.tavola[i][j] != None:
                    print(f"({solitario.tavola[i][j].seme},{solitario.tavola[i][j].valore})", end=" ")
                else:
                    print("  -  ", end=" ")

            print()
        
        print()
        print("HAI PERSO, RITENTA!")
