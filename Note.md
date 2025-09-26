# title

mkdir fsp
cd fsp

npm create vite@latest

cd frontend
npm install
npm run dev

> pas oublier d appuyer sur entree
------------------
python -m venv env
.\env\Scripts\activate
------------------
cd fsp
.\env\Scripts\activate
python.exe -m pip install --upgrade pip
pip install django djangorestframework django-cors-headers
cd.. 
dir
django-admin startproject core
dir 
move core backend 
dir
cd backend
dir >core-manage
python manage.py migrate
python manage.py createsuperuser
dvsp
dvrchipro@gmail.com
Dvsuperuser
python manage.py startapp posts
cd ..
cursor .
> back - front - env
python .\manage.py runserver 8004
-------------------------
>>> core/settingd []
    'restframework' ,
    'corsheaders' ,
    'posts',

CORS_ALLOWED_ORIGINS = ['http://localhost:5173'] 

-------------------------
>>>Apres le tralala (et dans backend)
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8004

-------------------------

http://127.0.0.1:8004/admin
/login/?next=/admin/

dvsp
Dvsuperuser

http://127.0.0.1:8004/api/
http://127.0.0.1:8004/api/posts


-------------------------
-------------------------

# git init

git add .
git commit -m "Initial local commit"

gh repo create Django_backent-react+vite_fronten-ajouts_posts_by_admin --public --source=. --remote=origin
git push -u origin master

-------------------------
-------------------------svelte

python.exe -m pip install --upgrade pip
pip install django
cd backend
python -m venv venv-backend
.\venv-backend\Scripts\activate

pip install django djangorestframework pillow

# django-admin startproject films_backend
cd films_backend # dossier de travail
# python manage.py startapp films
pip freeze > requirements.txt

# pip install django-cors-headers
python manage.py makemigrations
python manage.py migrate
pip install django-taggit   

python manage.py createsuperuser
dvsp
dvrchipro@gmail.com
Dvsuperuser

-------------------------
# supprimer le superuser

-------------------------

python manage.py runserver 8004

-------------------------$ ajout de media et de sitingd media+url

http://127.0.0.1:8000/
http://127.0.0.1:8000/admin
http://127.0.0.1:8000/api/

http://127.0.0.1:5173/ # frontend


````bash
# pip install
'rest_framework',
'corsheaders',
    'taggit'
django_cors_headers-4.4.0
````

-------------------------

    - Node et django se lance a la fois

-------------------------

``` bash app_threlte_dv
python manage.py makemigrations Base_threlte_dv
python manage.py migrate Base_threlte_dv
python manage.py runserver 8000
```

le 14/09/2021

``` svelte django_film

backend\venv-backend\Scripts\activate 
python backend/films_backend/manage.py runserver 8000