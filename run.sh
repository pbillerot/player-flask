#!/usr/bin/env bash
#
# Démarrage du player
#
/home/billerot/Git/player-flask/venv/bin/gunicorn -c /home/billerot/Git/player-flask/gunicorn.py wsgi:app
