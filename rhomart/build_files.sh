#usr/bin/bash

pip install requiremnts.txt
python manage.py makemigrations
python manage.py migrate
python 3.9 manage.py collectstatic --noinput