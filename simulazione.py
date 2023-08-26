import poeri_solitario
import buri_solitario
import os
import matplotlib.pyplot as plt

NUMERO_DI_PARTITE = 1000
NUMERO_DI_SIMBOLI_DI_AVANZAMENTO = 100

if __name__ == "__main__":
    poeri_solitario = poeri_solitario.Solitario()
    buri_solitario  = buri_solitario.Solitario()


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
    print("[Quello in cui sovrapponi mazzetti vicini se hai seme o valore uguale. Bisogna concludere la partita con un solo mazzetto.")
    print()
    print(f"Percentuale di vittorie: {buri_percentuale}%")
    print(f"Media dei mazzetti rimanenti sul tavolo a fine partita: {buri_media_mazzetti}")


    # PLOT 2D DEI VETTORI DEI RUSULTATI con label e legenda

    plt.plot(poeri_vettore_risultati_crescente, label="Solitario dei Poeri")
    plt.plot(buri_vettore_risultati_crescente, label="Solitario di Buri")
    plt.legend()
    plt.ylabel('Vittorie')
    plt.xlabel('Partite')
    plt.title('Vittorie dei solitari')
    plt.show()



    


    

