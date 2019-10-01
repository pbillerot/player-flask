import gunicorn
command = '/home/billerot/Git/player-flask/venv/bin/gunicorn'
pythonpath = '/home/billerot/Git/player-flask'
workers = 1
# user = 'billerot'
bind = '127.0.0.1:8053'
logconfig = "/home/billerot/Git/player-flask/gunicorn_logging.conf"
# pid = '/home/billerot/Git/player-flask/log/alexa-pid'
# errorlog = '/home/billerot/Git/player-flask/log/error.log'
# accesslog = '/home/billerot/Git/player-flask/log/access.log'
# access_log_format = '%({X-Real-IP}i)s %({X-Forwarded-For}i)s %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
# loglevel = 'warning'
capture_output = True
timeout = 90
reload = True
