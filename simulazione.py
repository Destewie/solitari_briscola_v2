import poeri_solitario as ps
import buri_solitario as bs
import buri_solitario_no_shuffle as bsn
import os
import matplotlib.pyplot as plt
import copy

NUMERO_DI_PARTITE = 10000
NUMERO_DI_SIMBOLI_DI_AVANZAMENTO = 100
NUMERO_PARTITE_PRIMA_DI_CAMBIARE_IL_MAZZO = 50
CAMBIAMENTI_TOTALI_DI_MAZZO = int(NUMERO_DI_PARTITE / NUMERO_PARTITE_PRIMA_DI_CAMBIARE_IL_MAZZO)

def stampa_caricamento(i_partita):
    # STAMPA PROGRESSO
    if i_partita % (NUMERO_DI_PARTITE/NUMERO_DI_SIMBOLI_DI_AVANZAMENTO) == 0:
        simboli_da_stampare = int(i / (NUMERO_DI_PARTITE/NUMERO_DI_SIMBOLI_DI_AVANZAMENTO))

        os.system("clear")
        print("ATTENDERE LA FINE DELLA SIMULAZIONE...")
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

    # Statistiche BURI NO SHUFFLE Sx -> Dx
    buriNS_sx_dx_partite_perse_inizialmente_tot = 0


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

            # STAT dx -> sx



            # RESET STAT dx -> sx
            buriNS_dx_sx_partite_perse_con_un_mazzo = 0
            buriNS_dx_sx_prima_partita_persa = False

            # RESET STAT sx -> dx


        buriNS_dx_sx_ultima_partita_vinta = False
        if buri_solitario_no_shuffle_dx_sx.gioca():
            # Se vince
            buriNS_dx_sx_ultima_partita_vinta = True
        else:
            # Se perde
            if(i % NUMERO_PARTITE_PRIMA_DI_CAMBIARE_IL_MAZZO == 0):
                buriNS_dx_sx_prima_partita_persa = True

            buriNS_dx_sx_partite_perse_con_un_mazzo += 1

        buri_solitario_no_shuffle_dx_sx.setup_post_game_da_destra_a_sinistra()

        #--------------------------------------------------------


    os.system("clear")


    # STAMPA RISULTATI POERI
    poeri_percentuale = poeri_vittorie_tot / NUMERO_DI_PARTITE * 100
    poeri_carte_medie_pescate = poeri_carte_pescate_totali / NUMERO_DI_PARTITE
    print("SOLITARIO DEI POERI")
    print("[Si conta continuamente da 1 a 3 sperando di non pescare il valore corrispondente]")
    print()
    print(f"Percentuale di vittorie: {poeri_percentuale}%")
    print(f"Carte medie pescate prima di perdere: {poeri_carte_medie_pescate}")

    print()
    print("---------------------------------------------")
    print()

    # STAMPA RISULTATI BURI
    buri_percentuale = buri_vittorie_tot / NUMERO_DI_PARTITE * 100
    buri_media_mazzetti = buri_mazzetti_totali / NUMERO_DI_PARTITE
    print("SOLITARIO DI BURI")
    print("[Quello in cui sovrapponi mazzetti vicini se hai seme o valore uguale. Bisogna concludere la partita con un solo mazzetto]")
    print()
    print(f"Percentuale di vittorie: {buri_percentuale}%")
    print(f"Media dei mazzetti rimanenti sul tavolo a fine partita: {buri_media_mazzetti}")

    print()
    print("---------------------------------------------")
    print()

    # STAMPA RISULTATI BURI NO SHUFFLE Dx -> Sx
    print("SOLITARIO DI BURI NO SHUFFLE Dx -> Sx")
    print("[Il solitario di Buri, solo che a fine game raccolgo i mazzetti impilandoli da quello più a destra a quello più a sinistra]")
    print()
    print(f"Le carte vengono rimescolate {CAMBIAMENTI_TOTALI_DI_MAZZO} volte")
    print(f"Percentuale esito positivo sovrapponendo i mazzetti a fine partita {NUMERO_PARTITE_PRIMA_DI_CAMBIARE_IL_MAZZO} volte prima di rimescolare casualmente il mazzo: {buriNS_dx_sx_volte_in_cui_alla_fine_vince_tot / CAMBIAMENTI_TOTALI_DI_MAZZO * 100}%")
    print(f"Media partite perse prima di entrare in streak di vittorie con lo stesso mazzo (quando la prima partita non è già vincente): {buriNS_dx_sx_n_perse_inizialmente_quando_poi_vince_tot / buriNS_dx_sx_volte_in_cui_alla_fine_vince_perdendo_la_prima_tot}")
    print("(Se la prima partita è vincente, anche tutte le successive lo sono)")

    print()
    print("---------------------------------------------")
    print()

    # STAMPA RISULTATI BURI NO SHUFFLE Sx -> Dx
    print("SOLITARIO DI BURI NO SHUFFLE Sx -> Dx")
    print("[Il solitario di Buri, solo che a fine game raccolgo i mazzetti impilandoli da quello più a sinistra a quello più a destra]")
    print()




    # PLOT 2D DEI VETTORI DEI RUSULTATI con label e legenda

    plt.plot(poeri_vettore_risultati_crescente, label="Solitario dei Poeri")
    plt.plot(buri_vettore_risultati_crescente, label="Solitario di Buri")
    plt.legend()
    plt.ylabel('Vittorie')
    plt.xlabel('Partite')
    plt.title('Vittorie dei solitari')
    plt.show()



    


    

