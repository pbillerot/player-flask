# -*- coding: utf-8 -*-
"""
  Point d'entrée du player
  https://medium.com/@trstringer/logging-flask-and-gunicorn-the-manageable-way-2e6f0b8beb2f
"""
import logging
from logging.handlers import RotatingFileHandler

import os
from flask import Flask

from player.player import player

# création de l'objet logger qui va nous servir à écrire dans les logs
# logger = logging.getLogger()
# on met le niveau du logger à DEBUG, comme ça il écrit tout
# logger.setLevel(logging.DEBUG)
# création d'un formateur qui va ajouter le temps, le niveau
# de chaque message quand on écrira un message dans le log
# formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 5Mo
# file_handler = RotatingFileHandler('log/player.log', 'a', 5000000, 1)
# on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
# créé précédement et on ajoute ce handler au logger
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
# création d'un second handler qui va rediriger chaque écriture de log
# sur la console
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
# logger.addHandler(stream_handler)

def create_app():
  app = Flask(__name__)
  app.register_blueprint(player)
  logging.info("Player en marche...")
  return app

app = create_app()
