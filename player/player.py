# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
import time
import os, logging

player = Blueprint('main', __name__, url_prefix="/")

# pgrep --list-name audaciou

@player.route('/')
def accueil():
  return 'Player à votre écoute\n'

@player.route('/play/<mediafile>')
def play(mediafile):
  message = "Play..."
  if os.system("pgrep --list-name audacious") == 0:
    filePath = os.path.join(player.root_path, 'media', mediafile)
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

@player.route('/stop')
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


# Tests unitaires
if __name__ == '__main__':
  # global app
  app = Flask(__name__)
  app.register_blueprint(player)
  logging.info("Player en marche...")
  app.run()
