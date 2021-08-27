## DCC Python/Django Example
---
### This application is a Django API that will maintain a log of date/timestamps for requests to the /access endpoint
---
## Requirements

* Port: The application runs on port 8000
* Environment Vars:
    * ACCESS_LOG_LOC: Define the directory where the access log will be stored, otherwise it will default to a temp directory.  This is useful for configuring a volume to store the access log file so it will be persisted.  This variable is optional.
* Volumes: The access log, by default, is stored in a temp directory and will be lost when the container restarts.  To persist the file, in conjunction with setting the ACCESS_LOG_LOC env variable we can create a volume for that location and have the log be stored in EFS
---
## How to Run
* The app start command is `python3 manage.py runserver`
---
## DCC Deployment
* This repository contains both a Dockerfile and a Procfile; the deployment can be done with either mechanism.

* Create the EFS share to hold the access log
  * <img src="https://user-images.githubusercontent.com/55393832/131189053-fba6f047-cc02-4bf3-bdb3-1f9e38772af5.jpg" width="60%">

* Setup the repository connection
  * <img src="https://user-images.githubusercontent.com/55393832/131189056-67846f21-c0e5-4358-ba36-655a327c19cb.jpg" width="60%">

* Configure the build - this demonstrates a BuildPack build, to create with a Dockerfile, set the BuildType to "Dockerfile" and set the Dockerfile Name to the match the Dockerfile in the root of this repo ("Dockerfile").  Note the 'procfile entry' field matches the key of the field from the repository Procfile that contains the application startup command.
  * <img src="https://user-images.githubusercontent.com/55393832/131189051-43ffd037-75c9-461e-a88a-65f60cd6c7ff.jpg" width="60%">

* Set the port to the port this application will run on, 8000.  Modify the scale/ram/cpu to meet your needs.
  * <img src="https://user-images.githubusercontent.com/55393832/131189052-848b7811-e0fd-48b6-ac14-c9b6fbff42ff.jpg" width="60%">

* Set the health check endpoint to use the designated route the application provides; the expected response is a 200.
  * <img src="https://user-images.githubusercontent.com/55393832/131189055-cc4a12dd-adfa-4eff-bfd4-c5645a97487e.jpg" width="60%">

* Set the listener path to listen on the root
  * <img src="https://user-images.githubusercontent.com/55393832/131189058-bace4038-8c24-43aa-8588-b6810e02285a.jpg" width="60%">

* In the add-ons, add the ACCESS_LOG_LOC environment variable.  This should reference the container path where the log file should be stored.
  * <img src="https://user-images.githubusercontent.com/55393832/131189054-6b2ed09a-8c59-40cd-824e-20606f5fb8c0.jpg" width="60%">

* In the add-ons, add a volume for the location defined in the previous step, using the EFS share that was created in step 1.  Mounting this directory as a volume will persist the log file between container reboots.
  * <img src="https://user-images.githubusercontent.com/55393832/131189057-b31bb6a4-3686-415c-8263-497262967941.jpg" width="60%">
