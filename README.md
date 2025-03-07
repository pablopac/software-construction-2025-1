# software-construction-2025-1


Como correr interface-segregation-case-one

precondiciones:

* python3.9
* homebrew 
* Crear un archivo credenciales llamado `email_credentials.ini` y almacenarlo en la raiz del folder `email_services`

Pasos:

* en el terminal ingresar al root folder `email_services` con
* Crear interpreter en Pycharm Preferences > Python interpreter
* habilitar ambiente virtual con source `.venv/bin/activate`
* instalar requerimientos con `pip3 install -r requirements.txt`
* Si no se reconocen los imports dar click derecho sobre el folder 'email_services' y marcarlo como `Sources Root`
* Correr test que funciona `pytest -m ethereal`