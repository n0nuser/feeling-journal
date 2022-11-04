FROM nginx:1.22-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY fullchain.pem /etc/nginx/conf.d/fullchain.pem
COPY privkey.pem /etc/nginx/conf.d/privkey.pem
COPY nginx.conf /etc/nginx/conf.d