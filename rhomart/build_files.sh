#usr/bin/bash
echo starting file

python3.9  pip install requirements.txt

python3.9 manage.py makemigrations
python3.9 manage.py migrate