FROM postgres:16

ENV POSTGRES_USER="postgres_user_123456789"
ENV POSTGRES_PASSWORD="password_123456789"
ENV POSTGRES_DB="backend_src_development"

COPY ./init/*.sql /docker-entrypoint-initdb.d/
