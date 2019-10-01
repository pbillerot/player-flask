# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import os, logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# création de l'objet logger qui va nous servir à écrire dans les logs
#logger = logging.getLogger()
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
# création d'un second handler qui va rediriger chaque écriture de log sur la console
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
# logger.addHandler(stream_handler)

@app.route('/')
def accueil():
  message = "Player à votre écoute..."
  info(message)
  return jsonify(message)

@app.route('/play/<mediafile>')
def play(mediafile):
  message = "Play..."
  if os.system("pgrep --list-name audacious") == 0:
    filePath = os.path.join(app.root_path, 'media', mediafile)
    if os.path.exists(filePath):
      command = f"audacious {filePath}"
      iret = os.system(command)
      message = f"play {iret} {command}"
      if iret == 0:
        info(message)
      else:
        error(message)
    else:
      message = f"{filePath} non trouvé"
      error(message)  
  else:
    message = f"Audacious non démarré"
    error(message)

  return jsonify(message)

@app.route('/stop')
def stop():
  message = "Stop.."
  if os.system("pgrep --list-name audacious") == 0:
    command = f"audacious --stop"
    iret = os.system(command)
    message = f"stop {iret}"
    if iret == 0:
      info(message)
    else:
      error(message)
  else:
    message = f"Audacious non démarré"
    error(message)

  return jsonify(message)

def info(message):
  app.logger.info(message)
def error(message):
  app.logger.error(message)

# Tests unitaires
if __name__ == '__main__':
  info("Player en marche...")
  app.run(host='0.0.0.0', port=8053, debug=True)
