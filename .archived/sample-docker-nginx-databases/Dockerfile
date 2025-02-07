FROM nginx:1.21

COPY nginx.conf /etc/nginx/nginx.conf

RUN apt-get update && apt-get install -y gettext-base

CMD ["/bin/sh", "-c", "envsubst '${ALLOWED_IPS} ${API_KEY}' < /etc/nginx/nginx.conf > /etc/nginx/nginx.conf.tmp && mv /etc/nginx/nginx.conf.tmp /etc/nginx/nginx.conf && nginx -g 'daemon off;'"]