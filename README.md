# DTLAB-CHAT
[WEEK 3] Applicazione per le lezioni degli studenti del Cisco DTLAB 2021 sui capitoli 5-6 del corso DEVASC.

## Descrizione
Utilizzando il web framework Flask, i file realizzano un semplice servizio REST con storage in memoria
di una web chat. Sono realizzate le seguenti funzionalità:
- signup e signin con email e password degli utenti;
- gli utenti possono inviare messaggi agli altri utenti identificati per email;
Documentazione del framework Flask: https://flask.palletsprojects.com/en/1.1.x/

## ESERCIZIO 1 (15 minuti)
In questo esercizio, lavoreremo sul modulo user aggiungendo la funzionalità di login e memorizzando i file su testo.

### ESERCIZIO 1.1
Creare una route '/login' che consenta agli utenti di effettuare il login con la fuzione Login del modulo user;

### ESERCIZIO 1.3
Testare le funzionalità create con Postman;

## ESERCIZIO 2 (35 minuti)
In questo esercizio, implementeremo le due funzioni fondamentali di messaggistica: invio e ricezione dei messaggi.

### ESERCIZIO 2.1
Creare un modulo 'message.py' con una funzione 'SaveMessage' che memorizza un messaggio.
In particolare, un messaggio deve contenere:
- mittente: id dell'utente che ha inviato il messaggio;
- destinatario: id dell'utente a cui è destinato il messaggio;
- contenuto: testo del messaggio;

#### DISCUSS: su altre informazioni che possono servire. Ad esempio:
- se volessi in futuro dare la possibilità di eliminare un messaggio inviato?
- se volessi mostrare i messaggi di una conversazione con quale ordine li mostrerei?
Come gli utenti i messaggi devono essere salvati su file.

#### DISCUSS: come gestiamo l'oggetto result? Nel codice iniziale era parte del modulo user, ma adesso anche il modulo message lo usa. Come facciamo a risolvere?

### ESERCIZIO 2.2
Creare una route POST "/INBOX" che consenta agli utenti di inviare i messaggi ad un altro utente;

### ESERCIZIO 2.3
Creare una funzione GetMessage che consente ad un utente di ricevere tutti i messaggi diretti a lui e aggiungerla in una route GET "/inbox";
Un utente per inviare un messaggio: scrive il corpo e lo manda ad un email.
Come faccio a capire chi sta inviando la richiesta? Mi serve il suo ID per inserirlo nel campo mittente...

#### HINT: utilizzare la documentazione per capire come accedere alla variabile <id_utente>
#### DISCUSS: ma quindi tutti quelli che hanno l'ID di un utente possono leggere i suoi messaggi?

### ESERCIZIO 2.4
Testare la funzionalità creata con Postman.

## ESERCIZIO 3 (20 minuti)
In questo esercizio, ci occupiamo di creare la funzione "Elimina account". Per questioni di sicurezza, ogni utente può eliminare SOLO il proprio account. Per fare ciò, dobbiamo inviare una richiesta autenticata: ovvero inserire nell'header un campo Authorization che contenga le informazioni che ci assicurano che chi sta facendo la richiesta è autorizzato.

### ESERCIZIO 3.1
Aggiungere la route:
- DELETE /user/<id_utente>: l'utente invia email e password per cancellare il suo account:  

#### HINT 1: utilizzare la documentazione per capire come accedere all'header della richiesta ed estrarre le credenziali dalla richiesta

Esempio
- DELETE /user/123 -> cancella utente con ID 123;

Per inviare una richiesta con autenticazione, bisogna utilizzare un "authorization header". Come abbiamo visto, gli header aggiungono ulteriori informazioni sul come trattare la richiesta; sottoforma di coppie chiave valore. Ad esempio:

**Content-Type: application/json**: indica di interpretare il contentuto del corpo della richiesta come json.

Utilizzando un Authorization header possiamo inviare informazioni per identificare l'utente nel sistema. Come visto in precedenza, ci sono diversi tipi di autorizzazione. Proviamo ad utilizzare la basic auth: inviamo username e password separati da ":" in base64;

Lato server, bisogna validare la richiesta verificando prima che le credenziali siano corrette e poi eseguire l'operazione. Se la convalida non va a buon fine, è buona norma ritornare "401 - Unauthorized". 

### ESERCIZIO 3.2 
Testare la funzionalità creata con Postman.

## ESERCIZIO 4 (20 minuti)
In questo esercizio, ci occupiamo di installare l'applicazione utilizzando Docker.

### ESERCIZIO 4.1
Innanzitutto dobbiamo decidere quale immagine utilizzare. Ci serve un'immagine di Python 3. Scegliamola da https://hub.docker.com

Se cerchiamo python e andiamo nella sezione tag, troviamo tantissime immagini Python, ognuna con versione e dimensione diversa. Proviamo a scegliere la versione 3.9.2 con dimensione minore. Questa sarà il punto di partenza del Dockerfile

### ESERCIZIO 4.2
Creiamo il Dockerfile e inseriamo come statement FROM il nome dell'immagine di scelta. 
Scegliamo una cartella dove mettere il nostro codice con lo statement WORKDIR.
Copiamo i file del codice e installiamo le dipendenze con pip usando lo statement RUN.
Terminiamo il file con lo statement CMD che eseguirà l'applicazione.

#### DISCUSS: se la creazione dell'immagine fallisse, dovremmo riscaricare tutte le dipendenze con l'esecuzione del comando RUN pip install ecc. Come possiamo fare per risparmiarci l'installazione delle dipendenze se modifichiamo il codice?

### ESERCIZIO 4.3
Creiamo l'immagine con il comando docker build.
Creiamo un container con il comando docker run.

#### HINT: non dimentichiamo di pubblicare la porta per raggiungere il container dall'esterno

### ESERCIZIO 4.4 
Testiamo l'applicazione da Postman.

## EXTRA
Salvare su file gli utenti e i messaggi per avere uno storage anche non volatile.

#### WARNING: la creazione di un Docker container abilita la creazione di un layer in scrittura temporeano. Quando chiudiamo un docker container perdiamo i file creati su di esso. Per rendere persistenti i progressi fatti da un Docker container, deve essere utilizzato un Docker Volume che esula dagli obiettivi del corso!


