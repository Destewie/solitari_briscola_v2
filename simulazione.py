import poeri_solitario

NUMERO_DI_PARTITE = 10000000

if __name__ == "__main__":
    solitario = poeri_solitario.Solitario()

    # Itera un milione di volte il solitario dei poeri e tira fuori la percentuale di vittorie
    carte_poeri_pescate_totali = 0
    contatore = 0
    for i in range(NUMERO_DI_PARTITE):
        carte_poeri_pescate_totali += solitario.mazzo.numero_carte_pescate()
        if solitario.gioca():
            contatore += 1

    percentuale = contatore / NUMERO_DI_PARTITE * 100
    carte_medie_pescate_poeri = carte_poeri_pescate_totali / NUMERO_DI_PARTITE
    print(f"Percentuale di vittorie solitario dei poeri: {percentuale}%")
    print(f"Carte medie pescate nel solitario dei poeri: {carte_medie_pescate_poeri}")
