### Forum API

Розгортання:

1. Склонуй проект за допомгою


    git clone https://github.com/kahadei/djang-drf-forum.git

2. Створи та активуй віртуальне оточення python


    python3 -m venv venv
    source venv/bin/activate

3. Інсталюй залежності проекту


    pip install -r requirements.txt

4. Виконай міграції проекту


    python manage.py makemigrations
    python manage.py migrate


5. Збери статичні данні:
    

    python manage.py collectstatic

6. Запусти сервер django

    
    python manage.py runserver


Потестувати можна за адресою: https://testmyapp.xyz/api/

### Баги/недопрацювання

1. При створенні користувача API повертає помилку сервера 500, але користувач створюється.
2. При додаванні користувача до форуму - повертається помилка, але користувача додано.