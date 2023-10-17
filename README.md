# solitari_briscola_v2
Simulazioni di solitari svolti con le carte da briscola.  
Di seguito si possono trovare tutte le informazioni riguardo alle regole e ai dati raccolti di ognuno.

## Solitario poeri
### Obiettivo
Riuscire ad estrarre con successo tutte le carte dal mazzo
### Regole 
- Si mescola il mazzo
- Si estraggono, una alla volta, le carte dalla cima del mazzo
- Ogni volta che viene estratta una carta, si conta
- Il conteggio avviene così: 1... 2... 3... 1... 2... 3... 
- Se il valore della carta estratta corrisponde al numero contato, allora si perde

### Analisi Dati 
- Percentuale di vittoria
- Media delle carte pescate dal mazzo prima di concludere una partita

## Solitario Buri
### Obiettivo
Rimanere alla fine del gioco con un solo mazzetto sul tavolo
### Regole 
- Si mescola il mazzo
- Si estraggono, una alla volta, le carte dalla cima del mazzo
- Le carte che vengono estratte verranno posizionate lungo una linea che si espande solo verso destra
- Ogni volta che si posiziona una nuova carta sul tabellone, c'è la possibilità che si possa sovrapporre ad uno dei due mazzetti alla sua sinistra
Regole per la sovrapposizione: 
1. Una carta (o mazzetto) si deve sovrapporre ad uno dei due mazzetti precedenti se ha seme o valore uguale con la carta in cima al mazzetto
2. Si parte a controllare dal mazzetto più vicino
- Quando si sovrappone una carta (o mazzetto) ad un altro mazzetto, l'effetto si deve propagare anche ai relativi mazzetti a sinistra
### Analisi Dati 
- Percentuale di vittoria
- Media dei mazzetti rimasti sul tavolo al concludersi di una partita

## Solitario Buri no shuffle da destra a sinistra
### Obiettivo
Lo stesso del gioco originale
### Regole 
- Per la prima partita il mazzo viene mescolato
- Il mazzo di tutte le _p_ partite successive verrà costruito sovrapponendo i mazzi rimasti sul tavolo partendo dal mazzetto più a destra fino a quello più a sinistra
### Analisi Dati 
Si è osservato che, una volta che un mazzo vince una volta, continuerà a vincere finché non viene rimescolato.  
Siamo interessati a:
- Percentuale di mescolate che portano ad una streak di vittorie.
- Medie di partite perse prima di entrare in una streak di vittorie

## Solitario Buri no shuffle da sinistra a destra
### Obiettivo
Lo stesso del gioco originale
### Regole 
- Per la prima partita il mazzo viene mescolato
- Il mazzo di tutte le _p_ partite successive verrà costruito sovrapponendo i mazzi rimasti sul tavolo partendo dal mazzetto più a sinistra fino a quello più a destra
### Analisi Dati 
Con questo metodo si è osservato che ogni mescolata porta inevitabilmente ad una vittoria dopo sufficienti partite.  
Siamo interessati a:
- Media di partite perse prima di entrare in una streak di vittorie

## Solitario dei re
### Obiettivo
Avere tutte le carte scoperte al posto giusto quando si pesca o si scopre il quarto re
### Regole
- Mescolo il mazzo
- Dispongo le carte in 4 file da 9 carte coperte ciascuna 
- Ogni fila rappresenta un determinato seme e ogni colonna i valori dall'asso al cavallo
- Le restanti 4 carte formano un mazzetto da cui si pescherà
- Pesco una carta tra le 4 non messe sul tavolo e la posiziono scoperta al suo posto sul tavolo
- Scopro la carta che prima stava nel posto della carta appena posizionata e la metto al suo posto
- Ripeto finché non pesco un re
- Ogni volta che pesco un re, lo metto al suo posto (finora non occupato da nessun'altra carta) e pesco nuovamente dal mazzetto
- Quando viene pescato il quarto re, il gioco finisce
- Si può vincere se, a fine partita, tutte le carte rimaste coperte sul tavolo sono al posto giusto
### Analisi Dati 


## Solitario dell'orologio
### Obiettivo
Coprire tutte le carte posizionate come le lancette dell'orologio
### Regole
- Mescolo il mazzo
- Dispongo 12 carte (dette l'orologio) sul tavolo estraendole dalla cima del mazzo 
> (Si chiama gioco dell'orologio perché quando viene fatto su un tavolo, le 12 carte menzionate prima vengono messe a mò di lancette dell'orologio)
- Dalle restanti carte se ne scarta una e se ne estrae un'altra
- Si coprono tutte le carte dell'orologio con valore uguale alla carta appena estratta dal mazzo di pesca
- Il gioco finisce quando il mazzo di pesca finisce o quando si coprono tutte le carte dell'orologio
