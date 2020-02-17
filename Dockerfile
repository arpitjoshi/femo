# pull official base image
FROM python:3.7-alpine

# set work directory
ADD . /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY . /app
RUN pip install -r requirements.txt

# EXPOSE 8000

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]
# CMD ["python", "app.py"]


