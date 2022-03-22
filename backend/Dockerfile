FROM python:3.10-alpine

LABEL MAINTAINER="Rickard Cronholm <rickard.cronholm@gmail.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /var/www/

# Add the application
COPY ./requirements.txt /tmp/
COPY ./app /var/www

RUN addgroup -g $GROUP_ID www && \
    adduser -D -u $USER_ID -G www www -s /bin/sh && \
    pip install pip --upgrade && \
    pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    chown -R www:www /var/www

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
