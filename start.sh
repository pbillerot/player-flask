#!/usr/bin/env bash
#
# Démarrage du player
#
echo Player en marche...

/home/billerot/Git/player-flask/venv/bin/gunicorn app:app -c /home/billerot/Git/player-flask/gunicorn.py -p /home/billerot/Git/player-flask/log/app.pid

echo
read -rsp $'Press any key to continue...\n' -n1 key
