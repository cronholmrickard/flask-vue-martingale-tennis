# build stage
FROM node:12.22.11-alpine3.15 as build

LABEL MAINTAINER="Rickard Cronholm <rickard.cronholm@gmail.com>"

WORKDIR /app

ENV PATH=/app/node_modules/.bin:$PATH

COPY package.json /app/package.json
COPY . /app

RUN npm install --silent && \
    npm install -g @vue/cli@4.5.11 && \
    npm install axios@0.21.1 --save && \
    npm install bootstrap@4.6.0 --save && \
    npm install chart.js@2.9.4 --save && \
    npm install vue-chartjs@3.2.1 --save && \
    npm install vue2-dropzone@3.6.0 --save && \
    npm run build

# production stage
FROM nginx:1.21.6-alpine

COPY --from=build /app/dist /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
