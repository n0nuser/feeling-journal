FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY cert.pem /etc/nginx/conf.d/cert.pem
COPY key.pem /etc/nginx/conf.d/key.pem
COPY nginx.conf /etc/nginx/conf.d