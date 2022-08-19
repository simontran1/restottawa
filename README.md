# restottawa

## Made by: Simon and Luke

## Description

A web app for finding nearby restaurants that you may like.

Utilizes Google Maps' [Places API](https://developers.google.com/maps/documentation/places/web-service) for finding the restaurants and fast food joints.

_NOTE:_ Despite the title, this web app can be used anywhere in the world provided you have access to an internet connnection.

https://user-images.githubusercontent.com/107209941/184470648-3cfbae35-3ec6-40b9-8397-84da9806e49f.mp4

## Setup

1. Git clone the repo
2. Create a Python virtual environment (steps for UNIX and Unix-like systems below)

```sh
python -m venv venv
source venv/bin/activate
```

3. Install pip packages

```sh
pip install -r requirements.txt
```

4. Create .env file in root project folder

```sh
touch .env
```

5. Add the following lines in the .env file and insert your keys.

```
API_KEY=your_key_goes_here
SECRET_KEY=your_key_goes_here
```

7. Run the web app

```sh
python app.py
```
