# **COMPONENTI**
Ventura Samuele  
Matricola: 793060  
Repository Git: [https://gitlab.com/s.ventura/prosvil1](https://gitlab.com/s.ventura/prosvil1)  

# **APPLICAZIONE**
Si è sviluppata una semplice applicazione web con la quale è possibile creare degli utenti o accedere tramite delle credenziali già registrate. 

Ad ogni accesso alla pagina _WelcomeUser.html_ l'applicazione mostra il numero di volte che l'utente ha già visitato questa pagina.

Per sviluppare l'app si è sfruttato il linguaggio _Python_ e il framework _Flask_, mentre per salvare i dati inseriti dall'utente e verifarne la presenza si è sfruttato un DB mysql.

# **PUNTI DEVOPS SVILUPPATI**
## **Containerization**
Il primo punto sviluppato è stata la creazione di immagini, da cui poi attivare i container necessari per eseguire l'app, sfruttando la piattaforma _Docker_.

Per creare le immagini sono stati scritti i tre seguenti file:

* _Dockerfile_
    * si è indicata l'immagine presente su _DockerHub_ da scaricare per avviare il file _app.py_
 
            FROM  python:2.7

    * si è creata una cartella di lavoro in cui sono stati copiati i file dell'app,  e il file da cui si installano automaticamente i moduli necessari
   
            ADD . /code
            WORKDIR /code/
            RUN pip install -r requirements.txt

    * si è definita la porta su cui il container possa comunicare con l'host su cui viene avviato.  
  
            EXPOSE 8082    
  
* _docker-compose.yml_ 
    * si sono definiti i due container, web che rappresenta la parte di interfaccia e server, e db che invece rappresenta la parte di database 

            links:
            - db    / prorpietà definita nel container web e indica la                   
                            dipendenza con il container db
            
            ports:
            - "3306:3306" / con questo comando si mappano le porte tra host e container


* _requirements.txt_ : file in cui si elencano i vari moduli, in questo caso librerie sfruttate dal linguaggio python
    

Per avviare l'app è necessario eseguire il comando _`docker-compose up`_ che legge ed esegue le istruzioni scritte nei tre file appena descritti e avvia i container implementati, eseguendo l'app, sulla porta specifica nel dockerfile.

Con il comando _`docker image ls`_ è possibile vedere tutte le immagini scaricate che possono essere avviate con _`docker run`_.\
Si possono anche elencare tutti i container e servizi attivi al momento con _`docker ps`_ e _`docker container ls`_.

## **Continuous Integration/Continuous Developmen**
Per implementare un pipeline di CI/CD si sfrutterà il tool interno di GitLab  