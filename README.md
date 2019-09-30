Player en Flask
===============

Programme écrit en Flask Python
qui utilise **audacious** en tant que player


Python dans un environnement virtuel 3.6
----------------------------------------
```
virtualenv -p python3 venv
source venv/bin/activate
pip install flask gunicorn
# Pour environnement de Dev VSCodium
pip install pylint rope
```

Tests unitaires
---------------
    source venv/bin/activate
    gunicorn --bind 127.0.0.1:3000 wsgi:app

