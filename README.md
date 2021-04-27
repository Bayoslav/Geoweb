# Geoweb

## Run this project locally

1. Clone this repo and inside your virtualenv run `pip install -r requirements.txt`
2. Load your virtualenv and just run `python manage.py runserver`

## How to use the API

### File conversion

1. `/api/convert-file` POST {file: [BinaryFile], to_json: [Boolean], to_shp: [Boolean]}
2. `/api/convert-file-ajax` POST, same as the one above,

### Report generation

1. `/api/generate-report` POST {file: [BinaryFile]}
