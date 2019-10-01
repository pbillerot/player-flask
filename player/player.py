# -*- coding: utf-8 -*-
from flask import Flask, Blueprint, jsonify
import time
import os, logging

app = Flask(__name__)

# pgrep --list-name audaciou

@app.route('/')
def accueil():
  message = "Player à votre écoute..."
  logging.info(f"player {message}")
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
        logging.info(f"player {message}")
      else:
        logging.error(f"player {message}")
    else:
      message = f"{filePath} non trouvé"
      logging.error(f"player {message}")  
  else:
    message = f"Audacious non démarré"
    logging.error(f"player {message}")

  return f'{message}\n'

@app.route('/stop')
def stop():
  message = "Stop.."
  if os.system("pgrep --list-name audacious") == 0:
    command = f"audacious --stop"
    iret = os.system(command)
    message = f"stop {iret}"
    if iret == 0:
      logging.info(f"player {message}")
    else:
      logging.error(f"player {message}")
  else:
    message = f"Audacious non démarré"
    logging.error(f"player {message}")

  return f'{message}\n'

def info(message):
  app.logger.info(f"player {message}")
def error(message):
  app.logger.error(f"player {message}")

# Tests unitaires
if __name__ == '__main__':
  # app = Flask(__name__)
  # app.register_blueprint(player)
  # logging.info("Player en marche...")
  app.run()

if __name__ != '__main__':
  gunicorn_logger = logging.getLogger('gunicorn.error')
  app.logger.handlers = gunicorn_logger.handlers
  # app.logger.level(gunicorn_logger.level)