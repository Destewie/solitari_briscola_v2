import poeri_solitario
import buri_solitario
import os

NUMERO_DI_PARTITE = 10000000
NUMERO_DI_SIMBOLI_DI_AVANZAMENTO = 100

if __name__ == "__main__":
    poeri_solitario = poeri_solitario.Solitario()
    buri_solitario  = buri_solitario.Solitario()


    # Statistiche POERI
    poeri_contatore = 0
    poeri_carte_pescate_totali = 0

    # Statistiche BURI
    buri_contatore = 0


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

        if poeri_solitario.gioca():
            poeri_contatore += 1

        poeri_carte_pescate_totali += poeri_solitario.mazzo.numero_carte_pescate()

        #--------------------------------------------------------

        if buri_solitario.gioca():
            buri_contatore += 1

        #--------------------------------------------------------

    os.system("clear")

    # STAMPA RISULTATI POERI
    poeri_percentuale = poeri_contatore / NUMERO_DI_PARTITE * 100
    poeri_carte_medie_pescate = poeri_carte_pescate_totali / NUMERO_DI_PARTITE
    print(f"Percentuale di vittorie solitario dei poeri: {poeri_percentuale}%")
    print(f"Carte medie pescate nel solitario dei poeri: {poeri_carte_medie_pescate}")

    print()

    # STAMPA RISULTATI BURI
    buri_percentuale = buri_contatore / NUMERO_DI_PARTITE * 100
    print(f"Percentuale di vittorie solitario di Buri: {buri_percentuale}%")

