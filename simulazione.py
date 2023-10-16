import solitario_poeri as ps
import solitario_buri as bs
import solitario_buri_no_shuffle as bsn
import os
import matplotlib.pyplot as plt
import copy
from termcolor import colored

NUMERO_DI_PARTITE = 1000000
NUMERO_DI_SIMBOLI_DI_AVANZAMENTO = 100
NUMERO_PARTITE_PRIMA_DI_CAMBIARE_IL_MAZZO = 50
CAMBIAMENTI_TOTALI_DI_MAZZO = int(NUMERO_DI_PARTITE / NUMERO_PARTITE_PRIMA_DI_CAMBIARE_IL_MAZZO)

def stampa_caricamento(i_partita):
    # STAMPA PROGRESSO
    if i_partita % (NUMERO_DI_PARTITE/NUMERO_DI_SIMBOLI_DI_AVANZAMENTO) == 0:
        simboli_da_stampare = int(i / (NUMERO_DI_PARTITE/NUMERO_DI_SIMBOLI_DI_AVANZAMENTO))

        os.system("clear")
        print(colored("ATTENDERE LA FINE DELLA SIMULAZIONE...", "red"))
        for j in range(simboli_da_stampare):
            print("#", end="", flush=True)
        for j in range(NUMERO_DI_SIMBOLI_DI_AVANZAMENTO - simboli_da_stampare):
            print("_", end="", flush=True)


def gioca_poeri(solitario, contatore_vittorie, carte_pescate_tot, vettore_risultati_crescente):
    vittorie_tot_finora = 0
    if solitario.gioca():
        contatore_vittorie += 1
        vittorie_tot_finora = 1

    if(len(vettore_risultati_crescente) != 0):
        vittorie_tot_finora += vettore_risultati_crescente[-1]

    vettore_risultati_crescente.append(vittorie_tot_finora)
    carte_pescate_tot += poeri_solitario.mazzo.numero_carte_pescate()
    return contatore_vittorie, carte_pescate_tot 


def gioca_buri(solitario, contatore_vittorie, mazzetti_a_fine_partita_tot, vettore_risultati_crescente):
        vittorie_tot_finora = 0
        if solitario.gioca():
            contatore_vittorie += 1
            vittorie_tot_finora = 1

        if(len(vettore_risultati_crescente) != 0):
            vittorie_tot_finora += vettore_risultati_crescente[-1]

        vettore_risultati_crescente.append(vittorie_tot_finora)
        mazzetti_a_fine_partita_tot += len(solitario.tavolo.mazzetti)

        return contatore_vittorie, mazzetti_a_fine_partita_tot
    
def setup_buri_no_shuffle(solitario_dx_sx, solitario_sx_dx):
    solitario_dx_sx = bsn.Solitario()
    solitario_sx_dx = bsn.Solitario()
    solitario_sx_dx.mazzo = copy.deepcopy(solitario_dx_sx.mazzo) #in modo da partire dallo stesso mazzo


