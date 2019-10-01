#!/usr/bin/env bash
#
# Démarrage du player
#
nohup /home/billerot/Git/player-flask/venv/bin/gunicorn app:app -c /home/billerot/Git/player-flask/gunicorn.py -p /home/billerot/Git/player-flask/log/app.pid 2>&1 >/dev/null