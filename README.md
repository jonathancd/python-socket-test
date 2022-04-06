# Instalar Virtualenviroment
    - pip install virtualenv

# Crear enviroment
    Ejecute el siguiente comando:
        - virtualenv venv

# Activar virtualenv
    Ejecute los siguientes comandos:
        - Set-ExecutionPolicy Unrestricted -Scope Process [Si no permite activar el venv en Windows]
        - venv\Scripts\activate

# Instalar dependencias/packages
    - pip install websockets
    - pip install sympy
    - pip install pytest

# Ejecutar script
    Una vez activado el venv, ejecute el siguiente comando:
        - python main.py

# Probar tests:
    Si ya instaló pytest, ejecute el siguiente comando: 
        - pytest