if __name__ == "__main__":
    poeri_solitario = ps.Solitario()
    buri_solitario  = bs.Solitario()
    buri_solitario_no_shuffle_dx_sx = bsn.Solitario()
    buri_solitario_no_shuffle_sx_dx = bsn.Solitario()
    buri_solitario_no_shuffle_sx_dx.mazzo = copy.deepcopy(buri_solitario_no_shuffle_dx_sx.mazzo) #in modo da partire dallo stesso mazzo


    buriNS_dx_sx_mazzo_vinto = False
    # Statistiche POERI
    poeri_vittorie_tot = 0
    poeri_carte_pescate_totali = 0
    poeri_vettore_risultati_crescente = []

    # Statistiche BURI
    buri_vittorie_tot = 0
    buri_mazzetti_totali = 0
    buri_vettore_risultati_crescente = []

    # Statistiche BURI NO SHUFFLE Dx -> Sx
    buriNS_dx_sx_n_perse_inizialmente_quando_poi_vince_tot = 0
    buriNS_dx_sx_volte_in_cui_alla_fine_vince_tot = 0
    buriNS_dx_sx_volte_in_cui_alla_fine_vince_perdendo_la_prima_tot = 0
    buriNS_dx_sx_partite_perse_con_un_mazzo = 0
    buriNS_dx_sx_ultima_partita_vinta = False
    buriNS_dx_sx_prima_partita_persa = False
    buriNS_dx_sx_mazzo_vinto = False

    # Statistiche BURI NO SHUFFLE Sx -> Dx
    buriNS_sx_dx_partite_perse_inizialmente_tot = 0
    buriNS_sx_dx_mazzo_vinto = False


    # STAMPA INIZIO
    #os.system("clear")
    print("ATTENDERE LA FINE DELLA SIMULAZIONE...")
    for i in range(NUMERO_DI_SIMBOLI_DI_AVANZAMENTO):
        print("_", end="", flush=True)

    # SIMULAZIONE
    for i in range(NUMERO_DI_PARTITE):

        stampa_caricamento(i)

        #--------------------------------------------------------

        poeri_vittorie_tot, poeri_carte_pescate_totali = gioca_poeri(poeri_solitario, poeri_vittorie_tot, poeri_carte_pescate_totali, poeri_vettore_risultati_crescente)

        #--------------------------------------------------------

        buri_vittorie_tot, buri_mazzetti_totali = gioca_buri(buri_solitario, buri_vittorie_tot, buri_mazzetti_totali, buri_vettore_risultati_crescente)

        #--------------------------------------------------------
        
        if(i % NUMERO_PARTITE_PRIMA_DI_CAMBIARE_IL_MAZZO == 0 and i != 0):
            #setup_buri_no_shuffle(buri_solitario_no_shuffle_dx_sx, buri_solitario_no_shuffle_sx_dx)
            buri_solitario_no_shuffle_dx_sx = bsn.Solitario()
            buri_solitario_no_shuffle_sx_dx = bsn.Solitario()
            buri_solitario_no_shuffle_sx_dx.mazzo = copy.deepcopy(buri_solitario_no_shuffle_dx_sx.mazzo) #in modo da partire dallo stesso mazzo


            # STAT dx -> sx
            if buriNS_dx_sx_ultima_partita_vinta:
                buriNS_dx_sx_volte_in_cui_alla_fine_vince_tot += 1

            if buriNS_dx_sx_ultima_partita_vinta and buriNS_dx_sx_prima_partita_persa:
                buriNS_dx_sx_volte_in_cui_alla_fine_vince_perdendo_la_prima_tot += 1
                buriNS_dx_sx_n_perse_inizialmente_quando_poi_vince_tot += buriNS_dx_sx_partite_perse_con_un_mazzo


            # RESET STAT dx -> sx
            buriNS_dx_sx_partite_perse_con_un_mazzo = 0
            buriNS_dx_sx_prima_partita_persa = False
            buriNS_dx_sx_mazzo_vinto = False

            # RESET STAT sx -> dx
            buriNS_sx_dx_mazzo_vinto = False


        if(not buriNS_dx_sx_mazzo_vinto):
            # GIOCA dx -> sx
            buriNS_dx_sx_ultima_partita_vinta = False
            if buri_solitario_no_shuffle_dx_sx.gioca():
                # Se vince
                buriNS_dx_sx_ultima_partita_vinta = True
                buriNS_dx_sx_mazzo_vinto = True

            else:
                # Se perde
                if(i % NUMERO_PARTITE_PRIMA_DI_CAMBIARE_IL_MAZZO == 0):
                    buriNS_dx_sx_prima_partita_persa = True

                buriNS_dx_sx_partite_perse_con_un_mazzo += 1

            buri_solitario_no_shuffle_dx_sx.setup_post_game_da_destra_a_sinistra()


        if(not buriNS_sx_dx_mazzo_vinto):
            # GIOCA sx -> dx
            if(not buri_solitario_no_shuffle_sx_dx.gioca()):
                # Se perde
                buriNS_sx_dx_partite_perse_inizialmente_tot += 1
            else:
                buriNS_sx_dx_mazzo_vinto = True

            buri_solitario_no_shuffle_sx_dx.setup_post_game_da_sinistra_a_destra()
