FROM node:12.22.11-alpine3.15

LABEL MAINTAINER="Rickard Cronholm <rickard.cronholm@gmail.com>"

WORKDIR /app

ENV PATH=/app/node_modules/.bin:$PATH


COPY package.json /app/package.json
COPY . /app

EXPOSE 8080

RUN npm install --silent && \
    npm install -g @vue/cli@4.5.11 && \
    npm install axios@0.21.1 --save

CMD ["npm","run","build"]
