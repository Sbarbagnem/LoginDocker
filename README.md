# **COMPONENTI**
Ventura Samuele  
Matricola: 793060  
Repository Git: [https://gitlab.com/s.ventura/prosvil1](https://gitlab.com/s.ventura/prosvil1)  

# **APPLICAZIONE**
Si è sviluppata una semplice applicazione web con la quale è possibile creare degli utenti (nome,cognome,email e password) e accedere attraverso le proprie credenziali. 

Ad ogni accesso alla pagina _WelcomeUser.html_ l'applicazione mostra il numero di volte che l'utente ha già visitato questa pagina.

Per sviluppare l'app si è sfruttato il linguaggio _Python_ e il framework _Flask_, mentre per salvare i dati inseriti dall'utente e verificarne la presenza si è sfruttato il database MySql.

# **PUNTI DEVOPS SVILUPPATI**
## **Containerization**
Il primo punto sviluppato è stata la creazione di immagini, da cui poi attivare i container necessari per eseguire l'app, sfruttando la piattaforma _Docker_.

Per creare le immagini sono stati scritti i seguenti file:

* 2 file denominati _Dockerfile_
    * sono stati utilizzati per creare due immagini, una per creare un container _MySQL_ e una per creare l'applicazione in ambiente _Python_. Per la prima si è sfruttata l'immagine ufficiale presente nel DockerHub mysql:5.6, per quanto rigurda python invece si è sfruttata un'immagine di partenza ridotta, python:2.7-alpine3.7 e si sono installati i pacchetti necessari per ridurre la dimensione dell'immagine stessa.
    
  
* _docker-compose.yml_ 
    * si sono definiti i due container, web che rappresenta la parte di interfaccia e server, e db che invece rappresenta la parte di database, ecco alcuni esempi di istruzioni inserite nel file


* _requirements.txt_ : file in cui si elencano i vari moduli, in questo caso librerie sfruttate dal linguaggio python
    

Per avviare l'app è necessario eseguire il comando <span style="color:red">**_docker-compose up_**</span> che legge ed esegue le istruzioni scritte nei tre file appena descritti e avvia i container implementati, eseguendo l'app, sulla porta specifica nel dockerfile.

Con il comando <span style="color:red">**_docker image ls_**</span> è possibile vedere tutte le immagini scaricate che possono essere avviate con  <span style="color:red">**_docker run_**</span>

Si possono anche elencare tutti i container e servizi attivi al momento con  <span style="color:red">**_docker ps_**</span>
          
Come si può vedere dall'immagine i servizi attivi sono i due indicati nel docker-compose.

## **Continuous Integration**
Per sviluppare una pipeline di continuous integration si è sfruttato il tool interno di gitlab che permette di definire vari stage automaticamente avviati nel momento di una commit.
Si sono definiti due stage:  

* build che costruisce le due immagini e avvia i due container 
* test che invece esegue dei semplici test sui templates creati

La commit è effettivamente realizzata solo se tutti gli stage sono eseguiti con successo.
 