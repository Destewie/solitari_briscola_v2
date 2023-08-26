import poeri_solitario as ps
import buri_solitario as bs
import buri_solitario_no_shuffle as bsn
import os
import matplotlib.pyplot as plt
import copy

NUMERO_DI_PARTITE = 10000
NUMERO_DI_SIMBOLI_DI_AVANZAMENTO = 100

if __name__ == "__main__":
    poeri_solitario = ps.Solitario()
    buri_solitario  = bs.Solitario()
    buri_solitario_no_shuffle_dx_sx = bsn.Solitario()
    buri_solitario_no_shuffle_sx_dx = bsn.Solitario()
    buri_solitario_no_shuffle_sx_dx.mazzo = copy.deepcopy(buri_solitario_no_shuffle_dx_sx.mazzo) #in modo da partire dallo stesso mazzo


    # Statistiche POERI
    poeri_contatore = 0
    poeri_carte_pescate_totali = 0
    poeri_vettore_risultati_crescente = []
    poeri_tmp = 0

    # Statistiche BURI
    buri_contatore = 0
    buri_mazzetti_totali = 0
    buri_vettore_risultati_crescente = []
    buri_tmp = 0

    # Statistiche BURI NO SHUFFLE Dx -> Sx
    buri_no_shuffle_dx_sx_contatore = 0
    buri_no_shuffle_mazzetti_dx_sx_totali = 0
    buri_no_shuffle_dx_sx_vettore_risultati_crescente = []
    buri_no_shuffle_dx_sx_tmp = 0

    # Statistiche BURI NO SHUFFLE Sx -> Dx
    buri_no_shuffle_sx_dx_contatore = 0
    buri_no_shuffle_mazzetti_sx_dx_totali = 0
    buri_no_shuffle_sx_dx_vettore_risultati_crescente = []
    buri_no_shuffle_sx_dx_tmp = 0


    # STAMPA INIZIO
    os.system("clear")
    print("ATTENDERE LA FINE DELLA SIMULAZIONE...")
    for i in range(NUMERO_DI_SIMBOLI_DI_AVANZAMENTO):
        print("_", end="", flush=True)

    # SIMULAZIONE
    for i in range(NUMERO_DI_PARTITE):

        # STAMPA PROGRESSO
        if i % (NUMERO_DI_PARTITE/NUMERO_DI_SIMBOLI_DI_AVANZAMENTO) == 0:
            simboli_da_stampare = int(i / (NUMERO_DI_PARTITE/NUMERO_DI_SIMBOLI_DI_AVANZAMENTO))

            os.system("clear")
            print("ATTENDERE LA FINE DELLA SIMULAZIONE...")
            for j in range(simboli_da_stampare):
                print("#", end="", flush=True)
            for j in range(NUMERO_DI_SIMBOLI_DI_AVANZAMENTO - simboli_da_stampare):
                print("_", end="", flush=True)


        #--------------------------------------------------------

        poeri_tmp = 0
        if poeri_solitario.gioca():
            poeri_contatore += 1
            poeri_tmp = 1

        if(len(poeri_vettore_risultati_crescente) == 0):
            poeri_vettore_risultati_crescente.append(poeri_tmp)
        else:
            poeri_tmp += poeri_vettore_risultati_crescente[-1]  
            poeri_vettore_risultati_crescente.append(poeri_tmp)

        poeri_carte_pescate_totali += poeri_solitario.mazzo.numero_carte_pescate()

        #--------------------------------------------------------

        buri_tmp = 0
        if buri_solitario.gioca():
            buri_contatore += 1
            buri_tmp = 1

        if(len(buri_vettore_risultati_crescente) != 0):
            buri_tmp += buri_vettore_risultati_crescente[-1]

        buri_vettore_risultati_crescente.append(buri_tmp)
        buri_mazzetti_totali += len(buri_solitario.tavolo.mazzetti)

        #--------------------------------------------------------

        buri_no_shuffle_dx_sx_tmp = 0
        if buri_solitario_no_shuffle_dx_sx.gioca():
            buri_no_shuffle_dx_sx_contatore += 1
            buri_no_shuffle_dx_sx_tmp = 1

        if(len(buri_no_shuffle_dx_sx_vettore_risultati_crescente) != 0):
            buri_no_shuffle_dx_sx_tmp += buri_no_shuffle_dx_sx_vettore_risultati_crescente[-1]

        buri_no_shuffle_dx_sx_vettore_risultati_crescente.append(buri_no_shuffle_dx_sx_tmp)
        buri_no_shuffle_mazzetti_dx_sx_totali += len(buri_solitario_no_shuffle_dx_sx.tavolo.mazzetti)

        buri_solitario_no_shuffle_dx_sx.setup_post_game_da_destra_a_sinistra()

        #--------------------------------------------------------

        buri_no_shuffle_sx_dx_tmp = 0
        if buri_solitario_no_shuffle_sx_dx.gioca():
            buri_no_shuffle_sx_dx_contatore += 1
            buri_no_shuffle_sx_dx_tmp = 1

        if(len(buri_no_shuffle_sx_dx_vettore_risultati_crescente) != 0):
            buri_no_shuffle_sx_dx_tmp += buri_no_shuffle_sx_dx_vettore_risultati_crescente[-1]

        buri_no_shuffle_sx_dx_vettore_risultati_crescente.append(buri_no_shuffle_sx_dx_tmp)
        buri_no_shuffle_mazzetti_sx_dx_totali += len(buri_solitario_no_shuffle_sx_dx.tavolo.mazzetti)

        buri_solitario_no_shuffle_sx_dx.setup_post_game_da_sinistra_a_destra()

        #--------------------------------------------------------


    os.system("clear")

    # STAMPA RISULTATI POERI
    poeri_percentuale = poeri_contatore / NUMERO_DI_PARTITE * 100
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
    buri_percentuale = buri_contatore / NUMERO_DI_PARTITE * 100
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
    buri_no_shuffle_dx_sx_percentuale = buri_no_shuffle_dx_sx_contatore / NUMERO_DI_PARTITE * 100
    buri_no_shuffle_dx_sx_media_mazzetti = buri_no_shuffle_mazzetti_dx_sx_totali / NUMERO_DI_PARTITE
    print("SOLITARIO DI BURI NO SHUFFLE Dx -> Sx")
    print("[Il solitario di Buri, solo che a fine game raccolgo i mazzetti impilandoli da quello più a destra a quello più a sinistra]")
    print()
    print(f"Percentuale di vittorie: {buri_no_shuffle_dx_sx_percentuale}%")
    print(f"Media dei mazzetti rimanenti sul tavolo a fine partita: {buri_no_shuffle_dx_sx_media_mazzetti}")

    print()
    print("---------------------------------------------")
    print()

    # STAMPA RISULTATI BURI NO SHUFFLE Sx -> Dx
    buri_no_shuffle_sx_dx_percentuale = buri_no_shuffle_sx_dx_contatore / NUMERO_DI_PARTITE * 100
    buri_no_shuffle_sx_dx_media_mazzetti = buri_no_shuffle_mazzetti_sx_dx_totali / NUMERO_DI_PARTITE
    print("SOLITARIO DI BURI NO SHUFFLE Sx -> Dx")
    print("[Il solitario di Buri, solo che a fine game raccolgo i mazzetti impilandoli da quello più a sinistra a quello più a destra]")
    print()
    print(f"Percentuale di vittorie: {buri_no_shuffle_sx_dx_percentuale}%")
    print(f"Media dei mazzetti rimanenti sul tavolo a fine partita: {buri_no_shuffle_sx_dx_media_mazzetti}")




    # PLOT 2D DEI VETTORI DEI RUSULTATI con label e legenda

    plt.plot(poeri_vettore_risultati_crescente, label="Solitario dei Poeri")
    plt.plot(buri_vettore_risultati_crescente, label="Solitario di Buri")
    plt.plot(buri_no_shuffle_dx_sx_vettore_risultati_crescente, label="Solitario di Buri NO SHUFFLE Dx -> Sx")
    plt.plot(buri_no_shuffle_sx_dx_vettore_risultati_crescente, label="Solitario di Buri NO SHUFFLE Sx -> Dx")
    plt.legend()
    plt.ylabel('Vittorie')
    plt.xlabel('Partite')
    plt.title('Vittorie dei solitari')

    # limita l'asse y al valore massimo raggiunto dai vettori dei risultati tranne sx-dx
    valore_max = max(poeri_vettore_risultati_crescente[-1], buri_vettore_risultati_crescente[-1], buri_no_shuffle_dx_sx_vettore_risultati_crescente[-1])
    plt.ylim(0, valore_max + valore_max/10)

    plt.show()



    


    

