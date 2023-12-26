#usr/bin/bash
echo starting file
python3.9 -m pip -r install requirements.txt

python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py collectstatic 