#!/bin/bash
source /home/user/проекты/testproject/venv/bin/activate
exec gunicorn -c /home/user/проекты/testproject/bboard/config/gunicorn/dev.py 
