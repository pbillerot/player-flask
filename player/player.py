# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
from flask import request, session
import pygame
import time
import os, logging

def playMediafile(filePath):
  if session["player"] is not None:
    session["player"] = pygame.mixer.Sound(filePath)
  else:
    logging.info(f"stop")
    session["player"].stop()
    session["player"] = pygame.mixer.Sound(filePath)
  logging.info(f"play: {filePath}")
  session["player"].play(-1)

player = Blueprint('main', __name__, url_prefix="/player")
#Initialisation Pygame
pygame.mixer.init()

@player.route('/')
def accueil():
  return 'Player à votre écoute\n'

@player.route('/play/<mediafile>')
def play(mediafile):
  filePath = os.path.join(player.root_path, 'media', mediafile)
  playMediafile(filePath)
  return f'Media: play {mediafile}\n'

@player.route('/stop')
def stop():
  if session["player"] is not None:
    logging.info(f"stop")
    session["player"].stop()
  return 'Media: stop\n'

# Tests unitaires
if __name__ == '__main__':
  # global app
  app = Flask(__name__)
  app.register_blueprint(player)
  app.run()
