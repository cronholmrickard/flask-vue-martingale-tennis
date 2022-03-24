FROM alpine:latest

LABEL MAINTAINER="Rickard Cronholm <rickard.cronholm@gmail.com>"

RUN apk --update add nginx && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    mkdir /etc/nginx/sites-enabled/ && \
    rm /etc/nginx/http.d/default.conf && \
    mkdir -p /run/nginx && \
    rm -rf /etc/nginx/conf.d/default.conf && \
    rm -rf /var/cache/apk/*

COPY http.d/*.conf /etc/nginx/http.d/

EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]
