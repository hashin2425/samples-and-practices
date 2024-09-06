FROM redis:latest

COPY redis.conf /usr/local/etc/redis/redis.conf
COPY backup.sh /backup.sh

RUN apt-get update && apt-get install -y cron

RUN echo "0 */6 * * * /backup.sh" | crontab -

CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]