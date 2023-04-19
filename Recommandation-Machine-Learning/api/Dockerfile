FROM python:3.8-slim

WORKDIR /app
ADD . /app

# install dependencies
RUN pip install -r requirements.txt

# expose port
EXPOSE 5000

# run application
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "app:app" ]