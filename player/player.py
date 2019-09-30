# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
import time
import os, logging

player = Blueprint('main', __name__, url_prefix="/player")

@player.route('/')
def accueil():
  return 'Player à votre écoute\n'

@player.route('/play/<mediafile>')
def play(mediafile):
  filePath = os.path.join(player.root_path, 'media', mediafile)
  command = f"audacious {filePath}"
  logging.info(command)
  os.system(command)
  return f'Play {command}\n'

@player.route('/stop')
def stop():
  logging.info("stop")
  os.system(f"audacious --stop")
  return 'Stop: current\n'

# Tests unitaires
if __name__ == '__main__':
  # global app
  app = Flask(__name__)
  app.register_blueprint(player)
  logging.info("Player en marche...")
  app.run()
