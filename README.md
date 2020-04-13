# sms-system

#### Procedure to setup and run :
- Navigate to your cloned repository
```
$ cd <project_directory>  #In This case sms-system    
```
- Setup a  virtual environment
```
$ python3 -m venv sms-system-env
$ source sms-system-env/bin/activate
```
- Use Pip to install other dependencies
```
$ pip install -r requirements.txt
```
- Make database migrations
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
- Create Super-user
```
$ python3 manage.py createsuperuser
```
- Run Development Server
```
$ python3 manage.py runserver
```

