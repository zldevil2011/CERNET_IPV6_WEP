#! /bin/bash
#source /home/hacker/django_project/wireless_ENV/bin/activate
ps -ef|grep uwsgi|grep -v grep|cut -c 9-15|xargs kill -9
uwsgi --ini /home/hacker/django_project/wireless_ENV/wireless/uwsgi.ini
