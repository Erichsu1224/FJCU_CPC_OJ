#! /bin/bash
rm -rf ./migrations
./rebuild_db.sh
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
