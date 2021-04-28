# TO Do Task 

this is Todo listing app where users can login, add items to their Todo list, mark them as done
and delete them. With an admin panel where the admin can manage the registered users.

          Usage
 
## Go and clone to_do_task  app's repo.

1. Create & Run a virtual environment for this app.

        Open your terminal, go to the wall app's cloned repo's directory, and run this command

2. Make sure you installed virtualenv

       pip install --upgrade virtualenv

3. Activate the to_do_task virtual environment
 
       source to_do_task/bin/activate


4. Install all of the needed packages.

       From your terminal running your to_do_taskvenv, run the following command

       pip install -r requirements.txt

5. If you'll use my test db, you don't need this step.

## Run the migrations

       python manage.py makemigrations
       python manage.py migrate


6. Now, your configs are completed just run the application.

       python manage.py runserver

##  use this links to router in project 

### to admin panal 
     http://127.0.0.1:8000/admin/

### list api user 
    http://127.0.0.1:8000/api/

    http://127.0.0.1:8000/api/profile/

### get user id to delet or put 

    http://127.0.0.1:8000/api/profile/id

### to use login api
    http://127.0.0.1:8000/api/profile/login/

### to list tasks api 
    http://127.0.0.1:8000/api/todos/

### to put update pr delete tasks api 
    http://127.0.0.1:8000/api/todos/id


