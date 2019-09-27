import logging
import os
from flask import Flask
from flask_ask_sdk.skill_adapter import SkillAdapter

from alexa.skill import sb
from player.player import player

logging.basicConfig(filename="log/alexa.log",level=logging.DEBUG)

def create_app():
  app = Flask(__name__)
  app.register_blueprint(player)
  skill_adapter = SkillAdapter(
    skill=sb.create(), 
    skill_id="amzn1.ask.skill.bd7515ac-93e7-48c6-b2b5-58dcd0fb0951", 
    app=app)
  skill_adapter.register(app=app, route="/alexa")

  return app

app = create_app()
