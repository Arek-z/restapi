instalacja virtualenv z poziomu admina
```sh
pip install virtualenv
```
konfiguracja 
```sh
git clone https://github.com/Arek-z/restapi
cd restapi
virtualenv env
env\Scripts\activate  
pip install -r requirements.txt  
cd rci_web  
powershell  
$env:DEBUG="True"; python manage.py makemigrations rciapi  
$env:DEBUG="True"; python manage.py migrate  
$env:DEBUG="False";$env:ALLOWED_HOSTS="127.0.0.1";$env:SECRET_KEY="XXX"; python manage.py runserver  
```
adresy:  
http://127.0.0.1:8000/rciapi/units/  
http://127.0.0.1:8000/rciapi/employees/
