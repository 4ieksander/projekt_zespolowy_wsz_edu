 # projekt_zespolowy_wsz_edu


To open project in django:
1. create virtual enviroment  ( python -m venv venv )
2. activate virtual enviroment (windows: ./venv/Scripts/activate | linux: source venv/Scripts/activate )
3. create DB
4. configure DB in Django( team_project_django/team_project/settings.py line 84 - 96
5. install requirements ( pip install -r requrements.txt ) 
6. create migration ( python  python manage.py makemigrations international_organ_players
7. migrate models ( python manage.py migrate )
8. create superuser ( python manage.py createsuperuser ) 
9. runserver ( python manage.py runserver )
10. add .env file into team_project directory, add DB_PASSWORD=Your_Password_Here
server is available under 127.0.0.1:8000/iop/ :)
