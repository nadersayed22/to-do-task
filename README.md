to-do-task

this is Todo listing app where users can login, add items to their Todo list, mark them as done
and delete them. With an admin panel where the admin can manage the registered users.

Usage
1. Go and clone wall app's repo.
2. Create & Run a virtual environment for this app.
Open your terminal, go to the wall app's cloned repo's directory, and run this command

# Make sure you installed virtualenv
pip install --upgrade virtualenv

# Activate the wallvenv virtual environment
source wallvenv/bin/activate


3. Install all of the needed packages.

From your terminal running your wallvenv, run the following command
pip install -r requirements.txt

4. If you'll use my test db, you don't need this step.
#Run the migrations
python manage.py makemigrations
python manage.py migrate


5. Now, your configs are completed just run the application.
python manage.py runserver

6.use this links to router in project 

#to admin panal 
http://127.0.0.1:8000/admin/

#list api user 
http://127.0.0.1:8000/api/

http://127.0.0.1:8000/api/profile/

#get user id to delet or put 

http://127.0.0.1:8000/api/profile/id

#to use login api
http://127.0.0.1:8000/api/profile/login/

#to list tasks api 
http://127.0.0.1:8000/api/todos/

#to put update pr delete tasks api 
http://127.0.0.1:8000/api/todos/id


