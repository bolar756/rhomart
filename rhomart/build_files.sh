#usr/bin/bash
echo starting file
pip -r install requiremnts.txt

python3.9 manage.py makemigrations
python3.9 manage.py migrate
python 3.9 manage.py collectstatic --noinput