# Django-Personal-Website

This project is using for personal training. I am trying to deploy this website in various way for learning deployment strategies and DevOps practices.  
With this project you can deploy Django website with SSL certificate. Nginx container comes with SSL proxy.

## Technologies

Python  
Django  
Docker  
Nginx  
PostgreSQL  
Let's Encrypt

## Manage Settings

#### Change servername


In docker-compose.yml and config/nginx/fatihkocnet.conf we have servername properties. If you want to deploy it in your local machine, change fatihkoc.net with localhost.  
**Warning **Be careful about it. Let's Encrypt allows you to create 10 certificates per week. Don't waste it while you are trying to deploy for test purposes.


#### Change Database Credentials

You can change database credentials in docker-compose.yml. You must change fatihkocnet/fatihkocnet/settings.py as well for database connections.

## Install & Run

    docker-compose up

Then go to the localhost:80.

Don't forget to remove unnessesary containers with

    docker-compose down
