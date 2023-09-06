# Nido-Django-Docker-Dev

## Usar ambiente virtual *(requiere tener python instalado)*

1.  Creacion de la carpeta 

    ```py -3 -m venv venv```


2.  Activando venv
    
    ```venv\Scripts\activate```
    
3.  Instalar django y otras dependecias 

    ``` pip install -r requirements.txt ```

4.  Correr el servidor

    ```cd server```

    ```manage.py runserver```

5.  Para revisar la pagina es ir a la url http://localhost:8000/nido/
## Usar contenedor mostrando el proyecto lo mas cercano a produccion *(requiere tener Docker instalado)*

[![Alt text](https://img.youtube.com/vi/_et7H0EQ8fY/0.jpg)](https://www.youtube.com/watch?v=_et7H0EQ8fY)


### Antes de crear el contenedor renombrar ".envcopy" a ".env"

### Crear y correr contenedor

``` docker-compose up --build ```

### Solo correr contendor 

``` docker-compose up ```

### Correr contenedor en background 

``` docker-compose up -d```
### Detener contenedor
``` docker-compose stop```
### Borrar contenedor
``` docker-compose down```
### Depurar docker borrando imagenes, contenedores y volumenes sin usar 
``` docker system prune```




### Carpetas y archivos a revisar

* _/server/nido/templates/nido/_
    
    Aqui se encuentran los archivos html

* _/server/nido/urls.py_

    Aqui estan las direciones de las paginas

* _/server/nido/views.py_

    Aqui tenemos las vistas de cada pagina

* _/server/static_

    Aqui estan los archivos estaticos 

    * css
    * img
    * js



//  manage.py makemigrations
    manage.py migrate

    docker exec -it cms_server sh


revisar que el archivo sh sea LF en vez de CRLF








docker exec -t <container_name_or_id> pg_dump -U <database_user> -d <database_name> > /path/on/aws/server/backup.sql
docker exec -t <98366c41e2a0> pg_dump -U <postgres> -d <cmsdb> > /cms/backup.sql
sudo docker exec -t 98366c41e2a0 pg_dump -U postgres -d cmsdb > /cms/backup.sql

sudo docker exec -it 98366c41e2a0 mkdir /backup


sudo docker exec -t 98366c41e2a0 sh -c "pg_dump -U postgres -d cmsdb > /backup/backup.sql"

sudo docker cp 98366c41e2a0:/backup/backup.sql /home/ubuntu/backup.sql

scp ubuntu@<aws_server_ip>:/home/ubuntu/backup.sql /path/on/your/local/pc/
scp ubuntu@123.456.789.123:/home/ubuntu/backup.sql ~/Downloads/
scp ubuntu@44.202.131.33:/home/ubuntu/backup.sql ~/Downloads/

scp C:\Users\jmgh8\Downloads\nido_claves.ppk ubuntu@44.202.131.33:/path/on/server/

ssh -i C:\Users\jmgh8\Downloads\nido_ssh.pem ubuntu@44.202.131.33

scp -i C:\Users\jmgh8\Downloads\nido_ssh.pem ubuntu@44.202.131.33:/home/ubuntu/backup.sql

scp -i C:\Users\jmgh8\Downloads\nido_ssh.pem ubuntu@44.202.131.33:/home/ubuntu/backup.sql C:\Users\jmgh8\Desktop


