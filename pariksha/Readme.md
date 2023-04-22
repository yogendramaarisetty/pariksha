Prerequisites 

    - Python 3.8>
    
    - Postgres 13
    
      - While istalling make sure the username and pwd are "postgres" otherwise you need to change settimgs.py


Clone the Project
 
Open cmd where manage.py exist i.e. pariksha/pariksha

Run:  py -m venv venv   

Activate the venv : venv\scripts\activate

Run: pip install -r requirements.txt

By default when you install postgres it will create a postgres

Run: py manage.py runserver

You application will run



Links which solved few issues while setting up
https://stackoverflow.com/questions/32794615/raise-improperly-configured-psycopg2postgresql
https://stackoverflow.com/questions/8237842/django-core-exceptions-improperlyconfigured-error-loading-psycopg-module-no-mo
https://stackoverflow.com/questions/57972019/django-core-exceptions-improperlyconfigured-error-loading-psycopg2-module-dll

