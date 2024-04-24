# Inialisation


## 1. Introduction

### A. Installation of the environement

For that project, you need to install an virtual environement in Python with these commands :

```bash
python3 -m venv env
source env/bin/activate
```

Please ensures that you installed the `venv` package with that command :

```bash
sudo apt get install python3.11-venv
```

### B. Installation of Django

To install `django`, you need to activate the `env`. When your `env` is activated, follow that command :

```bash
python -m pip install django
```

### C. Run the server

You have already a folder app installed. To run the django server, do that command :

Please make sure you are in the `env`

```bash
cd app
python manage.py runserver
```

## Version of modules



- Django : 5.0.4