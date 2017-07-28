FROM        pignu/weathersoundtest_ubuntu
MAINTAINER  HanYul Ryu hanyul.ryu@gmail.com


ENV         LANG C.UTF-8

COPY        . /srv/WeatherSoundTest
WORKDIR     /srv/WeatherSoundTest

RUN         /root/.pyenv/versions/WeatherSoundTest/bin/pip install -r .requirements/deploy.txt

COPY        .config_secret/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY        .config_secret/supervisor/nginx.conf /etc/supervisor/conf.d/
COPY        .config_secret/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config_secret/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf

RUN         rm -rf /etc/nginx/sites-enabled/default
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf

RUN         /root/.pyenv/versions/WeatherSoundTest/bin/python /srv/WeatherSoundTest/django_apps/manage.py  collectstatic --settings=config.settings.deploy --noinput

CMD         supervisord -n

EXPOSE      80 8000