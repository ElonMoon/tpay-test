FROM        python:3.8.5-slim
MAINTAINER  elonmoon@gmail.com

RUN         apt -y update
RUN         apt -y dist-upgrade

RUN         apt -y install gcc nginx supervisor
RUN         pip3 install uwsgi

COPY        requirements.txt /tmp/
RUN         pip3 install -r /tmp/requirements.txt

COPY        ./ /srv/tpay/
WORKDIR     /srv/tpay

WORKDIR     /srv/tpay/app
RUN         python3 manage.py collectstatic --noinput

RUN         rm -rf /etc/nginx/sites-available/*
RUN         rm -rf /etc/nginx/sites-enabled/*

RUN         cp -f  /srv/tpay/.config/app.nginx \
                   /etc/nginx/sites-available/

RUN         ln -sf /etc/nginx/sites-available/app.nginx \
                   /etc/nginx/sites-enabled/app.nginx

RUN         cp -f /srv/tpay/.config/supervisord.conf \
                  /etc/supervisor/conf.d/

EXPOSE      80

CMD         supervisord -n