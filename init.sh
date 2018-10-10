#!/bin/bash
# restart nginx
sudo ln -sf $(pwd)/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo unlink /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# start application
docker-compose up -d
