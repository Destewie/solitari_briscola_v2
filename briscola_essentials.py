from random import shuffle
from copy import copy

NOMI_DEI_SEMI = {1: 'Danari', 2: 'Coppe', 3: 'Spade', 4: 'Bastoni'}
NOMI_DEI_VALORI = {1: 'Asso', 2: 'Due', 3: 'Tre', 4: 'Quattro', 5: 'Cinque', 6: 'Sei', 7: 'Sette', 8: 'Fante', 9: 'Cavallo', 10: 'Re'}

class Carta:
    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore

    def __str__(self):      
        nome_seme = NOMI_DEI_SEMI.get(self.seme, f'Seme non valido ({self.seme}))')
        nome_valore = NOMI_DEI_VALORI.get(self.valore, f'Valore non valido ({self.valore})')

        return f'{nome_valore} di {nome_seme}'
    
    def __copy__(self):
        return Carta(self.seme, self.valore)

    #ridefinisco l'operatore per l'assegnazione tra due oggetti Carta



# bello perché le carte non vengono estratte per davvero
# questo ti consente di resettare l'oggetto mescolando le carte
class Mazzo:
    def __init__(self):
        self.indice_carta_da_pescare = 0
        self.carte = []
        for seme in NOMI_DEI_SEMI:
            for valore in NOMI_DEI_VALORI:
                self.carte.append(Carta(seme, valore))

    def __str__(self):
        # usa il metodo __str__ già definito in carta
        return '\n'.join(str(carta) for carta in self.carte)

    def __len__(self):
        return len(self.carte)

    def nuemero_carte_coperte(self):
        return len(self) - self.indice_carta_da_pescare

    def numero_carte_pescate(self):
        return self.indice_carta_da_pescare

    def mescola(self):
        shuffle(self.carte)
        self.indice_carta_da_pescare = 0;

    def pesca(self):
        if self.indice_carta_da_pescare >= len(self.carte):
            raise MazzoFinitoError('Non ci sono più carte da pescare')
        else:
            carta_pescata = self.carte[self.indice_carta_da_pescare]
            self.indice_carta_da_pescare += 1
            return carta_pescata


class MazzoFinitoError(Exception):
    pass





