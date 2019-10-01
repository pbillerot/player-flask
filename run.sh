#!/usr/bin/env bash
#
# Démarrage du player
#
/home/billerot/Git/player-flask/venv/bin/gunicorn app:app -c /home/billerot/Git/player-flask/gunicorn.py
