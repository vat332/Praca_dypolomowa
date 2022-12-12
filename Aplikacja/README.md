# Biblioteka z systemem rekomendacyjnym

## Spis treści

- [Technologie](#technologie)
- [Autor](#autor)
- [Komendy](#komendy)
- [Porty](#[porty])
- [RUN_TEST](#[RUN_TEST])
- [Aktualizowanie paczek](#[Aktualizowanie paczek])

## Technologie

- Django
- PostgreSQL
- React
- SWAGGER
- ESLINT
- PRETTIER
- DOCKER

## Autor:

- [@Sebastian Murawski](https://www.github.com/vat332)

## Porty:

- Frontend - `localhost:3000`
- Backend - `localhost:8000`
- Backend-admin `localhost:8000/admin`
  - login: admin
  - hasło: 1234
- Backend-swagger `localhost:8000/swagger`
- Pgadmin - `localhost:5050`

## Komendy:

1. Instalacja precommita `pre-commit install`// Jeszcze nie gotowe
2. Budowanie całego projektu `docker-compose build` or `docker-compose up`
3. Budowanie tylko frontendu `docker-compose build --no-cache frontend`
4. Tworzenie konta admina. Musisz wejść do kontenera z backendem `python manage.py createsuperuser`// Opcjonalnie
5. Migracja `python manage.py makemigrations <APP_NAME>` next `python manage.py migrate`
6. Podstawowe dane do bazy danych: `python manage.py loaddata <Name>.json`// Jeszcze nie gotowe

## Pgadmin:

1. Login: `admin@admin.com`
2. Hasło: `admin`
   <img src="https://user-images.githubusercontent.com/52125396/159588369-222c39bb-a65c-4903-9d83-d2937c8293b8.png" width="45%"></img>

## RUN_TEST:

!!!! Ważne Testy musza się zaczynać od słowa `test` !!!!

1. Przejdź do kontenera z Backend
2. Wpisz `python manage.py test ` nazwa aplikacji (np: users)

## Aktualizowanie paczek:

1. `npm install -g npm-check-updates`
2. `ncu --upgrade`
3. `npm install`
