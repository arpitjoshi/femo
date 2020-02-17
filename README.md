pip install -r requirements.txt



python app.py

-OR-

gunicorn --bind 0.0.0.0:5000 wsgi:app

-OR-

docker-compose build 
docker-compose up -d
