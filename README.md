# django-authentication

## 🌈Platform Introduction

Full Django user authentication backend implemented with django-allauth also with profile pic change included!
A very simple project where a user can send some reviews via a form.
The core of the project is the authentication system

[github](https://github.com/nicodem96/django-authentication)

## 🏭online experience

## development process

### Exporting dependency files 

> Open a command prompt and type in your project path

```shell
pip freeze > ./requirements.txt
```

### Development Environment Installation

***- Windows and Linux -*** 

```shell 
pip install -r requirements.txt -i https://pypi.douban.com/simple
```

## debug

### Open the command line and create a super administrator

- [Introducing the Django Admin](https://docs.djangoproject.com/en/4.2/intro/tutorial02/#introducing-the-django-admin)

### Creating an admin user

```shell
python manage.py migrate

python manage.py createsuperuser

# 接下来根据提示输入自己想设置的内容，参考：
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```

### Trial operation project

```shell
python manage.py runserver

#Open a browser and visit:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/admin/
# http://localhost:8000/accounts/login/
```