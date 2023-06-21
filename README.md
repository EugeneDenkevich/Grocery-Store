# Grocery-Store
Курсовой проект на Django по окончании курса от IT-Academy. Интернет-магазин продуктов питания
<hr>

```bash
python -m venv venv
cd venv/Scripts
.\activate
cd ../..
cd src
pip install -r requirements.txt
```

###  for Linux:
```bash
cd Grocery-Store
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```

<hr>

To work correctly you need to create .env file in src directory and set correct environment variables. Use this command:
```bash
cp .env-example .env
```

### 2. Start applications
```bash
cd src
``` 
```bash
python manage.py makemigrations
``` 
```bash
python manage.py migrate
``` 
```bash
python manage.py createsuperuser
``` 
Enter a new login, email and password. Remember your email. Use it at 127.0.0.1:8000/admin to add new Users. It's neccessary adding new adding form in 127.0.0.1:8000/address. In 127.0.0.1:8000/admin you also can add new Products. Use images in this directory: Grocery-Store\src\static\app_grocery_shoping\pic\goods. In this directory you can find fruits, vegitables and milks/meat production.

```bash
python manage.py runserver
``` 
###  4. For using the app just type 127.0.0.1:8000 in yout browser.
