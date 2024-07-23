# dockerAssignment
#This is assignment project for virtualization and cloud computing
AUTHOR -    VIDYUT BHASKAR
ROLL -      G23AI2128
COURSE-     PGDDE 2024-25
SUBJECT     VIRTUALIZATION AND CLOUD COMPUTING

Objective - Create a Docker image of Web Application and Deploy and Run inside the container

There are two options to build container applications
1. Build the project and later containerize it
2. Build the project inside the the container

In This assignment we will option2 to build and deploy a DjangoApplication inside the container

Assignment Requirements
1. Git-Hub Repos
2. Youtube Video

Software Pre-Requisites
1. Docker Desktop
2. IDE - VS Code
3. VS Code Extensions - Python and Docker from verified sources

Steps
1. Create docker-compose.yml - store container configuration
2. Create Dockerfile - store image information
3. Create requirements.txt - provide Django server version requirements
4. run command:  'docker-compose run web django-admin startproject myTestProject .' -- this will build project in the root folder
5. run container docker-compose up
6. Check container name in powershell docker ps
7. Start new app command  'docker exec dockerassignment-web-1 python manage.py startapp <app-name>

ex - let us change the response of the WelcomeUser App
