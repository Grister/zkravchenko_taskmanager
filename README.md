# task-manager

### Installation

Clone the repository
```
git clone https://github.com/edu-python-course/zkravchenko_taskmanager.git
```

Create and activate virtual environment
```
cd scraping-soup
python3 -m venv venv
source venv/bin/activate
```

Install project dependencies
```
pip3 install -r requirements.txt
```

### Run application

```
python3 manage.py runserver
```

### Endpoints that work

* /tasks/: The main page of the site.
* /about/: Provides information about the system, describing the functionality of the site.
* /: Same as /tasks/, as a shortcut to the main page.
* /<uuid:uuid>/: View details of a single task.
* /<uuid:uuid>/update/: The page for updating a task.
* /<uuid:uuid>/delete/: The task deletion page.
* /sign-up/: The user registration page.
* /sign-in/: The user login page.
* /logout/: The user's logout page.
