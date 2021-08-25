## DCC Python/Django Example
---
### This application is a Django API that will maintain a log of date/timestamps for requests to the /access endpoint
---
## Requirements

* Port: The application runs on port 8000 by default, this behavior can be overriden by setting the PORT environment variable
* Environment Vars:
    * ACCESS_LOG_LOC: Define the directory where the access log will be stored, otherwise it will default to a /tmp directory.  This is useful for configuring a volume to store the access log file so it will be persisted.  This variable is optional.
    * PORT: Configure the port the application will run on.  This variable is optional.
* Volumes: The access log, by default, is stored in the tmp directory and will be lost when the container restarts.  To persist the file, in conjunction with setting the ACCESS_LOG_LOC env variable we can create a volume for that location and have the log be stored in EFS
---
## How to Run
* For local development, the app should be started with `python3 manage.py runserver`
* For production use, the app should be deployed using gunicorn: `gunicorn dcc_python_django_example.wsgi`
---
## DCC Deployment
* This repository contains both a Dockerfile and a Procfile, so deployment can be done with either the Dockerfile or Buildpack mechanism.