# poo_ti32_Lprogramacion orientada a objetos 
Repositiorio con ejercicios de programacion orientada a objetos en python 
## 1. creacion del archivo .gitignore
Crear un archivo llamado .gitignore en la raiz del proyecto
 
````shell 
.gitignore
````



## 2 . crear virtual enviroment

````shell 


python -m venv venv
````

## 3. activar el entorno virtual
Se activa el ambiente virtual para el proyecto  

````shell
source  .venv/bin/activate
````
## 4. Actulizar **pip**
Se actualiza **pip** para poder instalar las ultimas versiones de las librerias
````shell
pip install --update pip
````
## 5. instalar los paquetes necesarios
Se utiliza **pip** para instalar los paquetes necesarios para el proyecto
````shell
pip install web.py
````
## 6. Generar el archivo **requirements.tx**
Generar el archivo **requirements.txt** con todas las dependencias necesarias para el proyecto
````shell
pip freeze > requirement.txt

````
## 7. Generar el archivo **runtime.txt**
Generar el archivo **runtime.txt** para indicar la version de python que se esta actualizando
````shell
python3 -V > runtime.txt

````

## 8. indexar los cambios utilizando **git**
se indexaron las modificaciones y nuevos archivos del proyecto
````shell
git add .
````
## 9.cramos un **commit** de los cambios 
Se genera un **comit** con un comentario que indica los cambios que se realizaron
````shell
git commit -m "crear configuracion basica "
````
## 10. Se actualiza el repositorio con los ultimos cambios
Se envian los cambios realizados al repositorio 
````shell
git push -u origin main 
````

