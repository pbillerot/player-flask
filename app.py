# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import os, logging, json
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Chargement des clés d'accès aux médias
with open('media/player.json') as outfile:
    medias = json.load(outfile)

@app.route('/')
def accueil():
  message = "Player a votre ecoute..."
  info(message)
  return jsonify(message)

@app.route('/play/<keyFile>')
def play(keyFile):
  message = "Play..."
  if os.system("pgrep --list-name audacious") == 0:
    if keyFile == "0":
      command = f"audacious --stop"
      iret = os.system(command)
      message = f"play {iret} {command}"
    elif keyFile == "1":
      command = f"audacious --pause"
      iret = os.system(command)
      message = f"play {iret} {command}"
    elif keyFile == "2":
      command = f"audacious --play"
      iret = os.system(command)
      message = f"play {iret} {command}"
    elif medias["drums"][keyFile] is not None:
      filePath = os.path.join(app.root_path, 'media', medias["drums"][keyFile])
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
      message(f"clé [{keyFile}] non trouvée")
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
