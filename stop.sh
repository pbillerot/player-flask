#!/usr/bin/env bash
#
# Arrêt du player
#
pgrep --list-name gunicorn
echo Pid: $(cat /home/billerot/Git/player-flask/log/app.pid)
kill -9 $(cat /home/billerot/Git/player-flask/log/app.pid)

echo
read -rsp $'Press any key to continue...\n' -n1 key