#--------------------------------------------------------


    os.system("clear")


    # STAMPA RISULTATI POERI
    poeri_percentuale = poeri_vittorie_tot / NUMERO_DI_PARTITE * 100
    poeri_carte_medie_pescate = poeri_carte_pescate_totali / NUMERO_DI_PARTITE
    print(colored("SOLITARIO DEI POERI", "red"))
    print(colored("[Si conta continuamente da 1 a 3 sperando di non pescare il valore corrispondente]", "yellow"))
    print()
    print("Percentuale di vittorie: " + colored(f"{poeri_percentuale}%", "blue"))
    print("Carte medie pescate prima di perdere: " + colored(poeri_carte_medie_pescate, "blue"))

    print()
    print("---------------------------------------------")

    # STAMPA RISULTATI BURI
    buri_percentuale = buri_vittorie_tot / NUMERO_DI_PARTITE * 100
    buri_media_mazzetti = buri_mazzetti_totali / NUMERO_DI_PARTITE
    print(colored("SOLITARIO DI BURI", "red"))
    print(colored("[Ogni volta che peschi una carta dal mazzo crei un nuovo mazzetto. Puoi sovrapporre un mazzetto ad uno dei suoi due precedenti se ha seme o valore uguale. Bisogna concludere la partita con un solo mazzetto]", "yellow"))
    print()
    print("Percentuale di vittorie: " + colored(f"{buri_percentuale}%", "blue"))
    print("Media dei mazzetti rimanenti sul tavolo a fine partita: " + colored(buri_media_mazzetti, "blue"))

    print()
    print("---------------------------------------------")
    print("DISCLAIMER: Nei prossimi due tipi di solitario, una volta vinta una partita si continua a vincere senza sosta.") 
    print("---------------------------------------------")

    # STAMPA RISULTATI BURI NO SHUFFLE Dx -> Sx
    print(colored("SOLITARIO DI BURI NO SHUFFLE Dx -> Sx", "red"))
    print(colored("[Il solitario di Buri, solo che a fine game raccolgo i mazzetti impilandoli da quello più a destra a quello più a sinistra (al posto che mescolare sempre)]", "yellow"))
    print()
    print(f"Probabilità che questo metodo porti ad una streak di vittorie: " + colored(f"{buriNS_dx_sx_volte_in_cui_alla_fine_vince_tot / CAMBIAMENTI_TOTALI_DI_MAZZO * 100}%", "blue"))
    print("(Considerando solo i mazzi che portano ad una streak) Media partite perse prima di entrare in una streak di vittorie: " + colored(str(buriNS_dx_sx_n_perse_inizialmente_quando_poi_vince_tot / buriNS_dx_sx_volte_in_cui_alla_fine_vince_perdendo_la_prima_tot), "blue"))

    print()
    print("---------------------------------------------")

    # STAMPA RISULTATI BURI NO SHUFFLE Sx -> Dx
    print(colored("SOLITARIO DI BURI NO SHUFFLE Sx -> Dx", "red"))
    print(colored("[Il solitario di Buri, solo che a fine game raccolgo i mazzetti impilandoli da quello più a sinistra a quello più a destra (al posto che mescolare sempre)]", "yellow"))
    print()
    print("Con questo metodo sei sicuro di vincere sempre dopo qualche tentativo!!")
    print("Media di partite perse prima di entrare in streak di vittorie: " + colored(str(buriNS_sx_dx_partite_perse_inizialmente_tot / CAMBIAMENTI_TOTALI_DI_MAZZO), "blue"))




    # PLOT 2D DEI VETTORI DEI RUSULTATI con label e legenda

    plt.plot(poeri_vettore_risultati_crescente, label="Solitario dei Poeri")
    plt.plot(buri_vettore_risultati_crescente, label="Solitario di Buri")
    plt.legend()
    plt.ylabel('Vittorie')
    plt.xlabel('Partite')
    plt.title('Vittorie dei solitari')
    plt.show()



    


    

