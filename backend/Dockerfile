FROM python:3.10-alpine as builder

LABEL MAINTAINER="Rickard Cronholm <rickard.cronholm@gmail.com>"

COPY ./requirements.txt /tmp/
COPY setup.py /tmp
COPY ./martingale_backend /tmp/martingale_backend

WORKDIR /tmp

RUN pip install pip --upgrade && \
    pip install wheel --upgrade && \
    pip install setuptools --upgrade && \
    mkdir -p /opt/docker/wheels && \
    pip download -r /tmp/requirements.txt --no-deps --dest /opt/docker/wheels && \
    python setup.py bdist_wheel --dist-dir /opt/docker/wheels


FROM python:3.10-alpine

LABEL MAINTAINER="Rickard Cronholm <rickard.cronholm@gmail.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /var/www/

# Add the application starter
COPY ./wsgi.py /var/www
# copy match data
COPY ./data /var/www/data
# copy build artifacts
COPY --from=builder /opt/docker/wheels /tmp/wheels

RUN addgroup -g $GROUP_ID www && \
    adduser -D -u $USER_ID -G www www -s /bin/sh && \
    chown www:www /var/www/wsgi.py && \
    su -c 'pip install pip --upgrade'  www && \
    su -c 'find /tmp/wheels -mindepth 1 -maxdepth 1 -type f \
        -exec pip install {} \
        --user \
        --no-deps \
        --no-cache-dir \
        --no-warn-script-location \;' www && \
    ln -s /home/www/.local/bin/* /usr/local/bin/

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]
