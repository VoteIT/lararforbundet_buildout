#!/bin/bash
#Ment to be run as root after buildout is done. Will obtain cert and install on nginx debian

cd /etc/nginx
ln -s /home/voteit/srv/lararforbundet_buildout/etc/nginx.conf ./sites-available/lararforbundet.conf
cd sites-enabled
ln -s ../sites-available/lararforbundet.conf

service nginx stop
certbot certonly --standalone -d lararforbundet.voteit.se
service nginx start
