# Readme

### (Django)
**1) Создать вируальное оркужение python:**
```sh
$ python3 -m venv env
```
**2) Перейдите в директорию проекта `<project_name>` и активируйте виртуальное окружение:**
```sh
$ cd <project_name>
$ env/bin/activate
.
├── env
├── testproject 
├── README.md 
└── requirements.txt
```
**3) Установка Django и зависимости Python:**
```sh

(env)$ pip3 install -r requirements.txt
```
Для деактивации виртуальной среды используется команда `deactivate`.

**4) Настройки проекта:**
создайте файл `local_settings.py`. Путь его нахождения:
```sh
 ~/testproject/local_settings.py
```
Отредактируйте
```sh
(env)$  sudo nano ~/testproject/local_settings.py
```
Добавьте в `local_settings.py` 
```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ваш секретный ключ'

IMDB_API_KEY = ''
IMDB_API_URL = 'https://imdb-api.com/en/API/'
```
Пример для генерации SECRET_KEY: https://djecrety.ir/
Для получения IMDB_API_KEY зарегестируйтесь на https://imdb-api.com/
**5) Делее делаем миграции Django, создаем суперпользователя, создаем нужные директоррии для статики и медиа файлов:**

>5.1. активируем виртуальное окружение проекта:
```sh
$ cd ~/<your_ctcareers_project>/
$ source env/bin/activate
(env) $ cd testproject
(env) $ python3 manage.py migrate
Operations to perform:
  Apply all migrations: api
Running migrations:
 Applying some_file.0001_initial... OK
 Applying some_file.0001_initial... OK
 ...
 Applying some_file.0001_initial... OK
```

>5.2. Создаем суперпользователя для проекта:
```sh
(env) $ python3 manage.py createsuperuser
Username (leave blank to use '<username>'): <Django admin username>
Email address: <email adress if necessary (can be blanked)>
Password: <set your password>
Password (again): <repeat your password>
Superuser created successfully.
```
